# GTOC-7145: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7145
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-09-19T10:26:05.000+0800
- Updated: 2025-03-06T18:01:40.444+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Log backup tasks are deleted without manual input. We also do not find br log or any hint indicate why. This happened multiple times in the past few weeks and we had to manual restart br task.

 

PD and BR logs are in s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]  
s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]  
s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]

TIKV logs: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]  
s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]  
s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]  
s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]  
s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]

## Recent Comments Excerpt

### 2024-09-19T10:26:49.000+0800 [REDACTED_USER]

log start: 2024/09/09 17:22:18 +00
  # log not found: 2024/09/18 18:37:57 +00

### 2024-09-19T10:27:23.000+0800 [REDACTED_USER]

log backup start 2024/09/09 17:22:16 on TiKV
  # log backup cancelled 2024/09/18 17:43:47 on TiKV
  # task recreate at 2024/09/18 18:40
  # No pitr task inside PD log from 17:43 - 18:40
  # No BR action from 17:43 - 18:40

### 2024-09-19T10:39:32.000+0800 [REDACTED_USER]

Is there any "Pause" or "fatal error" keywords in TiKV log from 09/09 to 09/18?

### 2024-09-19T13:39:21.000+0800 [REDACTED_USER]

From logs we can see all components (tidb advancer + tikv) receive the delete task event at same time around 09/18 17:43 within 1ms. and no tikv reports error.
[REDACTED_MEDIA]
So I think this task has been deleted at that time. 
But it's strange that in br.log there is no log related operation at that time.
Is it possible that customer [REDACTED_CUSTOMER]?

### 2024-09-19T15:48:25.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark
