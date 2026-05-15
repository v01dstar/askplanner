# GTOC-8051: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8051
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-11-20T09:32:35.858+0800
- Updated: 2026-01-13T20:51:09.824+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We observe following failure of log backup:

```
sh-5.1# var/lib/br-bin/br log status --pd=[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379 --ca=/var/lib/cluster-client-tls/ca.crt --cert=/var/lib/cluster-client-tls/tls.crt --key=/var/lib/cluster-client-tls/tls.key --send-credentials-to-tikv=false
[ ... cut by Vlad ... ]

● Total 1 Tasks.
> #1 <
                           name: [REDACTED_RESOURCE_NAME]
                         status: ○ ERROR
                          start: 2025-11-04 23:01:12.523 +0000
                            end: 2090-11-18 14:07:45.624 +0000
                        storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
                    speed(est.): 0.00 ops/s
             checkpoint[global]: 2025-11-15 07:28:22.459 +0000; gap=87h45m52s
          error[store=30861887]: KV:LogBackup:Io
error-happen-at[store=30861887]: 2025-11-16 00:32:54.527 +0000; gap=70h41m20s
  error-message[store=30861887]: I/O Error: failed to put object aws-sdk error: ServiceError(ServiceError { source: Unhandled(Unhandled { source: ErrorMetadata { code: Some("InvalidArgument"), message: Some("Part number must be an integer between 1 and 10000, inclusive"), extras: Some({"aws_request_id": "[REDACTED_AWS_REQUEST_ID]", "s3_
                                 extended_request_id": "iGC+vRKm7s99oUmiALvj0YMcxRqiJF+RkX09Zyoy/qdQ3kXi2k6QNuCyMo5cMd02Xc6E4U9fd1/wUMz7xy+l78AH9RxCPo6d"}) }, meta: ErrorMetadata { code: Some("InvalidArgument"), message: Some("Part number must be an integer between 1 and 10000, inclusive"), extras: Some({"aws_request_id": "D2VZ
                                 19H0M53HQYD8", "s3_extended_request_id": "[REDACTED_AWS_EXTENDED_REQUEST_ID]"}) } }), raw: Response { status: StatusCode(400), headers: Headers { headers: {"x-amz-request-id": HeaderValue { _private: H0("D2VZ19H0M53HQYD8") }, "x-amz-i
                                 d-2": HeaderValue { _private: H0("iGC+vRKm7s99oUmiALvj0YMcxRqiJF+RkX09Zyoy/qdQ3kXi2k6QNuCyMo5cMd02Xc6E4U9fd1/wUMz7xy+l78AH9RxCPo6d") }, "content-type": HeaderValue { _private: H0("application/xml") }, "transfer-encoding": HeaderValue { _private: H0("chunked") }, "date": HeaderValue { _private: H
                                 0("Sun, 16 Nov 2025 00:32:51 GMT") }, "connection": HeaderValue { _private: H0("close") }, "server": HeaderValue { _private: H0("AmazonS3") }} }, body: SdkBody { inner: Once(Some(b"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Error><Code>InvalidArgument</Code><Message>Part number must be an inte
                                 ger between 1 and 10000, inclusive</Message><ArgumentName>partNumber</ArgumentName><ArgumentValue>10001</ArgumentValue><RequestId>D2VZ19H0M53HQYD8</RequestId><HostId>iGC+vRKm7s99oUmiALvj0YMcxRqiJF+RkX09Zyoy/qdQ3kXi2k6QNuCyMo5cMd02Xc6E4U9fd1/wUMz7xy+l78AH9RxCPo6d</HostId></Error>")), retryable: t
                                 rue }, extensions: Extensions { extensions_02x: Extensions, extensions_1x: Extensions } } })
```

According to the tikv logs, the error is interpreted as fatal and it stopped log backup from running, see log:

## Recent Comments Excerpt

### 2025-11-20T09:32:40.672+0800 [REDACTED_USER]

fail to find L2 assignee: please escalate to L3

### 2025-11-20T09:32:43.410+0800 [REDACTED_USER]

assign to 廖坚钧([REDACTED_EMAIL])

### 2025-11-20T09:32:45.954+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b5ed2b50108a0c1a4ffa5f022186) by lark

### 2025-11-20T09:34:25.845+0800 [REDACTED_USER]

Regarding the suggestion of increasing 
s3-multi-part-size: 
Thank you. I understand the multipart upload limitation of 10000 parts. My question is why TiKV component tries to send more, it clearly looks like a bug in the upload code, please see our additional observations below.
 
As workaround, I think you can try to increase 
s3-multi-part-size
https://docs.pingcap.com/tidb/stable/tikv-configuration-file/#s3-[REDACTED_ENV_NAME]
We have this parameter increased already, per recommendation in

### 2025-11-20T10:42:22.116+0800 [REDACTED_USER]

Can you provide the error occurred TiKV log?
