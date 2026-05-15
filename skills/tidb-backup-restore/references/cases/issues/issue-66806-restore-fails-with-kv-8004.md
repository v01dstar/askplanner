# Issue 66806: Restore fails with [kv:8004]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/66806
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2026-03-09T07:18:04Z
- Updated: 2026-03-17T19:17:58Z
- Closed: 2026-03-17T19:17:58Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure, schema-metadata
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Restore fails with [kv:8004]`
- Search terms: BR; Restore; TiDB; restore-failure; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. snapshot backup cluster with much bind infos
2. snapshot restore with system restore

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
success
### 3. [REDACTED_USER]
Transaction is too large
```
Error: [kv:8004]Transaction is too large, size: 108312922
```
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
