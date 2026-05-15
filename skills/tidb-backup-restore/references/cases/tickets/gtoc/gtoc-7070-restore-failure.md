# GTOC-7070: Restore failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7070
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-08-12T14:26:37.000+0800
- Updated: 2025-03-06T18:03:49.535+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR, TiKV BR
- Categories: tikv-data-path, performance-resource, compatibility-upgrade
- Labels: N/A

## Symptom / Description Excerpt

备份太慢，tikv 的 backup cpu 使用很低

[REDACTED_MEDIA]
   
[https://pingcap-ticket.atlassian.net/browse/APID-10814](https://pingcap-ticket.atlassian.net/browse/APID-10814)

## Recent Comments Excerpt

### 2024-08-12T14:26:50.000+0800 [REDACTED_USER]

notified (陈书宁([REDACTED_EMAIL]), ) by lark

### 2024-08-12T14:28:03.000+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), ) by lark

### 2024-08-12T14:47:51.000+0800 [REDACTED_USER]

已知问题 
https://github.com/tikv/tikv/issues/17168
，当使用断点备份继续备份时，会有比较大的概率进行 fine grained backup 模式。建议调大 BR 参数 --concurrency 备份。 例如 --concurrency 16。

### 2024-08-13T11:22:13.000+0800 [REDACTED_USER]

客户先后进行了几次备份，麻烦看下最新一次的备份

[2024/08/11 08:37:38.926 +00:00] [INFO] [info.go:49] ["Welcome to Backup & Restore (BR)"] [release-version=v6.5.8] 
从这个时间之后，没有 fineGrainedBackup 关键字日志
