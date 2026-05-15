# GTOC-7891: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7891
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-09-08T09:05:07.508+0800
- Updated: 2025-09-15T09:48:33.373+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

### Problem [REDACTED_USER]

Point-in-Time Restore (PITR) does not work under TiDB Operator v1.6.3. When creating a `Restore` custom resource with `restoreMode: pitr`, no corresponding Kubernetes Job is created to perform the restore. Snapshot restores, however, continue to work as expected.

---

### Details [REDACTED_USER]

* **Restore CR Example**

    * Kind: `Restore`
    * Mode: `pitr`
    * Tool image: `docker.io/pingcap/br:v8.5.0-20250730-6bbe4cc`
    * Target cluster: `basic` in namespace `tidb-cluster`
    * S3 bucket: `michael-s3-us-east-2` (region `us-east-2`)
    * PITR timestamp: `2025-09-06T18:05:00+00:00`
    * Full backup and log backup prefixes provided.
    
* **Observed Behavior**

    * After applying the Restore CR, **no restore Job is created** in Kubernetes.
    * Operator logs show repeating error messages:
    
        ```
        sync failed modify volumes for tidb-cluster/[REDACTED_CLUSTER]:tikv failed: component phase is not Normal, requeuing
        
        ```
    * Interleaved with logs indicating successful StatefulSet updates and messages such as:

## Recent Comments Excerpt

### 2025-09-08T09:05:21.582+0800 [REDACTED_USER]

notified (刘金龙([REDACTED_EMAIL]), om_x100b44d6f3c3bcb80f2859cb57786ca) by lark

### 2025-09-08T09:07:17.802+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), om_x100b44d68a9c28d00ec7a4218f8c483) by lark

### 2025-09-08T09:17:52.858+0800 [REDACTED_USER]

This is pitr CR. It works in operator 1.6.1, but fails in 1.6.3:
kubectl -n tidb-cluster [REDACTED_CLUSTER] restore [REDACTED_RESOURCE_NAME]
cat << EOF | kubectl apply -f -
apiVersion: pingcap.com/v1alpha1
kind: Restore
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]

### 2025-09-08T17:18:53.052+0800 [REDACTED_USER]

It’s a bug when doing pitr and tikv config file is empty. this bug is introduces in v1.6.3.

the details can be found in github issue.

https://github.com/pingcap/tidb-operator/issues/6434

### 2025-09-15T09:48:33.373+0800 [REDACTED_USER]

This ticket can be closed now.
