# Issue 53723: Import fails with nil pointer

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/53723
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-05-31T10:45:47Z
- Updated: 2024-07-29T09:32:13Z
- Closed: 2024-07-29T09:28:24Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Import
- Components: TiDB, TiKV, BR, Lightning, PD
- Categories: region-split-scatter, sst-ingest-import, checkpoint-retry, performance-resource
- Labels: affects-6.5, affects-7.1, affects-7.5, component/br, impact/panic, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5

## Quick Match

- Title/error signature: `Import fails with nil pointer`
- Search terms: BR; Import; Lightning; PD; TiDB; TiKV; checkpoint-retry; performance-resource; region-split-scatter; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、br restore
2、inject pd io delay 1s

### 2. [REDACTED_USER]
br restore success

### 3. [REDACTED_USER]
br failed with panic
`panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x280a3e5]
goroutine 9160 [running]:
github.com/tikv/pd/client.(*client).ScanRegions(0xc00082a000, {0x68a7ea8, 0xc00feaed20}, {0xc00fcb1f60, 0x1b, 0x1b}, {0xc00fcb1f80, 0x1b, 0x1b}, 0x80)
	/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1086 +0x625
github.com/pingcap/tidb/br/pkg/restore/split.(*pdClient).ScanRegions(0x100000001?, {0x68a7ea8?, 0xc00feaed20?}, {0xc00fcb1f60?, 0x0?, 0x1a3185c5000?}, {0xc00fcb1f80?, 0x0?, 0x0?}, 0x80)
	/workspace/source/tidb/br/pkg/restore/split/client.go:523 +0x57
github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion.func1()
	/workspace/source/tidb/br/pkg/restore/split/split.go:122 +0x186
github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1({0x0?, 0x0?})
	/workspace/source/tidb/br/pkg/utils/retry.go:217 +0x13
github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]({0x68a7ea8?, 0xc00feaed20}, {0x6884188, 0xc00fcb1fa0}, 0xc00213aba0)
	/workspace/source/tidb/br/pkg/utils/retry.go:235 +0x98
github.com/pingcap/tidb/br/pkg/utils.WithRetry({0x68a7ea8?, 0xc00feaed20?}, 0x0?, {0x6884188?, 0xc00fcb1fa0?})
	/workspace/source/tidb/br/pkg/utils/retry.go:216 +0x50
github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion({0x68a7ea8?, 0xc00feaed20?}, {0x68cfe00?, 0xc002131100}, {0xc00fcb1f60, 0x1b, 0x1b}, {0xc00fcb1f80, 0x1b, 0x1b}, ...)
	/workspace/source/tidb/br/pkg/restore/split/split.go:117 +0x2ab
github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1()
	/workspace/source/tidb/br/pkg/restore/import.go:548 +0x179
github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1({0x57034a0?, 0xc00fead1d0?})
	/workspace/source/tidb/br/pkg/utils/retry.go:217 +0x13
github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]({0x68a7e38?, 0xc00a08e0a0}, {0x687da68, 0xc00fce5b40}, 0xc00213ba38)
	/workspace/source/tidb/br/pkg/utils/retry.go:235 +0x98
github.com/pingcap/tidb/br/pkg/utils.WithRetry({0x68a7e38?, 0xc00a08e0a0?}, 0x1?, {0x687da68?, 0xc00fce5b40?})
	/workspace/source/tidb/br/pkg/utils/retry.go:216 +0x50
github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles(0xc001f44020, {0x68a7e38?, 0xc00a08e0a0}, {0xc008fcf9e0?, 0x1, 0xc4}, 0xc004b56910, 0xc000ea4bb0, 0x0)
	/workspace/source/tidb/br/pkg/restore/import.go:544 +0x445
github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2.1(0xc009aecef0, {0x68a7cb0?, 0xc004e44fc0}, 0xc001f44000, {0x68a7e38, 0xc00a08e0a0}, 0x0?, {0xc008fcf9e0, 0x1, 0xc4})
	/workspace/source/tidb/br/pkg/restore/client.go:1458 +0x17c
github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2()
	/workspace/source/tidb/br/pkg/restore/client.go:1459 +0x1bd
github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1()
	/workspace/source/tidb/br/pkg/utils/worker.go:76 +0x6c
golang.org/x/sync/errgroup.(*Group).Go.func1()
	/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75 +0x56
created by golang.org/x/sync/errgroup.(*Group).Go in goroutine 2632
	/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:72 +0x96
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x280a3e5]
goroutine 9323 [running]:
github.com/tikv/pd/client.(*client).ScanRegions(0xc00082a000, {0x68a7ea8, 0xc00f38aa10}, {0xc00f3f42a0, 0x1b, 0x1b}, {0xc00f3f42c0, 0x1b, 0x1b}, 0x80)
	/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-634e05a87ee0/client.go:1086 +0x625
github.com/pingcap/tidb/br/pkg/restore/split.(*pdClient).ScanRegions(0x0?, {0x68a7ea8?, 0xc00f38aa10?}, {0xc00f3f42a0?, 0x0?, 0x0?}, {0xc00f3f42c0?, 0x0?, 0x0?}, 0x80)
	/workspace/source/tidb/br/pkg/restore/split/client.go:523 +0x57
github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion.func1()
	/workspace/source/tidb/br/pkg/restore/split/split.go:122 +0x186
github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1({0x0?, 0x0?})
	/workspace/source/tidb/br/pkg/utils/retry.go:217 +0x13
github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]({0x68a7ea8?, 0xc00f38aa10}, {0x6884188, 0xc00f3f42e0}, 0xc006524ba0)
	/workspace/source/tidb/br/pkg/utils/retry.go:235 +0x98
github.com/pingcap/tidb/br/pkg/utils.WithRetry({0x68a7ea8?, 0xc00f38aa10?}, 0x0?, {0x6884188?, 0xc00f3f42e0?})
	/workspace/source/tidb/br/pkg/utils/retry.go:216 +0x50
github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion({0x68a7ea8?, 0xc00f38aa10?}, {0x68cfe00?, 0xc002131100}, {0xc00f3f42a0, 0x1b, 0x1b}, {0xc00f3f42c0, 0x1b, 0x1b}, ...)
	/workspace/source/tidb/br/pkg/restore/split/split.go:117 +0x2ab
github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1()
	/workspace/source/tidb/br/pkg/restore/import.go:548 +0x179
github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1({0x1e2554f?, 0x7f629c662e60?})
	/workspace/source/tidb/br/pkg/utils/retry.go:217 +0x13
github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]({0x68a7e38?, 0xc009f7a0f0}, {0x687da68, 0xc00f3ecfe0}, 0xc006525a38)
	/workspace/source/tidb/br/pkg/utils/retry.go:235 +0x98
github.com/pingcap/tidb/br/pkg/utils.WithRetry({0x68a7e38?, 0xc009f7a0f0?}, 0x1?, {0x687da68?, 0xc00f3ecfe0?})
	/workspace/source/tidb/br/pkg/utils/retry.go:216 +0x50
github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles(0xc001f44020, {0x68a7e38?, 0xc009f7a0f0}, {0xc006f970d0?, 0x1, 0xe6}, 0xc004b56c30, 0xc000ea4bb0, 0x0)
	/workspace/source/tidb/br/pkg/restore/import.go:544 +0x445
github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2.1(0xc00f8beef0, {0x68a7cb0?, 0xc004e44fc0}, 0xc001f44000, {0x68a7e38, 0xc009f7a0f0}, 0x0?, {0xc006f970d0, 0x1, 0xe6})
	/workspace/source/tidb/br/pkg/restore/client.go:1458 +0x17c
github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2()
	/workspace/source/tidb/br/pkg/restore/client.go:1459 +0x1bd
github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1()
	/workspace/source/tidb/br/pkg/utils/worker.go:76 +0x6c
golang.org/x/sync/errgroup.(*Group).Go.func1()
	/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75 +0x56
created by golang.org/x/sync/errgroup.(*Group).Go in goroutine 5700
	/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:72 +0x96`

### 4. [REDACTED_USER]
tidb version:
./tidb-server -V
Release Version: v7.5.2
Edition: Community
Git Commit Hash: https://github.com/pingcap/tidb/commit/39ea2b30d32ab8cf486f30ca318cf2e4bd99eaef
Git Branch: HEAD
UTC Build Time: 2024-05-29 15:07:12
GoVersion: go1.21.10
Race Enabled: false
Check Table Before Drop: false
Store: unistore
2024-05-30T14:14:32.686+0800
