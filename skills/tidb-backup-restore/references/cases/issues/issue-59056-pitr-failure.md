# Issue 59056: PITR failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59056
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-01-21T03:10:51Z
- Updated: 2025-02-05T01:19:41Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, checkpoint-retry, observability-diagnosis
- Labels: component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `PITR failure`
- Search terms: BR; PITR; TiDB; checkpoint-retry; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. start tidb cluster `tiup playground nightly --tiflash=0`
2. start log backup `tiup br:nightly log start -s "local:///tmp/logx" --task-name=c`
3. **drop test database first and re-create it later in workload**.
4. start full backup `tiup br:nightly backup full -s "local:///tmp/fullx"`
5. create database `test` and some data into`test` database;
```
MySQL [test]> create table t(id int);
Query OK, 0 rows affected (0.10 sec)

MySQL [test]> insert into t values(1);
Query OK, 1 row affected (0.02 sec)

MySQL [test]> select * from t;
+------+
| id   |
+------+
|    1 |
+------+
```
6. wait for the checkpoint advanced and start another cluster.
7. doing a PITR to another cluster
```
tiup br:nightly restore point -s "local:///tmp/logx" --[REDACTED_RESOURCE_NAME] "local:///tmp/fullx" --pd [REDACTED_IP]:39656
```
### 2. [REDACTED_USER]
data is correct and cluster [REDACTED_CLUSTER] handle test database correct.

### 3. [REDACTED_USER]
data is correct but **cluster [REDACTED_CLUSTER] drop new restore table on test database**.
```
MySQL [test]> select * from t;
+------+
| id   |
+------+
|    1 |
+------+
1 row in set (0.01 sec)

MySQL [test]> drop table test.t;
ERROR 1051 (42S02): Unknown table 'test.t'
```
### 4. [REDACTED_USER]
master

<!-- Paste the output of SELECT tidb_version() -->
