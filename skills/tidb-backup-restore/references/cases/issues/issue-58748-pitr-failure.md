# Issue 58748: PITR failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58748
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-07T07:39:12Z
- Updated: 2025-01-09T06:46:06Z
- Closed: 2025-01-09T06:46:05Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, restore-failure, sst-ingest-import, observability-diagnosis
- Labels: component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `PITR failure`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; pitr-log-restore; restore-failure; sst-ingest-import

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/57716

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. use https://github.com/pingcap/tidb/pull/57716 build br
2. cluster open log backup
3. restore 500k+ tables to cluster

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
restore ok
### 3. [REDACTED_USER]
restore failed 
```
Error: failed to execute the delaied callback #0: failed to put sst 1006/4192_256_598b83294414ab2dec14b72390014a7990f3d9ada05d0f5b485e0f6c64ce29c4_1736192310897_write.sst: RequestError: send request failed
caused by: Put "https://qe-testing.ks3-cn-beijing-internal.ksyuncs.com/kernel-testing/scenario/log2-0106/v1/ext_backups/backup-0650F65E09D8007F/sst_files/1006/4192_256_598b83294414ab2dec14b72390014a7990f3d9ada05d0f5b485e0f6c64ce29c4_1736192310897_write.sst": dial tcp [REDACTED_IP]:443: connect: connection refused
```
after failure, repeat restore process, restore would also fail because of similiar error
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
