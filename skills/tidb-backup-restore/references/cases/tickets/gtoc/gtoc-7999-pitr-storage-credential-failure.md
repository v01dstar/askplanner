# GTOC-7999: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7999
- Status: Pending for fixes/proactive actions
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-10-31T03:42:33.036+0800
- Updated: 2025-11-07T18:21:27.169+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, performance-resource, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

While we were doing performance tests for PITR, we noticed a limitation of PITR. Once you restore a database to a specific timestamp using a log backup stream, you can't go back to an earlier time using the same stream for that DB, even if you use a different snapshot backup. So if a customer [REDACTED_CUSTOMER]do it, then they come back and say "actually we need 5 hours ago instead," we're stuck. We can't do it because the log backup data from 5-4 hours ago has already been used up. The only options after that are to restore to a time later than the 4-hour mark using the same log stream.

## Recent Comments Excerpt

### 2025-10-31T03:42:43.951+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100b5f0fb5db2ca00f2be95db97c31c) by lark and phone

### 2025-10-31T03:43:16.259+0800 [REDACTED_USER]

Response(not ack for Critical alert) in lark: om_x100b5f0fb5db2ca00f2be95db97c31c

### 2025-10-31T03:43:16.440+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2025-10-31T03:46:35.717+0800 [REDACTED_USER]

Atlassian has reported an issue. I’ve verified several scenarios (Test1–Test4), and the results are summarized in the document.
Currently, PITR behavior indeed has a limitation:

If a restore has already been performed using a given log stream (for example, restored to 
11:00
), any subsequent restore using the same snapshot to an 
earlier
 time (for example,

### 2025-10-31T03:48:06.296+0800 [REDACTED_USER]

Note: test 1,2 are successful, they just create a baseline. test 3 is successful, but test 4 fails. 
[REDACTED_MEDIA]
[REDACTED_MEDIA]
