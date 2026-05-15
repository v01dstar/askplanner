# GTOC-6939: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6939
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-05-24T17:41:16.000+0800
- Updated: 2025-03-06T18:11:18.002+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiDB Operator
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, restore-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: change-p2

## Symptom / Description Excerpt

Hi, We encountered an issue while using PITR, PITR restore works with only FULL backup, meaning we need to provide FULL backup pointer and restoredTS in the PITR restore mode. but the same will not work with Incremental backup.

Here are the steps

We have 1 full and incremental backup from the cluster and also PITR log backup is enabled. 

We know that Full + PITR log restore works, but what we want to know that is, does the Full restore and incremental + PITR log restore in PITR mode works? adding steps below

1. Restore full backup (one restore object)
2. Restore Incr + PITR log apply (one restore object) (`prod__297__tidb__2024-05-23__14-20-11__incr` in the manifest is incremental backup) 

```
---
apiVersion: pingcap.com/v1alpha1
kind: Restore
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
  labels:
    tidb-operator: v1.5.1
  annotations:
    sidecar.istio.io/inject: "false"
spec:
  podSecurityContext:
    runAsUser: 1000
    runAsGroup: 3000
    runAsNonRoot: true
  toolImage: "edge.fkinternal.com/docker-external/pingcap/br:v7.5.1"

## Recent Comments Excerpt

### 2024-05-31T13:26:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 31/May/24 5:26 AM

Raised the PR - 
https://github.com/pingcap/tidb-operator/issues/5657
 

RD(Eason & team) is working on it

### 2024-06-06T13:28:25.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Jun/24 5:28 AM

Hi [REDACTED_USER],
As discussed yesterday , please find the list of limitation on incremental backup 
https://docs.pingcap.com/tidb/dev/br-incremental-guide#limitations

### 2024-06-06T13:28:55.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Jun/24 5:28 AM
[REDACTED_MEDIA]

### 2024-06-06T13:55:00.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Jun/24 5:54 AM

Thanks Jana,
I have once question related to Stoping PITR log backup.
All our setup is on K8s, what is the process we should follow to stop the pitr log backup.
Can we just delete the PITR backups resource?
or 
We should first issue stop to running backups resource and then delete the backup resource ?

### 2024-07-02T14:59:27.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/Jul/24 6:59 AM

We have just discussed with Sachin about how to provide the patched image to Flipkart.
Currently Flipkart hosts a private Docker registry, however under their current architecture, the part that mirrors DockerHub (
edge.fkinternal.com/docker-external/«namespace»/«repository»
) has to be read-only.
Therefore, they would like us to create a pre-release tag of 
pingcap/tidb-operator
