# GTOC-8219: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8219
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2026-02-11T13:02:59.210+0800
- Updated: 2026-02-19T10:30:34.552+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB Operator
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

**Background:**

Customer [REDACTED_CUSTOMER],   
Environment: [REDACTED_ENV_NAME]

Affected Versions: v7.5.1

Customer [REDACTED_CUSTOMER]**PersistentVolume full** condition for cluster `[REDACTED_ENV_NAME]`.  
PVC `[REDACTED_RESOURCE_NAME]` (namespace: `[REDACTED_ENV_NAME]`) shows **0% free space**.

Customer [REDACTED_CUSTOMER]`spec.resources.requests.storage`, but later clarified that this was a misstatement.  
The actual change was made under:

```
spec.initializer.storage
```

However, despite increasing storage from **94Gi to 150Gi**, the updated storage value was **not picked up**, and the corresponding pod remains in **Terminating** state.

### Current [REDACTED_USER]

* Storage expansion does not appear to take effect.
* Pod failed to recover and is stuck in Terminating.

### Request [REDACTED_USER]

Kindly assist to:

## Recent Comments Excerpt

### 2026-02-11T13:26:46.331+0800 [REDACTED_USER]

notified (江华禧([REDACTED_EMAIL]), om_x100b57f57f91f0a4c2a532a9c18dd09) by lark

### 2026-02-11T15:02:40.393+0800 [REDACTED_USER]

1. Correct Method for Storage Expansion
The correct field in the TidbMonitor CR is 
spec.storage
.
But updating this field will NOT automatically resize the existing PVCs, because the TidbMonitor controller does not have the PVC

resizing logic implemented, and Kubernetes StatefulSet volumeClaimTemplates are immutable.
You must manually resize the PVC object using kubectl and then update

### 2026-02-11T15:37:02.559+0800 [REDACTED_USER]

Resolution Plan
Please follow these steps in order to recover the pod and expand storage.
Step 1: Manually Expand the PVC
Since the disk is full, we must expand it first. Ensure your StorageClass supports volume expansion (allowVolumeExpansion: true).Edit the PVC to increase storage to 150Gi:
kubectl edit pvc [REDACTED_RESOURCE_NAME] -n [REDACTED_ENV_NAME]

# Update the spec.resources.requests.storage field:
spec:

### 2026-02-12T09:44:45.273+0800 [REDACTED_USER]

@[REDACTED_USER]
 Followed the above resolution steps, It looks like the customer [REDACTED_CUSTOMER]hows the updated 150Gi capacity.
kubectl get pods --context=prod-hyd-2 -n [REDACTED_ENV_NAME] | grep [REDACTED_RESOURCE_NAME]
[REDACTED_RESOURCE_NAME]                      3/3     Running   0               6m25s
kubectl get pvc [REDACTED_RESOURCE_NAME] -n [REDACTED_ENV_NAME]
NAME                                       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS          VOLUMEATTRIBUTESCLASS   AGE
[REDACTED_RESOURCE_NAME]   Bound    pvc-[REDACTED_UUID]   150Gi      RWO            ebs-premium-1a-ext4   <unset>                 51d

### 2026-02-19T10:30:34.552+0800 [REDACTED_USER]

The issue has resolved, we can proceed to close ticket. Thank you for your effort!
