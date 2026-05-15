# GTOC-7292: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7292
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2024-12-04T12:55:29.000+0800
- Updated: 2025-03-06T17:45:42.325+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

**Currently, the uploaded restore logs are truncated, so don't rely on logs info...customer [REDACTED_CUSTOMER]et's see if we could get any root cause with following info, if not, we can wait for their new uploaded logs.**

 

We recently ran two PITR tests on our functional UDS cluster and wanted help debugging the performance of these restores. We ran two PITRs against two separate restore clusters w/ the same size/configuration that matches that of the source cluster, one test restoring 1hr of logs and the other restore 1d (24h) of logs.

Observations:

* Both snapshot restores took 1h45m to complete, each restoring 2.9TiB of data in S3, which results in 150GB/tikv/hr throughput

* Log restore took 6min for 1hr of logs and 115min for 1d of logs, resulting in log apply throughput of 0.3-0.5GB/tikv/hr

Both of these represent slower-than-expected performance (we expect 280GB/tikv/hr for snapshot restore and 30GB/tikv/hr for log restore). Can you help us understand why the restore performance is slow and how we can configure/improve it?

Setup:

* 12 tikv nodes, 16core r6i.4xl instances

* Each tikv has 1TiB EBS data volume w/ 8k IOPS and 800MB/s throughput quota

* snapshot contains 2.9TiB of data in S3

* 1hr restore contains 367.5MiB of logs in S3, 1d restore contains 11.4GiB of logs in S3

TiKV configs:

import.import-mode-timeout | 10m |  
import.memory-use-ratio | 0.3 |

## Recent Comments Excerpt

### 2024-12-04T13:55:56.000+0800 [REDACTED_USER]

For the log restore, you can increase the pitr-concurrency.
```

br:

  cluster: [REDACTED_CLUSTER]

  clusterNamespace: [REDACTED_NAMESPACE]

### 2024-12-05T13:12:12.000+0800 [REDACTED_USER]

Customer [REDACTED_CUSTOMER]:
 
ok, we ran a PITR w/ updated EBS configs and BR pitr-concurrency and are seeing much better performance/results!
We reran test 2, restoring 1d of logs. Snapshot restore completed in 25min (640GB/hr/tikv), and log restore completed in 16min (3.8GB/hr/tikv). Overall, these performance numbers are certainly good enough for our use-cases, and snapshot restore is much better than expectations.
Want to do a little bit of a deeper dive into log restore performance, specifically because testing results say we can expect up to 30GB/hr/tikv. Likely log restore is highly dependent on workload and specific nature of writes we are doing, so I think more variance is expected, but wondering if there’s anything obvious configuration/performance-wise we’re missing.
During KV apply, we see each tikv handling 50-75 QPS applies, w/ p99 latency of 319ms. EBS metrics show that we are not bottlenecked by IOPS or throughput, and raftstore metrics look good as well. Is this an opportunity to bump pitr-concurrency further? what are the tradeoffs there?
I’m attaching restore CR, restore pod logs, and clinic metrics: 
[REDACTED_CLINIC_URL]

### 2024-12-06T11:13:27.000+0800 [REDACTED_USER]

There are 12 TiKV nodes, so each TiKV only has about 10 apply requests at the same time.
You can try to set 
--pitr-concurrency=1536
 to rerun log restore.

### 2024-12-10T08:04:19.000+0800 [REDACTED_USER]

to clarify, pitr-concurrency then controls the concurrency on the br-kernel side? and we should always adjust the config accordingly based on the size/# of tikv nodes in the cluster we’re restoring into?
what is the default value? and for monitoring if we’ve set the concurrency too high, what should we check? duration/qps of the apply ops, as well as memory usage on the tikv?

### 2024-12-10T11:21:15.000+0800 [REDACTED_USER]

pitr-concurrency then controls the concurrency on the br-kernel side?
Yes
we should always adjust the config accordingly based on the size/# of tikv nodes in the cluster we’re restoring into?
If necessary
what is the default value? 
16
for monitoring if we’ve set the concurrency too high, what should we check?
the grpc qps
