# Issue 55609: Backup failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/55609
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-08-23T05:46:47Z
- Updated: 2025-03-31T10:13:40Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR, Storage
- Categories: storage-access, sst-ingest-import, checkpoint-retry
- Labels: affects-8.5, component/br, feature/developing, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/major, type/bug
- Affected versions: affects-8.5, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `Backup failure`
- Search terms: BR; Backup; Storage; TiDB; TiKV; checkpoint-retry; sst-ingest-import; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
In a scenario with a million databases and tables, `br full backup` constructs backup ranges based on the data and indexes of the tables. For example, with a million `sysbench` tables, it is necessary to construct 2 million ranges. `br` requests TiKV to upload the corresponding SST files to S3 according to the size of the ranges, which generates a large number of small files and the backup of the data is extremely time-consuming.

In actual testing, we created 1 million databases, 2 million tables, each table containing 2 row of data and one index, with approximately 50GB of for 3 replicas. The full backup took about 6 hours to reach a 60% progress, generating a million-level number of SST files. Ultimately, the backup task failed due to the creation of too many small files on Minio, causing Minio to return an error.
The minio files stats
```
[root@172 tiflash]# ls 1mdatabase-2table-2row-master6
1001  1004  1013  1019  1025  1026  backup.lock  checkpoints
[root@172 tiflash]# ls 1mdatabase-2table-2row-master6/1013 | wc -l
525132
[root@172 tiflash]# ls 1mdatabase-2table-2row-master6/1019 | wc -l
868737
[root@172 tiflash]# ls 1mdatabase-2table-2row-master6/1025 | wc -l
1204584
```

### 2. [REDACTED_USER]

### 3. [REDACTED_USER]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
master
