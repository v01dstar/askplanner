# Issue 57175: PITR fails with proto: BackupMeta: wiretype end group for non-group

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57175
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-11-06T09:34:08Z
- Updated: 2024-11-27T15:14:41Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, observability-diagnosis
- Labels: component/br, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR fails with proto: BackupMeta: wiretype end group for non-group`
- Search terms: BR; PITR; TiDB; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

TiDB v8.1

### 1. [REDACTED_USER]

```bash
pd=( --pd http://[REDACTED_IP]:2379 )
key=( --crypter.method aes256-ctr --crypter.key [REDACTED_LONG_ID] )
fd_log=/db_backup/blog 
fd_full=/db_backup/full
```

### 2. [REDACTED_USER]

```bash
br log start --task-name test "${pd[@]}" --storage $fd_log
br backup full "${pd[@]}" --storage $fd_full "${key[@]}"
```

### 3. [REDACTED_USER]

```bash
br restore point "${pd[@]}" -s $fd_log --[REDACTED_RESOURCE_NAME] $fd_full "${key[@]}"
#### Error: proto: BackupMeta: wiretype end group for non-group
```

### 4. [REDACTED_USER]

```bash
br restore full "${pd[@]}" -s $fd_full "${key[@]}"
br restore point "${pd[@]}" -s $fd_log "${key[@]}" --start-ts xxxxx 
```
