# Issue 65436: Backup failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/65436
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2026-01-06T07:54:40Z
- Updated: 2026-01-08T14:00:26Z
- Closed: 2026-01-08T14:00:26Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiKV, Operator, BR, Storage
- Categories: storage-access, checkpoint-retry, performance-resource, observability-diagnosis
- Labels: affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Backup failure`
- Search terms: BR; Backup; Operator; Storage; TiKV; checkpoint-retry; observability-diagnosis; performance-resource; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

### Summary
[REDACTED_USER]

### Error [REDACTED_USER]
```
[ERROR] [endpoint.rs:1151] ["backup create storage failed"] [err_code=KV:Unknown] [err="Custom { kind: InvalidInput, error: \"credential info not found\" }"]
```

### Expected [REDACTED_USER]
BR should recognize "credential info not found" as a non-retryable error and fail immediately with a clear error message, since this is a configuration issue that cannot be resolved by retry.

### Current [REDACTED_USER]
BR retries indefinitely, appearing to be stuck.

### Proposed [REDACTED_USER]
Add "credential info not found" to the list of non-retryable errors in `br/pkg/utils/error_handling.go`.
