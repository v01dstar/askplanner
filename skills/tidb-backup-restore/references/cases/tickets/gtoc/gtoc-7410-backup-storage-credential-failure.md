# GTOC-7410: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7410
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2025-02-20T08:56:20.092+0800
- Updated: 2025-03-06T17:37:22.547+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We have a cluster with scheduled EBS snapshot backups. Recently, due to a misconfiguration on the cluster we ended up with an invalid EBS snapshot data plane backup.

```
$ kubectl --context m-[REDACTED_ENV_NAME] -n [REDACTED_ENV_NAME] get bk fed-skd-2025-02-19t02-00-00 -o yaml | yq .status
status:
  conditions:
  - lastTransitionTime: "2025-02-19T02:00:26Z"
    message: not support backup TiDB cluster with no tikv replica
    reason: InvalidSpec
    status: "True"
    type: Invalid
  phase: Invalid
  timeCompleted: null
  timeStarted: null
ttlSecondsAfterFinished: 3600
```

However, what we notice is that even though the data plane backup is invalid, this is not a terminal status (ex. failed or complete) and the overarching volumebackup is still running:

```
kubectl --context m-[REDACTED_ENV_NAME] -n [REDACTED_ENV_NAME] get vbk skd-2025-02-19t02-00-00 -o yaml
apiVersion: federation.pingcap.com/v1alpha1
kind: VolumeBackup
metadata:
  annotations:
    artifact.spinnaker.io/location: [REDACTED_ENV_NAME]
    artifact.spinnaker.io/name: skd
    artifact.spinnaker.io/type: kubernetes/VolumeBackupSchedule.federation.pingcap.com

## Recent Comments Excerpt

### 2025-02-20T18:20:53.719+0800 [REDACTED_USER]

please ask michael to open a github issue to tidb operator repo.  We will work on the fix.

### 2025-02-21T05:18:43.267+0800 [REDACTED_USER]

notified (张建伟([REDACTED_EMAIL]), ) by lark
