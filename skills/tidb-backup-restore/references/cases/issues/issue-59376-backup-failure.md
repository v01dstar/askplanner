# Issue 59376: Backup failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59376
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-02-10T22:44:53Z
- Updated: 2025-02-14T08:07:06Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, TiKV, BR
- Categories: performance-resource, checksum-consistency
- Labels: component/br, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Backup failure`
- Search terms: BR; Backup; TiDB; TiKV; checksum-consistency; performance-resource

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report


### 1. [REDACTED_USER]

Run BR backup

### 2. [REDACTED_USER]

We expect BR backup should use some cpu/io resource, but not too high to impact cluster [REDACTED_CLUSTER]

### 3. [REDACTED_USER]

There is a spike at the beginning of checksum stage. It caused a production outage of a paid customer. Further analysis find that default value for table-concurrency is 64, and default value for checksum-concurrency is 4. This caused a total concurrency of 256 of intensive cpu/io utilization. 

Since 8.5 BR backup checksum is disabled by default. However there is still lack of documentation on table-concurrency and checksum-concurrency, users may risk cluster [REDACTED_CLUSTER] when performing BR backup with checksum enabled.

The default value of table-concurrency should be reduced to a level that it is safe to run without adjusting it, but allow user to increase if they want better performance.

### 4. [REDACTED_USER]

select tidb_version()\G
*************************** 1. row ***************************
tidb_version(): Release Version: v7.5.5
Edition: Community
Git Commit Hash: 287f27ea0e5b7be6d75bd4c6fc9982f9d80e4cf7
Git Branch: HEAD
UTC Build Time: 2024-12-26 07:05:21
GoVersion: go1.21.10
Race Enabled: false
Check Table Before Drop: false
Store: tikv
