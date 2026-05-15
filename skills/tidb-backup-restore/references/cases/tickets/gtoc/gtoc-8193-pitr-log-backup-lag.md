# GTOC-8193: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8193
- Status: Todo
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2026-02-02T09:54:45.930+0800
- Updated: 2026-02-13T21:45:36.059+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We have been getting a sev2 alert (LogBackupRunningRPOMoreThan30m_tidb-micros-temporal) several times in the past 24 hours due to the RPO of the log backup being higher than 30 minutes in our prod ca-central-1 cluster (7r6s).

I have restarted the log backup ([REDACTED_RESOURCE_NAME]) each time which causes the alert to close, but it keeps re-opening later. Can you please help root cause this issue? I have uploaded clinic data here: <custom data-type="smartlink" data-id="id-0">[REDACTED_CLINIC_URL]> 

FYI: For affected version, I think we are on v8.5.0-atl-sp-3 for TiKV and BR

## Recent Comments Excerpt

### 2026-02-03T14:06:08.393+0800 [REDACTED_USER]

@[REDACTED_USER]
 Can we verify the followings:
Which opensource version was TiKV 
v8.5.0-atl-sp3
 based on, and which PRs are cherry-picked into it? This warning did not exist on v8.5.0 (it appears since v8.5.1).
Have they ever modified any of the following code in the fork?
The 2nd and 5th parameter to function call of 
ConcurrencyManager::new_with_config

### 2026-02-04T03:11:57.846+0800 [REDACTED_USER]

[REDACTED_MEDIA]
log file uploaded.

### 2026-02-04T07:05:33.926+0800 [REDACTED_USER]

Thanks. (Below I’m going to use UTC since the log timestamp are all in UTC).
Name
Store ID
[REDACTED_RESOURCE_NAME]
1012
[REDACTED_RESOURCE_NAME]
1001
[REDACTED_RESOURCE_NAME]

### 2026-02-12T09:19:50.307+0800 [REDACTED_USER]

Customer [REDACTED_CUSTOMER]s clinic and log:
[REDACTED_CLINIC_URL]
 
[REDACTED_MEDIA]

### 2026-02-13T18:50:17.609+0800 [REDACTED_USER]

For some reason the Clinic did not show metrics before 2/10 18:01:45 (UTC-5).
We see that the CheckpointTS is stuck at 2/10 12:19:48 ([REDACTED_LONG_ID]). 
[advancer.go:313] ["current last region"] [category="log backup advancer hint"] [min="([?, ?), [REDACTED_LONG_ID])"] [for-polling=1] [min-ts=2026-02-10T17:19:48Z] [region-hint="ID=1008,Leader=1030,ConfVer=5,Version=7,Peers=[1001 1012 1030],RealRange=[?, ?)"]
...
[backoff.go:179] ["regionScheduling backoffer.maxSleep 200000ms is exceeded, errors:\nmessage:\"region 1008 is missing\" region_not_found:<region_id:1008 >  at 2026-02-10T18:25:48.20215271Z\nno leader, ctx: region ID: 1008, meta: id:1008 start_key:\"t\\200\\000\\377\\377\\377\\377\\377\\377\" end_key:\"x\\000\\000\\000\" region_epoch:<conf_ver:5 version:7 > peers:<id:1009 store_id:1001 > peers:<id:1014 store_id:1012 > peers:<id:1033 store_id:1030 > , peer: id:1033 store_id:1030 , addr: [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_ENV_NAME].svc:20160, idx: 0, reqStoreType: TiKvOnly, runStoreType: tikv at 2026-02-10T18:25:48.704017521Z\nmessage:\"region 1008 is missing\" region_not_found:<region_id:1008 >  at 2026-02-10T18:25:49.204638844Z\ntotal-backoff-times: 414, backoff-detail: regionMiss:165, regionScheduling:249, maxBackoffTimeExceeded: true, maxExcludedTimeExceeded: false\nlongest sleep type: regionScheduling, time: 121010ms"]
(redaction is only enabled in TiDB, but not on PD and TiKV.)
We see the key range of this missing region 1008 is 
[t281474976710655, x0)
