# GTOC-7593: Restore fails with [BR:Common:ErrUnknown\]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7593
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2025-05-15T21:32:51.715+0800
- Updated: 2025-05-16T10:19:27.180+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: restore-failure, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Detail BR log in restore.log   
\[2025/05/15 19:51:25.612 +08:00\] \[INFO\] \[collector.go:77\] \["Full Restore failed summary"\] \[total-ranges=0\] \[ranges-succeed=0\] \[ranges-failed=0\]  
Error: the config 'new_collation_enabled' not match, upstream:True, downstream: False: \[BR:Common:ErrUnknown\]internal error

## Recent Comments Excerpt

### 2025-05-15T21:33:10.129+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100b4d6a9fea09100f2bad0be0a0ea3) by lark and phone

### 2025-05-15T21:34:01.209+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2025-05-15T21:34:01.499+0800 [REDACTED_USER]

acked msg index: om_x100b4d6a9fea09100f2bad0be0a0ea3

### 2025-05-16T07:17:43.884+0800 [REDACTED_USER]

@[REDACTED_USER]
 please record your analysis here.

### 2025-05-16T09:28:04.024+0800 [REDACTED_USER]

You have to keep the downstream collation setting sync with upstream
https://tidb.net/book/book-rush/features/new-features/new-collation
