# GTOC-7136: Backup/Restore failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7136
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-09-13T12:39:51.000+0800
- Updated: 2025-03-06T18:01:56.260+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: BR
- Categories: tikv-data-path
- Labels: N/A

## Symptom / Description Excerpt

[https://pingcap-ticket.atlassian.net/browse/ST-976](https://pingcap-ticket.atlassian.net/browse/ST-976)  
br 备份失败，初步分析是某几个 region 有问题

## Recent Comments Excerpt

### 2024-09-13T12:40:00.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark

### 2024-09-13T14:12:42.000+0800 [REDACTED_USER]

从 BR 日志分析
[2024/09/13 05:05:03.388 +08:00] [INFO] [client.go:1028] ["find leader"] [range-sn=18] [Leader="{\"id\":2728797,\"store_id\":2512659}"] [key=7480000000000000FF1A5F698000000000FF0000010380000000FF00001D0603800000FF0000000000038000FF00000000000D0380FF0000000000008200FE]
刚启动备份时，就有 region 2728797 在 store 2512659 上无法备份，重试的报错，这个无法备份的 leader 就是导致失败的原因。进一步分析需要 store 2512659 的 tikv 日志，看看对应时刻（2024/09/13 05:05:03.388 +08:00 前后一小时）该 region 的情况。另外，最好也上传下 PD leader 的日志。有助于分析
