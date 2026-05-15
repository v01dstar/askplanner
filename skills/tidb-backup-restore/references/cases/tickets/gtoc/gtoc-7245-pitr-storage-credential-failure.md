# GTOC-7245: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7245
- Status: Todo
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-11-15T09:52:40.000+0800
- Updated: 2025-03-06T17:52:15.491+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

I tried to test PITR in staging ([REDACTED_ENV_NAME]) env but it is failing presumably due large number of schemas in this cluster. There are about 43,692 schemas and probably the restore job is hitting a Kubernetes size limit for configmaps?

Large log which prints the names of about 44K schemas attached.

Error:

```
restore E1114 00:43:41.679946      10 restore_status_updater.go:97] Failed to update restore [[REDACTED_ENV_NAME]/[REDACTED_ENV_NAME], error: Request entity too large: limit is 3145728
```

Here is the yaml used for restore

```
apiVersion: pingcap.com/v1alpha1
kind: Restore
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
spec:
  restoreMode: pitr
  serviceAccount: [REDACTED_RESOURCE_NAME]
  br:
    cluster: [REDACTED_CLUSTER]
    clusterNamespace: [REDACTED_NAMESPACE]
  s3:
    provider: aws
    region: us-west-2
    bucket: [REDACTED_BUCKET]

## Recent Comments Excerpt

### 2024-11-15T10:00:30.000+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2024-11-18T11:05:44.000+0800 [REDACTED_USER]

上传的这个日志看起来错误原因是“The current restore task is regarded as a new task [start-ts=[REDACTED_LONG_ID] [restored-ts=[REDACTED_LONG_ID] while the last task info: [start-ts=[REDACTED_LONG_ID] [restored-ts=[REDACTED_LONG_ID] [skip-snapshot-restore=true]. ”？

### 2024-12-01T03:53:54.000+0800 [REDACTED_USER]

This ticket can be closed now. thanks.
