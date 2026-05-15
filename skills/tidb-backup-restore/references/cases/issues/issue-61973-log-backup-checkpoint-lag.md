# Issue 61973: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61973
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-06-24T13:08:41Z
- Updated: 2025-06-26T19:20:23Z
- Closed: 2025-06-26T19:20:23Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, Operator, BR
- Categories: restore-failure, checkpoint-retry, observability-diagnosis
- Labels: component/br, feature/developing, severity/critical, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Operator; Restore; TiDB; checkpoint-retry; observability-diagnosis; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、br restore
2、restore br pod during br restore
3、rerun br restore

### 2. [REDACTED_USER]
br restore can succeed

### 3. [REDACTED_USER]
br full restore failed based on checkpoint
`Detail BR log in /tmp/br.log.2025-06-24T12.58.44Z 
[2025/06/24 12:58:45.021 +00:00] [INFO] [collector.go:77] ["DataBase Restore failed summary"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0]
Error: task with ID 2000001 already exists and is running: [BR:Common:ErrInvalidArgument]invalid argument`

[REDACTED_ATTACHMENT]

### 4. [REDACTED_USER]
sh-5.1# ./br -V
Release Version: v9.0.0-beta.1.pre-991-g22fe893
Git Commit Hash: 22fe893c88d3c51de74f20af9584d3bae7613be6
Git Branch: HEAD
Go Version: go1.23.10
UTC Build Time: 2025-06-24 11:54:49
Race Enabled: false
