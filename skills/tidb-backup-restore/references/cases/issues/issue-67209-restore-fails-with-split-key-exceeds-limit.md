# Issue 67209: Restore fails with split key exceeds limit

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67209
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-03-23T05:52:49Z
- Updated: 2026-03-24T02:31:48Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: TiDBX
- Operation: Restore
- Components: TiDB, TiKV, BR, Storage
- Categories: restore-failure, storage-access, region-split-scatter, performance-resource
- Labels: affects-8.5, component/br, contribution, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/major, type/bug
- Affected versions: affects-8.5, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `Restore fails with split key exceeds limit`
- Search terms: BR; Restore; Storage; TiDB; TiKV; performance-resource; region-split-scatter; restore-failure; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

### 1. [REDACTED_USER]

1. Backup a large-scale TiDB cluster with high region density.
2. Restore to **TiDB X (BYOC)** using BR.
3. During **Restore Pre-split**, BR generates > 1024 split keys for a single range/table.
4. BR sends all keys in one RPC batch, which the **rfstore** module rejects (hard limit: 1024).

### 2. [REDACTED_USER]

BR should automatically **chunk split key requests** into multiple batches (e.g., max 1024 per RPC) to ensure compatibility with cloud storage engine constraints without manual tuning.

### 3. [REDACTED_USER]

Restore fails with "split key count exceeds limit." 

Currently, users must use "hacky" workarounds to bypass this:
* `--merge-region-size-bytes=1159296000`
* `--merge-region-key-count=115000000`

These parameters force oversized regions and cause post-restore performance imbalances.

### 4. [REDACTED_USER]

v8.5.0
