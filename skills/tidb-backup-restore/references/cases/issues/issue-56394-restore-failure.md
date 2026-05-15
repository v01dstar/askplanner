# Issue 56394: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56394
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-09-29T03:35:32Z
- Updated: 2024-10-10T03:36:32Z
- Closed: 2024-10-08T10:46:42Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR, PD
- Categories: restore-failure
- Labels: component/br, severity/critical, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; PD; Restore; TiDB; TiKV; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br restore
2、kill one of tikv or kill pd leader or injection br network partition
3、br restore failed


### 2. [REDACTED_USER]
br restore success

### 3. [REDACTED_USER]
br restore failed

### 4. [REDACTED_USER]

./tidb-server -V
 Release Version: v8.4.0-alpha
Edition: Community
Git Commit Hash: f399e91cf873e21a8a5f8c9a74578cb76d20fd86
Git Branch: heads/refs/tags/v8.4.0-alpha
UTC Build Time: 2024-09-26 11:46:59
GoVersion: go1.21.10
Race Enabled: false
Check Table Before Drop: false
Store: unistore
2024-09-27T12:56:14.855+0800
