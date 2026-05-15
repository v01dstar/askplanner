# Issue 58845: PITR failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58845
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-09T20:27:23Z
- Updated: 2025-10-10T20:31:34Z
- Closed: 2025-01-21T04:11:37Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV, BR
- Categories: pitr-log-restore, checkpoint-retry, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, report/customer, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR failure`
- Search terms: BR; PITR; TiKV; checkpoint-retry; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

A customer [REDACTED_CUSTOMER]`rpcClient is idle` during log restore and causes the restore to fail, looks like some issue with the `client-go` lib that when it recycles the connection a request comes in and will fail with such error. 

At BR side we can probably add a retry logic and next try should create a new connection and works just fine

similar report https://github.com/tikv/client-go/issues/568
