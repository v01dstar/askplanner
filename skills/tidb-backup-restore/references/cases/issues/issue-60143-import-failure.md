# Issue 60143: Import failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60143
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-18T07:40:16Z
- Updated: 2025-06-23T10:18:06Z
- Closed: 2025-03-18T08:28:52Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Import
- Components: TiDB, Lightning, Storage
- Categories: storage-access, sst-ingest-import, checkpoint-retry
- Labels: affects-8.1, affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Import failure`
- Search terms: Import; Lightning; Storage; TiDB; checkpoint-retry; sst-ingest-import; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

When importing data from GCS, sometimes we may encounter errors like `http2: server sent GOAWAY and closed the connection; LastStreamID=XXX, ErrCode=NO_ERROR, debug="server_shutting_down"`, and this error can be resolved through retry.

But currently, this error is not included in the retry error list.

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]

Subtask should retry after meeting this error.

### 3. [REDACTED_USER]

Subtask failed.

### 4. [REDACTED_USER]

master

<!-- Paste the output of SELECT tidb_version() -->
