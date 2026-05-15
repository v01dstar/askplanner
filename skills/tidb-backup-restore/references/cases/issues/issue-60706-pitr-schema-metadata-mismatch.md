# Issue 60706: PITR schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60706
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-04-22T10:13:36Z
- Updated: 2025-05-08T06:47:02Z
- Closed: 2025-05-08T06:47:01Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, schema-metadata
- Labels: component/br, severity/moderate, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR schema metadata mismatch`
- Search terms: BR; PITR; TiDB; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. prepare a v7.5 cluster
2. br:v8.5 restore point ...

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

success

### 3. [REDACTED_USER]
table `mysql.tidb_pitr_id_map` does not exist.
### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
