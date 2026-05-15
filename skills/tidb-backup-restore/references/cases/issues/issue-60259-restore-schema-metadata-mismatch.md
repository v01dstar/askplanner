# Issue 60259: Restore schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60259
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-03-25T10:55:08Z
- Updated: 2025-07-11T02:06:01Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: restore-failure, schema-metadata, compatibility-upgrade
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Restore schema metadata mismatch`
- Search terms: BR; Restore; TiDB; compatibility-upgrade; restore-failure; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
	1.Upgrade a TiDB cluster from a version earlier than 8.4.0 to the master branch version.
	2.Create a large number of tables in a database on the upgraded cluster.
	3.Use the BR from the master branch to perform a database-level restore operation.
 <!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
restore succeed without error.
### 3. [REDACTED_USER]
sometimes restore fail and reports error  `Information schema is out of date: schema failed to update in 1 lease`
### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
