# GTOC-7495: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7495
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2025-03-27T02:44:33.134+0800
- Updated: 2025-04-23T14:27:12.770+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiDB Operator
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We have a log backup orchestrated by a backupschedule on our full-shadow cluster w/ 7d retention. However, looking in the log backup bucket, I see historical logs going backup 10+ days. In addition, I observe a TSO of [REDACTED_LONG_ID] (2025-03-13T06:05:21Z) in the v1_stream_trancate_safepoint.txt file.

We do observe snapshot backups from the schedule being properly cleaned up, just not logs.

I’ve attached the backupschedule and log backup CRs, as well as recent logs from tidb-operator from AZ 1a (the zone that the log backup object is in)

## Recent Comments Excerpt

### 2025-04-03T15:54:50.909+0800 [REDACTED_USER]

backup_tracker is a tracker against all backups of all namespaces across the whole cluster. See code 
https://github.com/pingcap/tidb-operator/blob/639482c0d2b92561b274bcc0c58df47716776103/pkg/backup/backup/backup_tracker.go#L80
 .

### 2025-04-05T01:01:10.842+0800 [REDACTED_USER]

Update from Customer : 
=====
The backup tracker was designed to monitor backups across all namespaces. Therefore, requiring cluster-scoped permissions does make sense in this context.
our deployment model deploys multiple tidb clusters in a single cluster, each w/ independent upgrade/rollout/deploy, so we want to manage namespace-specific backup resources
has this always been the case for log backup management? this is possible as this is the first time we are using a retention period for log backup
however we have previously used backup schedule retention for our EBS and logical snapshot backups. with the same permissions, we observe our logical and EBS snapshot backups both cleaned successfully. why do those cleanups succeed (w/out cluster [REDACTED_CLUSTER]), while log cleanup does not?
We can either adjust the permissions or consider updating the code if a more restricted scope is preferred.
yes, we’d like to update the operator to not require these permissions for our use-case, and only manage namespace-scoped log backups

### 2025-04-05T01:02:31.662+0800 [REDACTED_USER]

@[REDACTED_USER]
 As discussed, this will require a code change. Could you please provide an ETA so we can update the customer [REDACTED_CUSTOMER]?
Thanks
Aman

### 2025-04-23T14:20:53.755+0800 [REDACTED_USER]

fixed in 
https://github.com/pingcap/tidb-operator/pull/6160

### 2025-04-23T14:27:12.736+0800 [REDACTED_USER]

N/A
