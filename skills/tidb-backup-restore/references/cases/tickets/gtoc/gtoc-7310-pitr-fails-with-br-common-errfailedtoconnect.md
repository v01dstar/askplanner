# GTOC-7310: PITR fails with [BR:Common:ErrFailedToConnect]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7310
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-12-17T07:56:42.000+0800
- Updated: 2025-03-07T10:55:14.501+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We are running a log backup task on the full-shadow cluster. It appears the log backup task stopped during a TiKV rolling restart and did not resume properly. Furthermore, the current log backup CR shows that the task is still Running, even though it is paused/stopped. We are currently running 8.1.1 br kernel w/ a 1.5.1 tidb-operator fork.

Searching tidb logs for advancer, we see the advancer pause the log backup, and directly prior, we see the following log:

```java
[2024/12/09 19:18:42.455 +00:00] [WARN] [advancer.go:646] ["Subscriber meet error, would polling the checkpoint."] [category="log backup advancer"] [error="store 31253011 has error: failed to get log backup client: [BR:Common:ErrFailedToConnect]failed to make connection to store 31253011: context canceled"]
```

Store 31253011 corresponds to tikv-43-1e in our cluster. Metrics show that tikv-43-1e is restarting at the time that log backup stops. I’ve attached:

* Log backup CR
* Relevant “advancer” logs from tidb pods

    *  those are all tidb logs from all pods w/ “advancer” in them. metrics show that tidb-89-1a is the advancer during that time. full logs from that tidb pod is also attached
    
* Full logs from tikv-43-1e

 

Why did the log backup pause/stop when tikv-43-1e restarted? If the tikv is unreachable, how does br retry? It doesn’t appear the tikv was restarting for an unusually long period of time. We set the following in our backup CR:

```java
backoffRetryPolicy:
    maxRetryTimes: 2
    minRetryDuration: 300s
    retryTimeout: 30m
```

## Recent Comments Excerpt

### 2024-12-17T07:56:56.000+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), ) by lark

### 2024-12-17T14:41:20.000+0800 [REDACTED_USER]

{   "@timestamp": "2024-12-09T19:20:53.515Z",   "message": "[2024/12/09 19:20:53.515 +00:00] [INFO] [advancer.go:397] [\"Meet task event\"] [category=\"log backup advancer\"] [event=Pause(log-baseline)]",   "namespace": "[REDACTED_ENV_NAME]",   "kube_cluster": "us-east-1a",   "container_name": "tidb",   "pod_name": "[REDACTED_ENV_NAME]" }
{   "@timestamp": "2024-12-09T19:21:25.098Z",   "message": "[2024/12/09 19:21:25.098 +00:00] [INFO] [advancer.go:397] [\"Meet task event\"] [category=\"log backup advancer\"] [event=Pause(log-baseline)]",   "namespace": "[REDACTED_ENV_NAME]",   "kube_cluster": "us-east-1a",   "container_name": "tidb",   "pod_name": "[REDACTED_ENV_NAME]" }
{   "@timestamp": "2024-12-09T19:21:35.281Z",   "message": "[2024/12/09 19:21:35.280 +00:00] [INFO] [advancer.go:397] [\"Meet task event\"] [category=\"log backup advancer\"] [event=Pause(log-baseline)]",   "namespace": "[REDACTED_ENV_NAME]",   "kube_cluster": "us-east-1a",   "container_name": "tidb",   "pod_name": "[REDACTED_ENV_NAME]" }
 
 
It seems the task have been paused three times. And given the pause happened when advancer owner switching, consider:
https://github.com/pingcap/tidb/issues/53561
 (But this should already be fixed in v8.1.1)

### 2024-12-18T03:27:22.000+0800 [REDACTED_USER]

Clinic: 
[REDACTED_CLINIC_URL]
No “backup stream meet fatal error” logs during that time. There were some
[2024/12/09 19:19:57.894 +00:00] [WARN] [errors.rs:162] ["backup stream meet error"] [position="Location 

{ file: \"/tikv/components/backup-stream/src/checkpoint_manager.rs\", line: 104, col: 34 }"] [verbose_err=Grpc(RemoteStopped)] [err="gRPC meet error RemoteStopped"] [context="sending subscription"] [thread_id=219]
tikv log: [REDACTED_RESOURCE_NAME].json

### 2024-12-20T08:03:26.000+0800 [REDACTED_USER]

ah yes I see that the advancer owner switched around the time that the log backup stopped (from tidb-89-1a to tidb-0-1a).
[REDACTED_MEDIA]
in terms of naming convention, because of a limitation on our service mesh routing, we cannot route external traffic to pods w/ the same name across different k8s clusters. so if we were to deploy the same TC 
[REDACTED_ENV_NAME]
 across 1a/1b/1e, tidb-operator would provision tidb pods w/ the same names across each zone. instead, we deploy the main TC (
[REDACTED_ENV_NAME]
) w/ 1 tidb in 1a, and 0 tidbs in 1b/1e. We then deploy suffixed TCs (
[REDACTED_ENV_NAME]-<cell>

### 2025-01-14T05:11:33.000+0800 [REDACTED_USER]

From customer: [REDACTED_CUSTOMER]nable to get tidb pod logs from that period. we have restarted the log backup and will conduct subsequent rolling restart tests and let you know if we see a reoccurrence of this issue. you can close this issue for now.
