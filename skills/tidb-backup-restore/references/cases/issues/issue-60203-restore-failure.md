# Issue 60203: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60203
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-03-21T03:43:06Z
- Updated: 2025-03-26T06:12:52Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: performance-resource, checksum-consistency
- Labels: component/br, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; Restore; TiDB; checksum-consistency; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. open logbackup task
2. restore 1 milltion tables(500000 dbs, 2 tables per db)
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
no issue
### 3. [REDACTED_USER]
checksum is too slow (5h+)

[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]
v9.0
<!-- Paste the output of SELECT tidb_version() -->
