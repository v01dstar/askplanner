# GTOC-7295: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7295
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2024-12-06T11:35:03.000+0800
- Updated: 2025-03-06T17:45:36.944+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, storage-credential, tikv-data-path
- Labels: N/A

## Symptom / Description Excerpt

我们发现 Tier 1 集群中的 BR 持续时间存在问题，需要指导如何在以下约束下解决此问题：

1. 当我们以更高的吞吐量运行 BR 时，我们曾经发生过生产事故

1. 我们对 RTO 有 24 小时的合规承诺，目前 T1 集群上的运行时间长达 20 小时

我想讨论的是：

1. 如果我们要升级，那么哪些版本的 tidb（如果有）可以改善此导出负载和恢复时间

1. 如果这表明需要纯粹为了 DR 方面而扩展集群

1. 其他公司如何大规模实施这一举措？因为这似乎不具备可扩展性

1. 如何使用 AWS EBS 快照等非 BR 解决方案

 

在解决此问题时，我们目前未能履行 DR 的合规承诺，因为我们的备份至少需要 20 小时，而恢复集群还需要 4 小时，这使我们违反了恢复目标。

 

tikv 备份，  
num-threads 调整为 2  
   
参考   
[https://jira.tidbcloud.com/browse/GTOC-7234](https://jira.tidbcloud.com/browse/GTOC-7234)

## Recent Comments Excerpt

### 2024-12-06T11:35:15.000+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), ) by lark

### 2024-12-06T11:37:30.000+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), ) by lark

### 2025-01-07T14:59:56.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 is the problem resolved after tuning full backup parameters?

### 2025-01-07T19:09:22.000+0800 [REDACTED_USER]

hi 
@[REDACTED_USER]
 we can close this oncall ticket
[REDACTED_MEDIA]
{*}{*}
