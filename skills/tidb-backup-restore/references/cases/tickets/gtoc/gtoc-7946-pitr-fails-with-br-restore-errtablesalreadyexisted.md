# GTOC-7946: PITR fails with [BR:Restore:ErrTablesAlreadyExisted]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7946
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P0
- Issue type: Incident
- Created: 2025-10-09T08:37:25.448+0800
- Updated: 2026-01-13T20:53:32.248+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, restore-failure, storage-credential, tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

* Multi-tenant TiDB cluster, each tenant corresponds to a separate database.
* Customer [REDACTED_CUSTOMER]’s database.
* First **PiTR restore** failed.
* Then tried **snapshot restore**, which failed with  
  `[BR:Restore:ErrTablesAlreadyExisted] tables already existed in restored cluster`.
* Afterwards, customer **retried PiTR**, and this time it **succeeded**.
* However, **after the successful PiTR**, the **database does not exist** in the cluster.

## Recent Comments Excerpt

### 2025-10-09T13:43:54.487+0800 [REDACTED_USER]

The customer [REDACTED_CUSTOMER]42a3b046be918061526525baf6.
The first attempt using the full backup 
2025-10-07T20-00-12
 failed because the database was not included in that snapshot (likely dropped before the backup).
A subsequent restore using the earlier full backup 
2025-10-06T14-00-26
 succeeded.

### 2025-10-11T03:55:06.498+0800 [REDACTED_USER]

The customer’s PiTR restore still fails.  Refer 
failed-logs.txt
The error shows missing log backup metadata on S3:
Error: failed to restore kv files: failed during reading file ... NoSuchKey: The specified key does not exist.

Customer [REDACTED_CUSTOMER]

s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH][REDACTED_LONG_ID]-[REDACTED_UUID].meta

### 2025-10-14T17:00:21.568+0800 [REDACTED_USER]

Need double check the pitr log to make sure the issue root cause is related to log truncate when pitr.


if so, TiKV need upgrade with this issue: 
https://github.com/tikv/tikv/issues/18497

### 2025-10-15T01:27:09.052+0800 [REDACTED_USER]

Customer’s reponse: 
I don’t really have any timestamps. I don’t know what the 
[REDACTED_LONG_ID]
 is but that number seems to correlate to time in some way. It’s not epochMs so I’m not really sure what I’m looking at. 
The timestamps I could find in a similar timespot were all about a month before the time I was requesting PITR to. 

Also, when you check the 
backupmeta

### 2025-10-15T17:52:27.914+0800 [REDACTED_USER]

It’s more like previous suspect issue, running log truncate and PiTR simultaneously might cause the issue. upgrade tikv version should solve it.
