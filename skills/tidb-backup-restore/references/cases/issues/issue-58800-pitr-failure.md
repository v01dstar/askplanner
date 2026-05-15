# Issue 58800: PITR failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58800
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-08T10:03:34Z
- Updated: 2025-01-14T08:48:52Z
- Closed: 2025-01-14T08:48:50Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, observability-diagnosis
- Labels: component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `PITR failure`
- Search terms: BR; PITR; TiDB; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/57716

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. open log backup 
2. run 1m-tables workload
3. restore 500k row-wide data to cluster [REDACTED_CLUSTER] br built from https://github.com/pingcap/tidb/pull/57716
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
restore ok , and it applied little impact on cluster
### 3. [REDACTED_USER]
restore ok
[2025/01/08 09:28:02.878 +00:00] [INFO] [collector.go:77] ["Full Restore success summary"] [total-ranges=1902] [ranges-succeed=1902] [ranges-failed=0] [restore-ranges=951] [total-take=27m13.135616731s] [restore-data-size(after-compressed)=177.1GB] [Size=[REDACTED_LONG_ID] [BackupTS=[REDACTED_LONG_ID] [RestoreTS=[REDACTED_LONG_ID] [total-kv=3000000] [total-kv-size=240.8GB] [average-speed=147.4MB/s]

but qps is lower a lot
[REDACTED_ATTACHMENT]
[REDACTED_ATTACHMENT]


### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
