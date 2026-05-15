# GTOC-7347: PITR fails with EOF] [stack=

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7347
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-01-10T02:47:04.000+0800
- Updated: 2025-03-06T17:39:05.168+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

PITR is failing when trying to run a restore over a longer period of logs (3d) than in [https://jira.tidbcloud.com/browse/GTOC-7320](https://jira.tidbcloud.com/browse/GTOC-7320) (1d). However, we believe it is a different issue because the restore is failing during the meta restore phase, and we don’t observe any TiKV OOMs.

We observe the error:  
 

```java
{{cluster [REDACTED_CLUSTER]/baseline-2-3d, wait pipe message failed, errMsg [2025/01/08 19:22:17.946 +00:00] [ERROR] [advancer.go:400] ["listen task meet error, would reopen."] [error=EOF] [stack="github.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).StartTaskListener.func1\n\t/tidb/br/pkg/streamhelper/advancer.go:400"][2025/01/08 20:10:54.888 +00:00] [ERROR] [advancer.go:400] ["listen task meet error, would reopen."] [error=EOF] [stack="github.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).StartTaskListener.func1\n\t/tidb/br/pkg/streamhelper/advancer.go:400"]
[2025/01/08 21:02:50.499 +00:00] [ERROR] [advancer.go:400] ["listen task meet error, would reopen."] [error=EOF] [stack="github.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).StartTaskListener.func1\n\t/tidb/br/pkg/streamhelper/advancer.go:400"]
[2025/01/08 21:02:51.760 +00:00] [ERROR] [restore.go:76] ["failed to restore"] [error="failed to restore meta files: rpcClient is idle"] [errorVerbose="rpcClient is idle\ngithub.com/tikv/client-go/v2/internal/client.(*RPCClient).getConnArray\n\t/tidb/tikv-client-go/internal/client/client.go:495\ngithub.com/tikv/client-go/v2/internal/client.(*RPCClient).sendRequest\n\t/tidb/tikv-client-go/internal/client/client.go:661\ngithub.com/tikv/client-go/v2/internal/client.(*RPCClient).SendRequest\n\t/tidb/tikv-client-go/internal/client/client.go:742\ngithub.com/tikv/client-go/v2/internal/locate.(*RegionRequestSender).sendReqToRegion\n\t/tidb/tikv-client-go/internal/locate/region_request.go:2051\ngithub.com/tikv/client-go/v2/internal/locate.(*RegionRequestSender).SendReqCtx\n\t/tidb/tikv-client-go/internal/locate/region_request.go:1807\ngithub.com/tikv/client-go/v2/internal/locate.(*RegionRequestSender).SendReq\n\t/tidb/tikv-client-go/internal/locate/region_request.go:433\ngithub.com/tikv/client-go/v2/rawkv.(*Client).doBatchPut\n\t/tidb/tikv-client-go/rawkv/rawkv.go:942\ngithub.com/tikv/client-go/v2/rawkv.(*Client).sendBatchPut.func1\n\t/tidb/tikv-client-go/rawkv/rawkv.go:900\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\ngithub.com/tikv/client-go/v2/rawkv.(*Client).sendBatchPut\n\t/tidb/tikv-client-go/rawkv/rawkv.go:908\ngithub.com/tikv/client-go/v2/rawkv.(*Client).BatchPutWithTTL\n\t/tidb/tikv-client-go/rawkv/rawkv.go:421\ngithub.com/tikv/client-go/v2/rawkv.(*Client).BatchPut\n\t/tidb/tikv-client-go/rawkv/rawkv.go:403\ngithub.com/pingcap/tidb/br/pkg/restore.(*RawKVBatchClient).Put\n\t/tidb/br/pkg/restore/rawkv_client.go:94\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).restoreMetaKvEntries\n\t/tidb/br/pkg/restore/client.go:3277\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreBatchMetaKVFiles\n\t/tidb/br/pkg/restore/client.go:3232\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreMetaKVFilesWithBatchMethod\n\t/tidb/br/pkg/restore/client.go:3160\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreMetaKVFiles\n\t/tidb/br/pkg/restore/client.go:3034\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream.func6\n\t/tidb/br/pkg/task/stream.go:1399\ngithub.com/pingcap/tidb/br/pkg/task.withProgress\n\t/tidb/br/pkg/task/stream.go:1575\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream\n\t/tidb/br/pkg/task/stream.go:1397\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\n\t/tidb/br/pkg/task/stream.go:1218\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/tidb/br/pkg/task/restore.go:668\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:75\nmain.newStreamRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:249\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/errors.go:178\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/juju_adaptor.go:15\ngithub.com/pingcap/tidb/br/pkg/restore.(*RawKVBatchClient).Put\n\t/tidb/br/pkg/restore/rawkv_client.go:96\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).restoreMetaKvEntries\n\t/tidb/br/pkg/restore/client.go:3277\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreBatchMetaKVFiles\n\t/tidb/br/pkg/restore/client.go:3232\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreMetaKVFilesWithBatchMethod\n\t/tidb/br/pkg/restore/client.go:3160\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreMetaKVFiles\n\t/tidb/br/pkg/restore/client.go:3034\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream.func6\n\t/tidb/br/pkg/task/stream.go:1399\ngithub.com/pingcap/tidb/br/pkg/task.withProgress\n\t/tidb/br/pkg/task/stream.go:1575\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream\n\t/tidb/br/pkg/task/stream.go:1397\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\n\t/tidb/br/pkg/task/stream.go:1218\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/tidb/br/pkg/task/restore.go:668\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:75\nmain.newStreamRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:249\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\nfailed to restore meta files"] [stack="main.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:76\nmain.newStreamRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:249\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267"]
[2025/01/08 21:02:51.760 +00:00] [ERROR] [main.go:38] ["br failed"] [error="failed to restore meta files: rpcClient is idle"] [errorVerbose="rpcClient is idle\ngithub.com/tikv/client-go/v2/internal/client.(*RPCClient).getConnArray\n\t/tidb/tikv-client-go/internal/client/client.go:495\ngithub.com/tikv/client-go/v2/internal/client.(*RPCClient).sendRequest\n\t/tidb/tikv-client-go/internal/client/client.go:661\ngithub.com/tikv/client-go/v2/internal/client.(*RPCClient).SendRequest\n\t/tidb/tikv-client-go/internal/client/client.go:742\ngithub.com/tikv/client-go/v2/internal/locate.(*RegionRequestSender).sendReqToRegion\n\t/tidb/tikv-client-go/internal/locate/region_request.go:2051\ngithub.com/tikv/client-go/v2/internal/locate.(*RegionRequestSender).SendReqCtx\n\t/tidb/tikv-client-go/internal/locate/region_request.go:1807\ngithub.com/tikv/client-go/v2/internal/locate.(*RegionRequestSender).SendReq\n\t/tidb/tikv-client-go/internal/locate/region_request.go:433\ngithub.com/tikv/client-go/v2/rawkv.(*Client).doBatchPut\n\t/tidb/tikv-client-go/rawkv/rawkv.go:942\ngithub.com/tikv/client-go/v2/rawkv.(*Client).sendBatchPut.func1\n\t/tidb/tikv-client-go/rawkv/rawkv.go:900\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\ngithub.com/tikv/client-go/v2/rawkv.(*Client).sendBatchPut\n\t/tidb/tikv-client-go/rawkv/rawkv.go:908\ngithub.com/tikv/client-go/v2/rawkv.(*Client).BatchPutWithTTL\n\t/tidb/tikv-client-go/rawkv/rawkv.go:421\ngithub.com/tikv/client-go/v2/rawkv.(*Client).BatchPut\n\t/tidb/tikv-client-go/rawkv/rawkv.go:403\ngithub.com/pingcap/tidb/br/pkg/restore.(*RawKVBatchClient).Put\n\t/tidb/br/pkg/restore/rawkv_client.go:94\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).restoreMetaKvEntries\n\t/tidb/br/pkg/restore/client.go:3277\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreBatchMetaKVFiles\n\t/tidb/br/pkg/restore/client.go:3232\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreMetaKVFilesWithBatchMethod\n\t/tidb/br/pkg/restore/client.go:3160\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreMetaKVFiles\n\t/tidb/br/pkg/restore/client.go:3034\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream.func6\n\t/tidb/br/pkg/task/stre

_Trimmed; see Jira for full context._

## Recent Comments Excerpt

### 2025-01-10T10:13:56.000+0800 [REDACTED_USER]

Looks like related to an old issue in client_go repo in TiKV. It happens when connection got recycled and at the same time request comes in to that connection. Adding a retry on BR side should prevent this problem since next time will create a new connection 
Added an issue on BR side to also track the problem 

https://github.com/pingcap/tidb/issues/58845

### 2025-01-10T10:39:00.000+0800 [REDACTED_USER]

more added
found that user restored most of the meta files are write cf with no value, so a lot of skipping as we can see in the log, that can explain why connection can time out and move to idle state and cause this race condition error.
[client.go:3013] ["start to restore meta files"] ["total files"=17403] ["default files"=99] ["write files"=17304]

### 2025-01-14T04:12:42.000+0800 [REDACTED_USER]

Thanks for the update and issue.
From the issue:
when it recycles the connection a request comes in and will fail with such error
so then we expect this issue to occur for restores w/ longer log meta restore durations? ie. that take enough time so that the cxn is recycled? I am wondering in terms of unblocking our testing for longer restore periods (than the 1d we’ve conducted tests for). Do we need this fix for running restores for longer time periods (longer log meta durations)?

### 2025-01-14T07:08:34.000+0800 [REDACTED_USER]

right, the connection will get idle timeout reset every time it's used. 
It could get triggered w/ longer meta restore and at the same time w/ tons of write files and few default files since we write default files to TiKV so those conns are used but skip most of the write files.
I feel like it's safer to have the fix, let me confirm with the team

### 2025-01-21T08:41:52.797+0800 [REDACTED_USER]

Update from Airbnb: We are running a long PITR (3d) using a debug build from the 
referenced PR
 and the PITR successfully completed the meta restore phase, and I see a log from the new retry logic:
I0117 20:36:54.408726 9 restore.go:176] [2025/01/17 20:36:54.408 +00:00] [WARN] [client.go:3306] ["raw kv client put got error, retrying"] [error="rpcClient is idle"] [retry-after=500ms]
we will wait for the final version of the fix to merge before cherry-picking to our internal release, but otherwise the fix looks like it’s working for us. We will update if we see any other issues, but feel free to close this next week
