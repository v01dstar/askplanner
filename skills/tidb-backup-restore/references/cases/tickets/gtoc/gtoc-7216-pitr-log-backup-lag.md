# GTOC-7216: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7216
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-10-29T15:59:28.000+0800
- Updated: 2025-03-06T17:53:05.600+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, PiTR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Customer [REDACTED_CUSTOMER]:

" The backup task lag increased to 20 min. During the the 20 min, we saw the “failed to get initial snapshot“ error. After 20min, the task no longer had this error and the backup lag went down to the normal level“

 

 

TiKV-Details metrics provided, and the same time period TiDB, TiKV logs provided too

 

and in the same time period, we can see the resolved TS had the same spike, not sure they are related or not.

I found some related cases ( as below ), but seems not the same case

 

[https://jira.tidbcloud.com/browse/GTOC-5812](https://jira.tidbcloud.com/browse/GTOC-5812)

[https://pingcap.feishu.cn/docx/DLdIdnfjloj52JxCnKPcA8fYnNc?from=from_copylink](https://pingcap.feishu.cn/docx/DLdIdnfjloj52JxCnKPcA8fYnNc?from=from_copylink)

## Recent Comments Excerpt

### 2024-10-29T15:59:41.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark

### 2024-10-29T16:26:47.000+0800 [REDACTED_USER]

This might share the same root cause as the issue where the resolved ts is not advancing. Could you review the panel's content? I believe this might reveal the underlying cause 
[REDACTED_MEDIA]

### 2024-10-29T16:31:36.000+0800 [REDACTED_USER]

If it's due to lock. we cannot moving checkpoint forward, because we don't know the txn will success or fail.
