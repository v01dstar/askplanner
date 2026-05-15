# Issue 62366: Backup storage credential failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/62366
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-07-11T01:35:03Z
- Updated: 2025-07-15T02:21:10Z
- Closed: 2025-07-15T02:21:10Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: TiDBX
- Operation: Backup
- Components: TiDB, Operator, BR, Storage
- Categories: storage-access, compatibility-upgrade
- Labels: affects-7.5, component/br, type/bug
- Affected versions: affects-7.5

## Quick Match

- Title/error signature: `Backup storage credential failure`
- Search terms: BR; Backup; Operator; Storage; TiDB; compatibility-upgrade; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
<!-- a step by step guide for reproducing the bug. -->
1. TiDB Cloud upgrade k8s to 1.33
2. start a v7.5.6 TiDB Cloud dedicated cluster
3. do manual backup### 2. What did you expect to see? (Required)
manual backup job's status became success
### 3. [REDACTED_USER]
manual backup jobs' status remains running
error:
> Couldn't find AWS credentials in environment, credentials file, or IAM role;


### 4. [REDACTED_USER]
<!-- Paste the output of SELECT tidb_version() -->
v7.5.6
(v7.5.6-20250630-04b64cf)
