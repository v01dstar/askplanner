# GTOC-7320: PITR fails with execute over region id:2145218 start_key:\

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7320
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-12-21T09:21:42.000+0800
- Updated: 2025-03-06T17:44:51.455+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We are running a PITR test for a full-shadow snapshot and 1d of incremental logs. The restore fails during the KV restore phase. The first ERROR log I see from the restore pod is:

```java
I1220 18:18:57.315617 9 restore.go:176] [2024/12/20 18:18:57.314 +00:00] [ERROR] [client.go:2749] ["restore files failed"] [error="execute over region id:2145218 start_key:\"t\\200\\000\\000\\000\\000\\000n\\3778_i\\200\\000\\000\\000\\000\\377\\000\\000\\004\\000\\003\\200\\000\\001\\377\\224\\353\\340\\030\\271\\004\\000\\000\\377\\000\\000\\242\\023K\\303\\003\\200\\377\\000\\000\\000\\242\\023K\\303\\000\\376\" end_key:\"t\\200\\000\\000\\000\\000\\000n\\3778_i\\200\\000\\000\\000\\000\\377\\000\\000\\004\\000\\003\\200\\000\\001\\377\\224\\364B\\273\\267\\004\\000\\000\\377\\000\\000\\242R\\200\\250\\003\\200\\377\\000\\000\\000\\242R\\200\\250\\000\\376\" region_epoch:<conf_ver:65 version:4398 > peers:<id:2182868 store_id:17 > peers:<id:2182869 store_id:186 > peers:<id:2182867 store_id:365 > failed: rpc error: code = Canceled desc = CANCELLED"] [errorVerbose="rpc error: code = Canceled desc = CANCELLED\nexecute over region id:2145218 start_key:\"t\\200\\000\\000\\000\\000\\000n\\3778_i\\200\\000\\000\\000\\000\\377\\000\\000\\004\\000\\003\\200\\000\\001\\377\\224\\353\\340\\030\\271\\004\\000\\000\\377\\000\\000\\242\\023K\\303\\003\\200\\377\\000\\000\\000\\242\\023K\\303\\000\\376\" end_key:\"t\\200\\000\\000\\000\\000\\000n\\3778_i\\200\\000\\000\\000\\000\\377\\000\\000\\004\\000\\003\\200\\000\\001\\377\\224\\364B\\273\\267\\004\\000\\000\\377\\000\\000\\242R\\200\\250\\003\\200\\377\\000\\000\\000\\242R\\200\\250\\000\\376\" region_epoch:<conf_ver:65 version:4398 > peers:<id:2182868 store_id:17 > peers:<id:2182869 store_id:186 > peers:<id:2182867 store_id:365 > failed\ngithub.com/pingcap/tidb/br/pkg/restore.(*OverRegionsInRangeController).onError\n\t/tidb/br/pkg/restore/import_retry.go:56\ngithub.com/pingcap/tidb/br/pkg/restore.(*OverRegionsInRangeController).runInRegion\n\t/tidb/br/pkg/restore/import_retry.go:175\ngithub.com/pingcap/tidb/br/pkg/restore.(*OverRegionsInRangeController).runOverRegions\n\t/tidb/br/pkg/restore/import_retry.go:156\ngithub.com/pingcap/tidb/br/pkg/restore.(*OverRegionsInRangeController).Run\n\t/tidb/br/pkg/restore/import_retry.go:140\ngithub.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportKVFiles\n\t/tidb/br/pkg/restore/import.go:663\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreKVFiles.func2.1\n\t/tidb/br/pkg/restore/client.go:2733\ngithub.com/pingcap/tidb/pkg/util.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/tidb/pkg/util/worker_pool.go:81\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.7.0/errgroup/errgroup.go:78\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650"] [stack="github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreKVFiles\n\t/tidb/br/pkg/restore/client.go:2749\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream.func7\n\t/tidb/br/pkg/task/stream.go:1442\ngithub.com/pingcap/tidb/br/pkg/task.withProgress\n\t/tidb/br/pkg/task/stream.go:1572\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream\n\t/tidb/br/pkg/task/stream.go:1422\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\n\t/tidb/br/pkg/task/stream.go:1218\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/tidb/br/pkg/task/restore.go:668\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:75\nmain.newStreamRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:249\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267"]
```

the referenced stores 17, 186, and 365 correspond to tikv pods tikv-18-1a, tikv-20-1b, and tikv-33-1e respectively. I’ve attached logs from those tikvs around the time of the error (18:18:57Z).

