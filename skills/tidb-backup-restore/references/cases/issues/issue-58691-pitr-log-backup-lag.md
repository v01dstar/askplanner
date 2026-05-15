# Issue 58691: PITR log backup lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58691
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-06T02:09:58Z
- Updated: 2025-07-29T14:41:41Z
- Closed: 2025-03-11T10:30:08Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, checkpoint-retry, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR log backup lag`
- Search terms: BR; PITR; TiDB; TiKV; checkpoint-retry; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、enable IME
2、run muti mvcc workload
3、full backup
4、minio is full during full backup
5、log backup pause due to minio full
[REDACTED_ATTACHMENT]

6、clean up some space of minio
7、resume log backup task
8、log backup became normal

### 2. [REDACTED_USER]
after resume log backup，the lag should be less than 5mins

### 3. [REDACTED_USER]
log backup lag occasionally more than 5 minutes after resume log backup
and after rolling update tikv，the lag returns to be less than 3 minutes
[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]
./tidb-server -V
 Release Version: v8.5.0
Edition: Community
Git Commit Hash: d13e52ed6e22cc5789bed7c64c861578cd2ed55b
Git Branch: HEAD
UTC Build Time: 2024-12-18 02:26:06
GoVersion: go1.23.3
Race Enabled: false
Check Table Before Drop: false
Store: unistore
2025-01-06T05:48:54.781+0800
