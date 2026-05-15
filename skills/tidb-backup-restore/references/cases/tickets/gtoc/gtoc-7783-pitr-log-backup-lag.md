# GTOC-7783: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7783
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-07-19T04:13:41.923+0800
- Updated: 2025-08-06T18:09:35.762+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

log backup stop progressing for about 20 h

## Recent Comments Excerpt

### 2025-07-19T07:20:52.964+0800 [REDACTED_USER]

Paused for 10 minute and resume. But the problem is still here:
[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2025-07-23T00:03:06.606+0800 [REDACTED_USER]

[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2025-07-23T03:50:16.706+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2025-07-24T07:29:54.356+0800 [REDACTED_USER]

[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2025-08-06T18:07:19.062+0800 [REDACTED_USER]

Root cause: checkpoint-lag-limit is not configurable. If the log backup lags more than 48 hours, it becomes impossible to resume.

Workaround: 
 
https://docs.google.com/document/d/1yijtPAgwOZ2H3R_BKbePPPRzVUtV594jeJjGNKzzym4/edit?tab=t.0
 
You could patch the backupSchedule to restart a new log backup.
