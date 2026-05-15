# Issue 56228: Restore fails with [BR:Common:ErrInvalidRange]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56228
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-09-23T08:55:01Z
- Updated: 2024-09-30T04:12:12Z
- Closed: 2024-09-30T04:12:12Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR, Storage, PD
- Categories: storage-access, region-split-scatter, checkpoint-retry
- Labels: component/br, severity/moderate, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore fails with [BR:Common:ErrInvalidRange]`
- Search terms: BR; PD; Restore; Storage; TiDB; TiKV; checkpoint-retry; region-split-scatter; storage-access

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/52574

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. TiKV has region endKey is ""
2. backup txn (sucess)
3. restore txn (failed)

### 2. [REDACTED_USER]
restore txn always success.
### 3. [REDACTED_USER]
restore txn failed with error, report startKey > endKey, endKey was `0000000000000000f7`. Due to tikv encode rule, empty byte slice will encode as `0000000000000000f7`. And also I checked my tikv cluster, it did have a region, which endKey was `""`.

Same Issue also seen in` Restore txn kv fails and reports ErrRestoreInvalidRange ` #52574 , although this issue was resolved by pr https://github.com/pingcap/tidb/commit/80d4dec1c07038cf8f81746158ebca5c28720def.

but I find the br function `SplitKeysAndScatter` in `br/pkg/restore/split/client.go
`
https://github.com/pingcap/tidb/blob/master/br/pkg/restore/split/client.go#L536-L566 also encode the lastKey without check the lastKey is empty slices. and then it call `PaginateScanRegion`, which throw the  error.

I guess It was some issue like https://github.com/pingcap/tidb/issues/52574

report error：
```
[2024/09/23 13:33:05.816 +08:00] [ERROR] [main.go:38] ["br failed"] [error="startKey > endKey, startKey: 63616665fd448403ff0800000000000000ff000000002aff0000fd, endkey: 0000000000000000f7: [BR:Common:ErrInvalidRange]invalid restore range"] [errorVerbose="[BR:Common:ErrInvalidRange]invalid restore range\nstartKey > endKey, startKey: 63616665fd448403ff0800000000000000ff000000002aff0000fd, endkey: 0000000000000000f7\ngithub.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion\n\t/workspace/source/tidb/br/pkg/restore/split/split.go:100\ngithub.com/pingcap/tidb/br/pkg/restore/split.(*pdClient).SplitKeysAndScatter.func1\n\t/workspace/source/tidb/br/pkg/restore/split/client.go:566\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetryReturnLastErr\n\t/workspace/source/tidb/br/pkg/utils/retry.go:94\ngithub.com/pingcap/tidb/br/pkg/restore/split.(*pdClient).SplitKeysAndScatter\n\t/workspace/source/tidb/br/pkg/restore/split/client.go:558\ngithub.com/pingcap/tidb/br/pkg/restore/internal/snap_split.(*RegionSplitter).executeSplitByKeys\n\t/workspace/source/tidb/br/pkg/restore/internal/snap_split/split.go:89\ngithub.com/pingcap/tidb/br/pkg/restore/internal/snap_split.(*RegionSplitter).executeSplitByRanges\n\t/workspace/source/tidb/br/pkg/restore/internal/snap_split/split.go:72\ngithub.com/pingcap/tidb/br/pkg/restore/internal/snap_split.(*RegionSplitter).ExecuteSplit\n\t/workspace/source/tidb/br/pkg/restore/internal/snap_split/split.go:48\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).SplitPoints\n\t/workspace/source/tidb/br/pkg/restore/snap_client/tikv_sender.go:352\ngithub.com/pingcap/tidb/br/pkg/task.RunRestoreTxn\n\t/workspace/source/tidb/br/pkg/task/restore_txn.go:91\nmain.runRestoreTxnCommand\n\t/workspace/source/tidb/br/cmd/br/restore.go:136\nmain.newTxnRestoreCommand.func1\n\t/workspace/source/tidb/br/cmd/br/restore.go:235\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650"] [stack="main.main\n\t/workspace/source/tidb/br/cmd/br/main.go:38\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267"]
```
### 4. [REDACTED_USER]

Only Tikv and pd （v5.0.6)

br(v8.4.0-nigthly)
