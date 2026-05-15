# GTOC-7619: Backup overloads PD region scan

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7619
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2025-05-28T01:52:59.126+0800
- Updated: 2025-07-10T15:19:33.986+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB
- Categories: storage-credential, tikv-data-path, performance-resource
- Labels: N/A

## Symptom / Description Excerpt

tidb backup is causing high cpu usage and as a result, our servers are degrading.

## Recent Comments Excerpt

### 2025-05-28T08:13:06.337+0800 [REDACTED_USER]

acked msg index: om_x100b4c511ee1951c0ece4e0b5872aa6

### 2025-05-28T08:13:07.181+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2025-05-28T08:39:18.555+0800 [REDACTED_USER]

acked msg index: om_x100b4c515d93c0940ec07becc93b130

### 2025-05-28T08:39:18.579+0800 [REDACTED_USER]

acked msg index: om_x100b4c517f6594900f1cbecb3497a92

### 2025-05-28T09:13:49.936+0800 [REDACTED_USER]

The main reason is that the huge amount of get region requests have broken the pd server, triggering frequent leader election.
[REDACTED_MEDIA]
[REDACTED_MEDIA]
[REDACTED_MEDIA]

If it's just get region requests, we can consider the active follower feature.
But for this scenario, I think it's more recommended to use rate limiter (should be available in 8.1), circuit breaker (next release)
