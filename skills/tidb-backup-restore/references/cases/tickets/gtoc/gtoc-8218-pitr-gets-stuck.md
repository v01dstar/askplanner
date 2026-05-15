# GTOC-8218: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8218
- Status: Todo
- Resolution: N/A
- Priority: P1
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2026-02-11T10:03:20.110+0800
- Updated: 2026-02-17T23:29:06.968+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR, TiCDC
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

we had changefeed which ended up in bad state which cause our restore to fail in our shard. what is the recommended way to solve this ussye

```
Updating failure reason for migration: [REDACTED_UUID] to Restore failed after all retries: cluster [REDACTED_CLUSTER]/adhoc-3b0763412f17c6d7a77c69e8464106a7a5bf4c15f38b41-2, wait pipe message failed, errMsg [2026/02/10 21:59:11.370 +00:00] [ERROR] [restore.go:76] ["failed to restore"] [error="found CDC changefeed(s): cluster/[REDACTED_CLUSTER]: [REDACTED_NAMESPACE]/default changefeed(s): [test-kafka-debizum-1], please remove changefeed(s) before restore"] [errorVerbose="found CDC changefeed(s): cluster/[REDACTED_CLUSTER]: [REDACTED_NAMESPACE]/default changefeed(s): [test-kafka-debizum-1], please remove changefeed(s)
```

## Recent Comments Excerpt

### 2026-02-11T10:03:28.208+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), om_x100b578a783b68a4c106796bb9ffa01) by lark

### 2026-02-11T10:04:33.276+0800 [REDACTED_USER]

In the documentation 
https://docs.pingcap.com/tidb/stable/[REDACTED_RESOURCE_NAME]/
  , the compatibility behavior between BR and TiCDC is described only for 
snapshot restore
.

For BR v8.2.0 and later, if the target cluster has a TiCDC changefeed and the changefeed CheckpointTS is earlier than the BackupTS, BR will refuse to perform the restore.
However, the documentation does not clearly state whether the same rules apply to

### 2026-02-11T12:26:16.702+0800 [REDACTED_USER]

PiTR (
br restore point
) consists of 2 steps, (1) perform “snapshot restore” of the 
--[REDACTED_RESOURCE_NAME]
 (2) perform “stream restore” applying the logs inside 
--storage
. So the same restriction applies during step (1), i.e. if (changefeed’s CheckpointTS < backup’s BackupTS) it will fail precheck. 
(IMO the check should be further restricted to CheckpointTS <

### 2026-02-11T12:34:05.010+0800 [REDACTED_USER]

@[REDACTED_USER]
 
Thanks for the clarification.
Just to confirm the 
actual behavior in BR 8.5.5
:
After step (1) snapshot restore passes the precheck and completes successfully, does the presence of a TiCDC changefeed have 
any impact on step (2) stream restore

### 2026-02-11T12:58:23.506+0800 [REDACTED_USER]

It won’t trip precheck.
However, if the backup log archive has been pre-compacted, CDC will have problem replicating those compacted-SST-ingestion. That’s why I think the precheck condition should be tightened to 
< --restore-ts
.
