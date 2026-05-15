# GTOC-6850: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6850
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-16T21:33:36.000+0800
- Updated: 2025-03-06T18:14:09.821+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER], We are using BR tool to backup and restore the TiDB data deployed on Kubernetes, We are exploring ways to validate and ensure the backups are restorable.

Does the BR tool have capabilities that we can leverage here to validate the backups that we have taken. This validation should include both schema as well row data.

## Recent Comments Excerpt

### 2024-04-17T05:23:48.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 16/Apr/24 9:23 PM
Huh what. If checksum failed (whether it’s network issue or actual data inconsistency) the whole process also FAIL. Unless you explicitly disable it via 
--checksum=0
, in which the checksum calculation won’t run at all.
-
You could use 
br debug checksum
 to check the if the backup archive’s file-level SHA-256 hash is the same as the one recorded in the backupmeta. This command also calculated and logged the table-row-level CRC64-XOR checksum, but

### 2024-04-17T09:55:16.000+0800 [REDACTED_USER]

If checksum fails during backup or restore, the br job will be marked fail of course.  And BR provide the validation capability via command of `br debug`, and you can find more details from 
https://docs.pingcap.com/tidb/v6.1/br-usage-backup#[REDACTED_RESOURCE_NAME]
.

### 2024-04-17T14:50:40.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 6:50 AM

Hi [REDACTED_USER], 

Please find the update for your questions.
[REDACTED_MEDIA]
If checksum failed (whether it’s network issue or actual data inconsistency) the whole process also FAIL. Unless you explicitly disable it via --checksum=0, in which the checksum calculation won’t run at all.
If checksum fails during backup or restore, the br job will be marked fail of course.  And BR provide the validation capability via command of `br debug`, and you can find more details from

### 2024-04-25T17:14:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Apr/24 9:14 AM

hi @[REDACTED_USER] is the current situation for this ticket ?

### 2024-05-08T17:54:29.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/May/24 9:54 AM

hi @[REDACTED_USER] is the current situation?
If there are no follow-up questions, this issue will be closed.
If you has any other question, you can create new ticket .
