# Issue 53724: Import fails with [BR:PD:ErrPDBatchScanRegion]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/53724
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-05-31T10:51:30Z
- Updated: 2024-07-08T07:41:31Z
- Closed: 2024-07-08T07:41:31Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Import
- Components: TiDB, TiKV, BR, Lightning, PD
- Categories: restore-failure, region-split-scatter, sst-ingest-import, checkpoint-retry
- Labels: affects-6.5, affects-7.1, affects-7.5, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5

## Quick Match

- Title/error signature: `Import fails with [BR:PD:ErrPDBatchScanRegion]`
- Search terms: BR; Import; Lightning; PD; TiDB; TiKV; checkpoint-retry; region-split-scatter; restore-failure; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、br restore
2、pd rolling restart

### 2. [REDACTED_USER]
br restore success

### 3. [REDACTED_USER]
br restore failed
`error="region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region; region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region; region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region; region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region"] [errorVerbose="the following errors occurred:\n -  [BR:PD:ErrPDBatchScanRegion]batch scan region\n    region 714153's leader's store id is 0\n    github.com/pingcap/tidb/br/pkg/restore/split.CheckRegionConsistency\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:76\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion.func1\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:147\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:117\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1\n    \t/workspace/source/tidb/br/pkg/restore/import.go:548\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles\n    \t/workspace/source/tidb/br/pkg/restore/import.go:544\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2.1\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1458\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1459\n    github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n    \t/workspace/source/tidb/br/pkg/utils/worker.go:76\n    golang.org/x/sync/errgroup.(*Group).Go.func1\n    \t/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\n    runtime.goexit\n    \t/usr/local/go/src/runtime/asm_amd64.s:1650\n -  [BR:PD:ErrPDBatchScanRegion]batch scan region\n    region 714153's leader's store id is 0\n    github.com/pingcap/tidb/br/pkg/restore/split.CheckRegionConsistency\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:76\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion.func1\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:147\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:117\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1\n    \t/workspace/source/tidb/br/pkg/restore/import.go:548\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles\n    \t/workspace/source/tidb/br/pkg/restore/import.go:544\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2.1\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1458\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1459\n    github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n    \t/workspace/source/tidb/br/pkg/utils/worker.go:76\n    golang.org/x/sync/errgroup.(*Group).Go.func1\n    \t/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\n    runtime.goexit\n    \t/usr/local/go/src/runtime/asm_amd64.s:1650\n -  [BR:PD:ErrPDBatchScanRegion]batch scan region\n    region 714153's leader's store id is 0\n    github.com/pingcap/tidb/br/pkg/restore/split.CheckRegionConsistency\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:76\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion.func1\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:147\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:117\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1\n    \t/workspace/source/tidb/br/pkg/restore/import.go:548\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles\n    \t/workspace/source/tidb/br/pkg/restore/import.go:544\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2.1\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1458\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1459\n    github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n    \t/workspace/source/tidb/br/pkg/utils/worker.go:76\n    golang.org/x/sync/errgroup.(*Group).Go.func1\n    \t/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\n    runtime.goexit\n    \t/usr/local/go/src/runtime/asm_amd64.s:1650\n -  [BR:PD:ErrPDBatchScanRegion]batch scan region\n    region 714153's leader's store id is 0\n    github.com/pingcap/tidb/br/pkg/restore/split.CheckRegionConsistency\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:76\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion.func1\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:147\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore/split.PaginateScanRegion\n    \t/workspace/source/tidb/br/pkg/restore/split/split.go:117\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1\n    \t/workspace/source/tidb/br/pkg/restore/import.go:548\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:217\n    github.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:235\n    github.com/pingcap/tidb/br/pkg/utils.WithRetry\n    \t/workspace/source/tidb/br/pkg/utils/retry.go:216\n    github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles\n    \t/workspace/source/tidb/br/pkg/restore/import.go:544\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2.1\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1458\n    github.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2\n    \t/workspace/source/tidb/br/pkg/restore/client.go:1459\n    github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n    \t/workspace/source/tidb/br/pkg/utils/worker.go:76\n    golang.org/x/sync/errgroup.(*Group).Go.func1\n    \t/root/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\n    runtime.goexit\n    \t/usr/local/go/src/runtime/asm_amd64.s:1650"]
Error: region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region; region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region; region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region; region 714153's leader's store id is 0: [BR:PD:ErrPDBatchScanRegion]batch scan region`

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
