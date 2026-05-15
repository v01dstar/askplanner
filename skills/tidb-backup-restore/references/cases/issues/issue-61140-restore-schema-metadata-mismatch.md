# Issue 61140: Restore schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61140
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-05-15T12:04:49Z
- Updated: 2025-05-23T11:11:20Z
- Closed: 2025-05-23T11:11:20Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure, schema-metadata, observability-diagnosis
- Labels: component/br, feature/developing, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore schema metadata mismatch`
- Search terms: BR; Restore; TiDB; observability-diagnosis; restore-failure; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. restore 
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
success
### 3. [REDACTED_USER]
in TiDB log, maybe trigger by `select .. from mysql.stats_meta;`
```
[2025/05/15 15:30:57.350 +08:00] [INFO] [lock_resolver.go:1156] ["resolveLock rollback"] [lock="key: 7480000000000000165F69800000000000000104065B4B65B5200001038000000000000001, primary: 7480000000000000165F698000000000000002038000000000000070, txnStartTS: [REDACTED_LONG_ID], lockForUpdateTS:[REDACTED_LONG_ID], minCommitTs:[REDACTED_LONG_ID], ttl: 8395, type: Put, UseAsyncCommit: false, txnSize: 9000"]
```
in BR log, it takes much time to prewrite.
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
