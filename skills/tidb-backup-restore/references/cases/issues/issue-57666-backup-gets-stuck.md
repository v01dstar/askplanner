# Issue 57666: Backup gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57666
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-11-25T06:28:08Z
- Updated: 2025-04-01T01:59:19Z
- Closed: 2024-11-27T05:15:56Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, BR
- Categories: backup-failure, performance-resource
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Backup gets stuck`
- Search terms: BR; Backup; TiDB; backup-failure; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
similar with https://github.com/pingcap/tidb/issues/53480
but when backup large amount of tables on one store. and if backup slow, some requests might wait for more than one hour, cause the connection reset.
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
backup succeed
### 3. [REDACTED_USER]
backup stuck
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
