# GTOC-6877: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6877
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-04-26T17:49:27.000+0800
- Updated: 2025-03-06T18:13:23.774+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, restore-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER], we are evaluating BR PITR feature. for this we have trigerred FULL backup using steps mentioned here - <custom data-type="smartlink" data-id="id-0">https://docs.pingcap.com/tidb-in-kubernetes/stable/backup-to-gcs-using-br#ad-hoc-backup</custom> 

Along with this we have also initiated log backup using manifest <custom data-type="smartlink" data-id="id-1">https://docs.pingcap.com/tidb-in-kubernetes/stable/backup-to-gcs-using-br#start-log-backup</custom> 

After sometime I have stopped the log backup by adding “{{logStop}}: true” in the backup manifest I have used earlier and Backup status updated to **Stopped** from **Running.**

Now I have remove “\*logStop: true\*”   and added **logTruncateUntil: "[REDACTED_LONG_ID]"** to Backup manifest and applied to cleanup the older logs. it got completed. Now I not getting how to resume to log backup?

```
➜  ~ kubectl get backup [REDACTED_ENV_NAME]
NAME                       TYPE   MODE   STATUS    BACKUPPATH                               BACKUPSIZE   COMMITTS             LOGTRUNCATEUNTIL     AGE
[REDACTED_ENV_NAME]          log    Stopped   gcs://[REDACTED_ENV_NAME]/log-backup-folder/                [REDACTED_LONG_ID]   [REDACTED_LONG_ID]   141m
```

## Recent Comments Excerpt

### 2024-05-07T14:36:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 07/May/24 6:36 AM

hi @[REDACTED_USER] is the frequency of PITR log backup? Is it configurable?
log backup is a continuous backup. It will backup if any data changed. So I think there is no "frequency".
How do we get the size of amount of log between two checkpoint-ts?
Not support.
How to get the latest checkpoint-ts which can be applied/restored?

### 2024-05-08T15:13:29.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/May/24 7:13 AM

What is overhead on the cluster when the log backup is enabled? I mean what is the resource requirements on TiKV and PD to enable the PITR log backup.

### 2024-05-08T15:30:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/May/24 7:30 AM

hi  @[REDACTED_USER], resource consumption is not high, so there is no need for specialized configuration.

Here is a performance test data for reference : 
https://docs.pingcap.com/tidb/stable/br-pitr-guide#performance-capabilities-of-pitr

### 2024-05-10T14:54:48.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 10/May/24 6:54 AM

hi @[REDACTED_USER] is the current situation?
If there are no follow-up questions, this issue will be closed.
If you has any other question, you can create new ticket .

### 2024-05-13T16:29:21.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/May/24 8:29 AM

Log backup is working fine. We can close the ticket for now.
