# Issue 65060: Restore region split failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/65060
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-12-16T04:00:55Z
- Updated: 2026-02-06T14:24:31Z
- Closed: 2026-02-06T14:24:31Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: region-split-scatter
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Restore region split failure`
- Search terms: BR; Restore; TiDB; region-split-scatter

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. create table
```
create table test.t1 (a int, b int) SHARD_ROW_ID_BITS=2 PRE_SPLIT_REGIONS=2;
alter table test.t1 attributes "merge_option=deny";
```
2. snapshot backup and restore
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
```
show table test.t1 regions;
select * from information_schema.attributes from test.t1;
```
### 3. [REDACTED_USER]
nothing
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
