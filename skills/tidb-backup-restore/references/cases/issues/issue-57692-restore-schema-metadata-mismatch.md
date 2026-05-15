# Issue 57692: Restore schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57692
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-11-25T21:04:45Z
- Updated: 2024-11-29T09:58:23Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Restore
- Components: TiDB, Operator, BR, Storage
- Categories: storage-access, schema-metadata, performance-resource, observability-diagnosis
- Labels: component/br, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Restore schema metadata mismatch`
- Search terms: BR; Operator; Restore; Storage; TiDB; observability-diagnosis; performance-resource; schema-metadata; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

restore a cluster with schema count large enough.  
Trigger the err at (https://github.com/pingcap/tidb/blob/master/br/pkg/task/stream.go#L1864).
Because it will print all the schemas used here, the log would become too large to read.

*** Sometimes it would stuck the kubenates due to log length limit***
(ref:https://github.com/kubernetes/kubernetes/blob/db1990f48b92d603f469c1c89e2ad36da1b74846/test/integration/master/synthetic_master_test.go#L315)

### 2. [REDACTED_USER]

A smaller log.

### 3. [REDACTED_USER]

A too large log.

### 4. [REDACTED_USER]

master

<!-- Paste the output of SELECT tidb_version() -->
