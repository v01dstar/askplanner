# GTOC-7044: PITR fails with [BR:restore:ErrRestoreNotFreshCluster]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7044
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-08-01T15:59:44.000+0800
- Updated: 2025-03-06T18:07:59.738+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, storage-credential, tikv-data-path, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

two question from customer

1. We were planning to use the adhoc backup (with db filter) and restore to move dbs from one TiDb cluster to another. However, when testing that, we figured that restore is not allowed for clusters for which log backup is running. Since destination clusters would have log backup running, which we don't want to turn off (in order to meet our RPO), we are wondering if there is a workaround without stopping log backup. `Error: failed to check task exists: log backup task is running: [REDACTED_RESOURCE_NAME], please stop the task before restore` 
2. Attempting to restore into the cluster [REDACTED_CLUSTER] log backups running results in `user db/tables: quarantinedb1, table2: [BR:restore:ErrRestoreNotFreshCluster]cluster is not fresh`

## Recent Comments Excerpt

### 2024-08-01T15:59:54.000+0800 [REDACTED_USER]

notified (刘瀚阳([REDACTED_EMAIL]), ) by lark

### 2024-08-01T16:02:29.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark

### 2024-08-01T16:16:47.000+0800 [REDACTED_USER]

This is because log backup cannot be aware of any ingest SSTs. so log backup cannot properly handle `checkpointTS` without touch ingest SSTs. log backup only can handle txn data for now. so the workaround is to use a txn write tool(like dumpling) to restore these data.
Restore full assumed the cluster is empty and will use full resources to restore all backup data. this will impact other workloads on the cluster. if you still need to restore then you can use a filter parameter to specify the tables in backup data that needed to be restored.
./br restore full --filter "
.
" will force restore all backup data and skip empty cluster [REDACTED_CLUSTER]
