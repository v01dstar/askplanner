# Issue 60218: PITR schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60218
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-21T18:15:45Z
- Updated: 2025-03-25T04:01:13Z
- Closed: 2025-03-25T04:01:13Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, schema-metadata
- Labels: component/br, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR schema metadata mismatch`
- Search terms: BR; PITR; TiDB; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

recent change modifies the ordering when creating tables, need to keep table in the same schema next to each other in the list so can use batch
