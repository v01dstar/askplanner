# Issue 56488: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56488
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-10-09T01:19:48Z
- Updated: 2024-10-09T03:40:51Z
- Closed: 2024-10-09T03:40:51Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: restore-failure
- Labels: component/br, severity/critical, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; Restore; TiDB; TiKV; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
br full restore

### 2. [REDACTED_USER]
br full restore success

### 3. [REDACTED_USER]
br full restore failed

`[2024/10/04 19:37:06.375 +00:00] [FATAL] [prewrite.go:402] ["tikv committed a non-1pc transaction with 1pc protocol"] [startTS=[REDACTED_LONG_ID] [stack="github.com/tikv/client-go/v2/txnkv/transaction.actionPrewrite.handleSingleBatch\n\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-58f3322fc39a/txnkv/transaction/prewrite.go:402\ngithub.com/tikv/client-go/v2/txnkv/transaction.(*twoPhaseCommitter).doActionOnBatches\n\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-58f3322fc39a/txnkv/transaction/2pc.go:1093\ngithub.com/tikv/client-go/v2/txnkv/transaction.(*twoPhaseCommitter).doActionOnGroupMutations\n\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-58f3322fc39a/txnkv/transaction/2pc.go:1054\ngithub.com/tikv/client-go/v2/txnkv/transaction.(*twoPhaseCommitter).doActionOnMutations\n\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-58f3322fc39a/txnkv/transaction/2pc.go:816\ngithub.com/tikv/client-go/v2/txnkv/transaction.(*twoPhaseCommitter).prewriteMutations\n\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-58f3322fc39a/txnkv/transaction/prewrite.go:510\ngithub.com/tikv/client-go/v2/txnkv/transaction.(*twoPhaseCommitter).execute\n\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-58f3322fc39a/txnkv/transaction/2pc.go:1769\ngithub.com/tikv/client-go/v2/txnkv/transaction.(*KVTxn).Commit\n\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-58f3322fc39a/txnkv/transaction/txn.go:760\ngithub.com/pingcap/tidb/pkg/store/driver/txn.(*tikvTxn).Commit\n\t/workspace/source/tidb/pkg/store/driver/txn/txn_driver.go:117\ngithub.com/pingcap/tidb/pkg/session.(*LazyTxn).Commit\n\t/workspace/source/tidb/pkg/session/txn.go:434\ngithub.com/pingcap/tidb/pkg/session.(*session).commitTxnWithTemporaryData\n\t/workspace/source/tidb/pkg/session/session.go:673\ngithub.com/pingcap/tidb/pkg/session.(*session).doCommit\n\t/workspace/source/tidb/pkg/session/session.go:553\ngithub.com/pingcap/tidb/pkg/session.(*session).doCommitWithRetry\n\t/workspace/source/tidb/pkg/session/session.go:795\ngithub.com/pingcap/tidb/pkg/session.(*session).CommitTxn\n\t/workspace/source/tidb/pkg/session/session.go:925\ngithub.com/pingcap/tidb/pkg/session.autoCommitAfterStmt\n\t/workspace/source/tidb/pkg/session/tidb.go:288\ngithub.com/pingcap/tidb/pkg/session.finishStmt\n\t/workspace/source/tidb/pkg/session/tidb.go:250\ngithub.com/pingcap/tidb/pkg/session.runStmt\n\t/workspace/source/tidb/pkg/session/session.go:2322\ngithub.com/pingcap/tidb/pkg/session.(*session).ExecuteStmt\n\t/workspace/source/tidb/pkg/session/session.go:2153\ngithub.com/pingcap/tidb/pkg/session.(*session).ExecuteInternal\n\t/workspace/source/tidb/pkg/session/session.go:1526\ngithub.com/pingcap/tidb/br/pkg/gluetidb.(*tidbSession).ExecuteInternal\n\t/workspace/source/tidb/br/pkg/gluetidb/glue.go:203\ngithub.com/pingcap/tidb/br/pkg/gluetidb.(*tidbSession).Execute\n\t/workspace/source/tidb/br/pkg/gluetidb/glue.go:198\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).replaceTemporaryTableToSystable.func1\n\t/workspace/source/tidb/br/pkg/restore/snap_client/systable_restore.go:228\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).replaceTemporaryTableToSystable\n\t/workspace/source/tidb/br/pkg/restore/snap_client/systable_restore.go:291\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).restoreSystemSchema\n\t/workspace/source/tidb/br/pkg/restore/snap_client/systable_restore.go:146\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).RestoreSystemSchemas\n\t/workspace/source/tidb/br/pkg/restore/snap_client/systable_restore.go:104\ngithub.com/pingcap/tidb/br/pkg/task.runSnapshotRestore\n\t/workspace/source/tidb/br/pkg/task/restore.go:1159\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/workspace/source/tidb/br/pkg/task/restore.go:704\nmain.runRestoreCommand\n\t/workspace/source/tidb/br/cmd/br/restore.go:75\nmain.newFullRestoreCommand.func1\n\t/workspace/source/tidb/br/cmd/br/restore.go:181\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267"`

### 4. [REDACTED_USER]
./br -V
 Release Version: v8.4.0-alpha-345-gdf821b9bce
Git Commit Hash: df821b9bce05ad62f7a4888f81d082584e35e9e5
Git Branch: HEAD
Go Version: go1.23.2
UTC Build Time: 2024-10-08 16:50:00
Race Enabled: false
