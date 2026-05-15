# Issue 58574: PITR log backup lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58574
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-12-27T05:32:06Z
- Updated: 2025-09-16T07:01:11Z
- Closed: 2025-01-24T02:05:47Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR, Storage, PD
- Categories: pitr-log-restore, storage-access, checkpoint-retry, observability-diagnosis
- Labels: affects-8.5, component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/major, type/bug
- Affected versions: affects-8.5, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `PITR log backup lag`
- Search terms: BR; PD; PITR; Storage; TiDB; checkpoint-retry; observability-diagnosis; pitr-log-restore; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run tpcc
2、run log backup
3、inject pd leader io delay 500ms last for 10mins and then recover

### 2. [REDACTED_USER]
lag can recover after fault recover

### 3. [REDACTED_USER]
log backup lag more and more after injection pd leader io delay 500ms last for 10mins and then recover
[REDACTED_ATTACHMENT]
[REDACTED_ATTACHMENT]

sh-5.1# /br log status --task-name=pitr --pd="tc-pd.[REDACTED_ENV_NAME].svc:2379"
Detail BR log in /tmp/br.log.2024-12-27T04.49.35Z 
● Total 1 Tasks.
> #1 <
              name: pitr
            status: ● NORMAL
             start: 2024-12-25 18:23:57.664 +0000
               end: 2090-11-18 14:07:45.624 +0000
           storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
       speed(est.): 0.00 ops/s
checkpoint[global]: 2024-12-26 11:10:37.101 +0000; gap=17h38m58s

### 4. [REDACTED_USER]
./tidb-server -V
 Release Version: v8.5.0
Edition: Community
Git Commit Hash: d13e52ed6e22cc5789bed7c64c861578cd2ed55b
Git Branch: HEAD
UTC Build Time: 2024-12-23 03:40:21
GoVersion: go1.23.3
Race Enabled: false
Check Table Before Drop: false
Store: unistore
2024-12-26T17:49:31.016+0800
