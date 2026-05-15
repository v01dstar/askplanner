# Issue 63685: PITR fails with [domain:8028]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/63685
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-09-23T04:24:23Z
- Updated: 2025-10-22T03:08:54Z
- Closed: 2025-10-22T03:08:54Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, schema-metadata, checkpoint-retry, observability-diagnosis
- Labels: component/br, severity/moderate, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR fails with [domain:8028]`
- Search terms: BR; PITR; TiDB; checkpoint-retry; observability-diagnosis; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
PITR restore
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
success
### 3. [REDACTED_USER]
```
[2025/09/22 12:30:45.126 +00:00] [INFO] [collector.go:77] ["restore log failed summary"] [error="failed to reset tiflash replicas: [domain:8028]Information schema is changed during the execution of the statement(for example, table definition may be updated by other DDL ran in parallel). If you see this error often, try increasing `tidb_max_delta_schema_count`. [try again later]"] 
```
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
