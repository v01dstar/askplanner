# GTOC-7577: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7577
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-05-08T03:56:57.368+0800
- Updated: 2025-08-27T00:19:24.089+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We’d like to debug the slow meta-KV restore phase of a recent restore that we performed.

This was a filtered restore of our full-shadow cluster. The PITR filtered full-shadow to a subset of tables/databases and replayed 18h of logs. After the restore, the cluster [REDACTED_CLUSTER] 82TiB of compressed, 3x replicated data to the cluster.

The cluster is configured with 60 tikv nodes, each w/ 3TiB data EBS volume, 16vCPU and 128GiB RAM (r6i.4xl). Given above data and configuration, we don’t believe this is a case of restore being slow due to the amount of data being restored or not having enough compute resources.

The overall PITR process took 7h, and of this time, **3.5h was spent solely in the “Restore Meta Files” phase** according to the CR status. Within this phase, there are specifically two areas that I would like to investigate and debug.

For debugging purposes, I’ve attached the restore CR and the full set of logs from the BR restore pod (split due to large file size). If necessary, please request a Grafana token for metrics access to debug also.

1. “read meta from storage and parse”

As I understand, the BR pod scans all log-meta files in order to determine the startTs for the restore. From logs, we observe this phase take 1h16m (22:25Z - 23:41Z). Counting the log-lines, we observe the BR process scan over 4M log-meta files.

```
[2025-05-06T22:25:07.410Z] I0506 22:25:07.410568       9 restore.go:176] [2025/05/06 22:25:07.410 +00:00] [INFO] [log_file_manager.go:132] ["read meta from storage and parse"] [path=v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta] [min-ts=[REDACTED_LONG_ID] [max-ts=[REDACTED_LONG_ID] [meta-version=1]
...
[2025-05-06T23:41:36.871Z] I0506 23:41:36.871487       9 restore.go:176] [2025/05/06 23:41:36.871 +00:00] [INFO] [log_file_manager.go:132] ["read meta from storage and parse"] [path=v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta] [min-ts=[REDACTED_LONG_ID] [max-ts=[REDACTED_LONG_ID] [meta-version=1]
```

* Practically, this translates to \~900 files scanned per second, which seems reasonably fast. But this scanning does seem further parallelizable since we only need to track a global minStartTs, so I’m wondering **are there any ways to optimize/improve the performance of this scan?**
* 4M log-meta files from a source cluster w/ 135 tikvs and a 3min flush interval translates to 60d of log-meta retention. This indicates that the log-meta restore process is not only dependent on the period of logs being restored (18h), but also on the period of logs being retained. **Is this a correct assessment of the restore logic? If so, this is a significant design gap where we expect the performance of log replay to only depend on the amount of data being restored, not the amount of data being retained.** The large # of files in this specific case is related to [[REDACTED_TICKET_ID]([REDACTED_SUPPORT_URL]) where we are not properly truncating old logs. But our anticipated 35d retention would still result in over 2M log-meta files to scan

1. prior to “start to restore meta files”

From logs, scanning log-meta files completes at 23:41Z. However, the next stage of restore, “start to restore meta files”, does not start until 01:31Z, almost 2hrs after the scan completes. Logs don’t reveal what is happening during this period – **what are the specific steps that BR is performing during this time? And why does it take so long?**

```

## Recent Comments Excerpt

### 2025-05-08T03:57:13.204+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b4e8fffb00ca80ec4bef17203810) by lark

### 2025-05-08T03:57:30.890+0800 [REDACTED_USER]

Here's the summary of the restore:

Snapshot restore -> 1h52m

Log replay time-> 5h17m
Snapshot Restore:
[2025-05-06T22:25:01.164Z] I0506 22:25:01.164217       9 restore.go:176] [2025/05/06 22:25:01.164 +00:00] [INFO] [collector.go:264] ["Full Restore success summary"] [total-ranges=408509] [ranges-succeed=408509] [ranges-failed=0] [restore-ranges=210411] [total-take=1h52m17.245559285s] [RestoreTS=[REDACTED_LONG_ID] [total-kv=[REDACTED_LONG_ID] [total-kv-size=90.39TB] [average-speed=13.42GB/s] [restore-data-size(after-compressed)=29.41TB] [Size=[REDACTED_LONG_ID] [BackupTS=[REDACTED_LONG_ID]

### 2025-05-21T17:30:00.239+0800 [REDACTED_USER]

Currently BR needs to download and parse all the metas to get 
min-ts
, 
max-ts
 and 
min-default-ts
. We have some designs to accelerate to read and parse meta. It will be implemented in the future.
Add timestamp in the filename.
