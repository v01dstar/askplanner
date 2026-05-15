# GTOC-7308: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7308
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2024-12-16T10:47:18.000+0800
- Updated: 2025-03-07T10:55:16.355+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

[https://pingcap-ticket.atlassian.net/browse/APID-10999](https://pingcap-ticket.atlassian.net/browse/APID-10999)  
After rolling restart all pods in a TiDB cluster, the log backup (for the purpose of PiTR) paused with the following error:  
{  
"level": "INFO",  
"time": "2024/02/21 20:25:42.708 +00:00",  
"caller": "region_request.go:1285",  
"message": "throwing pseudo region error due to no replica available",  
"req-ts": [REDACTED_LONG_ID],  
"req-type": "Cop",  
"region": "{ region id: 160261, ver: 312, confVer: 206895 }",  
"region-is-valid": "true",  
"retry-times": 1,  
"replica-read-type": "leader",  
"replica-selector-state": "invalidStore",  
"stale-read": false,  
"replica-status": "peer: 160262, store: 188, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160263, store: 94, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160264, store: 282, isEpochStale: false, attempts: 1, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160265, store: 1, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160266, store: 141, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable",  
"total-backoff-ms": 0,  
"total-backoff-times": 0,  
"total-region-errors": "not_leader:1"  
}

Since the log backup is being stuck by the error, it is impacting our backup SLA because the old raft log files could be recycled over time and can no longer be retrieved.  
We need the issue to be resolved ASAP. 

The TiDB version is v6.5.6.

Thanks!

## Recent Comments Excerpt

### 2024-12-16T10:56:49.000+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_6726653a465ddb4ca46578312d4a2387) by lark and phone

### 2024-12-16T10:57:11.000+0800 [REDACTED_USER]

acked msg index: om_6726653a465ddb4ca46578312d4a2387

### 2024-12-16T10:57:11.000+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2024-12-16T11:00:26.000+0800 [REDACTED_USER]

看报错像是在关机过程中 RaftStore 已经停止，但是 Log Backup 没有停下来 Retry。因此最后耗尽了 retry 次数从而暂停了整个 Log Backup。

### 2024-12-16T11:00:56.000+0800 [REDACTED_USER]

https://github.com/tikv/tikv/issues/16554
这里有一个 issue，未来会修复这个问题。
