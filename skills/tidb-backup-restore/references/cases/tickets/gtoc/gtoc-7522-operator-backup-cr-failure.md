# GTOC-7522: Operator backup CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7522
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-04-11T10:18:38.277+0800
- Updated: 2025-05-08T14:49:09.086+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi, we had a scheduled snapshot backup that failed and did not retry despite having backoffRetryPolicy with maxRetryTimes = 2.

Can we find out:

1. why backup failed in this case (and how to avoid)
2. How we can have it automatically retry in cases like this

This issue was on v7.5.1, included br logs with FATAL error + k8s specs for BackupSchedule, Backup, k8s job that ran the backup

## Recent Comments Excerpt

### 2025-04-11T10:18:52.885+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100bb0b38e0fb88c0f10f20d2880de6) by lark

### 2025-04-11T12:07:46.532+0800 [REDACTED_USER]

This is due to a kernel br issue.
We the operator don’t support retry this kind of fail, need to modify the code to achieve this function.
