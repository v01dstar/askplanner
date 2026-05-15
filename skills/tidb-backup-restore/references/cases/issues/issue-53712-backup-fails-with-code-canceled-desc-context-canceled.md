# Issue 53712: Backup fails with code = Canceled desc = context canceled

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/53712
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-05-31T07:36:42Z
- Updated: 2024-10-25T09:39:50Z
- Closed: 2024-10-25T09:39:49Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR, PD
- Categories: backup-failure, checkpoint-retry, observability-diagnosis
- Labels: component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/major, type/bug
- Affected versions: may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `Backup fails with code = Canceled desc = context canceled`
- Search terms: BR; Backup; PD; TiDB; TiKV; backup-failure; checkpoint-retry; observability-diagnosis

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br backup
2、pd rolling restart
br log：
[br.log.2024-05-30T09.45.36Z.tar.gz]([REDACTED_ATTACHMENT_URL])

### 2. [REDACTED_USER]
br backup can success

### 3. [REDACTED_USER]
br backup failed
`[error="rpc error: code = Canceled desc = context canceled"] [errorVerbose="rpc error: code = Canceled desc = context canceled\ngithub.com/tikv/pd/client.(*client).respForErr\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1602\ngithub.com/tikv/pd/client.(*client).GetAllStores\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1193\ngithub.com/pingcap/tidb/br/pkg/conn/util.GetAllTiKVStores\n\t/workspace/source/tidb/br/pkg/conn/util/util.go:48\ngithub.com/pingcap/tidb/br/pkg/conn.GetAllTiKVStoresWithRetry.func1\n\t/workspace/source/tidb/br/pkg/conn/conn.go:83\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n\t/workspace/source/tidb/br/pkg/utils/retry.go:217\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n\t/workspace/source/tidb/br/pkg/utils/retry.go:235\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry\n\t/workspace/source/tidb/br/pkg/utils/retry.go:216\ngithub.com/pingcap/tidb/br/pkg/conn.GetAllTiKVStoresWithRetry\n\t/workspace/source/tidb/br/pkg/conn/conn.go:80\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRange\n\t/workspace/source/tidb/br/pkg/backup/client.go:917\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRanges.func2\n\t/workspace/source/tidb/br/pkg/backup/client.go:876\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/workspace/source/tidb/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650"] [unit-name="range start:7480000000000000f15f69800000000000000100 end:7480000000000000f15f698000000000000001fb"] [error="rpc error: code = Canceled desc = context canceled"] [errorVerbose="rpc error: code = Canceled desc = context canceled\ngithub.com/tikv/pd/client.(*client).respForErr\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1602\ngithub.com/tikv/pd/client.(*client).GetAllStores\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1193\ngithub.com/pingcap/tidb/br/pkg/conn/util.GetAllTiKVStores\n\t/workspace/source/tidb/br/pkg/conn/util/util.go:48\ngithub.com/pingcap/tidb/br/pkg/conn.GetAllTiKVStoresWithRetry.func1\n\t/workspace/source/tidb/br/pkg/conn/conn.go:83\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n\t/workspace/source/tidb/br/pkg/utils/retry.go:217\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n\t/workspace/source/tidb/br/pkg/utils/retry.go:235\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry\n\t/workspace/source/tidb/br/pkg/utils/retry.go:216\ngithub.com/pingcap/tidb/br/pkg/conn.GetAllTiKVStoresWithRetry\n\t/workspace/source/tidb/br/pkg/conn/conn.go:80\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRange\n\t/workspace/source/tidb/br/pkg/backup/client.go:917\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRanges.func2\n\t/workspace/source/tidb/br/pkg/backup/client.go:876\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/workspace/source/tidb/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650"] [unit-name="range start:74800000000000010a5f69800000000000000100 end:74800000000000010a5f698000000000000001fb"] [error="rpc error: code = Canceled desc = context canceled"] [errorVerbose="rpc error: code = Canceled desc = context canceled\ngithub.com/tikv/pd/client.(*client).respForErr\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1602\ngithub.com/tikv/pd/client.(*client).GetAllStores\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1193`

### 4. [REDACTED_USER]
./tidb-server -V
 Release Version: v7.5.2
Edition: Community
Git Commit Hash: 39ea2b30d32ab8cf486f30ca318cf2e4bd99eaef
Git Branch: HEAD
UTC Build Time: 2024-05-29 15:07:12
GoVersion: go1.21.10
Race Enabled: false
Check Table Before Drop: false
Store: unistore
2024-05-30T14:14:32.686+0800
