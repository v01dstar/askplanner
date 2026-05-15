# Issue 59152: PITR log backup lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59152
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-01-23T06:56:01Z
- Updated: 2025-01-24T02:19:37Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Lightning
- Categories: pitr-log-restore, schema-metadata, sst-ingest-import, checkpoint-retry, performance-resource, observability-diagnosis
- Labels: component/br, severity/moderate, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR log backup lag`
- Search terms: BR; Lightning; PITR; TiDB; TiKV; checkpoint-retry; observability-diagnosis; performance-resource; pitr-log-restore; schema-metadata; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
restore point with checkpoint
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
summary shows no error
### 3. [REDACTED_USER]
total-take is incorrent and speed is NaN
### 4. [REDACTED_USER]
```
[2025/01/22 15:52:48.838 +00:00] [INFO] [collector.go:77] ["restore log success summary"] [total-take=8m14.160280359s] [source-start-point=[REDACTED_LONG_ID] [source-end-point=[REDACTED_LONG_ID] [target-end-point=[REDACTED_LONG_ID] [source-start="2025-01-21 09:09:54.387 +0000"] [source-end="2025-01-22 02:57:48.087 +0000"] [target-end="2025-01-22 11:01:27.749 +0000"] [total-kv-count=12147041397] [skipped-kv-count-by-checkpoint=12136187042] [total-size=677.3GB] [skipped-size-by-checkpoint=675.7GB] ["average-speed (log)"=1.371GB/s] [restore-sst-kv-count=0] [restore-sst-kv-size=0] ["restore-sst-physical-size (after compression)"=0] [restore-sst-total-take=0s] ["average-speed (sst)"=NaNB/s]
```
before this restore, there is a former restore shows restore log duration is 4h+
```
[2025/01/22 10:57:38.548 +00:00] [INFO] [restore.go:543] ["set restore kv files concurrency"] [concurrency=1025]
[2025/01/22 10:57:38.548 +00:00] [INFO] [restore.go:546] ["set restore compacted sst files concurrency per store"] [concurrency=64]
[2025/01/22 10:57:38.548 +00:00] [WARN] [restore.go:1450] ["set max-index-length to max(3072*4) to skip check index length in DDL"]
[2025/01/22 10:57:38.548 +00:00] [WARN] [restore.go:1452] ["set index-limit to max(64*8) to skip check index count in DDL"]
[2025/01/22 10:57:38.548 +00:00] [WARN] [restore.go:1454] ["set table-column-count to max(4096) to skip check column count in DDL"]
...
[2025/01/22 15:03:00.642 +00:00] [INFO] [client.go:867] ["import files done"] [batch-count=8] [batch-size=6528] [take=252.212879ms] [files="[\"v1/20250122/01/1016/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20250122/01/1016/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20250122/02/1001/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20250122/02/1016/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20250122/02/1004/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20250122/02/1001/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20250122/02/1004/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20250122/02/1004/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \"]"]
```
<!-- Paste the output of SELECT tidb_version() -->
8.5.0
