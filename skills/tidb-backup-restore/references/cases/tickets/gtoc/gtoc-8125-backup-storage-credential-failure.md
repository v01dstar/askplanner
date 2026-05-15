# GTOC-8125: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8125
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2026-01-02T09:46:59.714+0800
- Updated: 2026-01-13T20:47:45.871+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

Here is a list of the last \~50 snapshot `Backup` creation timestamps (created via our `BackupSchedule`) in a particular cluster:

```
2025-12-30T11:08:36Z
2025-12-30T12:00:31Z
2025-12-30T13:03:11Z
2025-12-30T13:08:25Z
2025-12-30T14:00:20Z
2025-12-30T14:05:51Z
2025-12-30T15:03:13Z
2025-12-30T16:00:17Z
2025-12-30T16:05:49Z
2025-12-30T17:03:13Z
2025-12-30T18:00:17Z
2025-12-30T18:05:45Z
2025-12-30T19:03:04Z
2025-12-30T19:08:17Z
2025-12-30T20:02:45Z
2025-12-30T21:05:22Z
2025-12-30T21:10:32Z
2025-12-30T22:02:57Z
2025-12-30T22:08:10Z
2025-12-30T23:00:46Z
2025-12-31T00:03:21Z
2025-12-31T01:00:37Z
2025-12-31T01:05:55Z
2025-12-31T02:03:08Z
2025-12-31T02:08:21Z

## Recent Comments Excerpt

### 2026-01-02T09:47:04.479+0800 [REDACTED_USER]

fail to find L2 assignee: please escalate to L3

### 2026-01-02T09:47:06.678+0800 [REDACTED_USER]

assign to 余峻岑([REDACTED_EMAIL])

### 2026-01-02T09:47:08.704+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b5a467774d4a8c25e737243fbc5d) by lark

### 2026-01-02T09:48:27.268+0800 [REDACTED_USER]

Issue Summary: BackupSchedule triggering duplicate snapshot backups within the same schedule window
We are investigating an issue where a 
BackupSchedule
 with a cron schedule of 
0 * * * *
 is triggering 
multiple snapshot backups within the same hourly window
, typically within ~5 minutes of each other.

### 2026-01-07T04:17:34.042+0800 [REDACTED_USER]

Since root cause is already known. This ticket can be closed now.
