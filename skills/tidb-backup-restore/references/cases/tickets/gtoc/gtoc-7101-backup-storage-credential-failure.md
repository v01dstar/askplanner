# GTOC-7101: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7101
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-08-28T16:25:30.000+0800
- Updated: 2025-03-06T18:02:54.713+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: storage-credential, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

I’ve noticed that our prod cluster [REDACTED_CLUSTER] a multiple backup in parallel. As a result after 3 hours (we schedule backups every 30 minutes), we had 5 pending CreateSnapshot requests and starting getting `ConcurrentSnapshotLimitExceeded: Maximum allowed in-progress snapshots for a single volume exceeded.\n\tstatus code: 400` errors.

My understanding that TiDB should not trigger backup if the previous one is not completed yet.

To remind we run federated manager in zone A, and backup job in zone A failed pretty quickly, while in zone C it is stuck and then overlapped at the end. I’m attaching logs for 5 overlapping backup jobs in zone C as well as logs for federated backup manager in zone A

 

 

please assign to <custom data-type="mention" data-id="id-0">@[REDACTED_USER] wan</custom> thanks

## Recent Comments Excerpt

### 2024-08-28T16:25:44.000+0800 [REDACTED_USER]

notified (梁宇彤([REDACTED_EMAIL]), ) by lark

### 2024-08-28T16:26:33.000+0800 [REDACTED_USER]

notified (张建伟([REDACTED_EMAIL]), ) by lark

### 2024-08-28T16:59:22.000+0800 [REDACTED_USER]

From the federation-manager log, we can see volume backup `[REDACTED_ENV_NAME]/fed-skd-2024-08-28t01-35-00` is marked failed at 01:38:55 due to backup member at a-ea1-us failed. But backup member at c-ea1-us didn't exit until 03:43:23.
In between volume backups like fed-skd-2024-08-28t02-35-00 were scheduled because fed-skd-2024-08-28t01-35-00 is marked as failed.
EBS snapshot backup schedule logic needs to make a change. Volume backup should not be marked failed right away at any backup member failed.  Instead, volume backup can be marked failed only when all backup members run complete (either failed or complete), and some member failed.  Track issue is opened 
https://github.com/pingcap/tidb-operator/issues/5725
btw，we see create snapshot panic in the log. please apply pr 
https://github.com/pingcap/tidb/pull/54712
 to get mitigation.
