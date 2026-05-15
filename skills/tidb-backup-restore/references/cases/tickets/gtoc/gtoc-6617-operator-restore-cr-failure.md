# GTOC-6617: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6617
- Status: Canceled
- Resolution: Cancel
- Priority: P2
- Issue type: Incident
- Created: 2024-01-12T10:42:30.000+0800
- Updated: 2024-08-17T09:35:06.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello, we saw some volumebackups got deleted directly after failed due to gc safepoint exceeded during init process. We expect the volumebackups retain until recycle policy kicks in but not got deleted by federation manager right after failure. This backups are against a newly restored prod cluster, which has a high resolve-ts for a while. so wondering can you please help investigate the why they got deleted? thanks

federation manager log: <custom data-type="smartlink" data-id="id-0">https://gist.github.com/olivia-chen-github/199d7a6bfed15f1f52b9df202f30dd17</custom> 

init pod failure log: <custom data-type="smartlink" data-id="id-1">https://gist.github.com/olivia-chen-github/75ee0c6a4e75cd54059fdc96f91b4142</custom>

## Recent Comments Excerpt

### 2024-01-12T10:42:31.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 12/Jan/24 2:30 AM
Escalate to L3 Information 
[REDACTED_TICKET_ID]

This ticket is reported by 
PingCAP Employee
: Olivia Chen

### 2024-01-12T10:49:21.000+0800 [REDACTED_USER]

Customer [REDACTED_CUSTOMER]
`maxReservedTime`
  of the backup schedule. From the federation manager log, the failed backup was gc ~1 minute after it failed.

{{
I0111 02:45:42.385208
 }}{{{}      1 fed_volume_backup_control.go:90] VolumeBackup %!/(string=[REDACTED_ENV_NAME])skd-2024-01-11t02-45-00 update status, old: &{Backups:[{K8sClusterName:[REDACTED_RESOURCE_NAME] TCName:[REDACTED_RESOURCE_NAME] TCNamespace:[REDACTED_NAMESPACE] BackupName:[REDACTED_RESOURCE_NAME] Phase:VolumeBackupInitializeFailed BackupPath: BackupSize:0 CommitTs: Reason: Message:}] TimeStarted:2024-01-11 02:45:12 +0000 UTC TimeCompleted:0001-01-01 00:00:00 +0000 UTC TimeTaken: BackupSizeReadable: BackupSize:0 CommitTs: Phase:Running Conditions:[{Status:True Type:Running LastTransitionTime:2024-01-11 02:45:12 +0000 UTC Reason: Message:}]}, new: {Backups:[{K8sClusterName:[REDACTED_RESOURCE_NAME] TCName:[REDACTED_RESOURCE_NAME] TCNamespace:[REDACTED_NAMESPACE] BackupName:[REDACTED_RESOURCE_NAME] Phase:Failed BackupPath: BackupSize:0 CommitTs: Reason: Message:}] TimeStarted:2024-01-11 02:45:12 +0000 UTC TimeCompleted:2024-01-11 02:45:42.385182625 +0000 UTC m=+3046.745681892 TimeTaken:30s BackupSizeReadable:0 B BackupSize:0 CommitTs: Phase:Failed Conditions:[{Status:True Type:Running LastTransitionTime:2024-01-11 02:45:12 +0000 UTC Reason: Message:} {Status:True Type:Failed LastTransitionTime:2024-01-11 02:45:42.385184592 +0000 UTC m=+3046.745683850 Reason:VolumeBackupMemberFailed Message:backup member fed-skd-{}}}
_2024-01-11t02-45-00_

### 2024-01-13T02:12:42.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 12/Jan/24 6:12 PM

Seeing this ticket’s issue has been discussed on slack,
Brian Zhang
  
16 hours ago
@olivia.chen
 Can you check the

### 2024-02-05T08:17:32.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 05/Feb/24 12:17 AM

@[REDACTED_USER] you please let us know if we could close this ticket for now.

### 2024-02-08T19:26:36.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Feb/24 11:26 AM

Since we haven't hear your response for sometime, we would like to close this ticket for now. please feel free to reopen this ticket if there are any further questions
