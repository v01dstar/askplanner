# Issue 60577: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60577
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-04-15T07:38:02Z
- Updated: 2025-06-11T02:59:11Z
- Closed: 2025-04-15T10:01:24Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: restore-failure, sst-ingest-import
- Labels: affects-9.0, component/br, severity/critical, type/bug
- Affected versions: affects-9.0

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; Restore; TiDB; TiKV; restore-failure; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
A simple figure shows this case

[REDACTED_ATTACHMENT]

During a full backup, snapshot logic skips unfinished entries in the default column family. Therefore, when restoring from compacted SSTs, a shift mechanism is needed to ensure these default entries are correctly restored.

However, in the previous implementation, the rule was bound at the table level. Since a table can contain multiple column families (CFs), the rules could be applied at different times for each CF. This led to an incorrect rule set, where the start timestamp was not properly shifted as expected.

As a result, some transactional entries may be incomplete during restoration.
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
restore completely
### 3. [REDACTED_USER]
We observed default not found errors during restore, caused by missing default CF entries from transactions that began before the full backup but were not completed at the snapshot time.
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
