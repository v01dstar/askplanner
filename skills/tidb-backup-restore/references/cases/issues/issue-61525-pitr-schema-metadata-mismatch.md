# Issue 61525: PITR schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61525
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-06-05T09:16:40Z
- Updated: 2025-07-02T07:50:24Z
- Closed: 2025-07-02T07:48:47Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: PITR
- Components: TiDB, TiKV, Operator, BR
- Categories: pitr-log-restore, schema-metadata, checksum-consistency, observability-diagnosis
- Labels: affects-8.5, component/br, feature/developing, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR schema metadata mismatch`
- Search terms: BR; Operator; PITR; TiDB; TiKV; checksum-consistency; observability-diagnosis; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. start pitr with table filter
2. inject tikv pod failure 10min. duiring this failure, pitr would fail
3. restart pitr
4. pitr could success but data was inconsistent.

backup log has these operations：

1. create table `index_Data2_v2`
2. drop table `index_Data2`
3. rename table `index_Data2_v2` to `index_Data2`

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
no table `index_Data2_v2` 

### 3. [REDACTED_USER]
table `index_Data2_v2`  in restore mode

[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->

Release Version: v9.0.0-beta.1.pre-869-g2bd1417
Edition: Community
Git Commit Hash: 2bd14176d4aa185f2b6f88cb506b4b8cc754a18d
Git Branch: HEAD
UTC Build Time: 2025-06-04 07:10:25
GoVersion: go1.23.9
Race Enabled: false
Check Table Before Drop: false
Store: tikv
Kernel Type: Classic
