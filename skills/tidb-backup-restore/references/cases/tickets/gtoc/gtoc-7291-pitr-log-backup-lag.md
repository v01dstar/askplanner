# GTOC-7291: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7291
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-12-04T11:25:09.000+0800
- Updated: 2025-03-06T17:45:44.157+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

may I know why br log status --json does not have pitr status information? Is it on purpose? Thanks.

 

[REDACTED_USER]@[REDACTED_ENV_NAME]:\~$ br log status --json

Detail BR log in /tmp/br.log.2024-12-04T00.09.20Z

\[{"name":"pitr_dev_jiaqiwu_test","start_ts":[REDACTED_LONG_ID],"end_ts":[REDACTED_LONG_ID],"table_filter":\["."\],"progress":\[\],"storage":"s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]","checkpoint":[REDACTED_LONG_ID],"estimate_qps":0,"last_errors":\[\]}\]

[REDACTED_USER]@[REDACTED_ENV_NAME]:\~$ br log status

Detail BR log in /tmp/br.log.2024-12-04T00.09.43Z

● Total 1 Tasks.

#1 <

name: [REDACTED_RESOURCE_NAME]

status: ● PAUSE

start: 2024-12-03 23:46:00.052 +0000

end: 2090-11-18 14:07:45.624 +0000

storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]\_

## Recent Comments Excerpt

### 2024-12-04T11:25:20.000+0800 [REDACTED_USER]

notified (, om_1de7958c38d83c444c3de1132637aee3) by lark and phone

### 2024-12-04T11:25:46.000+0800 [REDACTED_USER]

acked msg index: om_1de7958c38d83c444c3de1132637aee3

### 2024-12-04T11:26:15.000+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), ) by lark

### 2024-12-04T11:28:35.000+0800 [REDACTED_USER]

Raised ticket to product team, waiting R&D fix the issue.

### 2024-12-04T11:31:09.000+0800 [REDACTED_USER]

tracking issue is opened 
https://github.com/pingcap/tidb/issues/57959
