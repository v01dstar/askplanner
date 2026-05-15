# GTOC-7367: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7367
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2025-01-24T13:24:22.883+0800
- Updated: 2025-03-06T17:38:35.921+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

For the following integrated backup schedule:

```
cat >[REDACTED_RESOURCE_NAME].yaml<<EOF
---
apiVersion: pingcap.com/v1alpha1
kind: BackupSchedule
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
spec:
  maxBackups: 3
  # maxReservedTime: "3h"
  schedule: "*/5 * * * *"
  backupTemplate:
    serviceAccount: [REDACTED_RESOURCE_NAME]
    backupType: full
    cleanPolicy: Delete
    br:
      cluster: [REDACTED_CLUSTER]
      clusterNamespace: [REDACTED_NAMESPACE]
      sendCredToTikv: false
    s3:
      provider: aws
      region: us-east-2
      bucket: [REDACTED_BUCKET]
      prefix: [REDACTED_RESOURCE_NAME]/full
  logBackupTemplate:

## Recent Comments Excerpt

### 2025-01-24T13:24:37.303+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), ) by lark

### 2025-01-24T18:48:22.748+0800 [REDACTED_USER]

According to the doc 
https://docs.pingcap.com/tidb-in-kubernetes/stable/[REDACTED_RESOURCE_NAME]#backupschedule-cr-fields
 the log backup are recycled based on the 
maxReservedTime
 setting only (which you have commented out). And indeed 
log truncation
 is only implemented in 
backupGCByMaxReservedTime()

### 2025-01-28T22:48:17.572+0800 [REDACTED_USER]

This ticket can be close. Thanks!
