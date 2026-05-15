# Issue 67196: PITR OOM during TiKV path

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67196
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-03-20T19:20:24Z
- Updated: 2026-03-24T03:06:46Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, sst-ingest-import, performance-resource, gc-safepoint, observability-diagnosis
- Labels: affects-8.5, component/br, contribution, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/critical, type/bug
- Affected versions: affects-8.5, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `PITR OOM during TiKV path`
- Search terms: BR; PITR; TiDB; TiKV; gc-safepoint; observability-diagnosis; performance-resource; pitr-log-restore; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

### 1. [REDACTED_USER]

1. Run a TiDB cluster with 10+ TiKV stores under a sustained write workload of 15,000+ QPS of `REPLACE INTO` statements. This causes heavy auto-increment/auto-random ID allocation, producing a high volume of MVCC versions for `mDB:*` meta keys in the PiTR log stream.
2. Enable PiTR (log backup) on the cluster and let it run for a significant window (hours to days).
3. Attempt a PiTR point-in-time restore using `br restore point`.
4. The `br` process runs out of memory and is OOM-killed during the `RestoreMetaKVFiles` phase.

### 2. [REDACTED_USER]

The PiTR restore completes successfully without the `br` process being OOM-killed. Memory usage during the `RestoreMetaKVFiles` phase should be bounded and proportional to the number of logical meta keys, not to the total number of MVCC versions accumulated across the
backup window.

### 3. [REDACTED_USER]

The `br` process was OOM-killed during the `RestoreMetaKVFiles` step. Heap profiling collected prior to the OOM showed approximately **58 GB cumulative** allocated within `RestoreMetaKVFiles`, with two dominant sites:

- `log_file_manager.go:395` — **16.47 GB in-use** / 276M objects: `KvEntryWithTS` struct allocations
- `stream_mgr.go:301` — **29.87 GB cumulative** / 133 objects: `decodeCompressedData` output buffers

**Root cause 1 — Sub-slice pinning:** `DecodeKVEntry` returns `key` and `value` as sub-slices of the large decompressed file buffer (not copies). These sub-slices are stored in `KvEntryWithTS` structs. Go's GC cannot free the decompressed buffer as long as any single
`KvEntryWithTS` references it. The `nextKvEntries` carry-forward mechanism (entries with `ts >= filterTS` passed from one batch to the next) means a single surviving entry per file pins the entire 200+ MB decompressed buffer across all subsequent batches.

**Root cause 2 — No within-file dedup:** Under high-QPS `REPLACE INTO` workloads, auto-increment and auto-random ID counters (`mDB:*:IID:*`, `mDB:*:TARID:*`) generate thousands of MVCC versions per logical key per backup file. All versions are loaded into memory and passed
 through the sort/rewrite pipeline, but `RawKVBatchClient.Put` already silently discards all but the highest-timestamp version at write time. This means hundreds of thousands of entries per file are allocated, sorted, and rewritten only to be thrown away — wasting both
memory and CPU.

### 4. [REDACTED_USER]

v8.5.2
