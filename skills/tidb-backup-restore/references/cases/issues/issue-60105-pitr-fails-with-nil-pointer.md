# Issue 60105: PITR fails with nil pointer

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60105
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-17T06:16:53Z
- Updated: 2025-04-07T09:12:23Z
- Closed: 2025-03-17T14:29:37Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Storage, PD
- Categories: pitr-log-restore, storage-access, checkpoint-retry, performance-resource, observability-diagnosis
- Labels: affects-9.0, component/br, impact/panic, severity/critical, type/bug, type/regression
- Affected versions: affects-9.0

## Quick Match

- Title/error signature: `PITR fails with nil pointer`
- Search terms: BR; PD; PITR; Storage; TiDB; TiKV; checkpoint-retry; observability-diagnosis; performance-resource; pitr-log-restore; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
log restore only

> /br  restore  point --storage s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
> &force-path-style=true --pd http://downstream-pd.brie-acceptance-pitr-tps-7831559-1-66:2379 --restored-ts [REDACTED_LONG_ID] --start-ts [REDACTED_LONG_ID] --concurrency=8 --check-requirements=false

### 2. [REDACTED_USER]
log restore success

### 3. [REDACTED_USER]

> panic: runtime error: invalid memory address or nil pointer dereference
> [signal SIGSEGV: segmentation violation code=0x1 addr=0x40 pc=0x5ba3247]
> 
> goroutine 1 [running]:
> github.com/pingcap/tidb/br/pkg/task.RunRestore({0x78731d0, 0xc0012411d0}, {0x7894bc0, 0xc001c966b0}, {0x6f26c84, 0xd}, 0xc0018d0f08)
>         /workspace/source/tidb/br/pkg/task/restore.go:839 +0x847
> main.runRestoreCommand(0xc001bf0c08, {0x6f26c84, 0xd})
>         /workspace/source/tidb/br/cmd/br/restore.go:80 +0x739
> main.newStreamRestoreCommand.func1(0xc001bf0c08?, {0xc001c03ae0?, 0x4?, 0x6f08b81?})
>         /workspace/source/tidb/br/cmd/br/restore.go:254 +0x1f
> github.com/spf13/cobra.(*Command).execute(0xc001bf0c08, {0xc00013c6b0, 0xa, 0xa})
>         /root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985 +0xaaa
> github.com/spf13/cobra.(*Command).ExecuteC(0xc0018d2908)
>         /root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117 +0x3ff
> github.com/spf13/cobra.(*Command).Execute(...)
>         /root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041
> main.main()
>         /workspace/source/tidb/br/cmd/br/main.go:37 +0x23a


br.log

> [2025/03/17 05:21:53.127 +00:00] [INFO] [stream.go:359] ["tsoStream.recvLoop ended"] [stream=[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].brie-acceptance-pitr-tps-7831559-1-66.svc:2379-3] [error="rpc error: code = Canceled desc = context canceled"] [errorVerbose="rpc error: code = Canceled desc = context canceled\ngithub.com/tikv/pd/client/clients/tso.(*tsoStream).recvLoop\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-bdd857e5503b/clients/tso/stream.go:427\nruntime.goexit\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/asm_amd64.s:1700"]
> [2025/03/17 05:21:53.131 +00:00] [ERROR] [checkpoint.go:421] ["send the error"] [category=checkpoint] [error="context canceled"] [stack="github.com/pingcap/tidb/br/pkg/checkpoint.(*CheckpointRunner[...]).sendError\n\t/workspace/source/tidb/br/pkg/checkpoint/checkpoint.go:421\ngithub.com/pingcap/tidb/br/pkg/checkpoint.(*CheckpointRunner[...]).startCheckpointMainLoop.func2\n\t/workspace/source/tidb/br/pkg/checkpoint/checkpoint.go:468"]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
Release Version: v9.0.0-beta.1
Edition: Community
Git Commit Hash: 7b4717bf180ec94d5d42dc4d5ca3711d34131370
Git Branch: HEAD
UTC Build Time: 2025-03-13 03:08:08
GoVersion: go1.23.7
Race Enabled: false
Check Table Before Drop: false
Store: tikv

/br -V
Release Version: v9.0.0-beta.1
Git Commit Hash: 7b4717bf180ec94d5d42dc4d5ca3711d34131370
Git Branch: HEAD
Go Version: go1.23.7
UTC Build Time: 2025-03-13 03:09:50
Race Enabled: false
