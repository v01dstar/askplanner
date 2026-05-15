# GTOC-7784: PITR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7784
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-07-19T04:30:21.417+0800
- Updated: 2025-07-29T10:34:42.727+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: Clinic
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Customer [REDACTED_CUSTOMER], with 3 namespaces, each namespace has a tidb cluster with same name as ‘basic’. And the TidbMonitor CR monitoring all 3.

Customer [REDACTED_CUSTOMER]:

```
curl -s http://localhost:4917/api/v1/collectors -X POST -d '{"clusterName": "basic","namespace": "tidb-system-shard", "monitor_namespace": "tidb-monitor", "from": "2025-07-13 11:00 -0700","to": "2025-07-13 07:00 -0700"}'
```

There is no error, but the data collected is from wrong namespace. 

Here is the data collected:<custom data-type="smartlink" data-id="id-0">[REDACTED_CLINIC_URL]> 

Comparing it to screenshot. This is in tikv-details->log backup:

[REDACTED_MEDIA]

## Recent Comments Excerpt

### 2025-07-19T04:30:35.594+0800 [REDACTED_USER]

notified (郭虎([REDACTED_EMAIL]), om_x100b489ea06290b80ec67e6a5fc1177) by lark

### 2025-07-29T09:38:50.908+0800 [REDACTED_USER]

use diag collectk to collect data. 
https://pingcap.feishu.cn/wiki/QPTfws8bqiXGGSkE7OVcWSgSnge
