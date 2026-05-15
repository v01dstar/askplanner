# Issue 67309: PITR schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67309
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-03-26T00:36:44Z
- Updated: 2026-04-17T02:41:39Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Lightning, Storage
- Categories: pitr-log-restore, restore-failure, storage-access, schema-metadata, region-split-scatter, sst-ingest-import, observability-diagnosis
- Labels: affects-8.5, component/br, contribution, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/critical, type/bug
- Affected versions: affects-8.5, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `PITR schema metadata mismatch`
- Search terms: BR; Lightning; PITR; Storage; TiDB; TiKV; observability-diagnosis; pitr-log-restore; region-split-scatter; restore-failure; schema-metadata; sst-ingest-import; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

### Bug [REDACTED_USER]

During PiTR (Point-in-Time Recovery) log restore, the `LogFilesIterWithSplitHelper` processes files in batches of 4096 (`SplitFilesBufferSize`). For each batch, it accumulates file metadata into a `LogSplitHelper`, calls `Split()` to compute and execute region splits, then
 proceeds to import the batch.

The problem is that `LogSplitHelper.iterator()` calls `delete(helper.tableSplitter, tableID)` for each entry as it builds the split iterator (split.go:86), draining the accumulated B-tree data. This means each batch starts with a fresh accumulator. For workloads that
spread writes across many regions (e.g., secondary index backfills), the per-region data accumulated within any single 4096-file batch is far below the split threshold — so no splits are triggered.

For example, with a 512MiB split threshold and data spread across 200+ regions, each batch might only accumulate ~10MiB per region — never reaching the threshold. The result is severely insufficient pre-splits (e.g., 22 instead of 200+), which causes regions to grow past
`coprocessor.region-max-size` during import, triggering TiKV-initiated auto-splits that produce `EpochNotMatch` cascades and eventual restore failure.

This is in contrast to snapshot restore, which already uses a two-pass approach: `SortAndValidateFileRanges()` scans ALL backup files upfront and computes all split keys before any data import begins (`snap_client/tikv_sender.go`).

### Reproduction [REDACTED_USER]

1. Set up a cluster with a large table (100+ GB) and a secondary index table (not a native index)
2. Run a full backup + continuous log backup
3. Perform a bulk secondary index backfill that generates ~24h of log data spread across many regions
4. Attempt PiTR restore replaying those logs
5. Observe that pre-split produces far too few split points, and restore fails with `EpochNotMatch` errors as TiKV auto-splits regions during import

### Expected [REDACTED_USER]

PiTR log restore should compute pre-splits based on the total cumulative data volume across ALL log files, not just within each 4096-file batch. This would produce accurate split points and prevent TiKV-initiated auto-splits during import.

### Proposed [REDACTED_USER]

Add a `PreSplitRegions` method that performs a full pre-scan over all DML file metadata (S3 metadata only — no data reads) before import begins, aligning with the two-pass pattern already used by snapshot restore:

1. Create a `LogSplitHelper` and iterate ALL DML files via `LoadDMLFiles()`, calling `helper.Merge()` for each
2. Call `helper.Split()` once after all files are merged
3. Then proceed to import with the existing per-batch path

The pre-split call should be non-fatal: on failure, fall through to the existing per-batch splitting for defense-in-depth.

**Note:** This fix is most effective when combined with removing the 1MiB `splitFileThreshold` filter in `LogSplitHelper.skipFile()`, which skips small PiTR virtual sub-range files from size estimation.

### Affected [REDACTED_USER]

Tested on v8.5.2. The bug exists in all versions with PiTR log restore support.

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
A lot of scattered inserts in the log backups

### 2. [REDACTED_USER]

Pre-splits to avoid splitting during log ApplyKVFile phase

### 3. [REDACTED_USER]

Excessive splits during log file applications, PiTR restore failure due to timeouts

### 4. [REDACTED_USER]

8.5.2
<!-- Paste the output of SELECT tidb_version() -->
