# Issue 67402: Restore fails with [BR:Common:ErrVersionMismatch]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67402
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2026-03-30T02:34:59Z
- Updated: 2026-03-30T10:48:06Z
- Closed: 2026-03-30T10:48:06Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: compatibility-upgrade
- Labels: affects-8.5, affects-9.0, component/br, severity/moderate, type/bug
- Affected versions: affects-8.5, affects-9.0

## Quick Match

- Title/error signature: `Restore fails with [BR:Common:ErrVersionMismatch]`
- Search terms: BR; Restore; TiDB; TiKV; compatibility-upgrade

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

Run BR restore with a version-mismatched cluster (e.g. BR v26.x against TiKV v8.x) and pass `--check-requirements=false`:

\`\`\`bash
br restore full \
  --pd "<pd-address>" \
  --storage "<storage-uri>" \
  --check-requirements=false
\`\`\`

### 2. [REDACTED_USER]

The restore should proceed without a version mismatch error, because `--check-requirements=false` is explicitly passed to skip version compatibility checks.

### 3. [REDACTED_USER]

BR still fails with:

\`\`\`
Error: TiKV node <address> version 8.5.4+branch-HEAD and BR v26.3.0-xxxx major version mismatch,
please use the same version of BR: [BR:Common:ErrVersionMismatch]version mismatch
\`\`\`

**Root cause:** `RunRestore` in `br/pkg/task/restore.go` calls `version.CheckClusterVersion` directly inside the `IsStreamRestore`/`else` branches without checking `cfg.CheckRequirements`. Only the call inside `NewMgr` (`br/pkg/conn/conn.go:177`) respects the flag; the second call at `restore.go:1027` is always executed regardless of `--check-requirements`.

### 4. [REDACTED_USER]

Affects all versions containing the dual version-check path in `RunRestore`.
