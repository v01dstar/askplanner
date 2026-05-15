# Issue 54139: Backup schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/54139
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-06-20T10:12:20Z
- Updated: 2024-06-24T12:08:52Z
- Closed: 2024-06-24T12:08:52Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, BR
- Categories: backup-failure, schema-metadata
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, severity/minor, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `Backup schema metadata mismatch`
- Search terms: BR; Backup; TiDB; backup-failure; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. start an incremental backup on a cluster that executes 200k ddls. 
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
1. backup succeed
### 3. [REDACTED_USER]
2. backup failed due to too many scan operations on history ddl jobs.
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
