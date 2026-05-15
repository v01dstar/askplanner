# Issue 62620: PITR log backup lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/62620
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-07-24T10:41:52Z
- Updated: 2025-07-24T10:48:13Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, observability-diagnosis
- Labels: affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR log backup lag`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. 10tidb(16C32G)-3pd(4C8G, 20G per)-18tikv(16C64G, 2000 per), 10T data
2.  enable log backup
3.  run workload, and make one of tikv failure 10 minutes

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
log backup log within 10 minutes

### 3. [REDACTED_USER]

[REDACTED_ATTACHMENT]

[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
Release Version: v8.5.3
Edition: Enterprise
Git Commit Hash: dcbfb10cd28823999e66aae541cdc5d904d231a6
Git Branch: HEAD
UTC Build Time: 2025-07-21 17:07:22
GoVersion: go1.23.8
Race Enabled: false
Check Table Before Drop: false
Store: tikv
Enterprise Extension Commit Hash: 7d43ff65ebc145bd63fa84cb368f8775be906998
