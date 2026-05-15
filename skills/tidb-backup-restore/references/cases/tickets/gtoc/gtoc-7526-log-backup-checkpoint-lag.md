# GTOC-7526: Log backup checkpoint lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7526
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-04-15T08:03:30.338+0800
- Updated: 2025-05-12T18:54:27.903+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

**Problem Statement**

We’re validating log flush feature behavior, and observe improvement in the checkpoint lag. However, log backup checkpoint is still lagging above 5minute mark (our SLO) during the rolling restart of TiKV.

**Observations (arbitrary example)**

Setup: 8.5.1 cluster with log backup job enabled; we initiate a rolling restart of tikv statefulset and observe lag jumping above 5 minutes.

We observe that log flush itself is working successfully, logs are being flushed. Stopped node has not leader regions before the eviction. Below are corresponding controller log record and tikv log record:

```
#tidb-controller logs

I0327 18:36:40.539853       1 tikv_upgrader.go:243] evictLeaderBeforeUpgrade: for tikv pod [REDACTED_ENV_NAME]/rp-[REDACTED_ENV_NAME]: leader count is 0, so ready to upgrade, triggering force flush when there are some log backup tasks
# Vlad: second attempt yields a warning because tikv started shutdown procedure
I0327 18:36:46.839249       1 tikv_upgrader.go:243] evictLeaderBeforeUpgrade: for tikv pod [REDACTED_ENV_NAME]/rp-[REDACTED_ENV_NAME]: leader count is 0, so ready to upgrade, triggering force flush when there are some log backup tasks
W0327 18:36:46.840852       1 tikv_upgrader.go:246] evictLeaderBeforeUpgrade: for tikv pod [REDACTED_ENV_NAME]/rp-[REDACTED_ENV_NAME]: failed to trigger force flush, continuing: rpc error: code = Unavailable desc = connection error: desc = "transport: Error while dialing dial tcp [REDACTED_IP]:20160: connect: connection refused"


#tikv logs
[2025/03/27 18:36:45.336 +00:00] [INFO] [router.rs:1499] ["log backup flush done"] [take=4.77s] [total_size=123447247] [files=1467] [merged_files=2] [thread_id=170]
# Vlad 18:36:45.336 - 4.77s matches the flush request from controller
```

However, we observe that log checkpoint is stuck for several minutes, tidb advancer logs show checkpoint at `[REDACTED_LONG_ID]` until `18:39:36.347`, which is more than 5 minutes. We do observe that checkpoint lag increases up to 8-9 minutes in many cases.

```
[2025/03/27 18:36:42.038 +00:00] [INFO] [advancer.go:619] ["updated log backup GC safe point."] [checkpoint=[REDACTED_LONG_ID] [target=[REDACTED_LONG_ID]

## Recent Comments Excerpt

### 2025-04-30T04:51:20.655+0800 [REDACTED_USER]

[REDACTED_MEDIA]
Screenshot with the metric attached. I have used >0 filter, such that we could see which stores had increased metrics value (looks like all of them).

### 2025-04-30T16:55:19.839+0800 [REDACTED_USER]

By the provided TiKV logs(it seems that it is not all the TiKV logs but the region 
6331391376
 above mentioned is in the TiKV whose logs are provided), we can see each TiKV can advance log backup checkpoint of local regions. 
[rp-[REDACTED_ENV_NAME].log] -- shutdown during 18:36 - 18:39
[2025/03/27 18:36:40.560 +00:00] [INFO] [endpoint.rs:846] ["rewriting resolved ts"] [new=[REDACTED_LONG_ID] [old=[REDACTED_LONG_ID] [thread_id=172]
[2025/03/27 18:39:14.312 +00:00] [INFO] [endpoint.rs:846] ["rewriting resolved ts"] [new=[REDACTED_LONG_ID] [old=[REDACTED_LONG_ID] [thread_id=172]

[rp-[REDACTED_ENV_NAME].log]

### 2025-05-08T05:23:11.859+0800 [REDACTED_USER]

@[REDACTED_USER]
  update from customer: [REDACTED_CUSTOMER], the logs in our kibana have expired. I’ll rerun the experiment, to collect the  
rewriting resolved ts
 messages.
Regaring the bug in 
optionalTick
, would it be possible to have a fix? Would the fix resolve the issue (I expect it would not, as we need to RCA the reason why flush subscriber is slow).
Regarding out-of-order logs, that is possible due to a fact that we’re using ELK for log storage and it does not provide a hard guarantee on log ordering.

### 2025-05-08T18:07:33.792+0800 [REDACTED_USER]

I find 
importantTick
 use another context, which is not cancelled. so in this case 
global checkpoint ts put in PD
 is the same as 
global checkpoint ts collected in TiDB
 that metrics shows.
I request a PR to fix that.

### 2025-05-12T18:54:27.722+0800 [REDACTED_USER]

awaiting the repro and the tikv log from customer.
