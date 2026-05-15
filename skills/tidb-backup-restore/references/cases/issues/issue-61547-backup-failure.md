# Issue 61547: Backup failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61547
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-06-06T07:11:33Z
- Updated: 2025-06-26T02:40:43Z
- Closed: 2025-06-06T23:08:26Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, Operator, BR, Storage
- Categories: backup-failure, storage-access
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, affects-9.0, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, affects-9.0

## Quick Match

- Title/error signature: `Backup failure`
- Search terms: BR; Backup; Operator; Storage; TiDB; backup-failure; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
	1.	Configure a Pod to assume an IAM role via Web Identity (IRSA) that grants S3 access permissions.
	2.	Specify a custom S3 endpoint (e.g., a FIPS endpoint) in the backup configuration.
	3.	Execute a full backup operation.
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
Backup success.
### 3. [REDACTED_USER]
Backup failed.
### 4. [REDACTED_USER]
master

<!-- Paste the output of SELECT tidb_version() -->
