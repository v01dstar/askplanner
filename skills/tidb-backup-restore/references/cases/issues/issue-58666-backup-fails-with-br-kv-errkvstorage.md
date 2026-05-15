# Issue 58666: Backup fails with [BR:KV:ErrKVStorage]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58666
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-02T12:16:18Z
- Updated: 2025-01-16T05:45:20Z
- Closed: 2025-01-16T05:45:20Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR, Storage
- Categories: backup-failure, storage-access
- Labels: affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Backup fails with [BR:KV:ErrKVStorage]`
- Search terms: BR; Backup; Storage; TiDB; TiKV; backup-failure; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run workload with multi mvcc
2、enable IME
3、br full backup

### 2. [REDACTED_USER]
br full backup can succeed

### 3. [REDACTED_USER]
br full backup failed
`[2025/01/02 11:32:09.287 +00:00] [ERROR] [backup.go:58] ["failed to backup"] [error="error happen in store 5: unknown error, retried too many times, give up: [BR:KV:ErrKVStorage]tikv storage occur I/O error"] [errorVerbose="[BR:KV:ErrKVStorage]tikv storage occur I/O error\nerror happen in store 5: unknown error, retried too many times, give up\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).OnBackupResponse\n\t/workspace/source/tidb/br/pkg/backup/client.go:1213\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).RunLoop\n\t/workspace/source/tidb/br/pkg/backup/client.go:341\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRanges\n\t/workspace/source/tidb/br/pkg/backup/client.go:1126\ngithub.com/pingcap/tidb/br/pkg/task.RunBackup\n\t/workspace/source/tidb/br/pkg/task/backup.go:689\nmain.runBackupCommand\n\t/workspace/source/tidb/br/cmd/br/backup.go:57\nmain.newFullBackupCommand.func1\n\t/workspace/source/tidb/br/cmd/br/backup.go:149\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1700"] [stack="main.runBackupCommand\n\t/workspace/source/tidb/br/cmd/br/backup.go:58\nmain.newFullBackupCommand.func1\n\t/workspace/source/tidb/br/cmd/br/backup.go:149\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272"]
[2025/01/02 11:32:09.287 +00:00] [ERROR] [main.go:38] ["br failed"] [error="error happen in store 5: unknown error, retried too many times, give up: [BR:KV:ErrKVStorage]tikv storage occur I/O error"] [errorVerbose="[BR:KV:ErrKVStorage]tikv storage occur I/O error\nerror happen in store 5: unknown error, retried too many times, give up\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).OnBackupResponse\n\t/workspace/source/tidb/br/pkg/backup/client.go:1213\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).RunLoop\n\t/workspace/source/tidb/br/pkg/backup/client.go:341\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRanges\n\t/workspace/source/tidb/br/pkg/backup/client.go:1126\ngithub.com/pingcap/tidb/br/pkg/task.RunBackup\n\t/workspace/source/tidb/br/pkg/task/backup.go:689\nmain.runBackupCommand\n\t/workspace/source/tidb/br/cmd/br/backup.go:57\nmain.newFullBackupCommand.func1\n\t/workspace/source/tidb/br/cmd/br/backup.go:149\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1700"] [stack="main.main\n\t/workspace/source/tidb/br/cmd/br/main.go:38\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272"]`

### 4. [REDACTED_USER]
sh-5.1# ./br -V
Release Version: v8.5.0
Git Commit Hash: d13e52ed6e22cc5789bed7c64c861578cd2ed55b
Git Branch: HEAD
Go Version: go1.23.3
UTC Build Time: 2024-12-18 02:28:02
Race Enabled: false
