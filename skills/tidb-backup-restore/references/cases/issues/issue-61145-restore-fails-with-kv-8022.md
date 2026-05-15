# Issue 61145: Restore fails with [kv:8022]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61145
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-05-16T02:06:48Z
- Updated: 2025-05-16T02:09:49Z
- Closed: 2025-05-16T02:07:48Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR, Storage
- Categories: restore-failure, storage-access, schema-metadata, checkpoint-retry
- Labels: component/br, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/critical, type/bug
- Affected versions: may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `Restore fails with [kv:8022]`
- Search terms: BR; Restore; Storage; TiDB; TiKV; checkpoint-retry; restore-failure; schema-metadata; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

1. deploy a tidb cluster with 2 tidb and 3 tikv.
2. br restore specific database from s3.

### 2. [REDACTED_USER]

No error.

### 3. [REDACTED_USER]

There is a high probability that br will fail and throw one of the following errors:

```
Error: previous statement: insert into mysql.stats_meta (version, table_id, count, modify_count) values ...... (len:119776): [kv:8022]Error: KV error safe to retry Error(Txn(Error(Mvcc(Error(TxnLockNotFound { start_ts: TimeStamp([REDACTED_LONG_ID]), commit_ts: TimeStamp([REDACTED_LONG_ID]), key: [116, 128, 0, 0, 0, 0, 0, 0, 22, 95, 105, 128, 0, 0, 0, 0, 0, 0, 2, 3, 128, 0, 0, 0, 0, 0, 2, 114], mvcc_info: None }))))) {tableID=22, indexID=2, indexValues={626, }} [try again later]
```

```
Error: previous statement: insert into mysql.stats_meta (version, table_id, count, modify_count) values ...... tikv aborts txn: Error(Txn(Error(Mvcc(Error(PessimisticLockNotFound { start_ts: TimeStamp([REDACTED_LONG_ID]), key: [116, 128, 0, 0, 0, 0, 0, 0, 22, 95, 105, 128, 0, 0, 0, 0, 0, 0, 2, 3, 128, 0, 0, 0, 0, 0, 20, 126], reason: LockMissingAmendFail })))))
```

```
Error: pessimistic lock retry limit reached
```

```
Error: lock wait timeout
```

### 4. [REDACTED_USER]

e24784a9bf2b4c16e236387da989e4143d9fe0d1 or recent master
