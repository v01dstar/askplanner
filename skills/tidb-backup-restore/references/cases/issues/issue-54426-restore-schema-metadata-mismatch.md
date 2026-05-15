# Issue 54426: Restore schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/54426
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-07-03T16:16:10Z
- Updated: 2024-07-08T04:48:10Z
- Closed: 2024-07-08T04:48:09Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: schema-metadata
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, impact/inconsistency, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `Restore schema metadata mismatch`
- Search terms: BR; Restore; TiDB; TiKV; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

```sql
use test;

-- 1. prepare the full backup

drop table if exists t;
create table t (pk bigint primary key, val int not null);
insert into t values (1, 11), (2, 22), (3, 33), (4, 44);
backup table t to 'local:///tmp/tidb_54426_full_backup';
-- ^ write down the reported backupts.
admin check table t;
select * from t;
/*
+----+-----+
| pk | val |
+----+-----+
|  1 |  11 |
|  2 |  22 |
|  3 |  33 |
|  4 |  44 |
+----+-----+
*/
```

```sql
-- 2. prepare the incr backup

create index index_val on t (val);
update t set val = 66 - val;
backup table t to 'local:///tmp/tidb_54426_incr_backup' last_backup = «fill_in_the_BackupTS_from_above_here»;
admin check table t;
select * from t use index (index_val);
/*
+----+-----+
| pk | val |
+----+-----+
|  4 |  22 |
|  3 |  33 |
|  2 |  44 |
|  1 |  55 |
+----+-----+
*/
```

```sql
-- 3. clean up
drop table t;
```

```sql
-- 4. perform the full restore
restore schema * from 'local:///tmp/tidb_54426_full_backup';
admin check table t;
select * from t;
/*
+----+-----+
| pk | val |
+----+-----+
|  1 |  11 |
|  2 |  22 |
|  3 |  33 |
|  4 |  44 |
+----+-----+
*/
```

```sql
-- 5. perform the incr restore
restore schema * from 'local:///tmp/tidb_54426_incr_backup';
admin check table t;
select * from t use index (index_val);
```

### 2. [REDACTED_USER]

In step 5, the `admin check table` passes and the `select *` has the same output as step 2.

### 3. [REDACTED_USER]

```sql
mysql> admin check table t;
ERROR 8223 (HY000): data inconsistency in table: t, index: index_val, handle: 1, index-values:"handle: 1, values: [KindInt64 11]" != record-values:"handle: 1, values: [KindInt64 55]"

mysql> select * from t use index (index_val);
+----+-----+
| pk | val |
+----+-----+
|  1 |  11 |
|  2 |  22 |
|  4 |  22 |
|  3 |  33 |
|  2 |  44 |
|  4 |  44 |
|  1 |  55 |
+----+-----+
7 rows in set (0.01 sec)
```

### 4. [REDACTED_USER]

```
Release Version: v8.1.0
Edition: Community
Git Commit Hash: 945d07c5d5c7a1ae212f6013adfb187f2de24b23
Git Branch: HEAD
UTC Build Time: 2024-05-21 03:52:40
GoVersion: go1.21.10
Race Enabled: false
Check Table Before Drop: false
Store: tikv
```
