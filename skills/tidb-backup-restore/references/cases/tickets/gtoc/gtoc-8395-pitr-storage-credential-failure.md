# GTOC-8395: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8395
- Status: Todo
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2026-04-21T23:26:14.777+0800
- Updated: 2026-04-24T08:02:26.735+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Seeing this in a cluster:

```
NAME                                TYPE   MODE   STATUS        BACKUPPATH                                                                                                            BACKUPSIZE   COMMITTS             LOGTRUNCATEUNTIL   TIMETAKEN   AGE
[REDACTED_RESOURCE_NAME]          log    RetryFailed   s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                [REDACTED_LONG_ID]                                  13h
```

```
apiVersion: pingcap.com/v1alpha1
kind: Backup
metadata:
  annotations:
    argocd.argoproj.io/tracking-id: [REDACTED_ENV_NAME]:pingcap.com/BackupSchedule:[REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME]
    atlassian.com/logging_id: [REDACTED_UUID]
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"pingcap.com/v1alpha1","kind":"BackupSchedule","metadata":{"annotations":{"argocd.argoproj.io/tracking-id":"[REDACTED_ENV_NAME]:pingcap.com/BackupSchedule:[REDACTED_ENV_NAME]/[REDACTED_RESOURCE_NAME]","atlassian.com/logging_id":"[REDACTED_UUID]"},"name":"[REDACTED_RESOURCE_NAME]","namespace":"[REDACTED_ENV_NAME]"},"spec":{"backupTemplate":{"backupType":"full","br":{"cluster":"basic","clusterNamespace":"[REDACTED_ENV_NAME]","sendCredToTikv":false},"cleanPolicy":"Retain","imagePullSecrets":[{"name":"image-pull-credentials"}],"s3":{"bucket":"[REDACTED_BUCKET]","prefix":"integrated-backups/[REDACTED_ENV_NAME]/snapshot","provider":"aws","region":"eu-central-1"},"serviceAccount":"[REDACTED_RESOURCE_NAME]","toolImage":"docker.atl-paas.net/sox/atlassian/titan/br:v8.5.5"},"logBackupTemplate":{"backupMode":"log","br":{"cluster":"basic","clusterNamespace":"[REDACTED_ENV_NAME]","sendCredToTikv":false},"cleanPolicy":"Retain","imagePullSecrets":[{"name":"image-pull-credentials"}],"s3":{"bucket":"[REDACTED_BUCKET]","prefix":"integrated-backups/[REDACTED_ENV_NAME]/log","provider":"aws","region":"eu-central-1"},"serviceAccount":"[REDACTED_RESOURCE_NAME]","toolImage":"docker.atl-paas.net/sox/atlassian/titan/br:v8.5.5"},"maxReservedTime":"720h","schedule":"0 * * * *"}}
  creationTimestamp: "2026-04-21T01:45:58Z"
  finalizers:
  - tidb.pingcap.com/backup-protection
  generation: 10
  labels:
    app.kubernetes.io/instance: [REDACTED_RESOURCE_NAME]
    app.kubernetes.io/managed-by: backup-schedule-operator
    app.kubernetes.io/name: [REDACTED_RESOURCE_NAME]
    tidb.pingcap.com/backup-schedule: [REDACTED_RESOURCE_NAME]
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
  ownerReferences:

## Recent Comments Excerpt

### 2026-04-21T23:26:19.735+0800 [REDACTED_USER]

fail to find L2 assignee, retry of choosing L2 assignee will be triggered 2 hours later.

if the issue is urgent, please escalate to L3 directly

### 2026-04-21T23:26:56.365+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), om_x100b514d3d39fca0c140debc7cfef8f) by lark

### 2026-04-21T23:31:34.188+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100b514dcb9fdca0c4a9091b82737d6) by lark

### 2026-04-24T08:02:26.631+0800 [REDACTED_USER]

The linked ticket has been resolved.
