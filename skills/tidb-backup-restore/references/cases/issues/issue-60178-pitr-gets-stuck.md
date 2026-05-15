# Issue 60178: PITR gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60178
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-19T11:10:26Z
- Updated: 2025-03-20T08:04:00Z
- Closed: 2025-03-20T08:04:00Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, restore-failure, performance-resource
- Labels: affects-9.0, component/br, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/critical, type/bug
- Affected versions: affects-9.0, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `PITR gets stuck`
- Search terms: BR; PITR; TiDB; performance-resource; pitr-log-restore; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
do PiTR on a DBaaS Cluster

### 2. [REDACTED_USER]
PiTR success

### 3. [REDACTED_USER]
always in restoring state

[REDACTED_ATTACHMENT]

[ERROR] [main.go:38] ["br failed"] [error="PiTR doesn't support custom filter to include system db, consider to exclude system db: [BR:Common:ErrInvalidArgument]invalid argument"] [errorVerbose="[BR:Common:ErrInvalidArgument]invalid argument\nPiTR doesn't support custom filter to include system db, consider to exclude system db\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\n\t/workspace/source/tidb/br/pkg/task/stream.go:1371\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/workspace/source/tidb/br/pkg/task/restore.go:814\nmain.runRestoreCommand\n\t/workspace/source/tidb/br/cmd/br/restore.go:80\nmain.newStreamRestoreCommand.func1\n\t/workspace/source/tidb/br/cmd/br/restore.go:254\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:37\nruntime.main\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/proc.go:272\nruntime.goexit\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/asm_amd64.s:1700"] [stack="main.main\n\t/workspace/source/tidb/br/cmd/br/main.go:38\nruntime.main\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/proc.go:272"]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
v9.0.0.beta.1
