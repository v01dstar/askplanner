# Issue 67210: Restore fails with [BR:Restore:ErrRestoreIncompatibleSys]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67210
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-03-23T06:02:54Z
- Updated: 2026-03-24T02:30:03Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure, schema-metadata, compatibility-upgrade
- Labels: affects-8.5, component/br, contribution, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/critical, type/bug
- Affected versions: affects-8.5, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `Restore fails with [BR:Restore:ErrRestoreIncompatibleSys]`
- Search terms: BR; Restore; TiDB; compatibility-upgrade; restore-failure; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

### 1. [REDACTED_USER]

1. Backup a TiDB v8.x cluster that was originally upgraded from v4.0 (carrying legacy `mysql.user` schema).
2. Restore the backup to a fresh TiDB v8.x cluster (initialized with modern schema).
3. BR fails during the system table compatibility check.

### 2. [REDACTED_USER]

BR should automatically handle or ignore legacy system table column variations (like `Create_tablespace_priv` casing/enum differences) when both clusters are on the same version.

### 3. [REDACTED_USER]

Restore fails with:
`[BR:Restore:ErrRestoreIncompatibleSys] incompatible system table`
`col in cluster: [REDACTED_CLUSTER] enum('N','Y'), col in backup: Create_tablespace_priv enum('N','Y')`

This blocks migrations of "brownfield" clusters that have a long upgrade history.

### 4. [REDACTED_USER]

v8.5.0 (Source upgraded from v4.0; Target is fresh v8.5.0)

---

### Proposed [REDACTED_USER]
1. **Code Fix:** Relax the `CheckSysTableCompatibility` logic for known legacy schema variations.
2. **Workaround:** Provide a flag to skip system table restoration or specific compatibility checks, allowing users to manually sync users/privileges post-restore.
