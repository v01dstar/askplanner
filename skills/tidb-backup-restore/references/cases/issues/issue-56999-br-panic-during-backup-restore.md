# Issue 56999: BR panic during backup/restore

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56999
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-10-30T09:13:45Z
- Updated: 2024-12-20T03:06:05Z
- Closed: 2024-10-30T15:45:40Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: TiDB, BR
- Categories: observability-diagnosis
- Labels: affects-8.4, component/br, impact/panic, severity/major, type/bug
- Affected versions: affects-8.4

## Quick Match

- Title/error signature: `BR panic during backup/restore`
- Search terms: BR; Backup/Restore; TiDB; observability-diagnosis

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/56075

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

1. Start a nightly cluster.
2. Run `br log status`.

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

BR should fail with message "incompatible".

### 3. [REDACTED_USER]

BR paniced.

### 4. [REDACTED_USER]

Master.

[REDACTED_ATTACHMENT]

<!-- Paste the output of SELECT tidb_version() -->

NOTE: The error was omitted at https://github.com/pingcap/tidb/pull/56075/files#diff-82ee5900311f16cef9a19f0efdc01606af750a36a92365bc7ac68bfb010eef44R186
