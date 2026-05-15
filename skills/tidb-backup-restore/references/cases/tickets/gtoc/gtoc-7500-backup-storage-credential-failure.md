# GTOC-7500: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7500
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-03-28T08:42:09.533+0800
- Updated: 2025-03-28T10:16:27.777+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

## Description

We have a system setup where all TiDB clusters are able to backup into all regions we have TiDB clusters in. We’re deployed \~12 regions right now. All TiDB clusters are able to backup into all regions **except for eu-central-2**. The S3 bucket has the exact same permissions as all of the other buckets. We even tried creating a debug pod with an `aws` CLI in it and attached the same service account to that debug pod. We were able to create, list, and put objects into this problematic bucket just fine. It is just TiDB itself that is unable to backup into this bucket. We see this error from the TiKV nodes:

```
[2025/03/27 20:44:03.952 +00:00] [ERROR] [endpoint.rs:1144] ["backup create storage failed"] [err_code=KV:Unknown] [err="Custom { kind: InvalidInput, error: \"invalid aws region format eu-central-2\" }"] [thread_id=15]
```

and we see logs like these from the backup pods:

```
I0328 00:31:25.013737       9 backup.go:334] [2025/03/28 00:31:25.012 +00:00] [INFO] [client.go:138] ["collect backups goroutine exits"] [round=7261]
I0328 00:31:25.218127       9 backup.go:334] [2025/03/28 00:31:25.217 +00:00] [INFO] [client.go:184] ["This round of backup starts..."] [round=7262]
I0328 00:31:25.219254       9 backup.go:334] [2025/03/28 00:31:25.217 +00:00] [INFO] [client.go:225] ["backup ranges"] [round=7262] [incomplete-ranges=138] [cost=423.039µs]
I0328 00:31:25.232113       9 backup.go:334] [2025/03/28 00:31:25.225 +00:00] [INFO] [store_manager.go:151] ["StoreManager: dialing to store."] [address=[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_ENV_NAME].svc:20160] [store-id=1001]
I0328 00:31:25.263637       9 backup.go:334] [2025/03/28 00:31:25.263 +00:00] [INFO] [store.go:210] ["starting backup to the corresponding store"] [storeID=1001] [requestCount=5] [concurrency=4]
I0328 00:31:25.266494       9 backup.go:334] [2025/03/28 00:31:25.266 +00:00] [INFO] [store_manager.go:151] ["StoreManager: dialing to store."] [address=[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_ENV_NAME].svc:20160] [store-id=1020]
I0328 00:31:25.277827       9 backup.go:334] [2025/03/28 00:31:25.276 +00:00] [INFO] [store.go:210] ["starting backup to the corresponding store"] [storeID=1020] [requestCount=5] [concurrency=4]
I0328 00:31:25.280465       9 backup.go:334] [2025/03/28 00:31:25.278 +00:00] [INFO] [store_manager.go:151] ["StoreManager: dialing to store."] [address=[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_ENV_NAME].svc:20160] [store-id=1030]
I0328 00:31:25.287383       9 backup.go:334] [2025/03/28 00:31:25.287 +00:00] [INFO] [client.go:147] ["start wait store backups"] [remainingProducers=3]
I0328 00:31:25.287780       9 backup.go:334] [2025/03/28 00:31:25.287 +00:00] [INFO] [store.go:210] ["starting backup to the corresponding store"] [storeID=1030] [requestCount=5] [concurrency=4]
I0328 00:31:25.294656       9 backup.go:334] [2025/03/28 00:31:25.294 +00:00] [INFO] [client.go:103] ["store backup goroutine exits"] [store=1001]
I0328 00:31:25.302744       9 backup.go:334] [2025/03/28 00:31:25.302 +00:00] [INFO] [client.go:103] ["store backup goroutine exits"] [store=1020]
I0328 00:31:25.314206       9 backup.go:334] [2025/03/28 00:31:25.313 +00:00] [INFO] [client.go:103] ["store backup goroutine exits"] [store=1030]
I0328 00:31:25.314436       9 backup.go:334] [2025/03/28 00:31:25.314 +00:00] [INFO] [client.go:138] ["collect backups goroutine exits"] [round=7262]
```

## Recent Comments Excerpt

### 2025-03-28T08:42:48.815+0800 [REDACTED_USER]

acked msg index: om_be2d1042d055ec04df159149b1e8b363

### 2025-03-28T08:42:49.716+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2025-03-28T08:55:50.066+0800 [REDACTED_USER]

The root cause is 
https://github.com/tikv/tikv/issues/18159
 .


To workaround, user can set 
--s3.endpoint="
s3-accesspoint.eu-central-2.amazonaws.com

### 2025-03-28T10:15:49.785+0800 [REDACTED_USER]

---
apiVersion: pingcap.com/v1alpha1
kind: Backup
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
spec:
  imagePullSecrets:

### 2025-03-28T10:16:27.777+0800 [REDACTED_USER]

[REDACTED_MEDIA]
Logs are the same regardless of 
https
 or 
http
