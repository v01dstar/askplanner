# GTOC-7775: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7775
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-07-16T23:44:18.568+0800
- Updated: 2025-07-28T14:11:21.919+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR, TiDB Operator
- Categories: storage-credential, tikv-data-path, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

The customer [REDACTED_CUSTOMER]hen trying EBS restore:

We recently performed an EBS restore that failed due to a misconfiguration issue (the name and resulting job name exceeded the k8s 63 char limit). However, we did not observe the overall restore process fail. Instead, we observed tidb-operator continue to retry EBS volume creation from snapshot in a loop, resulting in an error `pvc [REDACTED_ENV_NAME]/[REDACTED_ENV_NAME] already exists, and has different volume. please remove it carefully to continue volume restore process`. This process repeated continuously during tidb-operator reconciliation, causing many volumes to be created (and then leaked).

I’ve attached tidb-operator logs from the restore as well as the CR for the data plan restore in 1a.

## Recent Comments Excerpt

### 2025-07-16T23:44:33.535+0800 [REDACTED_USER]

notified (吴强([REDACTED_EMAIL]), om_x100b4848c0c0c0980f26dc028d211db) by lark

### 2025-07-17T10:15:21.569+0800 [REDACTED_USER]

notified (王乐([REDACTED_EMAIL]), om_x100b48b1854e253c0f193239c2ed7da) by lark

### 2025-07-17T11:46:58.054+0800 [REDACTED_USER]

I think that maybe there are PVCs with same name already existing before creating the restore. From the log, the first pvc that encountered “pvc already exists” error is [REDACTED_ENV_NAME], and its corresponding pv is pvc-[REDACTED_UUID]. Please help to check if the pvc [REDACTED_ENV_NAME] and the pv pvc-[REDACTED_UUID] was created before the restore.
In addition, after check codes, there should be no duplicate pv was created, and the duplicate pv means multiple PVs with same volume id. You can find logs with keyword “skip creating pv”.
So you should delete all existing conflict PVCs and corresponding PVs and reduce the restore name length. Then create the volume restore again.
