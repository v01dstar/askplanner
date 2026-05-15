# GTOC-6847: Backup fails with FileExistedInExternalStorage

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6847
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-16T13:38:30.000+0800
- Updated: 2025-03-06T18:14:14.898+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Single backup failure due to

```
E0409 20:06:22.213914       1 backup_manager.go:165] backup [REDACTED_ENV_NAME]/fed-skd-2024-04-09t20-05-00 create job backup-fed-skd-2024-04-09t20-05-00 failed, reason is , error backup [REDACTED_ENV_NAME]/fed-skd-2024-04-09t20-05-00, clustermeta exist, reason is FileExistedInExternalStorage.
```

Happening in data plane b. Didn’t see multiple backups occurring concurrently operator restart, so it might be a race or incorrectly handled retry in operator trying to backup cluster [REDACTED_CLUSTER]?

I’ve attached operator and backup job logs from that AZ

## Recent Comments Excerpt

### 2024-04-25T18:38:44.000+0800 [REDACTED_USER]

I think we need to check backup named ' [REDACTED_ENV_NAME]/fed-skd-2024-04-09t20-05-00' instead of ' [REDACTED_ENV_NAME]/fed-skd-2024-04-05t20-05-00'. The failed one is `[REDACTED_ENV_NAME]/fed-skd-2024-04-09t20-05-00` since double jobs created for it due to stale cache.

### 2024-04-25T19:31:22.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Apr/24 11:31 AM

Hi @[REDACTED_USER] operator-b.log the error
E0409 20:06:22.213914 1 backup_manager.go:165] backup [REDACTED_ENV_NAME]/fed-skd-2024-04-09t20-05-00 create job backup-fed-skd-2024-04-09t20-05-00 failed, reason is , error backup [REDACTED_ENV_NAME]/fed-skd-2024-04-09t20-05-00, clustermeta exist, reason is FileExistedInExternalStorage.
The failed backup job is 
[REDACTED_ENV_NAME]/fed-skd-2024-04-09t20-05-00
From backup-b.log, the begining:

### 2024-04-27T01:01:34.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 5:01 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-04-30T01:02:56.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/Apr/24 5:02 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-05-03T01:03:12.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/May/24 5:02 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
