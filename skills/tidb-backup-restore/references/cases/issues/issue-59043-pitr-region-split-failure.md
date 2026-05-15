# Issue 59043: PITR region split failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59043
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-20T10:00:28Z
- Updated: 2025-11-27T02:47:03Z
- Closed: 2025-01-20T12:13:55Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Storage
- Categories: pitr-log-restore, restore-failure, region-split-scatter, observability-diagnosis
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR region split failure`
- Search terms: BR; PITR; Storage; TiDB; TiKV; observability-diagnosis; pitr-log-restore; region-split-scatter; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. Start Log Backup and cluster at region A.
2. Restore from AWS Region B.  (Not the best practice, but anyway...)

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
Restore should success.

### 3. [REDACTED_USER]
Restore failed with:
```
BucketRegionError: incorrect region, the bucket is not in 'us-east-2' region at endpoint '', bucket is in 'us-west-2' region
```

### 4. [REDACTED_USER]

master
<!-- Paste the output of SELECT tidb_version() -->
