# Issue 58002: PITR region split failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58002
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-12-05T06:46:10Z
- Updated: 2025-04-01T01:40:41Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Lightning, PD
- Categories: pitr-log-restore, region-split-scatter, sst-ingest-import, checkpoint-retry, performance-resource, observability-diagnosis
- Labels: affects-8.5, component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/major, type/bug
- Affected versions: affects-8.5, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `PITR region split failure`
- Search terms: BR; Lightning; PD; PITR; TiDB; TiKV; checkpoint-retry; observability-diagnosis; performance-resource; pitr-log-restore; region-split-scatter; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
1 million tables and read/write on 100k tables
log backcup
log restore to a empty cluster , it takes 16h11m to restore for 171.5GB data.
```
[2024/12/04 18:53:05.417 +00:00] [INFO] [collector.go:77] ["restore log success summary"] [total-take=16h11m42.662016972s] [source-start-point=[REDACTED_LONG_ID] [source-end-point=[REDACTED_LONG_ID] [target-end-point=[REDACTED_LONG_ID] [source-start="2024-12-03 14:16:53.431 +0000"] [source-end="2024-12-04 00:08:31.031 +0000"] [target-end="2024-12-04 02:41:22.757 +0000"] [total-kv-count=1111389936] [skipped-kv-count-by-checkpoint=0] [total-size=171.5GB] [skipped-size-by-checkpoint=0B] [average-speed=2.942MB/s]
```
The br nearly need process 3048431 * 8 files when log restore.
```
[2024/12/04 17:50:03.865 +00:00] [INFO] [client.go:754] ["import files done"] [batch-count=8] [batch-size=65776] [take=578.003479ms] [files="[\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \",\"v1/20241203/23/1014/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \"]"]
```
```
root@benchtoolset2-0:/# grep "import files done" /tmp/br.log.2024-12-04T00.14* | wc -l
3048431
```
when increase the concurrency the restore speed increase(5h38m) but the restore process will pause for long time for tikv flow control
```
[2024/12/04 23:56:43.972 +00:00] [INFO] [collector.go:77] ["restore log success summary"] [total-take=5h38m50.532165537s] [source-start-point=[REDACTED_LONG_ID] [source-end-point=[REDACTED_LONG_ID] [target-end-point=[REDACTED_LONG_ID] [source-start="2024-12-03 14:16:53.431 +0000"] [source-end="2024-12-04 00:08:31.031 +0000"] [target-end="2024-12-04 18:17:53.448 +0000"] [total-kv-count=1111389936] [skipped-kv-count-by-checkpoint=0] [total-size=171.5GB] [skipped-size-by-checkpoint=0B] [average-speed=8.437MB/s]
```
[REDACTED_ATTACHMENT]
[REDACTED_ATTACHMENT]
the br log in the paused time
```
[2024/12/04 18:47:47.636 +00:00] [INFO] [store_cache.go:1060] ["store health status changed"] [storeID=1001] [isSlow=false] [healthDetail="{ ClientSideSlowScore: 1, TiKVSideSlowScore: 70 }"]
[2024/12/04 18:47:47.952 +00:00] [INFO] [store_cache.go:1060] ["store health status changed"] [storeID=1001] [isSlow=true] [healthDetail="{ ClientSideSlowScore: 100, TiKVSideSlowScore: 70 }"]
[2024/12/04 18:47:53.494 +00:00] [INFO] [pd.go:329] ["pause scheduler(configs)"] [name="[balance-region-scheduler,balance-leader-scheduler,balance-hot-region-scheduler]"] [cfg="{\"enable-location-replacement\":\"false\",\"leader-schedule-limit\":24,\"max-pending-peer-count\":2147483647,\"max-snapshot-count\":40,\"merge-schedule-limit\":0,\"region-schedule-limit\":40}"]
[2024/12/04 18:48:02.635 +00:00] [INFO] [store_cache.go:1060] ["store health status changed"] [storeID=1001] [isSlow=false] [healthDetail="{ ClientSideSlowScore: 1, TiKVSideSlowScore: 70 }"]
[2024/12/04 18:48:13.191 +00:00] [INFO] [store_cache.go:1060] ["store health status changed"] [storeID=1001] [isSlow=true] [healthDetail="{ ClientSideSlowScore: 100, TiKVSideSlowScore: 62 }"]
[2024/12/04 18:48:14.951 +00:00] [INFO] [progress.go:176] [progress] [step="Restore Files(SST + KV)"] [progress=6.81%] [count="83473512 / 1225755334"] [speed="206435 p/s"] [elapsed=20m0s] [remaining=1h32m13s]
```
### 2. [REDACTED_USER]

### 3. [REDACTED_USER]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
Release Version: v8.5.0-alpha-279-g9812d85d0d
Git Commit Hash: 9812d85d0d259547cf1dae88abbc7c406c56f935
Git Branch: HEAD
Go Version: go1.23.3
UTC Build Time: 2024-12-03 17:06:19
Race Enabled: false
