# Issue 60209: PITR failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/60209
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-03-21T08:57:23Z
- Updated: 2025-03-24T04:37:29Z
- Closed: 2025-03-24T04:37:29Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, BR, Storage
- Categories: pitr-log-restore, storage-access, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `PITR failure`
- Search terms: BR; PITR; Storage; TiDB; observability-diagnosis; pitr-log-restore; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

- do log backup on GCP cluster
- use  GCS credential file for permissions

### 2. [REDACTED_USER]
no GCS credential leak

### 3. [REDACTED_USER]
When using the GCS credential file, the credentials were exposed when adding the log backup task.

> 2025/03/10 13:49:28.778 +00:00] [INFO] [advancer.go:436] ["added event"] [task="storage:<gcs:<bucket:\"[REDACTED_ENV_NAME]\" prefix:\"logbackup\" CredentialsBlob:\"[REDACTED]\"type\\\": \\\"service_account\\\",\\n  \\\"project_id\\\": \\\"qa-[REDACTED_ENV_NAME]\\\",\\n  \\\"private_key_id\\\": \\\"xxxxx\\\",\\n  \\\"private_key\\\": \\\"-----BEGIN PRIVATE KEY-----\\\\

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->

9.0.0-master
