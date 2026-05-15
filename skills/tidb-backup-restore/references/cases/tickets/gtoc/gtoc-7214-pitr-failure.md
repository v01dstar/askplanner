# GTOC-7214: PITR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7214
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P1
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2024-10-29T09:10:58.000+0800
- Updated: 2025-03-06T17:53:09.283+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], observability-error-message
- Labels: BR

## Symptom / Description Excerpt

As of now TiDB has a BR limitation which is a blocker to us. Basically BR has the limitation which cannot support restore schema/table when it running the log backup. We want to understand what is the timeline for the limitation to be removed so we can perform adhoc restore while the cluster has log backup enabled.

## Recent Comments Excerpt

### 2024-10-29T09:11:11.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), om_b830e257ff8712e29d814fbc1fcb0e48) by lark and phone

### 2024-10-29T09:11:27.000+0800 [REDACTED_USER]

acked msg index: om_b830e257ff8712e29d814fbc1fcb0e48

### 2024-10-29T09:11:29.000+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2024-10-29T09:18:20.000+0800 [REDACTED_USER]

Regarding this request, we have potential solutions to be discussed, but there is currently no specific timeline for delivery. BTW which customer [REDACTED_CUSTOMER]?

### 2024-10-29T09:40:04.000+0800 [REDACTED_USER]

This customer [REDACTED_CUSTOMER]ases. It's a constant need to restore some of the databases. This should not require stopping the log backup.
