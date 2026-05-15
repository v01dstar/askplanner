# Issue 58430: PITR fails with [ddl:1071]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58430
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-12-20T07:12:17Z
- Updated: 2025-09-25T10:55:27Z
- Closed: 2025-09-25T10:55:27Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, schema-metadata, sst-ingest-import, checkpoint-retry, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, report/customer, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR fails with [ddl:1071]`
- Search terms: BR; PITR; TiDB; TiKV; checkpoint-retry; observability-diagnosis; pitr-log-restore; schema-metadata; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

Start a cluster with:

```fish
tiup playground nightly --tiflash=0 --db.config=./op/adhoc/index-length-8001.toml
```

Where the config `index-length-8001.toml` is:

```toml
max-index-length = 8001
```

Do the following:

```fish
mycli --port 4000 --execute "DROP TABLE IF EXISTS test.huge_idx;"
mycli --port 4000 --execute "CREATE TABLE test.huge_idx(id int AUTO_INCREMENT, blob1 varchar(1000), blob2 varchar(1000))"

$br backup full -s (s3path "$strg_prefix-full") $argv
set backupts (mcli cat "loc/breeze/$strg_prefix-full/backupmeta" | _get_brpb BackupMeta | rg -r '$1' 'end_version: (\d+)$')
$br log start -s (s3path "$strg_prefix-incr") --task-name test $argv --start-ts "$backupts"

mycli --port 4000 --execute "CREATE INDEX huge ON test.huge_idx(blob1, blob2);"

# Wait until the checkpoint advances...
$br restore point -s (s3path huge_index-incr) --[REDACTED_RESOURCE_NAME] (s3path huge_index-full)
```

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

Restore should success.

### 3. [REDACTED_USER]

```
repair ingest index huge for table test.huge_idx  ABORTED
["restore log failed summary"] [error="failed to repair ingest index: [ddl:1071]Specified key was too long (4000 bytes); max key length is 3072 bytes"]
```

### 4. [REDACTED_USER]

nightly

<!-- Paste the output of SELECT tidb_version() -->
