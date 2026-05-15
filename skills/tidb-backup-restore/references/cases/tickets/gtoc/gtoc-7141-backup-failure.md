# GTOC-7141: Backup failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7141
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2024-09-18T10:33:00.000+0800
- Updated: 2025-03-06T18:01:47.587+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: uncategorized
- Labels: N/A

## Symptom / Description Excerpt

TiDBCloud上备份目前不支持表级快照备份及增量备份，客户是否能使用 backup SQL来满足需求，以及相关原理希望能了解一下，官方文档中解释较少

## Recent Comments Excerpt

### 2024-09-18T10:33:10.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark

### 2024-09-18T10:48:08.000+0800 [REDACTED_USER]

客户具体的需求是什么？
是从 OP 执行一次性任务，备份恢复到 TiDB Cloud？
还是定期在 TiDB Cloud 备份某张表？

### 2024-09-18T11:09:46.000+0800 [REDACTED_USER]

需求是TiDB Cloud 的表级备份，对部分核心表定期快照备份+增量备份，目前考虑是否能通过 backup SQL来满足需求，感谢
