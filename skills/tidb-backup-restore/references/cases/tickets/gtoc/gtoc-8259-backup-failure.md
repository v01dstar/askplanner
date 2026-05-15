# GTOC-8259: Backup failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8259
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2026-03-03T14:49:40.766+0800
- Updated: 2026-03-06T16:44:20.133+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: tikv-data-path, performance-resource
- Labels: N/A

## Symptom / Description Excerpt

巡检发现，客户环境gc未推进，发现目前存在4个br备份进程，目前原因暂时不明确

## Recent Comments Excerpt

### 2026-03-03T14:49:47.790+0800 [REDACTED_USER]

assign to 陈青璟([REDACTED_EMAIL])

### 2026-03-03T14:49:49.289+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), om_x100b555c06074c90c296f36188ebd66) by lark

### 2026-03-03T14:49:59.530+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b555c07a344b4c424a74f60f477a) by lark

### 2026-03-03T18:11:09.514+0800 [REDACTED_USER]

adjust backup.num-threads from 2 to 4 back.

### 2026-03-06T16:44:00.101+0800 [REDACTED_USER]

See Grafana 
TiKV-Details → Backup & Import → Backup CPU utilization
, found the TiKV configuration 
backup.num-threads
 is adjusted from 4 to 2 on Feb 7th.
