# Issue 56046: Restore region split failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56046
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-09-12T08:53:44Z
- Updated: 2024-10-25T09:43:20Z
- Closed: 2024-10-25T09:43:19Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: restore-failure, observability-diagnosis
- Labels: component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/major, type/bug
- Affected versions: may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `Restore region split failure`
- Search terms: BR; Restore; TiDB; TiKV; observability-diagnosis; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、br restore failed
2、injection tikv failure 5 minutes every 5 minutes and total injection fault twice

[br.log.2024-09-10T18.03.34Z.zip]([REDACTED_ATTACHMENT_URL])



### 2. [REDACTED_USER]
br restore success

### 3. [REDACTED_USER]
br restore

start time: 2024-09-11 02:03:34, failed time: 2024-09-11 02:19:48
stdout:
Detail BR log in /tmp/br.log.2024-09-10T18.03.34Z 

[2024/09/10 18:19:48.220 +00:00] [INFO] [collector.go:73] [DataBase Restore failed summary] [total-ranges=129] [ranges-succeed=128] [ranges-failed=1] [split-region=9m5.021030894s] [restore-ranges=7897] [unit-name=file] [error=rpc error: code = Unavailable desc = Cancelling all calls; rpc error: code = Unavailable desc = connection error: desc = \transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): connect: connection refused\; rpc error: code = Unavailable desc = connection error

### 4. [REDACTED_USER]
./tidb-server -V
 Release Version: v6.5.11
Edition: Community
Git Commit Hash: 305cf424997144f38c268112055fc446d30b7938
Git Branch: HEAD
UTC Build Time: 2024-09-10 08:34:23
GoVersion: go1.19.13
Race Enabled: false
TiKV Min Version: 6.2.0-alpha
Check Table Before Drop: false
Store: unistore
2024-09-11T02:03:30.451+0800

./br -V
 Release Version: v6.5.11
Git Commit Hash: 305cf424997144f38c268112055fc446d30b7938
Git Branch: HEAD
Go Version: go1.19.13
UTC Build Time: 2024-09-10 08:35:44
Race Enabled: false
