# Issue 63928: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/63928
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-10-13T09:22:47Z
- Updated: 2025-11-14T08:44:48Z
- Closed: 2025-11-14T08:44:48Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: checkpoint-retry, performance-resource
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Restore; TiDB; checkpoint-retry; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. retry to run br snapshot restore with checkpoint
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
1. quickly start to restore tables
### 3. [REDACTED_USER]
1. stuck on the function `PreCheckTableClusterIndex` 2 hours.
### 4. [REDACTED_USER]
nightly
<!-- Paste the output of SELECT tidb_version() -->
