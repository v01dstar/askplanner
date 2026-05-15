# GTOC-6565: Backup gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6565
- Status: Resolved
- Resolution: Done
- Priority: P0
- Issue type: Incident
- Created: 2023-12-13T10:23:17.000+0800
- Updated: 2024-10-14T10:07:12.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: operator-cr, performance-resource
- Labels: N/A

## Symptom / Description Excerpt

I managed to block the pod initialization for the init backup br 

[REDACTED_RESOURCE_NAME]                      0/2     PodInitializing   0              7m20s

but volumebacup cr is still in Running state

[REDACTED_RESOURCE_NAME]   Running                                       16m

## Recent Comments Excerpt

### 2023-12-13T10:30:25.000+0800 [REDACTED_USER]

notified (王乐([REDACTED_EMAIL]), om_80eeb27f4a49266dc3949facd2397d51) by lark and phone

### 2023-12-13T10:46:59.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/Dec/23 2:46 AM
[REDACTED_MEDIA]

### 2023-12-13T11:44:29.000+0800 [REDACTED_USER]

PR opened 
https://github.com/pingcap/tidb-operator/pull/5457

### 2023-12-17T11:48:48.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Dec/23 3:48 AM

FYI
PR opened 
https://github.com/pingcap/tidb-operator/pull/5457

### 2023-12-20T05:00:34.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 19/Dec/23 9:00 PM

Fix has been verified. Feel free to close.
