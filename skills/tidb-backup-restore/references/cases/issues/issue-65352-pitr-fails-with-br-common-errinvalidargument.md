# Issue 65352: PITR fails with [BR:Common:ErrInvalidArgument]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/65352
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-12-31T03:08:22Z
- Updated: 2026-03-13T08:04:41Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Storage
- Categories: pitr-log-restore, restore-failure, storage-access, schema-metadata, region-split-scatter
- Labels: affects-8.5, component/br, contribution, severity/major, type/bug, type/regression
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR fails with [BR:Common:ErrInvalidArgument]`
- Search terms: BR; PITR; Storage; TiDB; TiKV; pitr-log-restore; region-split-scatter; restore-failure; schema-metadata; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
When I used this command to perform pitr restore on v8.5.5, an error occurred, but the same operation worked fine on 8.5.4.
```
9 restore.go:133] Running br command with args: [restore point --pd=<PD_HOST>:2379 --ca=/var/lib/cluster-client-tls/ca.crt --cert=/var/lib/cluster-client-tls/tls.crt --key=/var/lib/cluster-client-tls/tls.key --send-credentials-to-tikv=false --storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]<LOG_ID> --s3.region=<AWS_REGION> --s3.provider=aws --check-requirements=false --checksum=false --with-sys-table --filter=*.* --filter=!__TiDB_BR_Temporary_*.* --filter=!mysql.* --filter=mysql.user --filter=mysql.db --filter=mysql.tables_priv --filter=mysql.columns_priv --filter=mysql.global_priv --filter=mysql.global_grants --filter=mysql.default_roles --filter=mysql.role_edges --filter=!sys.* --filter=!INFORMATION_SCHEMA.* --filter=!PERFORMANCE_SCHEMA.* --filter=!METRICS_SCHEMA.* --filter=!INSPECTION_SCHEMA.* --filter=mysql.bind_info --restored-ts=<TIMESTAMP> --[REDACTED_RESOURCE_NAME]=s3://[REDACTED_BUCKET]/<BACKUP_ID>]
```

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
PITR restore success 

### 3. [REDACTED_USER]
PITR restore failed 
```
Error: PiTR doesn't support custom filter to include system db, consider to exclude system db: [BR:Common:ErrInvalidArgument]invalid argument
2025-12-29 15:21:11	
[2025/12/29 07:21:11.582 +00:00] [ERROR] [main.go:43] ["br failed"] [error="PiTR doesn't support custom filter to include system db, consider to exclude system db: [BR:Common:ErrInvalidArgument]invalid argument"] [errorVerbose="[BR:Common:ErrInvalidArgument]invalid argument\nPiTR doesn't support custom filter to include system db, consider to exclude system db\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\n\t/workspace/source/tidb/br/pkg/task/stream.go:1399\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/workspace/source/tidb/br/pkg/task/restore.go:991\nmain.runRestoreCommand\n\t/workspace/source/tidb/br/cmd/br/restore.go:75\nmain.newStreamRestoreCommand.func1\n\t/workspace/source/tidb/br/cmd/br/restore.go:249\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:42\nruntime.main\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/proc.go:285\nruntime.goexit\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/asm_amd64.s:1693"] [stack="main.main\n\t/workspace/source/tidb/br/cmd/br/main.go:43\nruntime.main\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/proc.go:285"]
```
### 4. [REDACTED_USER]

```
2025-12-29 15:21:10	
I1229 07:21:10.688140       9 restore.go:181] [2025/12/29 07:21:10.687 +00:00] [INFO] [info.go:53] ["Welcome to Backup & Restore (BR)"] [release-version=v8.5.5] [git-hash=05b4a34ba2a12b55f9a338a850c4944d78aedf7e] [git-branch=HEAD] [go-version=go1.25.5] [utc-build-time="2025-12-23 02:51:46"] [race-enabled=false]
```
<!-- Paste the output of SELECT tidb_version() -->
