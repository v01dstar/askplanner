# GTOC-7494: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7494
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-03-27T02:29:14.533+0800
- Updated: 2025-09-02T17:03:25.764+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

For an integrated backupschedule. From k8s it looks log backup is running 

```
hli5@~❯ kubectl get backup -n [REDACTED_ENV_NAME]
[REDACTED_RESOURCE_NAME]                                log        Running       s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                              [REDACTED_LONG_ID]                                  49d 
```

But if check using `br` directly, log backup has stopped. 

```
root@install-tiup:~/.tiup/bin# ./tiup br log status  --pd="[REDACTED_IP]:2379"
Starting component br: /root/.tiup/components/br/v8.5.1/br log status --pd=[REDACTED_IP]:2379
Detail BR log in /tmp/br.log.2025-03-25T21.56.33Z
○ No Task Yet.
```

## Recent Comments Excerpt

### 2025-03-27T02:29:48.299+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), om_42305233ccda17865e17f3194068beef) by lark

### 2025-03-27T10:46:45.445+0800 [REDACTED_USER]

Could you give me the details how the config is incorrect.

### 2025-03-28T03:19:39.000+0800 [REDACTED_USER]

[REDACTED_INTERNAL_URL]

### 2025-04-02T16:31:09.393+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_3460384c689a4e1555a79582228da9dc) by lark
