# Issue 55562: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/55562
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-08-21T07:22:46Z
- Updated: 2024-10-31T15:57:23Z
- Closed: 2024-09-03T12:28:28Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure
- Labels: component/br, severity/major, type/bug, type/regression
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; Restore; TiDB; restore-failure

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/55044

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

ref: https://github.com/pingcap/tidb/pull/55044

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

1. create a db and write some data into it
2. do full backup
3. write more data into it
4. do incremental backup
5. create a downstream cluster
6. do full restore and then increasement restore

### 2. [REDACTED_USER]

All restore success.

### 3. [REDACTED_USER]

The increasement restore failed and reports: `BR:Restore:ErrTablesAlreadyExisted`

### 4. [REDACTED_USER]

master

<!-- Paste the output of SELECT tidb_version() -->
