# Issue 56373: Restore schema metadata mismatch

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56373
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-09-27T08:03:43Z
- Updated: 2024-11-19T08:59:46Z
- Closed: 2024-11-18T16:42:16Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR
- Categories: schema-metadata, checksum-consistency
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/moderate, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Restore schema metadata mismatch`
- Search terms: BR; Restore; TiDB; checksum-consistency; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

1. Perform `br backup full --checksum=0`
2. Perform `br restore full --checksum=1`

### 2. [REDACTED_USER]

BR restore compare the `ADMIN CHECKSUM` with the sum of crc64xor of all files, which are always computed in `br backup` regardless of original `--checksum`.

### 3. [REDACTED_USER]

BR restore does not compare the checksum because it used the Schema's crc64xor which are not populated without `--checksum=1`.

### 4. [REDACTED_USER]

v6.5 and above

<!-- Paste the output of SELECT tidb_version() -->
