# GTOC-7506: PITR fails with some flags [--PITRRestoredTs] are missing.

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7506
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-04-01T08:26:09.248+0800
- Updated: 2025-04-02T16:28:45.648+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiDB Operator
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

A PITR we scheduled via tidb-operator Restore CR failed due to the error:

```
/[REDACTED_RESOURCE_NAME] restore --namespace=[REDACTED_NAMESPACE] --restoreName=[REDACTED_RESOURCE_NAME] --tikvVersion=v8.5.1-2d4f043 --mode=pitr --pitrRestoredTs=
error: some flags [--pitrRestoredTs] are missing.
```

Our expectation is that the `pitrRestoredTs` param is optional, and if unspecified PITR will use the latest available checkpoint TS. It appears the logic is specified here in BR: <custom data-type="smartlink" data-id="id-0">https://github.com/pingcap/tidb/blob/master/br/pkg/task/stream.go#L1314</custom> 

However operator side considers it a required arg and always specifies an empty flag: <custom data-type="smartlink" data-id="id-1">https://github.com/pingcap/tidb-operator/blob/master/pkg/backup/restore/restore_manager.go#L771</custom> . Then the CLI flag validation fails: <custom data-type="smartlink" data-id="id-2">https://github.com/pingcap/tidb-operator/blob/master/cmd/backup-manager/app/cmd/restore.go#L41</custom> 

Here is the final restore CR yaml:

```
apiVersion: pingcap.com/v1alpha1
kind: Restore
metadata:
  annotations:
    com.airbnb.container-injector-mutator/additional-env-vars: '[{"name": "HTTPS_PROXY_PASSWORD",
      "valueFrom": {"secretKeyRef":{"key": "loggingHttpsProxyPassword", "name": "shared-secret"}}}]'
    com.airbnb.container-injector-mutator/inject-logging: runtime
    com.airbnb.container-injector-mutator/injected-version-logging: 0.0.1
    iam.amazonaws.com/role: tidb-shared-iam
    kube-gen.airbnb.io: faked
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"tidb.airbnb.com/v1","kind":"LogicalRestore","metadata":{"annotations":{},"name":"[REDACTED_ENV_NAME]","namespace":"[REDACTED_ENV_NAME]"},"spec":{"backup":{"logBackupStorageProvider":{"s3":{"bucket":"[REDACTED_BUCKET]","prefix":"rp-[REDACTED_ENV_NAME]/scheduled/log/log-2025-03-10t19-51-51"}},"snapshotBackupStorageProvider":{"s3":{"bucket":"[REDACTED_BUCKET]","prefix":"rp-[REDACTED_ENV_NAME]/scheduled/snapshot/rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]"}}},"restore":{"brOptions":{"checksum":false,"concurrency":256,"metadataDownloadBatchSize":1024,"pitrBatchCount":1024,"pitrBatchSize":67108864,"pitrConcurrency":4096},"cluster":"rp-[REDACTED_ENV_NAME]","gitSha":"6dfedb6291d7cbdb9f6e217e236cead5d0d78179","namespace":"[REDACTED_ENV_NAME]","restoreMode":"pitr","tableFilter":["oyster_production.*","airbed3_production.*","oyster_dyson.*"],"toolImage":"[REDACTED_LONG_ID].dkr.ecr.us-east-1.amazonaws.com/tidb/br:v8.5.1-1fe1967"}}}
  creationTimestamp: "2025-03-31T19:39:18Z"
  generation: 3

## Recent Comments Excerpt

### 2025-04-01T08:26:25.242+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_0833e44fbb892969871553ec1cb784a6) by lark

### 2025-04-01T08:26:53.636+0800 [REDACTED_USER]

This appears to be a small issue but need code fix.  Assign to BR first, please re-assign as appropriate.

### 2025-04-01T10:47:33.600+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_08ec3f1c137f1af6ee990b1e2aee5c5c) by lark

### 2025-04-02T16:26:44.008+0800 [REDACTED_USER]

https://github.com/pingcap/tidb-operator/pull/6135
This issue has been fixed and cherry-picked to 1.6 and 1.5
 
@[REDACTED_USER]
