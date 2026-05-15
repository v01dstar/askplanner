# GTOC-8008: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8008
- Status: Todo
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-11-04T10:30:51.709+0800
- Updated: 2025-11-24T06:23:10.319+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We have tested PITR on a 10GB database. We’ve increased TiKV storage from 20GB to 50GB before running the tests. After running PITR maybe twice, even though we deleted the PITR restore jobs, the disk storage is still being consumed:

```
kubectl exec [REDACTED_RESOURCE_NAME] -n [REDACTED_ENV_NAME] -c tikv -- df -h                                       
 /dev/nvme6n1     50G   37G   13G  75% /var/lib/tikv                                                                
 /dev/nvme4n1     30G   12G   18G  40% /var/lib/raft                                                                
 /dev/nvme1n1     20G  1.7G   18G   9% /var/lib/wal
```

```
# Even worse on tikv-2:                                                                                            
 kubectl exec [REDACTED_RESOURCE_NAME] -n [REDACTED_ENV_NAME] -c tikv -- df -h                                       
 /dev/nvme6n1     50G   50G     0 100% /var/lib/tikv  # COMPLETELY FULL                                             
 /dev/nvme8n1     30G   12G   18G  40% /var/lib/raft                                                                
 /dev/nvme7n1     20G  596M   19G   3% /var/lib/wal
```

We have run the clean up manually as suggested by pingCap: 

```
nohup /tikv-ctl --pd http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME]:2379 compact-cluster -d kv -c write --threads 8 >> /var/lib/tikv/nohup.out 2>&1 &
nohup /tikv-ctl --pd http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME]:2379 compact-cluster -d kv -c default --threads 8 --bottommost=force >> /var/lib/tikv/nohup.out 2>&1 &
```

However, after the job finished we have: 

```
tail -f /var/lib/tikv/nohup.out

## Recent Comments Excerpt

### 2025-11-06T07:11:18.183+0800 [REDACTED_USER]

[REDACTED_MEDIA]
 
[REDACTED_MEDIA]
 
[REDACTED_MEDIA]
 
[REDACTED_MEDIA]

### 2025-11-06T07:11:33.486+0800 [REDACTED_USER]

I’ve started PITR perf tests on Oct 29. And I did few runs with 10GB DB. The tikv-2 went into disk full on Oct 30.
It’s almost impossible for me to download the log for tikv nodes as there are so many logs on splunk and splunk doesn’t let do it. Based on the provided information above is there any smaller time window you are interested in?

### 2025-11-06T08:52:51.504+0800 [REDACTED_USER]

Please also review clinic from the time of restore test: 
[REDACTED_CLINIC_URL]

### 2025-11-07T08:34:53.707+0800 [REDACTED_USER]

summary:
In a TiKV cluster with three replicas and three tikvs, 
repeated PITR (Point-in-Time Recovery) restore and drop database operations
 caused uneven physical space usage among the TiKV nodes.
Detailed analysis:
After multiple rounds of 
restore
 and

### 2025-11-24T06:23:10.319+0800 [REDACTED_USER]

[REDACTED_MEDIA]
Customer [REDACTED_CUSTOMER] free-space chart:
The cluster has 
12 TiKV nodes
, each with 
75–125 GB of free space
 before PITR.
Customer
