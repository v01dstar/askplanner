# Issue 53480: Backup gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/53480
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-05-22T07:41:32Z
- Updated: 2024-10-30T11:21:45Z
- Closed: 2024-08-13T08:57:03Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR
- Categories: performance-resource
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.4, component/br, severity/moderate, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.4

## Quick Match

- Title/error signature: `Backup gets stuck`
- Search terms: BR; Backup; TiDB; TiKV; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. backup
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
success
### 3. [REDACTED_USER]
br stuck

```
goroutine 17165 [select, 1399 minutes]:
google.golang.org/grpc/internal/transport.(*Stream).waitonHleader(..)
google.golang.org/grpc/internal/transport.(*Stream).RecvCompress(..)
google.golang.org/grpc.(*csAttempt).recvMsg(..)
google.golang.org/grpc.(*clientStream).RecvMsg.func1(..)
google.golang.org/grpc.(*clientStream).withRetry(..)
google.golang.org/grpc.(*clientStream).RecvMsg(..}
github.com/pingcap/kvproto/pkg/brpb.(*backupBackupClient).Recv(..)
github.com/pingcap/tidb/br/pkg/backup.doSendBackup(..)
```

### 4. [REDACTED_USER]
7.1
<!-- Paste the output of SELECT tidb_version() -->
