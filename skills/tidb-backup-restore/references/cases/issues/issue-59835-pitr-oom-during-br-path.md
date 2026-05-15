# Issue 59835: PITR OOM during BR path

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59835
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-02-28T03:44:55Z
- Updated: 2025-04-11T03:22:23Z
- Closed: 2025-02-28T09:21:44Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR, Storage
- Categories: pitr-log-restore, storage-access, performance-resource, observability-diagnosis
- Labels: affects-8.5, component/br, impact/oom, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR OOM during BR path`
- Search terms: BR; PITR; Storage; TiDB; observability-diagnosis; performance-resource; pitr-log-restore; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

Enable log backup, then restore with a backup contains ~200k tables from S3. 

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

Should success, though slow.

### 3. [REDACTED_USER]

OOM when `CopySST` was throttled, BR OOMs.

### 4. [REDACTED_USER]

Current master.

<!-- Paste the output of SELECT tidb_version() -->
