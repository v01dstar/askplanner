# GTOC-7452: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7452
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-03-07T02:39:04.974+0800
- Updated: 2025-03-27T11:03:45.461+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

If you configure a `BackupSchedule` with no S3 bucket for both the snapshot and log based backups it will spawn two `Backup` CRs (one snapshot, one log) but both will be invalid because it has no S3 bucket (this is expected and fine). If you then go update the `BackupSchedule` manifest to include the S3 bucket the controller will not fix the problem without you also deleting the entire `BackupSchedule` and recreating it.

## Recent Comments Excerpt

### 2025-03-19T11:08:51.189+0800 [REDACTED_USER]

Maybe we will fix this in the next edition.
As for now, a method is to delete the 
Status.LogBackup
 and delete the running log task in kernel. Why do you need to keep the schedule with wrong storage setting?

### 2025-03-20T00:19:03.763+0800 [REDACTED_USER]

@[REDACTED_USER]
 , they do not want to keep wrong backup schedule, but to be able to modify it (fix the error: in this case to add s3). We would need to tell them when/version it will be scheduled for fix.

### 2025-03-24T23:23:27.658+0800 [REDACTED_USER]

Hi 
@[REDACTED_USER]
 , any idea when/release will this issue be fixed? What should   we tell the customer? Thank you. Miles

### 2025-03-26T23:00:12.376+0800 [REDACTED_USER]

Hi 
@[REDACTED_USER]
 and 
@[REDACTED_USER]
 , could you please provide an update so I can communicate that to the customer? Thank you. Miles

### 2025-03-27T10:56:58.125+0800 [REDACTED_USER]

@[REDACTED_USER]
 Currently, there is no dedicated solution to fix this issue. Our plan is to add a feature that allows the scheduler to regularly check the status of log backup. If any problems are detected, it can trigger an alarm or perform a retry. This may potentially solve the problem.
But I‘m wondering that, if user use a invalid config for log backup, it will fail immediately when created. Why can’t user delete and restart scheduler?
