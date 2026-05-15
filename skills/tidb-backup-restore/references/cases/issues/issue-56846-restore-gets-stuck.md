# Issue 56846: Restore gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56846
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-10-25T09:50:52Z
- Updated: 2024-12-17T06:26:55Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: backup-failure, performance-resource
- Labels: component/br, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore gets stuck`
- Search terms: BR; Restore; TiDB; backup-failure; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. create volumebackupschedule
2. create cluster

### 2. [REDACTED_USER]
1. snapshot backup will not stuck when encountered error, it will be set to failed Immediately

### 3. [REDACTED_USER]
1. snapshot backup stuck when encountered error

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
[REDACTED_ATTACHMENT]
