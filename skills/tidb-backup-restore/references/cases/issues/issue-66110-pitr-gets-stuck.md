# Issue 66110: PITR gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/66110
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2026-02-06T07:01:13Z
- Updated: 2026-03-06T18:33:46Z
- Closed: 2026-03-06T18:33:46Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR
- Categories: pitr-log-restore, schema-metadata, performance-resource, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, affects-9.0, component/br, severity/critical, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, affects-9.0

## Quick Match

- Title/error signature: `PITR gets stuck`
- Search terms: BR; PITR; TiDB; observability-diagnosis; performance-resource; pitr-log-restore; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

1. (TODO generate the appropriate backup)
2. `br restore point --[REDACTED_RESOURCE_NAME]=... --restored-ts=... --storage=...`
3. Watch the BR log and wait until reaching `["waiting for schema info finishes reloading"]`

### 2. [REDACTED_USER]

4. BR should quickly go on to `["reloading schema finished"]`.

### 3. [REDACTED_USER]

4. BR is stuck for 15 minutes, then failed with `["restore log failed summary"] [error="failed to wait until schema reload: waitUntil timed out after waiting for 15m0s"]`

### 4. [REDACTED_USER]

v8.5.2

(Internal reference: TICKET-8221)

<!-- Paste the output of SELECT tidb_version() -->
