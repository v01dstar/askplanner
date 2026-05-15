# Issue 58663: Restore schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58663
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-02T09:20:04Z
- Updated: 2025-12-09T11:15:44Z
- Closed: 2025-12-09T11:15:44Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR, Storage
- Categories: storage-access, schema-metadata
- Labels: affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, severity/moderate, type/bug
- Affected versions: affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Restore schema metadata mismatch`
- Search terms: BR; Restore; Storage; TiDB; schema-metadata; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

In tidb master version, `mysql.bind_info` is added as a could be restored (https://github.com/pingcap/tidb/blob/release-8.5/br/cmd/br/cmd.go#L40). 

But when check the sys table compatibility, it is omitted (https://github.com/pingcap/tidb/blob/release-8.5/br/pkg/restore/snap_client/systable_restore.go#L48).

We need to check its compatibility in case of any schema change in the future.
