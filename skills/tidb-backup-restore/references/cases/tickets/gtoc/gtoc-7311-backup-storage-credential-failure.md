# GTOC-7311: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7311
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-12-17T08:11:40.000+0800
- Updated: 2025-03-07T10:55:12.537+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We’ve conducted further backup testing on the full-shadow cluster [REDACTED_CLUSTER] updated configs. Backup performance is much improved (full backup takes < 3hrs). We would like to debug/investigate the impact the backup had to online traffic on the cluster. Important backup configs are as follows:

* br.concurrency = 128

* backup.num-threads = 8

* backup.enable-auto-tune = false

backup.num-threads was deliberately selected to minimize impact of the backup. During the backup, we observe TiKVs using up to 10cpus of the 32 total on the node. If backup uses the full allotted 8cpus, then total cpu usage will be \~18cpus, or <60% of the total cpu. During the backup, we observe the hottest TiKV using 17.5 cpus, validating these configs.

During the backup, we observe some impact to low-level TiKV operations, specifically in coprocessor read latencies. We observe a \~30% increase in p99 cop index/select operations (and similar increase in p99.9). We observe similar latency increases in KV gRPC operations, where kv_batch_get, kv_get, kv_resolve_lock, and coprocessor operations show 25-50% p99 latency increases.

1. **Can we attribute these latency increases to the backup?** These latency increases correlate directly with backup duration, and we don’t observe any significant change in workload or underlying EBS performance.

1. **What is the mechanism by which the backup impacts these lower-level operations?** Is it primarily due to slower RocksDB reads due to the backup process scanning all the data there? There is remaining CPU on the node, and once again, we don’t observe any EBS degradation or throttling, nor do we observe any significant impact of GC (ex. ratio of keys scanned to keys processed).

Despite the impact to low-level TiKV operations, we do observe significantly less impact to TiDB statement latencies. We observe a \~5% increase (negligible) in tail (p99/p99.9) select latencies. We do observe some impact (50% increase) in our p99.9 DELETE query latency without any significant change in delete workload. In our full-shadow workload, we run replication from Aurora using DM in safe-mode, so DELETE queries represent UPDATE traffic from the source Aurora clusters.

1. **Once again, can we attribute** DELETE **latency increase to the backup?** And if so, why is backup impacting these queries but not impacting reads generally or other writes (UPDATEs)?

Though we observe negligible impact to TiDB reads generally, during the \~3hr backup we observe 3 separate significant read latency spikes that span 1-2mins. Curiously, each of these spikes occur 30min after the hour, likely indicating some offline or cyclical load from our shadow traffic. However, I’d like to investigate further why these latency spikes are occurring. Once again, during these spikes, we don’t see any significant change in workload or underlying EBS performance.

1. **What is the cause of these read latency spikes?**

I’ve attached the backup CR, full backup logs, and clinic metrics for the following periods:

1. [[REDACTED_CLINIC_URL]) 30min prior to the backup (baseline)

## Recent Comments Excerpt

### 2024-12-18T11:51:02.000+0800 [REDACTED_USER]

Can we attribute these latency increases to the backup?
 
It seems during backup, RocksDB's `seek` latency increases. 
What is the mechanism by which the backup impacts these lower-level operations?
We need further investigation about the relationship between backup and the regression of `seek`s.
Once again, can we attribute
 
DELETE

### 2025-01-15T04:59:47.000+0800 [REDACTED_USER]

Now that we’ve run the backup under new s3 configs to reduce throttling and increase backup performance, we want to revisit the impact of the backup on the full-shadow cluster [REDACTED_CLUSTER] the new context
We run the backup w/ the following config:

 

 {{backup.enable-auto-tune: falsebackup.num-threads: 8

br.concurrency: 256

### 2025-01-16T17:09:06.000+0800 [REDACTED_USER]

p99 select latency increases by 14% (from 6.49ms to 7.43ms). This is borderline w/in our requirements, but is close enough that we’d like to debug it further here. Can we attribute this latency increase to the backup and its affect on underlying RocksDB/coprocessor operations?
p99 delete latency increases by over 50% (from 3.98ms to 6.68ms). We’ve previously discussed a possible mechanism as these are primarily point deletes, which first require a point get, which is affected by RocksDB seek latency increase that we observe during the backup. Is there a similar mechanism present here during this backup? And once again, can we attribute this latency increase to the backup?
Yes, it seems the P99 seek latency increases about 5x during backing up (100µs → 500µs). To check whether it contributes to the latency increcement, you may describe the select statments, if there is a `Point_Get` or `Batch_Point_Get`, then this statement is probably impacted by backup.
The mechanism of how backup makes the RocksDB seek latency increase is still not clear. I have checked the perf context of RocksDB in the uploaded clinic but it seems some of contents like 
seek_on_memtable_time
, 
seek_child_seek_time
 are lost.

### 2025-01-23T03:34:38.373+0800 [REDACTED_USER]

our instance metrics are not exported in any clinic dumps. Here are the screenshots of the relevant panels
for reference, our EBS volume provisioned quotas are 8k iops and 800MB/s throughput
[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2025-01-30T04:03:57.992+0800 [REDACTED_USER]

the disk IO time per second, disk io bytes per second, (server section), write io bytes, read io bytes (IO breakdown section) for tikv-0-1a.

[REDACTED_MEDIA]
 
[REDACTED_MEDIA]
 
 
[REDACTED_MEDIA]
