# Issue 56845: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56845
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-10-25T09:50:46Z
- Updated: 2024-12-17T06:27:08Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: checkpoint-retry, performance-resource
- Labels: component/br, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Restore; TiDB; checkpoint-retry; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. do rolling restart
2. do volumebackup

### 2. [REDACTED_USER]
1. volumebackup success
2. The pause schedule lasts for a short period of time

### 3. [REDACTED_USER]
1. volumebackup is stuck, when exceed Volume Backup Init Job Max Active Seconds, volumebackup is set to failed
[REDACTED_ATTACHMENT]
[REDACTED_ATTACHMENT]
[REDACTED_ATTACHMENT]
[REDACTED_ATTACHMENT]


### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
