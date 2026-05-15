# Issue 54511: Backup fails with nil pointer

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/54511
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-07-08T18:17:37Z
- Updated: 2024-08-02T11:32:13Z
- Closed: 2024-07-18T07:12:04Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR
- Categories: backup-failure, performance-resource
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, impact/panic, report/customer, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `Backup fails with nil pointer`
- Search terms: BR; Backup; TiDB; TiKV; backup-failure; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

Perform an EBS snapshot backup where one of the underlying AWS EBS snapshots fails.

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

Volumebackup fails w/out panic

### 3. [REDACTED_USER]

Backup panics due to:

```
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x4474931]

goroutine 1 [running]:
github.com/pingcap/tidb/br/pkg/aws.(*EC2Session).WaitSnapshotsCreated(0xc03e03f660, 0xc0073997d0, {0x5c81370, 0xc00c4a6b00})
  /tidb/br/pkg/aws/ebs.go:255 +0xa71
github.com/pingcap/tidb/br/pkg/task.RunBackupEBS({0x5c814f8, 0xc000193b80}, {0x5c940b8?, 0x86bcdc0?}, 0xc000c1fc00)
  /tidb/br/pkg/task/backup_ebs.go:255 +0x1c8a
main.runBackupCommand(0xc000c20000, {0x53bfc8f, 0xb})
  /tidb/br/cmd/br/backup.go:36 +0x1d4
main.newFullBackupCommand.func1(0xc00079a800?, {0xc000c480c0?, 0x4?, 0x53adfc5?})
  /tidb/br/cmd/br/backup.go:117 +0x1f
github.com/spf13/cobra.(*Command).execute(0xc000c20000, {0xc00026e030, 0xc, 0xc})
  /go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916 +0x87c
github.com/spf13/cobra.(*Command).ExecuteC(0xc000c04000)
  /go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044 +0x3a5
github.com/spf13/cobra.(*Command).Execute(...)
  /go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968
main.main()
  /tidb/br/cmd/br/main.go:36 +0x212
```

### 4. [REDACTED_USER]

```
tidb> select tidb_version();
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tidb_version()                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release Version: v6.5.4-v15.2-abnb
Edition: Community
Git Commit Hash: 26e36fba0c2e890e7a3d565113cb25091c890543
Git Branch: heads/v6.5.4-v15.2-abnb
UTC Build Time: 2024-05-08 21:58:30
GoVersion: go1.21.10
Race Enabled: false
TiKV Min Version: 6.2.0-alpha
Check Table Before Drop: false
Store: tikv |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.09 sec)

```

<!-- Paste the output of SELECT tidb_version() -->
