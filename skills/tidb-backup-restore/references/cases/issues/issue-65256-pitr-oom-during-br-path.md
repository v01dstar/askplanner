# Issue 65256: PITR OOM during BR path

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/65256
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-12-25T07:00:57Z
- Updated: 2026-02-09T06:46:53Z
- Closed: 2026-01-08T02:48:48Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: pitr-log-restore, schema-metadata, sst-ingest-import, checkpoint-retry, performance-resource, observability-diagnosis
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `PITR OOM during BR path`
- Search terms: BR; PITR; checkpoint-retry; observability-diagnosis; performance-resource; pitr-log-restore; schema-metadata; sst-ingest-import

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/65394
- https://github.com/pingcap/tidb/pull/65631

## Issue Body

## Bug Report

### major [REDACTED_USER]
- [x] [PR1] **Should skip if db/table id is not found in `dbReplaces` from PiTR id map for A<->A PITR.** the metakv restore during log restore will put a default cf kv with original timestamp and rewritten dbID/tableID. Therefore, when retry restore, the kv will be loaded but not found in PiTR id map.
- [x] [PR1] **The restore id is 0 of PiTR id map.**
- [x] [RP2] **Database is duplicated.** If a database is created during log restore, and there is already a database with the same name in the downstream cluster, br will create another database with the same name so that the cluster has 2 databases with the same name.
- [x] [PR1] **The restore start ts of block list file should be recorded in the checkpoint.**


### corner [REDACTED_USER]

- [ ] **Constraint name is duplicated.** If log restore a table with a constraint named `chk1` and there is already another table in the same database having a constraint named `chk1` too, it won't report any error. The workaround is log restore by database level to avoid this case.
- [ ] **Table may still be cache status.** br should set `(*model.TableInfo).TableCacheStatusType` to `TableCacheStatusDisable` when rewrite entry for table.
- [x] [PR1] **Maybe the count of write cf meta kv is more than that of default cf meta kv.** `default cf kv is lost when processing write cf kv for table`

### Adjustment [REDACTED_USER]

- [ ] If a foreign key is created during log restore, report error only when recreate the foreign key if PITR only restore child table.
- [ ] Waiting 5 minutes to retry restore is too long after restore exits unexpectedly(oom or panic).
- [x] [PR1] If PITR restore specifies `--restored-ts` and exits unexpectedly(oom or panic), the retry restore cannot specify `--restored-ts`.
- [x] [PR1] blocklist error shows the `RestoreStartTs` too. (for example `cannot restore the table...`).

## Fix PR List
- PR1: #65394
- PR2: #65631
