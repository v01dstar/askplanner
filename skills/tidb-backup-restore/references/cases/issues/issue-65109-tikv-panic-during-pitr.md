# Issue 65109: TiKV panic during PITR

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/65109
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-12-18T03:42:19Z
- Updated: 2025-12-19T01:49:09Z
- Closed: 2025-12-19T01:49:09Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, sst-ingest-import, observability-diagnosis
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `TiKV panic during PITR`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; pitr-log-restore; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

### 1. [REDACTED_USER]

1. Call `SetSSTs()` on a `CopiedSST` instance with valid input:
   - An empty slice: `sst.SetSSTs([])`
   - A single-element slice: `sst.SetSSTs([]*backuppb.File{file})`
2. Observe the panic

### 2. [REDACTED_USER]

The function should return successfully without panicking when provided with valid input (empty slice or single-element slice). The panic should only occur when multiple files are passed.

### 3. [REDACTED_USER]

The function panics even with valid input because the `log.Panic()` statement at the end of the method executes after the valid cases are handled. The missing `return` statements allow execution to fall through to the panic call.

### 4. [REDACTED_USER]

This is a bug in the BR (Backup & Restore) module's `log_client/ssts.go` file. Not version-specific, affects all versions using the current code.

**Location:** `br/pkg/restore/log_client/ssts.go` in the `SetSSTs` method

**Root Cause:** Missing `return` statements after handling valid cases (lines 124 and 129)
