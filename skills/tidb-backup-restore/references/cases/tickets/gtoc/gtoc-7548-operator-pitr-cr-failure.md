# GTOC-7548: Operator PITR CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7548
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-04-23T10:31:49.023+0800
- Updated: 2025-08-11T10:43:33.240+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi,

We have a TiDB cluster [REDACTED_CLUSTER] log-backup seems to be stuck. One of the TiKV pods is having high CPU.

**What we tried?**

1. Pause and resume log backup. It recovered for a bit, and then it started increasing again. A different TiKV pod had high CPU after this.
2. Evicted leaders from the pod with high CPU. The issue recovered for a bit, and then a different TiKV pod had high CPU.

 

Could you please help us remediate this incident?

‌

L1 check  
log-backup.num-threads is 12，tikv vCore is 30

[REDACTED_MEDIA]
[REDACTED_MEDIA]
‌

but backup log CPU usage is full. 

[REDACTED_MEDIA]
seems the backup worker CPU is not reaching 12，**but from log-backup metrics，seems 100% used**

Not sure why there's this difference, please  L3 help check.

## Recent Comments Excerpt

### 2025-04-23T10:32:07.830+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b4fb15c8930080ecf481ec833fcf) by lark and phone

### 2025-04-23T10:32:14.949+0800 [REDACTED_USER]

acked msg index: om_x100b4fb15c8930080ecf481ec833fcf

### 2025-04-23T10:32:15.191+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2025-04-23T10:45:47.425+0800 [REDACTED_USER]

Would you upload the advancer-owned (
webapp-1
) log?
