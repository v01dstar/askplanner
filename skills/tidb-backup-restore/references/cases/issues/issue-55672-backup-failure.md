# Issue 55672: Backup failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/55672
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-08-27T03:16:22Z
- Updated: 2024-09-09T05:17:32Z
- Closed: 2024-09-09T05:17:32Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, BR
- Categories: checkpoint-retry, performance-resource, observability-diagnosis
- Labels: affects-6.5, affects-7.5, component/br, severity/moderate, type/bug
- Affected versions: affects-6.5, affects-7.5

## Quick Match

- Title/error signature: `Backup failure`
- Search terms: BR; Backup; TiDB; checkpoint-retry; observability-diagnosis; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
Run EBS snapshot backup, when AWS get unavailable.

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
It should report the error we have encountered and have reasonable retry. 

### 3. [REDACTED_USER]
No log printed. The retry is too frequency and we have exceeded the quota of AWS EBS. 

### 4. [REDACTED_USER]
A release version of `6.5`.

<!-- Paste the output of SELECT tidb_version() -->
