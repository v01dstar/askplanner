# Issue 63358: Backup/Restore fails with nil pointer

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/63358
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-09-03T09:46:30Z
- Updated: 2025-09-19T06:46:46Z
- Closed: 2025-09-19T06:46:46Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: TiDB, BR
- Categories: performance-resource, observability-diagnosis
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Backup/Restore fails with nil pointer`
- Search terms: BR; Backup/Restore; TiDB; observability-diagnosis; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

Perform `br log truncate --until`

### 2. [REDACTED_USER]

Truncate happens successfully.

### 3. [REDACTED_USER]

Panics with this stack trace:

```
We are going to truncate 3030 files, up to TS 2025-09-03 01:42:23.0000.
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x10 pc=0х5848f74]

goroutine 3865 [running]:
github.com/pingcap/tidb/br/pkg/stream.MigrationExt.cleanUpFor({...}, 0x4002720fc0, 0x400084eed8)
    /.../release/tidb/br/pkg/stream/stream_netas.go:896 +0x584
github.com/pingcap/tidb/br/pkg/stream.MigrationExt.doTruncateLogs.func3()
    /.../release/tidb/br/pkg/stream/stream_metas.go:1102 +0x2c4
...
```

### 4. [REDACTED_USER]

v8.5.1
