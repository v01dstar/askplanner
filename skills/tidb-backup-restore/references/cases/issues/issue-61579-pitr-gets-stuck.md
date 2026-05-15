# Issue 61579: PITR gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61579
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-06-09T04:36:11Z
- Updated: 2025-06-16T05:58:49Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR, Storage
- Categories: pitr-log-restore, restore-failure, storage-access, region-split-scatter, performance-resource, observability-diagnosis
- Labels: component/br, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `PITR gets stuck`
- Search terms: BR; PITR; Storage; TiDB; TiKV; observability-diagnosis; performance-resource; pitr-log-restore; region-split-scatter; restore-failure; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

From [AskTUG](https://asktug.com/t/topic/1042889/21).

### 1. [REDACTED_USER]

1. Start a cluster.
2. Start a log backup task.
3. Write data immediately with enough throughput (maybe `sysbench prepare`) to generate log files huge enough to trigger split when restoring.
4. Drop existing databases and restore.

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

Restore successed.

### 3. [REDACTED_USER]

Restore was stuck at splitting tables.

```
github.com/tikv/pd/client.(*client).ScanRegions(/*pd_client*/0xc000cf40a0, /*ctx*/{0x56808b0, 0xc003539740}, /*start_key*/{0x0, 0x0, 0x0}, /*end_key*/{0xc0031279f8, 0x12, 0x12}, /*limit*/0x40)
        /go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-7d0389306a8b/client.go:1519+0x637
```

### 4. [REDACTED_USER]

v6.6.0

### Notes

[REDACTED_USER]
https://github.com/pingcap/tidb/blob/a165d9fd7c01dbde901701ea9312ccd41b0268dc/br/pkg/restore/split/splitter.go#L275-L299

If last of scanned region is the last region (end key = ""), this may be sutck in an infinite loop.
<!-- Paste the output of SELECT tidb_version() -->
