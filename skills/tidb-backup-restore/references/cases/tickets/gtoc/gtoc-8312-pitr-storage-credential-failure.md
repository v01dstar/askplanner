# GTOC-8312: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8312
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2026-03-18T17:16:14.867+0800
- Updated: 2026-03-26T02:24:13.891+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

## 客户提单详情

[REDACTED_IP] 每天网卡流量升高报警（客户自定义了网卡流量告警）

[REDACTED_MEDIA]
该节点部署了定时 BR backup 任务，其中 12:10 开始的 br log truncate 清理任务会导致节点网络流量升高，从日志看到，开始时间 12:10 和 结束时间 12:16 与网卡流量升高时间能对应上，主要是 in 流量

[REDACTED_MEDIA]
[REDACTED_MEDIA]
客户通过抓包确认，[REDACTED_IP] 网卡 in 流量都来自于 S3

[REDACTED_MEDIA]
问题：

1. 为何 br log truncate 需要从 S3 读这么大流量的数据，是否符合预期
2. 是否有方法对流量限速，避免超过报警阈值

请 GS 老师协助，谢谢

---

## 排查过程：

> 1. 为何 br log truncate 需要从 S3 读这么大流量的数据，是否符合预期
> 

对于这一点， 官方文档里有提到以下

## Recent Comments Excerpt

### 2026-03-20T13:57:15.356+0800 [REDACTED_USER]

@[REDACTED_USER]
 可以使用 BR v8.5.5、加上 
--metadata-download-batch-size=16
 參數去跑 log truncate 嗎？把 concurrency 從 128 調低到 16。

### 2026-03-20T14:23:23.541+0800 [REDACTED_USER]

@[REDACTED_USER]
 是不是客户用 br:v8.5.6 就行了，不需要 tidb 集群升级的？现在 tidb 集群是 v8.5.1

### 2026-03-20T14:23:29.125+0800 [REDACTED_USER]

@[REDACTED_USER]
 了解

### 2026-03-20T15:19:21.893+0800 [REDACTED_USER]

@[REDACTED_USER]
 br:v8.5.6 也可以，不需要升集群，
但建議後面找個時間升級，因為 TiKV v8.5.3 把 meta 命名方式從 
{resolvedTS}-{RandomUUID}.meta
 改為 
{flushTs}-{minDefaultTs}-{minTs}-{maxTs}.meta
 了 
https://docs.pingcap.com/zh/tidb/stable/br-log-architecture/#%E5%A4%87%E4%BB%BD%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84

### 2026-03-23T15:02:53.298+0800 [REDACTED_USER]

The linked ticket has been resolved.
