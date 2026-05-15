# Issue 63567: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/63567
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-09-17T08:14:54Z
- Updated: 2025-12-31T16:12:22Z
- Closed: 2025-12-31T16:12:22Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: TiDB
- Categories: schema-metadata, checkpoint-retry, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: Backup/Restore; TiDB; checkpoint-retry; observability-diagnosis; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. run log truncate but failed, and the metadata is not updated
2. retry to run log truncate but failed
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
success
### 3. [REDACTED_USER]
failed because the object does not exist
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
