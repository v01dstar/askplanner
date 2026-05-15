# GTOC-7663: Restore fails with [BR:Restore:ErrRestoreChecksumMismatch]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7663
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P4
- Issue type: Incident
- Created: 2025-06-10T10:29:23.630+0800
- Updated: 2025-07-03T13:02:55.288+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, storage-credential, tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

A restore process was started by mistake in a production environment. The restore destination cluster was not empty. The backup was generated from the same cluster a few hours earlier. This is, the backup source is the same cluster as the restore destination.

* The `tiup br:v8.5.1 restore full` process was abruptly cancelled before it completes. As a consequence we found tables with broken indexes that failed the `ADMIN CHECK TABLE`. 
* The damaged indexes were recreated, and `ADMIN CHECK TABLE` reported no errors. 

* Hours later, `ADMIN CHECK TABLE` reported damaged indexes again.  
  INSERT and UPDATE statements were allowed, but not DELETE statements. We are looking for possible reasons that could cause the indices to break again for no apparent reason.

* We know the reason the index failed the first time (due to an incomplete backup restore). But the indexes failed again, and we're not sure if this could happen again.

* We still have the `__TiDB_BR_Temporary_Snapshot_Restore_Checkpoint` schema in the cluster if it can help in any way.

* The incident occurred between `2025-05-29` `11:41` and `2025-05-29` `11:45`, and the index was subsequently recreated. We believe the indexes failed again around `2025-05-30 03:00`, but they were only recovered this morning `2025-06-03` \~`09:40`  
  Due to the upload file size limit, logs were collected from `2025-05-29T10:00:00Z` to `2025-05-30T10:00:00Z` to cover the incident and subsequent index failure.   
  _I will share the link to this request as soon as the logs package is ready and uploaded._

The impact is low at the moment as the indices have recovered, but we do not have an alert system to check if the index breaks down again.

Sequence of execution:

* BR restore full:

```
/usr/local/bin/tiup br:v8.5.1 restore full \\\n\t--pd='[REDACTED_RESOURCE_NAME].sqldb:2379,[REDACTED_RESOURCE_NAME].sqldb:2379,[REDACTED_RESOURCE_NAME].sqldb:2379' \\\n\t--storage='s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH][REDACTED_LONG_ID]-full?region=eu-central-1' \\\n\t--send-credentials-to-tikv=false \\\n\t--log-file='/tmp/br-restore-full-[REDACTED_LONG_ID].log' --filter='taxify_*.*'"
Starting component br: /root/.tiup/components/br/v8.5.1/br restore full --pd=[REDACTED_RESOURCE_NAME].sqldb:2379,[REDACTED_RESOURCE_NAME].sqldb:2379,[REDACTED_RESOURCE_NAME].sqldb:2379 --storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH][REDACTED_LONG_ID]-full?region=eu-central-1 --send-credentials-to-tikv=false --log-file=/tmp/br-restore-full-[REDACTED_LONG_ID].log --filter=taxify_*.*

Detail BR log in /tmp/br-restore-full-[REDACTED_LONG_ID].log
Error: failed to validate checksum: [BR:Restore:ErrRestoreChecksumMismatch]restore checksum mismatch

## Recent Comments Excerpt

### 2025-06-10T10:35:06.071+0800 [REDACTED_USER]

@[REDACTED_USER]
 Please help to confirm if there’s other possibility for data and index inconsistency like corruptted sst files due to mistaken BR restore.
[REDACTED_CLINIC_URL]
 
customer [REDACTED_CUSTOMER]:
https://tidb.atlassian.net/browse/EMID-10044

### 2025-06-13T10:04:38.260+0800 [REDACTED_USER]

I have involved 
@[REDACTED_USER]
 (廖坚钧) and 
@[REDACTED_USER]
 (廖坚钧) in this ticket. The discussion was mainly in lark group. According to them, it seems that rebuilding the index is not enough to fix the broken index due to this abrupt cancellation to BR restore.

### 2025-07-02T15:26:19.823+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2025-07-02T15:26:33.404+0800 [REDACTED_USER]

@[REDACTED_USER]
 any updates?

### 2025-07-03T08:42:14.916+0800 [REDACTED_USER]

@[REDACTED_USER]
 
I will cc 
@[REDACTED_USER]
 and 
@[REDACTED_USER]
 in here, so you are aware they’ve been involved from the beginning and are the right contacts for this issue. The nature of this issue is not really about DDL but rather the underlining storage. I believe this is also what we have been discussed clearly in the lark group that is related to this ticket. 
https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=[REDACTED_SECRET]
