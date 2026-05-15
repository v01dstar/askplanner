# GTOC-8379: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8379
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2026-04-15T09:12:40.206+0800
- Updated: 2026-04-30T16:18:13.961+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

The Ticdc metrics:

[REDACTED_MEDIA]
BR status:

[REDACTED_USER]@[REDACTED_ENV_NAME]:\~$ br log status  
Detail BR log in /tmp/br.log.2026-04-15T00.19.28Z  
● Total 1 Tasks.

> #1 <  
> name: pitr  
> status: ● NORMAL  
> start: 2025-12-13 02:48:31.736 +0000  
> end: 2090-11-18 14:07:45.624 +0000  
> storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]  
> speed(est.): 37822.08 ops/s  
> checkpoint\[global\]: 2026-04-14 21:32:07.076 +0000; gap=2h47m30s

slow region found in TiCDC:

```
[2026/04/15 00:12:27.905 +00:00] [INFO] [subscription_client.go:1055] ["subscription client finds a initialized slow region"] [subscriptionID=46] [slowRegion="{\"RegionID\":8512635,\"ResolvedTs\":[REDACTED_LONG_ID],\"Initialized\":true,\"Created\":\"2026-04-02T21:40:08.964067534Z\"}"]
[2026/04/15 00:12:27.905 +00:00] [INFO] [subscription_client.go:1055] ["subscription client finds a initialized slow region"] [subscriptionID=31] [slowRegion="{\"RegionID\":11029343,\"ResolvedTs\":[REDACTED_LONG_ID],\"Initialized\":true,\"Created\":\"2026-04-02T21:40:03.633839882Z\"}"]
[2026/04/15 00:12:27.906 +00:00] [INFO] [subscription_client.go:1055] ["subscription client finds a initialized slow region"] [subscriptionID=898] [slowRegion="{\"RegionID\":84260935,\"ResolvedTs\":[REDACTED_LONG_ID],\"Initialized\":true,\"Created\":\"2026-04-02T22:10:19.427189432Z\"}"]
[2026/04/15 00:12:28.019 +00:00] [INFO] [gc_service.go:59] ["set gc safepoint for changefeed"] [gcServiceID=cdc_schema_store-keeper-default_node_infra-[REDACTED_ENV_NAME]-0a01eb43_ec2_pin220_com_8300_keyspace_0] [expectedGCSafepoint=[REDACTED_LONG_ID] [actualGCSafepoint=[REDACTED_LONG_ID] [ttl=7200]
```

They are pointing to store 70009316.

## Recent Comments Excerpt

### 2026-04-15T09:15:08.694+0800 [REDACTED_USER]

lag already cleaned after restart tikv node
[REDACTED_MEDIA]

### 2026-04-15T09:15:28.093+0800 [REDACTED_USER]

[REDACTED_USER]@[REDACTED_ENV_NAME]:~$ br log status

Detail BR log in /tmp/br.log.2026-04-15T01.15.13Z

● Total 1 Tasks.
#1 <

              name: pitr

### 2026-04-17T00:20:13.678+0800 [REDACTED_USER]

The checkpoint lag was mainly caused by region 
6484420
 stuck by lock with ts=
[REDACTED_LONG_ID]
TiKV’s resolved-ts logic was stuck on region 6484420 because of rts_cm_min_lock / min_memory_lock at ts=[REDACTED_LONG_ID] in gtoc-8367-tikv.log:734. Right before restart, region 6484420 was still frozen at that same old ts in gtoc-8367-tikv.log:529977, and the issue disappears after Welcome to TiKV at gtoc-8367-tikv.log:529984.

TiKV server metrics show the same result
[REDACTED_MEDIA]

### 2026-04-20T09:13:24.200+0800 [REDACTED_USER]

Another doubt is the server report failure errors, which also recovered after restart the node (not just the TiKV process)
[REDACTED_MEDIA]
There are lots of following logs in the log file of node 
0a096077

{"level":"ERROR","caller":"raft_client.rs:860","message":"wait connect timeout","time":"2026/04/14 23:18:44.982 +00:00","thread_id":83,"addr":"
[REDACTED_ENV_NAME].ec2.pin220.com:20160
","store_id":15644331}

### 2026-04-20T12:00:59.780+0800 [REDACTED_USER]

notified (黄必胜([REDACTED_EMAIL]), om_x100b516e0164c0acc11a894f6b7d015) by lark
