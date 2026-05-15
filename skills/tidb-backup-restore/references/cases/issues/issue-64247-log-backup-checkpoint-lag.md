# Issue 64247: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/64247
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-11-03T13:26:52Z
- Updated: 2025-11-05T10:48:12Z
- Closed: 2025-11-05T10:48:12Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure, checkpoint-retry
- Labels: component/br, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Restore; TiDB; checkpoint-retry; restore-failure

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
	1.	Start a restore job.
	2.	Interrupt the job (e.g. by killing the process).
	3.	Attempt to resume the restore from checkpoint.
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
Restore should resume from the checkpoint and complete successfully.
### 3. [REDACTED_USER]
Restore fails with the following error:

```
error="task with ID 1 already exists and is running: [BR:Common:ErrInvalidArgument]invalid argument"] [
```

### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
