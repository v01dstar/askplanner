# GTOC-8213: PITR fails with HTTP 411 Length Required

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8213
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2026-02-07T23:27:31.693+0800
- Updated: 2026-02-10T01:40:12.892+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiDB
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We did an upgrade from v7.5.1 to v8.5.5.  
The backups are not working with the error. Please help to resolve this.

[REDACTED_MEDIA][REDACTED_MEDIA]Also, backups to a newly created .v8.5.5 version seems to be working fine.

Please help in providing a resolution for the same. We have a cutover to this cluster [REDACTED_CLUSTER] and we would like to ensure that backups are working as expected.

```
atharva.tandon@[REDACTED_USER]1089-223769L ~ % kubectl logs [REDACTED_ENV_NAME] --context=prod-hyd-2 -n [REDACTED_ENV_NAME] > [REDACTED_ENV_NAME].txt
Defaulted container "backup" out of: backup, br (init)
atharva.tandon@[REDACTED_USER]1089-223769L ~ % kubectl get backups --context=prod-hyd-2 -n [REDACTED_ENV_NAME] | grep [REDACTED_ENV_NAME]                                  
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      35h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      35h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      21h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      17h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      37h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      23h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      11h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      18s
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      29h
b-[REDACTED_ENV_NAME]               full   snapshot   Failed     s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                                                      6h
[REDACTED_ENV_NAME]                      log        Running    s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                                            [REDACTED_LONG_ID]   [REDACTED_LONG_ID]               11d
```

Also, PITR backup was paused and resumed as part of upgrade flow so seems to be working fine.

## Recent Comments Excerpt

### 2026-02-07T23:33:57.536+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2026-02-07T23:38:54.928+0800 [REDACTED_USER]

Here is the specific error:
The **411 (Length Required)** error happened because:
TiKV's internal AWS SDK sent a POST request to initiate a multipart upload to http://storage.googleapis.com
GCS's S3-compatible XML API rejected it because the Content-Length header was missing from the request
This is a known incompatibility between certain AWS SDK versions and GCS's S3-compat layer

### 2026-02-09T23:54:54.431+0800 [REDACTED_USER]

Latest Customer [REDACTED_CUSTOMER]
Atharva Tandon
2 hours ago
Full backups are working, getting same error for PITR backups though
31]: 
2026-02-09 18:16:45.438 +0530; gap=1h15m44s
  error-message[store=31]: 
[store = 31] I/O Error: failed to put object aws-sdk error: ServiceError(ServiceError { source: Unhandled(Unhandled { source: XmlDecodeError { kind: Custom("no root element") }, meta: ErrorMetadata { code: None, mes

### 2026-02-10T01:39:26.434+0800 [REDACTED_USER]

atharva.tandon@[REDACTED_USER]1089-223769L ~ % kubectl get backup [REDACTED_ENV_NAME] --context=prod-hyd-2 -n [REDACTED_ENV_NAME] -oyaml
apiVersion: pingcap.com/v1alpha1
kind: Backup
metadata:
  annotations:
    sidecar.istio.io/inject: "false"
  creationTimestamp: "2026-02-09T12:42:49Z"
  finalizers:

### 2026-02-10T01:40:12.892+0800 [REDACTED_USER]

atharva.tandon@[REDACTED_USER]1089-223769L ~ % kubectl exec -it [REDACTED_ENV_NAME] --context=prod-hyd-2 -n [REDACTED_ENV_NAME] -- sh                                                                                                    
sh-5.1$ ./br log status --pd http://[REDACTED_ENV_NAME]:2379
Detail BR log in /tmp/br.log.2026-02-09T23.00.27+0530 
● Total 1 Tasks.
> #1 <
                     name: [REDACTED_RESOURCE_NAME]
                   status: ○ ERROR
                    start: 2026-02-09 17:04:25.015 +0530