It’s not immediately obvious to me from logs what the specific restore error is. I don’t see any s3 or external AWS errors from tikv logs during the restore. How can we determine what is going wrong during the restore and how should we best debug these kinds of restore errors?

Clinic: [[REDACTED_CLINIC_URL])

## Recent Comments Excerpt

### 2025-01-14T03:16:31.000+0800 [REDACTED_USER]

2.The traffic burst appears to be momentary, but the slowdown caused by throttling is sustained and lasts for a considerable period (around 30 minutes). Reducing the duration of throttling would significantly alleviate the issue.
can you explain how we determine this? Is this an observation that rate of throttled requests > 0 for >30min? the previous chart I shared is on log-scale, so there is only significant rate of throttled packets for a couple minutes around 00:47Z (>2k pps), and at all other times there is ~10s of pps throttled. Is the low rate of dropped/queued packets sufficient to slow down the restore process?
1.Although overall bandwidth usage is within reasonable limits, throttling was triggered, which could be due to the number of requests (similar to IOPS) exceeding certain thresholds.
we don’t observe pps exceeded throttling, so we don’t believe it is a matter of too many packets. However, AWS support suggests that the throttling is due to short bursts of bandwidth exceeded that we don’t observe in our metrics due to the high time granularity. The metric is reported at 15s granularity and we observe max bandwidth of ~200MB/s (1.6Gbps) for a single 15s sample. If the data transfer were concentrated in a short time range w/in the sample, we could still exceed the bandwidth limit. Is there a way to determine from tikv logs/metrics whether this is occurring? And if so, AWS’s suggestion is to pace the client traffic, is there a mechanism to do that w/in tikv?
also, from the investigation doc
Agreed. We need to implement flow control in BR to prevent crashes during the restore process. However, even with flow control in place, ensuring there are no slow download nodes remains critical to achieving the desired RTO in a disaster recovery scenario.
is there an issue/PR that we can track for this?

### 2025-01-15T11:12:24.000+0800 [REDACTED_USER]

I file an issue about the flow control on log restore: 
https://github.com/tikv/tikv/issues/18124

### 2025-01-22T09:38:29.057+0800 [REDACTED_USER]

From Airbnb: We ran 3 additional PITR tests that reduce the 
import.num-threads
 slightly (from 30 -> 28) and see all 3 successfully restored w/ significant improvement to TiKV memory usage. This seems to support the hypothesis that CPU starvation of non-import tasks contributes to TiKV OOM. We’d like to investigate that further to see if we can confirm that is the case by comparing results from PITRs using 30 and 28 threads.
For comparison I will use the initial failed restore included here (
[REDACTED_CLINIC_URL]
 ), where tikv-20-1b OOMed w/ 30 threads and 1d of logs, and a subsequent successful PITR for 3d of logs w/ 28 threads.
From failed restore, we can see the instance restart when it approaches the memory limit for the instance (128GB)
[REDACTED_MEDIA]

### 2025-01-22T10:42:21.258+0800 [REDACTED_USER]

TiKV OOM is a direct consequence of high CPU usage. When S3 download speeds slow down, tasks accumulate in the system, leading to an increased rate of context switching. This elevated context switching exacerbates CPU contention, ultimately contributing to TiKV’s OOM. 


As I showed before, from metrics we can see the source of import requests keep increased. (TiKV-Details → Import RPC Count). but the all components(import, raftdb, rocksdb) on that slow node become slow, that indicated the Higher CPU Usage.

Yes, the Raft engine plays a role in log replay during PITR (Point-in-Time Recovery). A lack of sufficient CPU resources for Raft tasks can indeed contribute to slowdowns and increased memory usage. However, the primary root cause is task accumulation due to slower processes, such as delayed S3 downloads, which create a cascading effect:
Accumulated tasks consume system resources, leading to CPU contention.
Reduced CPU availability impacts the Raft engine’s ability to replay logs efficiently.

### 2025-01-23T07:39:24.068+0800 [REDACTED_USER]

Here are the clinic metrics (
[REDACTED_CLINIC_URL]
) from a 28-thread PITR, which I shared in 
[REDACTED_SUPPORT_URL]
 . Note that this is not the same exact 28-thread PITR that I shared screenshots from above, but it is the same backup snapshot and same period of restored logs and instead uses higher concurrency of 2048, and the same trends I outlined in the metrics hold generally for this PITR as well.
