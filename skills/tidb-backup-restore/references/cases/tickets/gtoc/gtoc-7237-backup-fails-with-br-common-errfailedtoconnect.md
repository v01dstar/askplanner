# GTOC-7237: Backup fails with [BR:Common:ErrFailedToConnect]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7237
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-11-12T08:47:04.000+0800
- Updated: 2025-03-06T17:52:30.158+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, storage-credential, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

The backup was triggered on [REDACTED_ENV_NAME], with its log uploaded to s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]

The tikv was [REDACTED_ENV_NAME], with its log uploaded to s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]

## Recent Comments Excerpt

### 2024-11-12T08:48:20.000+0800 [REDACTED_USER]

On 2024/11/07 02:39:03, the backup encountered connection timeout errors and failed to reset the gRPC connection. It then attempted to reconnect but timed out with a context deadline exceeded error. TiKV showed a handshake error at the same time.

 
[REDACTED_MEDIA]
 
Then, it printed a warning log every 30 seconds for an unknown reason.
[REDACTED_MEDIA]
[2024/11/08 17:38:02.861 +00:00] [WARN] [client.go:1243] ["failed to connect to store, skipping"] [range-sn=104] [error="[BR:Common:ErrFailedToConnect]failed to make connection to store 4550818640: context deadline exceeded"] [storeID=4550818640]
