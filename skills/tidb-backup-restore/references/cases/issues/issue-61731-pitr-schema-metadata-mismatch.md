# Issue 61731: PITR schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61731
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-06-13T09:47:39Z
- Updated: 2025-11-27T02:46:05Z
- Closed: 2025-06-16T17:00:52Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, schema-metadata, observability-diagnosis
- Labels: affects-8.5, component/br, feature/developing, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR schema metadata mismatch`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

1. do PiTR on cluster B , which use cluster A‘s snapshot and log
2. after cluster B PiTR table filter success, do PiTR on cluster C which use cluster B‘s log and  use `--filter=!=sbtest*.*` to exclude  data from cluster A

### 2. [REDACTED_USER]
pitr success

### 3. [REDACTED_USER]
pitr fail
`[ERROR] [restore.go:76] ["failed to restore"] [error="cannot restore the table(Id=2002902) because it is log restored(at [REDACTED_LONG_ID]) before snapshot backup(at [REDACTED_LONG_ID]). Please respecify the filter that does not contain the table or replace with a newer snapshot backup."]`

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
Release Version: v8.5.0-20250609-a850b6f
Edition: Community
Git Commit Hash: https://github.com/pingcap/tidb/commit/a850b6f2634ee51c32b2ab8623c78035186e1278
Git Branch: heads/refs/tags/v8.5.0-20250609-a850b6f
UTC Build Time: 2025-06-09 02:24:01
GoVersion: go1.23.3
Race Enabled: false
Check Table Before Drop: false
Store: tikv
