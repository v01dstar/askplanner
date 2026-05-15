# GTOC-7533: Backup fails with FileExistedInExternalStorage

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7533
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-04-16T02:34:56.236+0800
- Updated: 2025-05-29T12:54:59.736+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We have had backups failing for almost 24h on our staging cluster, [REDACTED_ENV_NAME] due to the above error. This is a staging cluster we are using to test blue-green for major version upgrade, so it is running on v7.5.1 (rather than on v6.5.4 like [REDACTED_ENV_NAME]). However it is running on our same internal 1.5.1 operator fork.

This occurs during the step where the volume snapshot backup attempts to save cluster [REDACTED_CLUSTER] to the backup folder. I have confirmed that no other clusters are using the given backup folder, so only the backup process on this cluster [REDACTED_CLUSTER] be attempting to save to that location, meaning the cluster’s backup is conflicting with itself.

This issue started 4/15 14:00 pacific, and has happened consistently for subsequent backup attempts since then,

For debugging, I’ve included CRs for one such failed backup as well as operator and backup job logs from the period across all zones

## Recent Comments Excerpt

### 2025-04-23T22:16:41.753+0800 [REDACTED_USER]

@[REDACTED_USER]
 Please take another look if you get a chance, thanks!

### 2025-05-12T18:56:53.157+0800 [REDACTED_USER]

trying recreate locally.

### 2025-05-12T19:33:02.398+0800 [REDACTED_USER]

We sus that it may because the user deleted the backup job by mistake.
There is no clue if it only happen once, let me know if it happens again.

### 2025-05-22T18:09:50.157+0800 [REDACTED_USER]

@[REDACTED_USER]
 can we close the ticket now since there is no update from the customer [REDACTED_CUSTOMER]

### 2025-05-29T12:54:59.736+0800 [REDACTED_USER]

@[REDACTED_USER]
 seems like customer [REDACTED_CUSTOMER]bugging, we can close this one for now. if they have further question, i can add comment here.
