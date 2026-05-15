# Issue 67970: Restore fails with [BR:Backup:ErrBackupGCSafepointExceeded]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67970
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-04-22T13:55:43Z
- Updated: 2026-04-27T07:16:26Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Restore
- Components: TiDB, BR, PD
- Categories: restore-failure, gc-safepoint, observability-diagnosis
- Labels: component/br, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `Restore fails with [BR:Backup:ErrBackupGCSafepointExceeded]`
- Search terms: BR; PD; Restore; TiDB; gc-safepoint; observability-diagnosis; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1，run br restore
2，pd rolling restart

### 2. [REDACTED_USER]
br restore can succeed

### 3. [REDACTED_USER]
br restore failed with panic
2026/04/19 12:31:54.360 +00:00] [PANIC] [safepoint.go:110] ["cannot pass gc safe point check, aborting"] [error="GC safepoint [REDACTED_LONG_ID] exceed TS [REDACTED_LONG_ID]: [BR:Backup:ErrBackupGCSafepointExceeded]backup GC safepoint exceeded"] [errorVerbose="[BR:Backup:ErrBackupGCSafepointExceeded]backup GC safepoint exceeded\nGC safepoint [REDACTED_LONG_ID] exceed TS [REDACTED_LONG_ID]\ngithub.com/pingcap/tidb/br/pkg/gc.CheckGCSafePoint\n\t/workspace/source/tidb/br/pkg/gc/safepoint.go:65\ngithub.com/pingcap/tidb/br/pkg/gc.StartServiceSafePointKeeper.func1\n\t/workspace/source/tidb/br/pkg/gc/safepoint.go:109\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1693"] [safePoint="{ID=br-[REDACTED_UUID],TTL=5m0s,BackupTime=\"2026-04-19 12:12:42.373 +0000 UTC\",BackupTS=[REDACTED_LONG_ID]}"] [stack="github.com/pingcap/tidb/br/pkg/gc.StartServiceSafePointKeeper.func1\n\t/workspace/source/tidb/br/pkg/gc/safepoint.go:110"]

[br.log.2026-04-19T12.12.41Z.zip]([REDACTED_ATTACHMENT_URL])

### 4. [REDACTED_USER]
./br -V
 Release Version: v9.0.0-beta.2.pre-1584-ga10a43ada5
Git Commit Hash: a10a43ada5abe6cbd7ce5e4a9f3ca7654089ee34
Git Branch: HEAD
Go Version: go1.25.8
UTC Build Time: 2026-04-19 05:06:43
Race Enabled: false
Kernel Type: Classic
