# Issue 64514: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/64514
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-11-17T04:07:39Z
- Updated: 2026-01-13T16:29:18Z
- Closed: 2026-01-13T16:29:18Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Restore
- Components: TiDB, BR, PD
- Categories: restore-failure, observability-diagnosis
- Labels: component/br, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; PD; Restore; TiDB; observability-diagnosis; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br restore
2、simulated pd network partition

### 2. [REDACTED_USER]
br restore can succeed

### 3. [REDACTED_USER]
BR restore failed with error "type:UNKNOWN message:\"invalid store ID 0, not found\"

[br.log.2025-11-14T03.40.11Z.zip]([REDACTED_ATTACHMENT_URL])

### 4. [REDACTED_USER]
./tidb-server -V
 Release Version: v9.0.0-beta.2.pre-784-gcf74287377
Edition: Community
Git Commit Hash: cf742873771db9f9c99e559b6db289a45067ef12
Git Branch: HEAD
UTC Build Time: 2025-11-11 08:42:59
GoVersion: go1.25.4
Race Enabled: false
Check Table Before Drop: false
Store: unistore
Kernel Type: Classic
