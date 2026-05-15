# Issue 61642: PITR failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61642
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-06-11T03:41:08Z
- Updated: 2025-08-29T06:25:53Z
- Closed: 2025-08-29T06:25:53Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: pitr-log-restore, observability-diagnosis
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR failure`
- Search terms: BR; PITR; observability-diagnosis; pitr-log-restore

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Testing locally found that if adding foreign key during log backup, it will automatically add an index. In the PiTR restore process, it will first drop the index and then recreate it. However due to foreign key constraint, the drop index op will fail since violating constraint, causing the pitr to fail
