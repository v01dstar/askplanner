# Issue 61423: Restore gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61423
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-05-30T02:19:46Z
- Updated: 2025-12-12T04:28:38Z
- Closed: 2025-12-12T04:28:38Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: checkpoint-retry, performance-resource, checksum-consistency, observability-diagnosis
- Labels: affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Restore gets stuck`
- Search terms: BR; Restore; TiDB; checkpoint-retry; checksum-consistency; observability-diagnosis; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

1. Backup a cluster with large amount of small tables.
2. Restore it.
3. Observe the `[progress]` numbers in the log

### 2. [REDACTED_USER]

The progress increases smoothly from 0% to 100%

### 3. [REDACTED_USER]

The grows "smoothly" from 0% to maybe about 40%, and the keep unchanged during checksum, and suddenly jump to 100% at the end.

### 4. [REDACTED_USER]

BR v8.5.1
