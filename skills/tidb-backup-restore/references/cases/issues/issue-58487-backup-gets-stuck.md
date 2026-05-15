# Issue 58487: Backup gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58487
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-12-23T10:31:36Z
- Updated: 2024-12-27T06:54:20Z
- Closed: 2024-12-27T06:54:20Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR
- Categories: performance-resource, observability-diagnosis
- Labels: affects-7.5, affects-8.1, component/br, severity/major, type/bug
- Affected versions: affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `Backup gets stuck`
- Search terms: BR; Backup; TiDB; TiKV; observability-diagnosis; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br backup
2、inject one of tikv network partition lasts for 3mins
[br.log.2024-12-23T01.10.24Z.zip]([REDACTED_ATTACHMENT_URL])

### 2. [REDACTED_USER]
br backup can succeed

### 3. [REDACTED_USER]
backup br stuck after injection one of tikv network partition

### 4. [REDACTED_USER]
./br -V
 Release Version: v7.5.5
Git Commit Hash: f3038bc996a4ad74a447324d64451a76447eae74
Git Branch: HEAD
Go Version: go1.21.13
UTC Build Time: 2024-12-20 07:35:36
Race Enabled: false
