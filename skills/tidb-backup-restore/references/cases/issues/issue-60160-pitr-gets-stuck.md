# Issue 60160: PITR gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60160
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-03-19T03:59:56Z
- Updated: 2025-03-19T04:01:22Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Storage
- Categories: pitr-log-restore, storage-access, region-split-scatter, checkpoint-retry, performance-resource, observability-diagnosis
- Labels: affects-9.0, component/br, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: affects-9.0, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `PITR gets stuck`
- Search terms: BR; PITR; Storage; TiDB; TiKV; checkpoint-retry; observability-diagnosis; performance-resource; pitr-log-restore; region-split-scatter; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

- Large-scale cluster, data volume of 200TB, TiKV 100 nodes
- Large wide table
- do PiTR for this tidb cluster

### 2. [REDACTED_USER]
PiTR success

### 3. [REDACTED_USER]
log restore progress is stuck

[REDACTED_ATTACHMENT]

[2025/03/18 12:34:27.972 +00:00] [WARN] [checkpoint.go:318] ["failed to flush checkpoint data"] [error="[tikv:9005]Region is unavailable"] [errorVerbose="[tikv:9005]Region is unavailable\ngithub.com/pingcap/errors.AddStack\n\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/errors.go:178\ngithub.com/pingcap/errors.Trace\n\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/juju_adaptor.go:15\ngithub.com/pingcap/tidb/br/pkg/gluetidb.(*tidbSession).ExecuteInternal\n\t/workspace/source/tidb/br/pkg/gluetidb/glue.go:208\ngithub.com/pingcap/tidb/br/pkg/checkpoint.(*tableCheckpointStorage).flushCheckpointData\n\t/workspace/source/tidb/br/pkg/checkpoint/storage.go:151\ngithub.com/pingcap/tidb/br/pkg/checkpoint.(*CheckpointRunner[...]).doFlush\n\t/workspace/source/tidb/br/pkg/checkpoint/checkpoint.go:601\ngithub.com/pingcap/tidb/br/pkg/checkpoint.(*flusher[...]).doFlush\n\t/workspace/source/tidb/br/pkg/checkpoint/checkpoint.go:317\ngithub.com/pingcap/tidb/br/pkg/checkpoint.(*CheckpointRunner[...]).startCheckpointFlushLoop.func1\n\t/workspace/source/tidb/br/pkg/checkpoint/checkpoint.go:391\nruntime.goexit\n\t/root/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/asm_amd64.s:1700"]
[2025/03/18 12:35:39.497 +00:00] [INFO] [region_request.go:970] ["throwing pseudo region error due to no replica available"] [req-ts=[REDACTED_LONG_ID] [req-type=Prewrite] [region="{ region id: 1084, ver: 24375, confVer: 83 }"] [replica-read-type=leader] [stale-read=false] [request-sender="{rpcError:<nil>, replicaSelector: replicaSelectorV2{replicaReadType: leader, attempts: 14, cacheRegionIsValid: false, replicaStatus: [peer: 1401, store: 1039, isEpochStale: false, attempts: 10, attempts_time: 1.81ms, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable peer: 1725, store: 1539, isEpochStale: false, attempts: 1, attempts_time: 1.84ms, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable peer: 1744, store: 1503, isEpochStale: false, attempts: 1, attempts_time: 1.99ms, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable]}}"] [total-round-stats="{total-backoff: 1m11.5s, total-backoff-times: 11}"] [current-round-stats="{time: 1m11.5s, backoff: 1m11.5s, timeout: 30s, req-max-exec-timeout: 20s, retry-times: 13}"]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
./br -V
Release Version: v9.0.0-beta.1.pre-433-g80d6b56
Git Commit Hash: 80d6b5683c5c9e655d1eab432b198d7fea9b7d5f
Git Branch: HEAD
Go Version: go1.23.7
UTC Build Time: 2025-03-18 02:44:07
Race Enabled: false
