# Issue 61226: PITR fails with nil pointer

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61226
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-05-21T01:49:08Z
- Updated: 2025-05-28T07:44:53Z
- Closed: 2025-05-22T18:58:17Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR, Storage, PD
- Categories: pitr-log-restore, storage-access, performance-resource, observability-diagnosis
- Labels: component/br, feature/developing, impact/panic, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR fails with nil pointer`
- Search terms: BR; PD; PITR; Storage; TiDB; observability-diagnosis; performance-resource; pitr-log-restore; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

- first step: pitr with full backup, log backup, and restore-ts `[REDACTED_LONG_ID]`

```
/br  restore  point --storage s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] --pd http://downstream-pd.brie-acceptance-pitr-tps-7864765-1-953:2379 --restored-ts [REDACTED_LONG_ID] --[REDACTED_RESOURCE_NAME] s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] --concurrency=8 --check-requirements=false
```

- second step: log restore only with start-ts `[REDACTED_LONG_ID]`
```
/br  restore  point --storage s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] --pd http://downstream-pd.brie-acceptance-pitr-tps-7864765-1-953:2379 --restored-ts [REDACTED_LONG_ID] --start-ts [REDACTED_LONG_ID] --concurrency=8 --check-requirements=false
```

### 2. [REDACTED_USER]
success when log restore only

### 3. [REDACTED_USER]
first step success, and second step panic
```
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x5c0f1ba]

goroutine 1 [running]:
github.com/pingcap/tidb/br/pkg/utils.(*PiTRIdTracker).ContainsDB(...)
/workspace/source/tidb/br/pkg/utils/filter.go:120
github.com/pingcap/tidb/br/pkg/stream.(*TableMappingManager).ApplyFilterToDBReplaceMap(0xc001892b40?,0x0)
/workspace/source/tidb/br/pkg/stream/table_mapping.go:472+0x9a
github.com/pingcap/tidb/br/pkg/task.buildAndSaveIDMapIfNeeded({0x79d8130, 0xc0036f0640}, 0xc001892b40, 0xc0035c4800)
/workspace/source/tidb/br/pkg/task/stream.go:2134 +0xb3
github.com/pingcap/tidb/br/pkg/task.restoreStream({0x79d8130, 0xc001c5bb80}, 0xc00139d900, {0x79face0, 0xc0018df1e0}, 0xc0035c4800)
/workspace/source/tidb/br/pkg/task/stream.go:1562 +0xaa5
github.com/pingcap/tidb/br/pkg/task.RunStreamRestore({0x79d8130?, 0xc001c5a1e0?}, 0xc00139d900, {0x79face0, 0xc0018df1e0}, 0xc001c4ea08)
/workspace/source/tidb/br/pkg/task/stream.go:1422 +0x1266
github.com/pingcap/tidb/br/pkg/task.RunRestore({0x79d8130, 0xc001c5a1e0}, {0x79face0, 0xc0018df1e0}, {0x706afa7, 0xd}, 0xc001c4ea08)
/workspace/source/tidb/br/pkg/task/restore.go:818 +0x42e
main.runRestoreCommand(0xc001c8a608, {0x706afa7, 0xd})
/workspace/source/tidb/br/cmd/br/restore.go:80 +0x739
main.newStreamRestoreCommand.func1(0xc001c8a608?, {0xc001ca0dc0?, 0x4?,0x704cac7?})
/workspace/source/tidb/br/cmd/br/restore.go:254 +0x1f
github.com/spf13/cobra.(*Command).execute(0xc001c8a608, {0xc0000746b0, 0xa,0xa})
/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1015 +0xa94
github.com/spf13/cobra(*Command).ExecuteC(0xc000c2c308)
/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1148 +0x40c
github.com/spf13/cobra(*Command).Execute(...)
/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1071
main.main()
/workspace/source/tidb/br/cmd/br/main.go:37 +0x23a
```

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
[release-version=v9.0.0-beta.1.pre-761-ge3478a5] [git-hash=e3478a5c15ea0322aad1a7fd0ee05371a6972b20] [git-branch=HEAD] [go-version=go1.23.9] [utc-build-time="2025-05-20 06:16:39"] [race-enabled=false]
