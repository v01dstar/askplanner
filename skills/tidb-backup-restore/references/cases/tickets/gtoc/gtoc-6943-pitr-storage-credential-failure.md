# GTOC-6943: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6943
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-05-29T20:12:27.000+0800
- Updated: 2025-03-07T10:55:30.005+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We have a backup schedule that should be scheduling snapshot and log backups. We have been successfully taking the snapshot backup’s, but we have not been taking any log backups, which is preventing us from fully testing point in time recovery

## Recent Comments Excerpt

### 2024-06-25T22:44:56.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Jun/24 2:44 PM

Hi [REDACTED_USER],
“Why isn’t it recreating the Log job right now ? The BackupSchedule manifest is set up to have a logs backup job, but there is no job running. The operator should be checking if the job is working and if its not it should restart it.”
– Yes, I can’t agree with you more, in the theory, I think k8s will re-create it if it is not running, but in fact not.
“We do plan on re-creating the backup job, but what this is telling me is that if the log job fails for any reason it will never get re-created.“
– Currently we are working on finding the root cause, but we didn’t find it base on current logs, that’s why I am asking you whether you can provide the logs for the problematic time period, if you can’t, it is hard for us to further investigate. So may be need you reproduce the issue to get the necessary logs. 
Regards

### 2024-07-10T03:56:35.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/Jul/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-07-17T03:57:17.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 16/Jul/24 7:57 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-07-24T03:56:46.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 23/Jul/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-07-31T03:56:34.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/Jul/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.
