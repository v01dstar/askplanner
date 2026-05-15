# GTOC-7666: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7666
- Status: PM Review
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-06-11T05:38:49.746+0800
- Updated: 2025-06-12T12:11:15.234+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB Operator
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

## Description

We are noticing there are many stale images being used in our log truncate flow which is managed by tidb-operator. The cause was identified to be a result of the backup spec not ever being updated after creation, this causes the br image that is defined in the original spec to be used until its manually recreated. This can cause the truncate flow to use a older br tool than expected.

 

It would be ideal if tidb-operator could detect spec changes in the parent CR and propagate them to the backup CR.

 

Example BackupSchedule Spec

```
apiVersion: pingcap.com/v1alpha1
kind: BackupSchedule
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: tidb
spec:
  backupTemplate:
    azblob:
      accessTier: Hot
      container: backup-data
      prefix: snapshot-shared
      secretName: [REDACTED_RESOURCE_NAME]
    backoffRetryPolicy:
      maxRetryTimes: 2
      minRetryDuration: 300s

## Recent Comments Excerpt

### 2025-06-11T05:39:08.229+0800 [REDACTED_USER]

notified (俞锶浩([REDACTED_EMAIL]), om_x100b4bbe117a7cb00f277594dca7b0c) by lark

### 2025-06-11T09:49:02.918+0800 [REDACTED_USER]

BackupSchedule creates the Backup periodically, so if you change the BackupSchedule, the next Backup created will be changed. 

Backup will run immediately and only run once after it is created, so I think there is no need to propagate changes to existing Backups.

### 2025-06-12T03:19:11.122+0800 [REDACTED_USER]

Response from Customer : 
[REDACTED_CUSTOMER]; I might see the confusion here - these are not daily snapshot backups - in our production tidbclusters we have define a log backup as part of that backupschedule as show in original ticket (see the section 
logBackupTemplate
). This defines the backup job with 
backupMode
 log (also indicated in the name 
name: [REDACTED_RESOURCE_NAME]
) which will configure a log start job that runs once. However, we ALSO use the tidb-operator feature that will run log-truncate to trim old logs not needed anymore about once per day.

### 2025-06-12T12:03:54.013+0800 [REDACTED_USER]

Sorry, I have misunderstood the log backup, and it’s different from snapshot backups. Now, tidb-operator doesn’t update the log Backup image, it’s a BUG.

We will further discuss this feature。

### 2025-06-12T12:11:15.234+0800 [REDACTED_USER]

I have created an FRM to follow this issue.

https://tidb.atlassian.net/browse/FRM-2789
