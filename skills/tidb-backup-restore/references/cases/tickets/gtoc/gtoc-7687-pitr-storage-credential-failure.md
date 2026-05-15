# GTOC-7687: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7687
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-06-18T07:08:04.580+0800
- Updated: 2025-07-07T10:11:19.698+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, restore-failure, storage-credential, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Recent PITR failed due to the error

```
[error="failed during reading file v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta: failed to read s3 file, file info: input.bucket='[REDACTED_ENV_NAME]', input.key='[REDACTED_ENV_NAME]/scheduled/log/log-2025-03-11t22-22-14/v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta': NoSuchKey: The specified key does not exist.\n\tstatus code: 404, request id: [REDACTED_REQUEST_ID], host id: [REDACTED_HOST_ID]"]
```

This restore occurred concurrent with a log backup truncation job for the source cluster that happened at the same time. I can confirm from the truncation logs that the meta file that could not be found was one of the files processed by the truncation:

```
I0616 02:25:58.827750       9 backup.go:302] v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta [v1/20250608/02/22661861/[REDACTED_LONG_ID]-[REDACTED_UUID].log] v1/20250608/02/22661861/[REDACTED_LONG_ID]-[REDACTED_UUID].log true
```

* Is this expected behavior? Is it generally unsafe to run a PITR while the source backup is being cleaned?

    * We have been unaware of this issue on our side, and if the case, this would present a blocker for BR given that we don’t explicitly control when backup cleanup occurs via operator. Specifically we have various automated daily restore workflows that could fail if the source cluster [REDACTED_CLUSTER] happens to perform a cleanup
    
* The intended PITR itself only restored a recent period of logs, whereas the log that was being truncated was from 7d ago based on our retention. We’ve discussed planned improvements to lift log metadata into the filenames and update the BR process to filter these meta files based on name rather than downloading/parsing. Would this improvement have resolved this issue given that the meta file was outside of the intended range of log-replay?

I’ve attached snippets of logs from the BR restore pod as well as the backup cleanup pod to demonstrate that the restore and truncation are concurrent.

## Recent Comments Excerpt

### 2025-06-19T15:19:30.364+0800 [REDACTED_USER]

For question1:
You are basically correct，here is the introduction doc of log checkpoint.
https://docs.pingcap.com/tidb/stable/br-checkpoint-restore/#log-restore
For question2:
You are correct. You could see the impl of this pr: 
https://github.com/pingcap/tidb/pull/61347
 
For question3:

### 2025-06-20T01:55:06.605+0800 [REDACTED_USER]

Thanks for the ans. Questions to better understand how it works
Q1: For “2. The operator will always do a backup before truncate, and set the truncate until-ts before it.”.  What does operator backup,  the to-be-truncated log files? Where does operator backup the files to? Is this configurable in operator?
Q2: For the above question 2: so there are two passes to restore:
Without fix:
pass 1:  scan all metadata or log files stored in S3 and save the list (including all scanned files) somewhere.
pass 2: download all metadata/log files from S3 to actually run recover, regardless of whether the log file is required for recover or not. 
With the fix:  
pass 1: scan all metadata or log files stored in S3 and make list of log files required for recover

### 2025-06-23T20:37:29.213+0800 [REDACTED_USER]

For the question 1, it is a fixed process in operator, to protect the ongoing backup not being truncated. It is not configurable and you should not disable that.

### 2025-06-24T08:17:15.493+0800 [REDACTED_USER]

The customer [REDACTED_CUSTOMER]:
Thanks for the updates and confirmation.
This kind of restore is dangerous. You shouldn’t try to restore to a timestamp where file has been truncated.
Agreed here. Our concern is that we are building automated systems and workflows around restore, so we would expect that those processes should attempt to restore logs from any available/valid timestamp, even ones near the until-ts.
The truncate will set a timestamp on the S3 storage, to inform the upcoming restore what file will be truncated.
When/how does this occur? Specifically, does the log truncate first delete files, then persist the until-ts to external storage? or does it update the until-ts checkpoint first and then attempt to delete files. The former would allow a scenario where a restore believes that logs after the stale until-ts are valid even though they have actually been deleted, and attempts to restore them.
my read of 
https://github.com/pingcap/tidb/blob/master/br/pkg/task/stream.go#L1194

### 2025-06-24T15:50:32.932+0800 [REDACTED_USER]

in general, we are looking for confirmation that: any PITR attempting to restore logs that are concurrently being truncated should 
never succeed with partial data
 and should either complete successfully w/ all data or should fai

SetTsToFile (sets until-ts) runs 
before
 truncating the logs.
getLogRangeWithStorage is called
