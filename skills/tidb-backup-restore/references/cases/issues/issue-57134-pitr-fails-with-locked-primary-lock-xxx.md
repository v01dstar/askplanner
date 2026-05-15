# Issue 57134: PITR fails with <locked:<primary_lock:xxx

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57134
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-11-05T08:59:17Z
- Updated: 2025-10-17T07:04:24Z
- Closed: 2024-11-11T05:12:40Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, region-split-scatter, performance-resource, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/minor, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR fails with <locked:<primary_lock:xxx`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; performance-resource; pitr-log-restore; region-split-scatter

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
To reproduce this issue:
1. In a log backup cluster, ensure there is an existing lock and trigger the advancer to resolve the lock on specific regions.
2. Ensure the region contains a new lock ts in memory(from another new transaction).

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
Resolve Lock success

### 3. [REDACTED_USER]
Resolve Lock Failed, wait for next round.
```
resolve locks failed, wait for next tick"",""category"":""advancer"",""uuid"":""log backup advancer"",""error"":""unexpected scanlock error: error:<locked:<primary_lock:xxx
```


### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
