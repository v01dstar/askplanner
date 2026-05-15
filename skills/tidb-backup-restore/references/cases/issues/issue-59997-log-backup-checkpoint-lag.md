# Issue 59997: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59997
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-03-11T01:37:42Z
- Updated: 2025-03-11T11:40:57Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, checkpoint-retry, observability-diagnosis
- Labels: affects-9.0, component/br, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: affects-9.0, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; PITR; TiDB; TiKV; checkpoint-retry; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

- create gcp cluster
- use br restore data from v8.1.2 to master version
- after restore finished，start log backup

### 2. [REDACTED_USER]
checkpoint ts lag is less than 5min

### 3. [REDACTED_USER]
`[2025/03/11 01:28:15.065 +00:00] [WARN] [regioniter.go:141] ["failed with trying to scan regions"] [error="rpc error: code = DeadlineExceeded desc = context deadline exceeded"] [start=74] [end=75]`

[REDACTED_ATTACHMENT]

[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->

Release Version: v9.0.0-alpha-381-g739a934
Edition: Community
Git Commit Hash: 739a934f631eb413ff3b150b0a7fc9db55eefcbd
Git Branch: HEAD
UTC Build Time: 2025-03-10 06:19:26
GoVersion: go1.23.7
Race Enabled: false
Check Table Before Drop: false
Store: tikv
