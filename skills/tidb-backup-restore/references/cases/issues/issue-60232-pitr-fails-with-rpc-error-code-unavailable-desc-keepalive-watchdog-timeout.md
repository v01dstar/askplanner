# Issue 60232: PITR fails with rpc error: code = Unavailable desc = keepalive watchdog timeout

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60232
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-24T06:59:29Z
- Updated: 2025-06-19T02:11:20Z
- Closed: 2025-06-19T02:11:20Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, restore-failure, performance-resource, observability-diagnosis
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR fails with rpc error: code = Unavailable desc = keepalive watchdog timeout`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; performance-resource; pitr-log-restore; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. open log backup task
2. run million table workload
3. restore to cluster
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
no error
### 3. [REDACTED_USER]
Detail BR log in /tmp/br.log.2025-03-23T16.32.52Z
[2025/03/23 16:34:40.293 +00:00] [INFO] [collector.go:77] ["Full Restore failed summary"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0]
Error: rpc error: code = Unavailable desc = keepalive watchdog timeout

cluster tikv cpu is not so busy
[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]
v9.0
<!-- Paste the output of SELECT tidb_version() -->
