# Issue 53463: Backup/Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/53463
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-05-22T03:14:09Z
- Updated: 2024-06-03T07:30:59Z
- Closed: 2024-05-27T08:27:42Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: TiDB, BR
- Categories: uncategorized
- Labels: affects-6.1, affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, may-affects-5.4, report/community, severity/major, type/bug
- Affected versions: affects-6.1, affects-6.5, affects-7.1, affects-7.5, affects-8.1, may-affects-5.4

## Quick Match

- Title/error signature: `Backup/Restore failure`
- Search terms: BR; Backup/Restore; TiDB; uncategorized

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/34309

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. set the ak/sk through set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` enviroment variables
2. dumpling/br the data to aliyun provider

from asktug: https://asktug.com/t/topic/1026409
after https://github.com/pingcap/tidb/pull/34309,  for Aliyun's provider will ignore the  ak/sk in the environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
dumpling/br success  with the env `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` ak/sk
### 3. [REDACTED_USER]
dumpling/br failed 
### 4. [REDACTED_USER]
affect release-6.1, 6.5, 7.1, 7.5, 8.1
<!-- Paste the output of SELECT tidb_version() -->
