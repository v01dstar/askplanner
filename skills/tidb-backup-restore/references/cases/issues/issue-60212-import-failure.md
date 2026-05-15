# Issue 60212: Import failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60212
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-21T09:40:06Z
- Updated: 2025-04-23T06:51:54Z
- Closed: 2025-04-23T06:51:54Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Import
- Components: TiDB, TiKV, BR, Lightning
- Categories: sst-ingest-import
- Labels: affects-8.1, affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Import failure`
- Search terms: BR; Import; Lightning; TiDB; TiKV; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

There is a query expression error in the tidb_cluster [REDACTED_CLUSTER] option of the Grafana Backup & Import dashboard settings.

### 2. [REDACTED_USER]

label_values(tikv_engine_size_bytes{k8s_cluster="$k8s_cluster"}, tidb_cluster)

### 3. [REDACTED_USER]

label_values(tikv_engine_size_bytes{k8s_cluster="$k8s_cluster", tidb_cluster)

### 4. [REDACTED_USER]
v8.1.1、v8.5.1

<!-- Paste the output of SELECT tidb_version() -->

--------------------------------+
| tidb_version()                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release Version: v8.1.1
Edition: Community
Git Commit Hash: a7df4f9845d5d6a590c5d45dad0dcc9f21aa8765
Git Branch: HEAD
UTC Build Time: 2024-08-22 05:50:03
GoVersion: go1.21.13
Race Enabled: false
Check Table Before Drop: false
Store: tikv |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
