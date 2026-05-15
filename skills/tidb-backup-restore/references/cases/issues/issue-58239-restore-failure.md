# Issue 58239: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58239
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-12-13T03:59:38Z
- Updated: 2025-01-08T10:13:58Z
- Closed: 2025-01-08T10:13:58Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR, PD
- Categories: uncategorized
- Labels: affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; PD; Restore; TiDB; uncategorized

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. run br restore, there is a tmp error resulting in tso client not created successfully.

### 2. [REDACTED_USER]
br restore should be able to tolerate tmp error like this.

### 3. [REDACTED_USER]
br restore doesn't tolerate the tmp error
[REDACTED_ATTACHMENT]


### 4. [REDACTED_USER]
v8.5.0
