# Issue 67016: Restore schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67016
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2026-03-15T08:17:18Z
- Updated: 2026-04-16T10:15:08Z
- Closed: 2026-04-16T10:15:08Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: schema-metadata, region-split-scatter, compatibility-upgrade
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Restore schema metadata mismatch`
- Search terms: BR; Restore; TiDB; TiKV; compatibility-upgrade; region-split-scatter; schema-metadata

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/66637

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

This issue happens on the tool-version split:
- cluster: `v8.5.5`
- new backup tool: BR containing `#66637`
- old restore tool: `br:v8.5.5`

A minimal local Playground reproduction is:

1. Start a local cluster:
   ```bash
   tiup playground v8.5.5 --db 1 --pd 1 --kv 1 --tiflash 0 --without-monitor
   ```
2. Create a normal table with `merge_option=allow`:
   ```sql
   create database compat66637;
   create table compat66637.t_normal (a int primary key, b varchar(100));
   insert into compat66637.t_normal values (1,'test1'),(2,'test2'),(3,'test3');
   alter table compat66637.t_normal attributes='merge_option=allow';
   ```
3. Verify before backup:
   ```sql
   select id, type, attributes
   from information_schema.attributes
   where db_name='compat66637' and table_name='t_normal';
   ```
   The attribute is present before backup.
4. Use a new BR that already contains `#66637` to run backup.
5. Decode or inspect the backup metadata and confirm it contains the new field:
   - `is_merge_option_allowed: true`
6. Restore the backup with old `br:v8.5.5`:
   ```bash
   tiup br:v8.5.5 restore full -s local:///tmp/compat66637-repro/normal_backup --pd [REDACTED_IP]:18379
   ```
7. Check after restore:
   ```sql
   select count(*) from compat66637.t_normal;
   select id, type, attributes
   from information_schema.attributes
   where db_name='compat66637' and table_name='t_normal';
   ```

The same problem can also be reproduced on a partitioned table where:
- table-level attribute is `merge_option=allow`
- partition-level attribute is `merge_option=deny`

### 2. [REDACTED_USER]

I expected that if the new backup artifact already carries the `merge_option` metadata, then restore should preserve those attributes.

Concretely:
- restore should succeed
- row counts should remain correct
- `information_schema.attributes` should still show the same `merge_option` attributes after restore

### 3. [REDACTED_USER]

Old `br:v8.5.5` restore succeeded and data was restored correctly, but the `merge_option` attributes were silently lost.

For the normal table case:
- row count after restore stayed `3`
- but `information_schema.attributes` became empty for that table

For the partition table case:
- row count after restore stayed `2`
- but both table-level and partition-level attributes disappeared

A control restore of the same backup with the new BR preserved the attributes, so the backup artifact itself is correct. The loss happens on the old restore path.

### 4. [REDACTED_USER]

Cluster [REDACTED_CLUSTER]:
```text
Release Version: v8.5.5
```

### Additional [REDACTED_USER]

This is not simply an old feature limitation.

`merge_option` attributes can already exist on a `v8.5.5` cluster. The compatibility bug is that a new BR backup artifact really contains the metadata, but an old `br:v8.5.5` restore tool still drops it silently.

This is a tool-version compatibility issue in the restore path: restore appears successful, but metadata semantics are incomplete afterward.

The reproduction was validated locally with Playground. The new backup tool was a BR built from `origin/release-8.5` at `0d5390c1de`, which contains commit `8f1e9a98f9` / PR `#66637`. A detailed local report artifact is available on my side if needed.
