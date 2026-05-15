# Issue 53561: PITR log backup lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/53561
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-05-27T05:28:12Z
- Updated: 2025-03-21T03:34:43Z
- Closed: 2024-06-11T15:46:31Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, report/customer, severity/major, type/bug, type/regression
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `PITR log backup lag`
- Search terms: BR; PITR; TiDB; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. start a log backup
2. wait for 48h(the default lag check threshold)
3. restart tidb advancer(or other scenarios that make advancer owner changed)

### 2. [REDACTED_USER]
a normal log backup status.
### 3. [REDACTED_USER]
log backup paused by chance.

(The chance is the lastCheckpoint cannot be updated in time before checking. e.g. regions has a hole will make lastCheckpoint skip update this time and wait for next tick. )
<!-- a step by step guide for reproducing the bug. -->
### 4. [REDACTED_USER]
v6.5.9/v7.1.5/v8.1.0/master
<!-- Paste the output of SELECT tidb_version() -->
