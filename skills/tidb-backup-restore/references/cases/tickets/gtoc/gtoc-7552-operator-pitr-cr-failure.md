# GTOC-7552: Operator PITR CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7552
- Status: CAN'T REPRODUCE
- Resolution: Cannot Reproduce
- Priority: P3
- Issue type: Incident
- Created: 2025-04-24T17:42:08.632+0800
- Updated: 2025-05-08T14:51:30.804+0800
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

Thanks

## Recent Comments Excerpt

### 2025-04-24T17:42:56.580+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b4f94373144e80f248c2e3c162ec) by lark

### 2025-04-25T15:02:29.202+0800 [REDACTED_USER]

这个先 cancel 了。和 
https://tidb.atlassian.net/browse/GTOC-7548
  重复了。
