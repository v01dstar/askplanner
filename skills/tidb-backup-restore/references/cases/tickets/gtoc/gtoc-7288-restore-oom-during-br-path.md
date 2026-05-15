# GTOC-7288: Restore OOM during BR path

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7288
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-12-04T07:35:00.000+0800
- Updated: 2025-03-20T10:45:49.854+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: restore-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We are performing restore of a TiDB cluster on a standby cluster.   
Here’s the source cluster [REDACTED_CLUSTER]:

Size: **175.0 TB**  
Number of regions: 1.5 Million

 

The cluster was able to split and scatter the region on the target TiDB cluster, but during the ingestion of the SST files the GR process crashed the PD host. The instance type for the PD hots:  
 c7i.16xlarge

[REDACTED_MEDIA]
 

{{}}

```java
sudo grep -i 'killed process' /var/log/syslog Dec 3 22:25:11 [REDACTED_ENV_NAME] kernel: Out of memory: Killed process 6956 (br) total-vm:80485916kB, anon-rss:72375208kB, file-rss:0kB, shmem-rss:0kB, UID:1000 pgtables:145188kB oom_score_adj:0
```

{{}}

## Recent Comments Excerpt

### 2024-12-04T18:40:26.000+0800 [REDACTED_USER]

Phase update:
Summary: Further investigation is needed. Please provide complete PD logs, TiKV logs, and monitoring data from each component for a comprehensive analysis. The possibility of this issue reoccurring after the separate deployment of BR cannot be ruled out.
 
Known issues
The strange `remove-orphan-peer` operator, which normally should not occur, only appears when there are excess peers. BR has an operation called `scatter-region`, which generates a combination of `add-peer` and `remove-peer`, but they always appear together. Generally, there should not be a situation where the `scatter-region` (add-peer) operation causes PD to mistakenly treat the newly added peer as an orphan peer. However, in special cases, such as when the scatter region fails or times out, this situation may occur. We still suspect that there is an unknown bug involved.
Although there was an OOM issue later on, there were also service interruptions at the first two time points, and corresponding error logs are present in the BR logs. We need the PD logs for the entire period.  
[REDACTED_MEDIA]
At 5:44, the resource usage of PD spiked sharply, with memory increasing nearly tenfold and the number of goroutines rising by hundreds of times. This moment coincided with BR waiting for the scatter region to finish and the start of the import process. It is suspected that during the import, some type of request (possibly from TiKV) triggered a flood of requests to PD, which, for unknown reasons, was unable to process them normally. This led to a backlog of requests, a rapid increase in resource usage, and ultimately resulted in an OOM error.

### 2024-12-04T19:22:46.000+0800 [REDACTED_USER]

The PD heartbeat has many errors, performs very poorly, and the timing is completely synchronized. This may be the root cause, and I will continue to investigate in this direction.
By the way, TiDB has released a series of 
optimizations
 for heartbeat in version 8.2, specifically targeting scenarios with massive regions, and these optimizations have been thoroughly tested. If user is conducting tests, it is strongly recommended to use version 8.2 or higher.
[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2024-12-12T11:57:29.000+0800 [REDACTED_USER]

Conclusion: The PD crash was caused by the enormous number of scan region requests from BR.

 

Analysis process: # 

The time points of the spikes in ScanRegion and PD memory/goroutines correspond to each other.
[REDACTED_MEDIA]

### 2024-12-17T11:15:09.000+0800 [REDACTED_USER]

If there are no further questions, I will close this issue.

### 2024-12-18T01:40:26.000+0800 [REDACTED_USER]

Yes, the ticket can be closed. Thanks!
