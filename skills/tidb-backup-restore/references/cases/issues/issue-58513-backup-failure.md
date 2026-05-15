# Issue 58513: Backup failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58513
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-12-24T13:21:38Z
- Updated: 2024-12-26T08:44:01Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Backup
- Components: TiDB, TiKV, BR, Storage
- Categories: backup-failure, storage-access, checkpoint-retry, observability-diagnosis
- Labels: component/br, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Backup failure`
- Search terms: BR; Backup; Storage; TiDB; TiKV; backup-failure; checkpoint-retry; observability-diagnosis; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

Issue Description:
Our application is a SAAS based Multi-tenancy application with each tenant will have a DB , in which we have more than 14k databases and having more than 600k Tables.

While we have a strick backup requirement when we run the BR full backup its not showing any progress and gets failed with some RPC error

Command and Log:

```$ tiup br:v8.1.1 backup full --pd "[REDACTED_IP]:2379" --storage "s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]" --log-file backupdec232024.log
Starting component br: /home/ec2-user/.tiup/components/br/v8.1.1/br backup full --pd [REDACTED_IP]:2379 --storage s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] --log-file backupdec232024.log
Detail BR log in backupdec232024.log 

Full Backup <..................................................................................................................................................................> 0.00%```


Am also attaching the details logs as well


### 2. [REDACTED_USER]

We expect the backup to run completely and consistently

### 3. [REDACTED_USER]
we see backup failures and BR backup is not happening

### 4. [REDACTED_USER]

```mysql> select tidb_version();
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tidb_version()                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release Version: v8.1.1
Edition: Community
Git Commit Hash: a7df4f9845d5d6a590c5d45dad0dcc9f21aa8765
Git Branch: HEAD
UTC Build Time: 2024-08-22 05:49:03
GoVersion: go1.21.13
Race Enabled: false
Check Table Before Drop: false
Store: tikv |```[backup_log.txt]([REDACTED_ATTACHMENT_URL])
