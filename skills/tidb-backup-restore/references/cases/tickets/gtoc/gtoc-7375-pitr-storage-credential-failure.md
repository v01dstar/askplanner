# GTOC-7375: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7375
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-01-30T05:02:09.736+0800
- Updated: 2025-03-28T15:18:04.057+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

A snapshot backup is failing consistently and the logs do not give good reason as to why. Here is the `Backup` CR manifest:

```
apiVersion: pingcap.com/v1alpha1
kind: Backup
metadata:
  creationTimestamp: "2025-01-28T01:53:06Z"
  finalizers:
  - tidb.pingcap.com/backup-protection
  generation: 20
  name: [REDACTED_RESOURCE_NAME][REDACTED_LONG_ID]
  namespace: [REDACTED_NAMESPACE]
  resourceVersion: "436292072"
  uid: [REDACTED_UUID]
spec:
  backoffRetryPolicy:
    maxRetryTimes: 2
    minRetryDuration: 300s
    retryTimeout: 30m
  backupMode: snapshot
  backupType: full
  br:
    cluster: [REDACTED_CLUSTER]
    clusterNamespace: [REDACTED_NAMESPACE]
    logLevel: info
    sendCredToTikv: false
  calcSizeLevel: all
  cleanPolicy: Delete

## Recent Comments Excerpt

### 2025-03-18T20:13:19.661+0800 [REDACTED_USER]

This is time break down:
50mins for restore create all dbs (without tables)
2:30mins to create all tables in previously created dbs
“update metas” took 2:40mins
6 hours total ( log backup off , checksums off)

### 2025-03-18T20:27:02.600+0800 [REDACTED_USER]

I think after 
[REDACTED_INTERNAL_URL]
 is delivered, BR may be able to use this feature. But we also need to look for other ways of improvement.

### 2025-03-19T12:57:30.778+0800 [REDACTED_USER]

@[REDACTED_USER]
 The table creation performance meeted the prior expectations. FD2199 is aim to improve the performance of “add column” from 840/min to 6000/min. Is there a new goal for the performance of db/table creation？

### 2025-03-28T09:44:11.370+0800 [REDACTED_USER]

@[REDACTED_USER]
 can we close this ticket and discuss restore rto in 
https://pingcap-ticket.atlassian.net/browse/GTOC-7475
 ?

### 2025-03-28T09:51:33.653+0800 [REDACTED_USER]

@[REDACTED_USER]
 feel free to close this ticket.
Thanks.
