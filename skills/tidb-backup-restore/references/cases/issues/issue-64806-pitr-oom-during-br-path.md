# Issue 64806: PITR OOM during BR path

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/64806
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-12-02T04:25:46Z
- Updated: 2025-12-09T07:17:08Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR, Storage
- Categories: pitr-log-restore, restore-failure, storage-access, performance-resource, observability-diagnosis
- Labels: affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR OOM during BR path`
- Search terms: BR; PITR; Storage; TiDB; observability-diagnosis; performance-resource; pitr-log-restore; restore-failure; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
Create a log backup with many small writes in meta key.

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
This backup should be able to be restored. As we are grouping meta key editions, BR should not OOM.

### 3. [REDACTED_USER]
BR OOM during restoring meta key.
Here is a part of the goroutine dump:

```go
github.com/pingcap/tidb/br/pkg/stream.(*MetadataHelper).ReadFile(
  0xc1abb84510, // MetadataHelper (this pointer)
  {0x7644810, 0xc00404d630}, // Context (interface fat pointer)
  {0xc3bbbadc20, 0x5f}, // File Name (String,len=95)
  0x0, // File Start Offset (0)
  0x193e6ec1, // File Raw Content Size (423521985, 404MiB)
  0x3, // Compression Type (ZSTD)
  {0x766a860, 0xc0c36f1d70}, // Storage (interface fat pointer)
...)
```

Also it seems we have encountered a huge batch:
```go
github.com/pingcap/tidb/br/pkg/restore/log_client.(*LogClient).RestoreBatchMetaKVFiles(
  0xc04e9c77a0,                                   // LogClient receiver (this pointer)
  {0x7644810, 0xc00404d630},                      // ctx context.Context (interface fat pointer)
  {0xc0700b7810, 0x564, 0x59c7305?},              // files []*backuppb.DataFileInfo (data ptr, len=1380, cap≈0x59c7305)
  0xc08287dc70,                                   // schemasReplace *stream.SchemasReplace mapper
  {0xc03aade000, 0x67a7, 0x6c00},                 // kvEntries []*KvEntryWithTS (spillover buffer, len=26 599, cap=27 648)
  0x???????????????,                              // filterTS uint64 (not shown in snippet, next word in frame)
  {0x????????, 0x????????},                       // updateStats func(kvCount,uint64) (function value = {code,context})
  {0x????????, 0x????????},                       // progressInc func() (function value)
  {0x????????, 0x?},                              // cf string (“default” or “write”; header = {data,len})
  ...                                             // error return slot & spill space follow
)
```

It seems when batching, we were only counting size from default CF but ignored write CF. Also statistics during restoring meta KV is lacking.

### 4. [REDACTED_USER]
v8.5.2

<!-- Paste the output of SELECT tidb_version() -->
