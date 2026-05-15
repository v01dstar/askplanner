# Issue 65911: PITR fails with no base id map found

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/65911
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-01-29T10:14:35Z
- Updated: 2026-01-30T08:21:57Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: PITR
- Components: TiDB, TiKV, BR, Storage, PD
- Categories: pitr-log-restore, storage-access, observability-diagnosis
- Labels: component/br, contribution, severity/moderate, type/bug, type/regression
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR fails with no base id map found`
- Search terms: BR; PD; PITR; Storage; TiDB; TiKV; observability-diagnosis; pitr-log-restore; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
1. create log backup
2. do full backup
3. run workload
4. do restore point 
5. wait a moment 
6. restore point again
```
Execute command {"command": " /br  restore  point "--storage" "s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]" "--pd" "http://downstream-pd.xxx:2379" "--restored-ts" "[REDACTED_LONG_ID]" "--start-ts" "[REDACTED_LONG_ID]" "--concurrency=8" "--check-requirements=false" "--checksum=true"", "timeout": "120m", "resource name": "br"}
```

### 2. [REDACTED_USER]
second restore point can success.

### 3. [REDACTED_USER]
second restore point failed: 
```
[2026/01/27 02:10:41.566 +00:00] [INFO] [collector.go:77] ["restore log failed summary"] [error="no base id map found from saved id or last restored PiTR"] [errorVerbose="no base id map found from saved id or last restored PiTR\ngithub.com/pingcap/tidb/br/pkg/restore/log_client.(*LogClient).GetBaseIDMapAndMerge\n\t/workspace/source/tidb/br/pkg/restore/log_client/client.go:1061\ngithub.com/pingcap/tidb/br/pkg/task.buildAndSaveIDMapIfNeeded\n\t/workspace/source/tidb/br/pkg/task/stream.go:2221\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream\n\t/workspace/source/tidb/br/pkg/task/stream.go:1621\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\n\t/workspace/source/tidb/br/pkg/task/stream.go:1469\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/workspace/source/tidb/br/pkg/task/restore.go:1003\nmain.runRestoreCommand\n\t/workspace/source/tidb/br/cmd/br/restore.go:91\nmain.newStreamRestoreCommand.func1\n\t/workspace/source/tidb/br/cmd/br/restore.go:265\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1015\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1148\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1071\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:42\nruntime.main\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/proc.go:285\nruntime.goexit\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/asm_amd64.s:1693"]
```

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
 Release Version: v9.0.0-beta.2.pre-1125-g5ee2924
Edition: Community
Git Commit Hash: 5ee2924cb1a162d49daff0e96b43d8efe35528ff
Git Branch: HEAD
UTC Build Time: 2026-01-27 12:06:45
GoVersion: go1.25.6
Race Enabled: false
Check Table Before Drop: false
Store: tikv
Kernel Type: Classic
