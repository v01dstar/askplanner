# GTOC-6864: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6864
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-04-22T09:45:36.000+0800
- Updated: 2025-03-06T18:13:46.713+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, restore-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER],

We were wondering if there are any tricks or tips to speed up BR restore.

Currently, we’re testing `br restore` against one of our larger databases (\~7TB) and it’s taking us 6-6.5 hours to restore. We also tested against a `~2.1TB` database and it took us \~4-4.5 hours to restore. Below, I’ve included a table of some of our results as more of a data point.

We restored them onto clusters with:

* 3 TiDBs (Each have 8 vCPUs, 16 GiB Mem)
* 3 PDs (Each have 4 vCPUs, 8 GiB Mem)
* 6 TiKVs (Each have 8 vCPUs, 64 GiB Mem)

When we restore, the clusters should be empty.

A few questions:

* In this [doc](https://docs.pingcap.com/tidb/stable/[REDACTED_RESOURCE_NAME]#some-tips), I see that it mentions that `BR uses resources of the target cluster as much as possible` . Does this mean that the only way to increase the speed of BR restore is to increase the resource of the target cluster? 
* When I restore, I notice that the data is imported into the cluster [REDACTED_CLUSTER] a few hours (i.e. the TiKV data size dashboard increases) and then it spends almost as much time doing some post processing. Is there any way to speed up one of these parts vs the other? Are there any parts of the post processing that can be skipped? (I attached a screenshot below with an example of what this looks like in metrics).

| Time of Execution | Data Size | Avg Speed | Total Time | Import Job Characteristics |
| --- | --- | --- | --- | --- |
| 2024-04-17T21.47.32Z | \~3TB | 359.4MB/s | 4h10m34s | Restore `result_events` Empty Cluster 8 Import Threads Rate Limit: 100MiB Switch-mode-interval: 15m /tmp/br.log.2024-04-17T21.47.32Z |
| 2024-04-17T23.48.14Z | \~7TB | 435.8MB/s | 6h29m27s | Restore `data_deletion_production` Empty Cluster 4 import Threads Rate Limit: 100MiB Switch-mode-interval:15m /tmp/br.log.2024-04-17T23.48.14Z |
| 2024-04-18T04.12.04Z | \~7TB | 470.7MB/s | 6h0m33s | Restore `data_deletion_production` Empty Cluster 8 import Threads Rate Limit: 150MiB Switch-mode-interval: (default, 5m) /tmp/br.log.2024-04-18T04.12.04Z |
| 2024-04-18T06.54.34Z | \~7TB | 438.4MB/s | 6h27m10s | Restore `data_deletion_production` Empty Cluster 4 import Threads Rate Limit: 200MiB Switch-mode-interval: (default, 5m) /tmp/br.log.2024-04-18T06.54.34Z |
| 2024-04-18T18.13.02Z | \~7TB | 467.1MB/s | 6h3m23s | Restore `data_deletion_production` Empty Cluster 8 import Threads Rate Limit: None Switch-mode-interval: (default, 5m) /tmp/br.log.2024-04-18T18.13.02Z |
| 2024-04-18T18.56.45Z | \~7TB | 488.3MB/s | 5h47m35s | Restore `data_deletion_production` Empty Cluster 8 import Threads Rate Limit: None Switch-mode-interval: (default, 5m) /tmp/br.log.2024-04-18T18.56.45Z |
| 2024-04-19T01.02.56Z | \~2.1TB | 510.9MB/s | 4h18m13s | Restore `transaction_changeset_production` Empty Cluster 8 import Threads Rate Limit: None Switch-mode-interval: (default, 5m) /tmp/br.log.2024-04-19T01.02.56Z |

## Recent Comments Excerpt

### 2024-04-23T03:50:59.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 22/Apr/24 7:50 PM

Okay, I will test with restoring onto a brand new cluster. (I’ll just 
tiup cluster [REDACTED_CLUSTER]
 one of our test clusters, 
tiup cluster [REDACTED_CLUSTER]
, and try again).
Also another BR related question - does the BR backup command backup all data from the moment the

### 2024-04-23T04:31:04.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 22/Apr/24 8:30 PM

Hi Andrew:
Please refer:
https://docs.pingcap.com/tidb/v6.5/br-snapshot-manual#back-up-cluster-snapshots
 
There is even a 
--backupts

### 2024-04-30T01:03:01.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/Apr/24 5:02 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-05-03T01:03:16.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/May/24 5:02 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-05-06T01:02:24.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 05/May/24 5:01 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
