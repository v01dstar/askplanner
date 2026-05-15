# Issue 59900: PITR gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59900
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-04T13:12:25Z
- Updated: 2025-03-05T10:25:07Z
- Closed: 2025-03-05T10:25:07Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, sst-ingest-import, observability-diagnosis
- Labels: component/br, feature/developing, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR gets stuck`
- Search terms: BR; PITR; TiDB; TiKV; observability-diagnosis; pitr-log-restore; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
Workload characteristics: a large number of small tables, with sporadic updates

### 2. [REDACTED_USER]
After using log backup compaction, the PiTR time is shorter than before using it.

### 3. [REDACTED_USER]
After using log backup compaction, the PiTR time is longer than before using it
Before using: 

> [2025/02/28 06:02:40.164 +00:00] [INFO] [collector.go:77] ["restore log success summary"] [total-take=22m42.6293174s] [source-start-point=[REDACTED_LONG_ID] [source-end-point=[REDACTED_LONG_ID] [target-end-point=[REDACTED_LONG_ID] [source-start="2025-02-19 08:07:55.035 +0000"] [source-end="2025-02-20 04:07:55.035 +0000"] [target-end="2025-02-28 05:39:57.519 +0000"] [total-kv-count=660055326] [skipped-kv-count-by-checkpoint=0] [total-size=261.4GB] [skipped-size-by-checkpoint=0B] [average-speed=191.8MB/s]

After using:

> [2025/03/04 03:01:16.073 +00:00] [INFO] [collector.go:77] ["restore log success summary"] [total-take=34m4.712071141s] [source-start-point=[REDACTED_LONG_ID] [source-end-point=[REDACTED_LONG_ID] [target-end-point=[REDACTED_LONG_ID] [source-start="2025-02-28 09:47:31.085 +0000"]
> [source-end="2025-03-01 05:47:31.085 +0000"] [target-end="2025-03-04 02:27:14.229 +0000"] [total-kv-count=242577383] [skipped-kv-count-by-checkpoint=0] [total-size=31.62GB] [skipped-size-by-checkpoint=0B] ["average-speed (log)"=15.46MB/s] [restore-sst-kv-count=416309359] [restore-s
> st-kv-size=[REDACTED_LONG_ID] ["restore-sst-physical-size (after compression)"=35416437434] [restore-sst-total-take=1m44.679031567s] ["average-speed (sst)"=2.149GB/s]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
TiDB version:
Release Version: v9.0.0-alpha-354-gb500d9e
Edition: Community
Git Commit Hash: b500d9e1eba04b617314fd6aa6b3d002bde2e379
Git Branch: HEAD
UTC Build Time: 2025-03-04 02:26:29
GoVersion: go1.23.6
Race Enabled: false
Check Table Before Drop: false
Store: tikv

BR version:
Release Version: v9.0.0-alpha-354-gb500d9e1eb-dirty
Git Commit Hash: b500d9e1eba04b617314fd6aa6b3d002bde2e379
Git Branch: master
Go Version: go1.24.0
UTC Build Time: 2025-03-04 08:05:07
Race Enabled: false
