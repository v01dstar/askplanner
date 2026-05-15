# GTOC-7762: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7762
- Status: Resolved
- Resolution: Done
- Priority: P0
- Issue type: Incident
- Created: 2025-07-12T03:11:40.671+0800
- Updated: 2025-07-15T04:56:28.243+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

All of our restores (driven by E2E tests, very small amounts of data just to ensure we are operationally sound still) are failing only in eu-central-1. This isn’t an incident **yet**, but can very easily turn into one if we get a data residency request into this cluster, so this is a very big deal. Attached are logs from a restore that has been stuck for 30 minutes so far.

## Recent Comments Excerpt

### 2025-07-12T03:13:42.191+0800 [REDACTED_USER]

This one started 7 July
% k -n [REDACTED_ENV_NAME] describe pod/restore-adhoc-24bd6bc2544959660c1f7d9980e3894172c112ccdd594v9fk
Name:             [REDACTED_RESOURCE_NAME]
Namespace:        [REDACTED_NAMESPACE]
Priority:         0
Service Account:  [REDACTED_RESOURCE_NAME]
Node:             ip-10-20-174-174.eu-central-1.compute.internal/[REDACTED_IP]
Start Time:       Mon, 07 Jul 2025 21:13:47 -0700

### 2025-07-12T03:14:19.467+0800 [REDACTED_USER]

There is also 1 single restore pod that failed with this error: 
The node was low on resource: ephemeral-storage. Threshold quantity: 41585984107, available: 39209744Ki. Container restore was using 548Ki, request is 0, has larger consumption of ephemeral-storage.

### 2025-07-12T03:33:48.437+0800 [REDACTED_USER]

For clinic please use 
[REDACTED_CLINIC_URL]

### 2025-07-13T01:36:26.311+0800 [REDACTED_USER]

This ticket can be closed now. Thanks for all the help.

### 2025-07-15T04:56:28.243+0800 [REDACTED_USER]

From log we can see
I0711 17:58:36.777300       9 restore.go:179] [2025/07/11 17:58:36.777 +00:00] [INFO] [locking.go:292] ["Encountered lock, will retry then."] [error="there is something about the lock: locked, meta = Locked(at: 2025-07-07 11:57:07, host: restore-adhoc-3d0d630c228b91edc18ab79a39f8e58121e76f32a5f4l9h29, pid: 25, hint: AppendMigration): during initial check: there is conflict file v1/LOCK.WRIT; there is conflict file v1/LOCK.WRIT"] [path=v1/LOCK] [retry-after=5.183s]
This could due to a previous restore job terminated abnormally, leaving a lock file 
v1/LOCK.WRIT
 on the external storage   in the backup. Right now we don’t have any tools to cleanup this lock file. You can locate the lock file in the backup and manually remove it.
