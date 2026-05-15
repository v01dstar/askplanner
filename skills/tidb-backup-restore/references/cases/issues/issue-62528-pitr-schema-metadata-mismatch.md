# Issue 62528: PITR schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/62528
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-07-21T04:35:55Z
- Updated: 2025-11-27T02:42:52Z
- Closed: 2025-07-24T15:07:11Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, schema-metadata, observability-diagnosis
- Labels: affects-8.5, component/br, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR schema metadata mismatch`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

We noticed in our current test, although passing, has an error log saying "failed to load schema diff" due to drop db + table issue. Problem lies in the DDL drop table will check tableInfo on TiKV but in BR case the db is gone already so the check will fail. However, in the test this error is silent since DDL will fall back to schema full reload so the final result is still correct. 

impact master and latest 9.0 and one 8.5 hot fix branch
