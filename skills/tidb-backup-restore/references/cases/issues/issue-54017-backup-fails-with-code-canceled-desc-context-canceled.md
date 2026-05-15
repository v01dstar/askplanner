# Issue 54017: Backup fails with code = Canceled desc = context canceled

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/54017
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-06-14T02:21:57Z
- Updated: 2024-07-24T10:04:48Z
- Closed: 2024-06-21T01:49:38Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR, PD
- Categories: backup-failure, checkpoint-retry
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `Backup fails with code = Canceled desc = context canceled`
- Search terms: BR; Backup; PD; TiDB; TiKV; backup-failure; checkpoint-retry

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br backup
2、kill pd leader or injection network partition between pd leader and pd followers

### 2. [REDACTED_USER]
br backup can success

### 3. [REDACTED_USER]
br backup failed

`(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.7.0/errgroup/errgroup.go:78\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"] [unit-name="range start:74800000000000014f5f720000000000000000 end:74800000000000014f5f72ffffffffffffffff00"] [error="rpc error: code = Canceled desc = context canceled"] [errorVerbose="rpc error: code = Canceled desc = context canceled\ngithub.com/tikv/pd/client.(*client).respForErr\n\t/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-947701a32c05/client.go:1942\ngithub.com/tikv/pd/client.(*client).GetAllStores\n\t/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-947701a32c05/client.go:1611\ngithub.com/pingcap/tidb/br/pkg/conn/util.GetAllTiKVStores\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/conn/util/util.go:48\ngithub.com/pingcap/tidb/br/pkg/conn.GetAllTiKVStoresWithRetry.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/conn/conn.go:82\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:216\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:234\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:215\ngithub.com/pingcap/tidb/br/pkg/conn.GetAllTiKVStoresWithRetry\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/conn/conn.go:79\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRange\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/backup/client.go:880\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRanges.func2\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/backup/client.go:839\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.7.0/errgroup/errgroup.go:78\nruntime.goexit`

[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]
./tidb-server -V
 Release Version: v6.5.10
Edition: Community
Git Commit Hash: 23062507bab86d03a616c2793607c3f4dd349235
Git Branch: heads/refs/tags/v6.5.10
UTC Build Time: 2024-06-12 08:25:43
GoVersion: go1.19.13
Race Enabled: false
TiKV Min Version: 6.2.0-alpha
Check Table Before Drop: false
Store: unistore
2024-06-13T06:58:24.395+0800
