# Issue 60216: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60216
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-03-21T13:01:29Z
- Updated: 2025-09-22T11:31:04Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: TiDBX
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: checkpoint-retry
- Labels: affects-9.0, component/br, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: affects-9.0, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Restore; TiDB; TiKV; checkpoint-retry

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
1. start a v9.0.0 cluster on tidb cloud
2. prepare tpcc data
3. do backup on tidb cloud
4. restore backup
5. during restore procedure, the progress value start with 100%, then 112%, then 100%.

### 2. [REDACTED_USER]
Accurate progress value gradually increasing to 100%

### 3. [REDACTED_USER]
112% in progress

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
Release Version: v9.0.0-beta.1
Edition: Enterprise
Git Commit Hash: 7b4717bf180ec94d5d42dc4d5ca3711d34131370
Git Branch: HEAD
UTC Build Time: 2025-03-13 03:08:16
GoVersion: go1.23.7
Race Enabled: false
Check Table Before Drop: false
Store: tikv
Enterprise Extension Commit Hash: dc633aae52eb11b4e3549e3a7ef5b0ed14e159b1
