# GTOC-8347: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8347
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2026-04-07T02:25:36.198+0800
- Updated: 2026-04-09T00:23:02.590+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

I am looking into how partial PITR (i.e restoring only a subset of dbs) would impact ongoing changefeeds and logbackups. AI says that both of them will be broken by PITR that directly restores SST bypassing change logs which makes sense. This means

1. Changefeed needs to be restarted - Not very clear how though
2. Log backups - A snapshot backup needs to taken immediately, because the partial restore breaks log continuity.

Could you please confirm if my understanding is right?

## Recent Comments Excerpt

### 2026-04-07T02:27:36.487+0800 [REDACTED_USER]

For question 2, it is very clearly documented, that a snapshot backup needs to taken immediately.
However for question 1, I’m not how how partial PiTR restore of a few databases would impact TiCDC. Please help.

### 2026-04-07T04:54:28.934+0800 [REDACTED_USER]

I think I have created an FRM before: 
https://tidb.atlassian.net/browse/FRM-3614

### 2026-04-07T15:13:31.813+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b527ea77e8cb4c4ae40d924f2fc6) by lark

### 2026-04-08T09:35:28.942+0800 [REDACTED_USER]

一、背景
当前在分析 
Partial PITR（仅恢复部分 DB）
 对以下组件的影响：
CDC（changefeed）
Log Backup（PITR 日志链）
在分析过程中，发现 
PITR 与 Snapshot Restore 在 CDC 相关行为上存在潜在不一致

### 2026-04-09T00:22:59.331+0800 [REDACTED_USER]

感谢梳理，结合目前的底层机制和后续的维护成本，我再系统地对齐一下这几个点：
问题 1（准入检查不一致）：
 是预期的。现在的准入约束最早就是给 Snapshot Restore 做的，并没有专门为 PITR 的 recovery TS 设计拦截，跨越 CDC checkpoint 是典型的 
Undefined Behavior
。
不过需要明确一点：
 考虑到 PITR 目前的底层架构确实难以兼容 CDC，我们现在的预期行为应该是——
只要集群存在 CDC Changefeed，PITR 就应该直接拒绝执行（报错失败）
