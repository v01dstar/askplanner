# Issue 61964: Restore fails with [BR:Common:ErrInvalidArgument]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61964
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-06-24T09:21:39Z
- Updated: 2025-06-30T03:03:01Z
- Closed: 2025-06-30T03:03:01Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure, storage-access, schema-metadata, observability-diagnosis
- Labels: component/br, feature/developing, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore fails with [BR:Common:ErrInvalidArgument]`
- Search terms: BR; Restore; TiDB; observability-diagnosis; restore-failure; schema-metadata; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、classic br restore to keyspace
2、br restore failed
3、drop TiDB_BR_Temporary_Snapshot_Restore_Checkpoint
4、there is no permission  to clean mysql.tidb_restore_registry which causes it can not restore again 

[2025/06/24 08:29:59.297 +00:00] [INFO] [collector.go:77] ["DataBase Restore failed summary"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0]
Error: task with ID 1 already exists and is running: [BR:Common:ErrInvalidArgument]invalid argument

[REDACTED_ATTACHMENT]


### 2. [REDACTED_USER]
provide some way to clean history restore info so that user can restore aging

### 3. [REDACTED_USER]
No permission to clean mysql.tidb_restore_registry after br full restore failed, it will prevent restore again if the registry info exist 

### 4. [REDACTED_USER]
sh-5.1# ./br -V
Release Version: v9.0.0-beta.1.pre-986-gcadde3a
Git Commit Hash: cadde3aaf8059635273a98200233c5f853bafb5e
Git Branch: HEAD
Go Version: go1.23.10
UTC Build Time: 2025-06-24 05:00:44
Race Enabled: false
