# GTOC-7244: Backup gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7244
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-11-15T09:29:27.000+0800
- Updated: 2025-03-06T17:52:17.331+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We're seeing some weird behavior with backups. We're backing up a table that has 3 tables, two of which are empty and the third has 7 small rows. The backup gets to progress=71.43% and count=5/7 and then gets stuck there for about 10 minutes (still reporting logs and restating that it is right there). Then after about 10 minutes it is able to get to progress=100% and count=7/7, but then hangs. I'm letting it run still, but I have no idea how to debug this. Looking at the TiDB dashboard and Grafana nothing looks immediately obvious as to what could be wrong.

```
apiVersion: pingcap.com/v1alpha1
kind: Backup
metadata:
  name: [REDACTED_ENV_NAME]
  namespace: [REDACTED_NAMESPACE]
spec:
  imagePullSecrets:
    - name: [REDACTED_RESOURCE_NAME]
  backupType: full
  tableFilter: 
    - titan_schema_metadata.*
  cleanPolicy: Delete
  br:
    cluster: [REDACTED_CLUSTER]
    clusterNamespace: [REDACTED_NAMESPACE]
    sendCredToTikv: false
    logLevel: info
    concurrency: 1
  s3:
    secretName: [REDACTED_RESOURCE_NAME]
    provider: minio
    bucket: backups
    endpoint: http://minio-hl.minio.svc.cluster.local:9000
```

## Recent Comments Excerpt

### 2024-11-15T09:30:07.000+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2024-11-20T02:33:04.000+0800 [REDACTED_USER]

[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2024-12-01T03:51:10.000+0800 [REDACTED_USER]

This ticket can be closed now. Thanks.
