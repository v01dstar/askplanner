# Issue 62939: Backup/Restore fails with nil pointer

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/62939
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-08-12T04:55:22Z
- Updated: 2025-08-13T02:38:49Z
- Closed: 2025-08-13T02:38:49Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: TiDB, BR
- Categories: performance-resource
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, impact/panic, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Backup/Restore fails with nil pointer`
- Search terms: BR; Backup/Restore; TiDB; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

### 3. [REDACTED_USER]

```
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x2a365f3]
goroutine 47 [running]:
github.com/pingcap/tidb/br/pkg/streamhelper.(*FlushSubscriber).Clear(0x0)
	br/pkg/streamhelper/flush_subscriber.go:113 +0x2d3
github.com/pingcap/tidb/br/pkg/streamhelper.(*FlushSubscriber).Drop(...)
	br/pkg/streamhelper/flush_subscriber.go:121
github.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).stopSubscriber(0xc00047e980)
	br/pkg/streamhelper/advancer.go:518 +0xb8
github.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).OnStop(0xc00047e980)
	br/pkg/streamhelper/advancer_daemon.go:52 +0x7e
github.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).OnBecomeOwner.func1()
	br/pkg/streamhelper/advancer_daemon.go:40 +0x54
created by github.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).OnBecomeOwner in goroutine 163
	br/pkg/streamhelper/advancer_daemon.go:38 +0x113 
```
### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
