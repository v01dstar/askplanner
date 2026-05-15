# GTOC-6977: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6977
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2024-06-20T21:31:30.000+0800
- Updated: 2025-03-06T18:09:54.526+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB
- Categories: restore-failure, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We tried to backup a specific schema on the Production TiDB to Azure Blob Storage. The backup completed and we are able see the metadata being reflected in Azure Blob Storage Container. However, when we tried to restore it failed and checking the Kubernetes Pod Logs it shows that Restore checksum mismatch. Despite countless time of amending the BR restore.yaml and dropping the schema and restoring also return the same result.

## Recent Comments Excerpt

### 2024-06-24T12:09:03.000+0800 [REDACTED_USER]

It is OK if the client does not have a retry mechanism.

### 2024-06-24T12:20:45.000+0800 [REDACTED_USER]

If you just want to prevent all writes, perhaps you can change the root password during recovery and then change it back after recovery.

### 2024-06-24T15:04:12.000+0800 [REDACTED_USER]

commented by [REDACTED_EMAIL] - 24/Jun/24 7:04 AM

Hi [REDACTED_USER], 

We managed to find a way to restore it. 
Since we can see there are writing operation during restore job, we tried to scale down all the application pods that could be potentially writing data into the TiDB Cluster, only then we tried restoring. It works now. 
[REDACTED_MEDIA]

### 2024-06-24T15:04:32.000+0800 [REDACTED_USER]

commented by [REDACTED_EMAIL] - 24/Jun/24 7:04 AM

Thanks for all the support provided. I believe this ticket can be closed now.

### 2024-06-25T22:18:49.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Jun/24 2:18 PM

hi @[REDACTED_USER] 
I so glad to hear this message. I will close this ticket.
