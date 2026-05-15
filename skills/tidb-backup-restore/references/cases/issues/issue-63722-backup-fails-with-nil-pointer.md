# Issue 63722: Backup fails with nil pointer

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/63722
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-09-24T07:47:15Z
- Updated: 2025-10-11T19:34:34Z
- Closed: 2025-10-11T19:34:34Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Backup
- Components: TiDB, BR, Storage
- Categories: backup-failure, storage-access, schema-metadata, performance-resource, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Backup fails with nil pointer`
- Search terms: BR; Backup; Storage; TiDB; backup-failure; observability-diagnosis; performance-resource; schema-metadata; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

1. Do a backup with no schema to backp

### 2. [REDACTED_USER]

2. Just finish the backup

### 3. [REDACTED_USER]

AZURE_STORAGE_ACCOUNT=mitstoragehanzhenzhong tiup br:nightly backup full     --pd "[REDACTED_IP]:2379"     --storage "azure://mitstoragehanzhenzhong/[REDACTED_ENV_NAME]"     --log-file br-backup.log
Starting component br: /home/azureuser/.tiup/components/br/v9.0.0-beta.2.pre-nightly/br backup full --pd [REDACTED_IP]:2379 --storage azure://mitstoragehanzhenzhong/[REDACTED_ENV_NAME] --log-file br-backup.log
Detail BR log in br-backup.log 
[2025/09/24 07:07:38.131 +00:00] [INFO] [collector.go:77] ["Full Backup failed summary"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0]
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x54c4a39]

goroutine 1 [running]:
github.com/pingcap/tidb/br/pkg/backup.(*Schemas).SetCheckpointChecksum(...)
	/workspace/source/tidb/br/pkg/backup/schema.go:69
github.com/pingcap/tidb/br/pkg/backup.(*Client).BuildBackupRangeAndSchema(0xc0001dc480, {0x7c577e8?, 0xc00193dc20?}, {0x7bf16e0?, 0xc0015eba60?}, 0x27?, 0xe0?)
	/workspace/source/tidb/br/pkg/backup/client.go:695 +0x59
github.com/pingcap/tidb/br/pkg/task.RunBackup({0x7c09f10, 0xc0001970e0}, {0x7c2af60, 0xc001565a48}, {0x726733a, 0xb}, 0xc001203808)
	/workspace/source/tidb/br/pkg/task/backup.go:575 +0x13cc
main.runBackupCommand(0xc001d48308, {0x726733a, 0xb})
	/workspace/source/tidb/br/cmd/br/backup.go:61 +0x4e6
main.newFullBackupCommand.func1(0xc001d48308?, {0xc000fd0f60?, 0x4?, 0x7251404?})
	/workspace/source/tidb/br/cmd/br/backup.go:150 +0x1f
github.com/spf13/cobra.(*Command).execute(0xc001d48308, {0xc00016e030, 0x6, 0x6})
	/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1015 +0xa94
github.com/spf13/cobra.(*Command).ExecuteC(0xc00152c308)
	/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1148 +0x40c
github.com/spf13/cobra.(*Command).Execute(...)
	/root/go/pkg/mod/github.com/spf13/cobra@v1.9.1/command.go:1071
main.main()
	/workspace/source/tidb/br/cmd/br/main.go:42 +0x269

### 4. [REDACTED_USER]

9.0.0

<!-- Paste the output of SELECT tidb_version() -->
