# GTOC-6792: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6792
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-03-20T22:42:00.000+0800
- Updated: 2025-05-29T00:33:18.504+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER],

I recently performed restore using the DMR 7.6 version and here’s my findings:

The restore was carried out on a 51 TiKV stores (c6id.4xlarge) and a concurrency of 1024. While using the concurrency of 2048, the performance was degraded. 

a) \~30 TB data was restored in 1.1 hour (51 TiKV stores)  
b) TiKV CPU was being throttled for the first 14 mins, after which it was around 50%  
c) Disk write throughput for each store was \~295 MB/s for the fist 14 mins and it settled down to \~130 MB/s for the rest of the duration  
d) Import speed was \~18 GB/s for the first 14 mins and \~13 GB/s for the rest.

I’ve the following questions:

a) The resources of the TiKV instances were only throttled for the first 14 mins. Can you please explain why the drop was observed on CPU and TiKV throughput? 

b) Is there any other patch I can include in v7.6 which can further improve the restoration speed? 

clinic: <custom data-type="smartlink" data-id="id-0">[REDACTED_CLINIC_URL]>

## Recent Comments Excerpt

### 2024-03-20T22:42:01.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 19/Mar/24 6:19 PM
[REDACTED_MEDIA]
Here’s the BR log. 
command used: 
[__command="br restore full"] [ca=/var/lib/normandie/fuse/ca/root] [cert=/var/lib/normandie/fuse/chain/generic] [checksum=false] [concurrency=1024] [key=/var/lib/normandie/fuse/key/generic] [log-file=/var/log/tidb/br.log] [pd="[[REDACTED_ENV_NAME].ec2.pin220.com:2379]"] [s3.region=us-east-1] [send-credentials-to-tikv=false] [storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
I can see the regions are equally split and scattered across all the stores
[REDACTED_MEDIA]

### 2024-03-20T22:42:02.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 19/Mar/24 6:20 PM
Escalate to L3 Information 
[REDACTED_TICKET_ID]

This ticket is reported by 
PingCAP Employee
: Pankaj Choudhary

### 2024-03-21T11:06:13.000+0800 [REDACTED_USER]

For current situation
      I think the download speed at first 14min is due to the size of restore SST Files is large than others. Because of the less download ops and more download duration. which means with the same concurrency but different download file size. the download speed can be different at different time.
For further improvement
From metrics I saw the rewrite table id happened, because the backup table's ID has been occupied by other table existed before. and rewrite would consume more CPU resources and slow down the whole restoration. So build a new cluster with table id allocator to be small enough then, the start a fresh restore could help. And it's better to have this PR 
https://github.com/pingcap/tidb/pull/51737
 to try the best effort to keep the table id from BR perspective.

### 2024-03-28T06:07:00.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 27/Mar/24 10:06 PM

@[REDACTED_USER]
 Hi, had Cheng Luan’s answer above answered the questions?
Cherry-pick PRs of 
https://github.com/pingcap/tidb/pull/51737
  to 6.5, 7.1 and 7.5 are submitted yesterday. But customer [REDACTED_CUSTOMER], and I don't think we cherry-pick to DMR branches normally. From the ticket description I suppose the customer [REDACTED_CUSTOMER]ry?

### 2024-04-11T06:59:03.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 10/Apr/24 10:58 PM

Ran a restore with DM8.0 and the restore speed is quite impressive. 

total-time=35m, Restore Size: 31.5 TB.
[REDACTED_MEDIA]
[REDACTED_MEDIA]
[REDACTED_MEDIA]
