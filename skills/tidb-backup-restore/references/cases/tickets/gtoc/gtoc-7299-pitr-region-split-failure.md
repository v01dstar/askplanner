# GTOC-7299: PITR region split failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7299
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-12-11T10:42:33.000+0800
- Updated: 2025-03-07T10:55:20.189+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, tikv-data-path, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We are running a PIT restore that is erroring due to TiKV disk full even though the cluster [REDACTED_CLUSTER] has sufficient disk space.

* Based on the timestamp we are trying to restore to and the source cluster [REDACTED_CLUSTER], we know the restore should require \~11TB of disk space

* The target cluster has 15 TiKV nodes, each w/ 1TB data volumes

* This target cluster has a slightly different topology than the source cluster (which only has 12 nodes)

* At the point the restore failed, 3 TiKVs have no available space (tikv-2-1a, tikv-1-1b, and tikv-3-1e), while the remaining tikvs have 400+GB of available space

* Disk full error occurs during the log apply phase of restore

We understand that snapshot restore will split/scatter regions across all tikvs of the cluster. Is the resulting imbalance of data across the TiKVs due to the different cluster [REDACTED_CLUSTER] of the source and restore cluster? Or is it due to skew in our workload’s writes after the snapshot, where our KV applies target a subset of regions/TiKVs specifically?

If our workload is indeed skewing writes to a subset of regions/TiKVs, how can we successfully complete the restore in this case? Is the only possibility to increase the volume size of the TiKVs that are full?

I’ve attached restore CR, restore logs, and Clinic metrics

## Recent Comments Excerpt

### 2024-12-11T10:44:24.000+0800 [REDACTED_USER]

Clinic 
[REDACTED_CLINIC_URL]

### 2024-12-11T10:45:22.000+0800 [REDACTED_USER]

[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2024-12-18T17:56:25.000+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), ) by lark

### 2024-12-18T17:59:14.000+0800 [REDACTED_USER]

it's similar to a known issue 
https://github.com/tikv/tikv/issues/17508. 
log compaction optimization can mitigate the write hot spot by scattering ahead of restore.

### 2025-03-02T11:06:20.156+0800 [REDACTED_USER]

@[REDACTED_USER]
 This ticket can be closed now. Thanks.
