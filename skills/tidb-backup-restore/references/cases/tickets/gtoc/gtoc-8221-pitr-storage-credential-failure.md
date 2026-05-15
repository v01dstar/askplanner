# GTOC-8221: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8221
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2026-02-12T10:05:25.420+0800
- Updated: 2026-02-14T03:31:21.261+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

<custom data-type="smartlink" data-id="id-0">https://atlassian.slack.com/archives/C07133BSTPX/p1770839940007549</custom> 

Copy paste from slack thread:

> Hi [REDACTED_USER], We are experiencing restore job failures in one of our production clusters after scaling up TiKV volume from 60G to 120G yesterday.
>
> We also checked for the `lock.writ` file in S3 but it does not exist.
>
> Can you please help investigate?

## Recent Comments Excerpt

### 2026-02-12T10:10:43.317+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100b57e724dd68a8c25753c8089ffba) by lark and phone

### 2026-02-12T10:11:24.769+0800 [REDACTED_USER]

Response(not ack for Critical alert) in lark: om_x100b57e724dd68a8c25753c8089ffba

### 2026-02-12T10:11:25.524+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2026-02-12T20:04:54.028+0800 [REDACTED_USER]

[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2026-02-12T20:53:49.149+0800 [REDACTED_USER]

This is clinic: 
[REDACTED_CLINIC_URL]
