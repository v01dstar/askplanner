# Issue 58031: PITR log backup lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58031
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-12-06T01:01:23Z
- Updated: 2025-10-17T07:04:19Z
- Closed: 2024-12-13T13:14:17Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, region-split-scatter, checkpoint-retry, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, report/customer, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR log backup lag`
- Search terms: BR; PITR; TiDB; TiKV; checkpoint-retry; observability-diagnosis; pitr-log-restore; region-split-scatter

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. Another TiDB node becomes new log backup advancer owner.
2. the `--start-ts` of the log backup task is recorded as current global checkpoint ts at the first.
3. the advancer failed to collect the whole region level checkpoint ts, so it can't update the new global checkpoint ts.
4. it compares the current ts with its recorded global checkpoint ts(`--start-ts`), and finds that the gap is so large.
5. Therefore, the advancer stop the log backup task.
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

### 3. [REDACTED_USER]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
