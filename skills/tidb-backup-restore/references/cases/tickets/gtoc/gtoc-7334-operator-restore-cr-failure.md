# GTOC-7334: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7334
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-12-31T11:04:11.000+0800
- Updated: 2025-03-06T17:44:26.824+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: restore-failure, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

database test3 does not exist, but I can specify it in the restore CR and can restore successfully, from the logs, no any errors or warnings say test3  not exist

## Recent Comments Excerpt

### 2024-12-31T11:04:21.000+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), ) by lark

### 2024-12-31T15:01:42.000+0800 [REDACTED_USER]

BR will not check the table existence

./br restore full --filter "test3.*"  

 

BR will check "test3.*"
