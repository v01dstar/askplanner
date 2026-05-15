# Issue 60233: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60233
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-03-24T07:22:40Z
- Updated: 2025-07-09T04:02:57Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR, Storage
- Categories: restore-failure, storage-access, schema-metadata, checkpoint-retry, observability-diagnosis
- Labels: component/br, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Restore; Storage; TiDB; TiKV; checkpoint-retry; observability-diagnosis; restore-failure; schema-metadata; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. restore to cluster
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
no error
### 3. [REDACTED_USER]
console shows restore success
```
Detail BR log in /tmp/br.log.2025-03-21T08.52.26Z
[2025/03/21 10:49:16.921 +00:00] [INFO] [collector.go:77] ["Full Restore success summary"] [total-ranges=8637] [ranges-succeed=8637] [range
s-failed=0] [restore-files=1h39m15.105158713s] [restore-pipeline=14m50.439864315s] [merge-ranges=72.253028ms] [split-regions=29.436590878s]
 [default-CF-files=0] [write-CF-files=8637] [split-keys=8633] [total-take=1h56m50.68558604s] [RestoreTS=[REDACTED_LONG_ID] [total-kv=12000
000000] [total-kv-size=1.524TB] [average-speed=217.4MB/s] [restore-data-size(after-compressed)=657.4GB] [Size=[REDACTED_LONG_ID] [BackupTS=45498
[REDACTED_LONG_ID]
```
but br log shows that checkpoint data are not cleaned successfully, and console doesn't report warning or error about it
```
[2025/03/21 11:00:38.253 +00:00] [WARN] [restore.go:846] ["failed to remove checkpoint data for snapshot restore"] [error="[domain:8027]Information schema is out of date: schema failed to update in 1 lease, please make sure TiDB can connect to TiKV"] [errorVerbose="[domain:8027]Information schema is out of date: schema failed to update in 1 lease, please make sure TiDB can connect to TiKV\ngithub.com/pingcap/errors.AddStack\n\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/errors.go:178\ngithub.com/pingcap/errors.Trace\n\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/juju_adaptor.go:15\ngithub.com/pingcap/tidb/pkg/executor.(*DDLExec).toErr\n\t/workspace/source/tidb/pkg/executor/ddl.go:74\ngithub.com/pingcap/tidb/pkg/executor.(*DDLExec).Next\n\t/workspace/source/tidb/pkg/executor/ddl.go:234\ngithub.com/pingcap/tidb/pkg/executor/internal/exec.Next\n\t/workspace/source/tidb/pkg/executor/internal/exec/executor.go:460\ngithub.com/pingcap/tidb/pkg/executor.(*ExecStmt).next\n\t/workspace/source/tidb/pkg/executor/adapter.go:1269\ngithub.com/pingcap/tidb/pkg/executor.(*ExecStmt).handleNoDelayExecutor\n\t/workspace/source/tidb/pkg/executor/adapter.go:1018\ngithub.com/pingcap/tidb/pkg/executor.(*ExecStmt).handleNoDelay\n\t/workspace/source/tidb/pkg/executor/adapter.go:851\ngithub.com/pingcap/tidb/pkg/executor.(*ExecStmt).Exec\n\t/workspace/source/tidb/pkg/executor/adapter.go:614\ngithub.com/pingcap/tidb/pkg/session.runStmt\n\t/workspace/source/tidb/pkg/session/session.go:2305\ngithub.com/pingcap/tidb/pkg/session.(*session).ExecuteStmt\n\t/workspace/source/tidb/pkg/session/session.go:2167\ngithub.com/pingcap/tidb/pkg/session.(*session).ExecuteInternal\n\t/workspace/source/tidb/pkg/session/session.go:1540\ngithub.com/pingcap/tidb/br/pkg/gluetidb.(*tidbSession).ExecuteInternal\n\t/workspace/source/tidb/br/pkg/gluetidb/glue.go:210\ngithub.com/pingcap/tidb/br/pkg/checkpoint.dropCheckpointTables\n\t/workspace/source/tidb/br/pkg/checkpoint/storage.go:331\ngithub.com/pingcap/tidb/br/pkg/checkpoint.(*TableMetaManager[...]).RemoveCheckpointData\n\t/workspace/source/tidb/br/pkg/checkpoint/manager.go:201\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/workspace/source/tidb/br/pkg/task/restore.go:844\nmain.runRestoreCommand\n\t/workspace/source/tidb/br/cmd/br/restore.go:80\nmain.newFullRestoreCommand.func1\n\t/workspace/source/tidb/br/cmd/br/restore.go:186\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:37\nruntime.main\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/proc.go:272\nruntime.goexit\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/asm_amd64.s:1700"]
```
### 4. [REDACTED_USER]
master
v9.0
<!-- Paste the output of SELECT tidb_version() -->
