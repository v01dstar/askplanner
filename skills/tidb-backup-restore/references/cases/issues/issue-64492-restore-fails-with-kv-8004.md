# Issue 64492: Restore fails with [kv:8004]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/64492
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-11-14T07:06:31Z
- Updated: 2026-03-18T01:50:07Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: uncategorized
- Labels: affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Restore fails with [kv:8004]`
- Search terms: BR; Restore; TiDB; uncategorized

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. restore X tables in the same database with the parameter `--ddl-batch-size X`
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
restore successfully
### 3. [REDACTED_USER]
```
Error: [kv:8004]Transaction is too large, size: 108312922
```
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
