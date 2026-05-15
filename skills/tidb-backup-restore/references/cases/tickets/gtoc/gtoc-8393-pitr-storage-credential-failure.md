# GTOC-8393: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8393
- Status: Todo
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2026-04-21T06:59:34.343+0800
- Updated: 2026-04-22T12:04:50.866+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

[REDACTED_MEDIA][REDACTED_MEDIA]
[REDACTED_MEDIA]
[REDACTED_MEDIA]
From AI：

Incident Report: TiKV Store 8375726 — Raft Election Storm & Checkpoint Stall

Date: 2026-04-20  
Duration: 16:38 \~ 20:00 UTC (3 hours 22 minutes)  
Affected Store: 8375726 ([REDACTED_ENV_NAME], store on EC2)  
Impact: \~463 regions stuck without leader, log backup checkpoint stalled, write latency up to 2.5 hours on  
affected regions

---

Summary

After a routine restart of TiKV store 8375726, approximately 463 out of 38,832 regions entered a persistent  
Raft pre-vote loop and were unable to elect a leader for over 3 hours. This caused log backup (PITR)  
checkpoint to stall, produced \~580K warning logs per 30-minute rotation, and blocked writes on affected  
regions for up to 2.5 hours. The issue resolved when store 6082026 (a key peer for the affected regions)  
was restarted, re-establishing TLS connections and allowing Raft consensus to complete.

---

Timeline

┌────────────────┬──────────────────────────────────────────────────────────────────────────────────────┐

## Recent Comments Excerpt

### 2026-04-21T10:59:41.511+0800 [REDACTED_USER]

assign to 江红梅([REDACTED_EMAIL])

### 2026-04-21T10:59:43.375+0800 [REDACTED_USER]

notified (江红梅([REDACTED_EMAIL]), om_x100b515acf2ef890c446403e73d530a) by lark

### 2026-04-21T19:08:25.618+0800 [REDACTED_USER]

Hi ，
首先，我们先说明最严重的问题：
tikv 
[REDACTED_ENV_NAME].ec2.pin220.com:20180
 重启后，可以连上 
[REDACTED_ENV_NAME].ec2.pin220.com:20180
 ，但是后者一直连不上前者，一直报如下的 unreachable 错误，直到后者在 20:00 重启了。
[REDACTED_MEDIA]

### 2026-04-21T19:14:08.620+0800 [REDACTED_USER]

@[REDACTED_USER]
 建议可以请客户找云平台排查一下当时的网络监控。

### 2026-04-22T12:04:50.792+0800 [REDACTED_USER]

核实：Hongmei 的分析结论

整体评价：结论方向正确，主要判断（网络故障 > TLS）有充分的时间线逻辑支撑。

一、根因是网络故障而非 TLS ✅ 正确
时间线关键反证：TLS 握手失败在 17:17 停止，但选举风暴持续至 20:00（又延续 2.5 小时），直到 store 6082026 重启后 30 秒内消失。若根因是 TLS，17:17 之后选举应当停止，与实际不符。AI 描述中的 TLS 根因分析有误。

二、单向连通性断裂 ✅ 正确（证据略有瑕疵）
