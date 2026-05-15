# Issue 58168: Restore fails with [BR:Restore:ErrRestoreChecksumMismatch]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58168
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-12-11T09:30:19Z
- Updated: 2024-12-13T06:16:44Z
- Closed: 2024-12-13T06:16:44Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure, checksum-consistency
- Labels: affects-6.1, affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-6.1, affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Restore fails with [BR:Restore:ErrRestoreChecksumMismatch]`
- Search terms: BR; Restore; TiDB; checksum-consistency; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. create table db1.t1 on the cluster
2. insert some data into db1.t1
3. run restore  `tiup br restore table db1.t1` to restore to the table
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
`ERROR 8125 (HY000): Restore failed: table already exists`

### 3. [REDACTED_USER]
`Error: failed to validate checksum: [BR:Restore:ErrRestoreChecksumMismatch]restore checksum mismatch`

### 4. [REDACTED_USER]
master

<!-- Paste the output of SELECT tidb_version() -->
