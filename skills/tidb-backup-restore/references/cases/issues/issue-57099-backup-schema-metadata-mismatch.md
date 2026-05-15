# Issue 57099: Backup schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57099
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-11-04T07:16:51Z
- Updated: 2024-11-04T07:16:52Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, BR
- Categories: schema-metadata, performance-resource
- Labels: component/br, severity/moderate, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Backup schema metadata mismatch`
- Search terms: BR; Backup; TiDB; performance-resource; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. backup
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
success
### 3. [REDACTED_USER]
1. br start `domain` component to get some cluster [REDACTED_CLUSTER] information.
2. `ddl` component initialization is too slow.
3. br close `domain` component and stop `ddl` component.
4. `ddl` component fatal because it stop before initialization done.
### 4. [REDACTED_USER]
v8.1.1
<!-- Paste the output of SELECT tidb_version() -->
