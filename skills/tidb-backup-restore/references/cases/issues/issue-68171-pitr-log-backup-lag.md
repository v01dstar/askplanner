# Issue 68171: PITR log backup lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/68171
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-05-06T04:09:34Z
- Updated: 2026-05-06T04:09:50Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, checkpoint-retry, observability-diagnosis
- Labels: affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR log backup lag`
- Search terms: BR; PITR; TiDB; checkpoint-retry; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. run restore on cluster [REDACTED_CLUSTER] log backup but failed
2. run restore again and success
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
1. blocklist is written
### 3. [REDACTED_USER]
1. no blocklist
### 4. [REDACTED_USER]
master/8.5
<!-- Paste the output of SELECT tidb_version() -->
