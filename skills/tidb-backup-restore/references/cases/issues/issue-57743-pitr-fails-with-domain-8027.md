# Issue 57743: PITR fails with [domain:8027]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57743
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-11-26T20:23:21Z
- Updated: 2025-01-09T03:45:23Z
- Closed: 2024-12-03T04:30:21Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, schema-metadata
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, report/customer, severity/minor, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR fails with [domain:8027]`
- Search terms: BR; PITR; TiDB; TiKV; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

In a cluster with large number of tables but minimal actual data, during PiTR restore infoSchema can take minutes to load the restore change, and since actual data restore finished within seconds, restore process tries to use infoSchema for insertGCRow before its reloading finished, and it can cause problem of the below 
```
[error="[domain:8027]Information schema is out of date: schema failed to update in 1 lease, please make sure TiDB can connect to TiKV"]
```
