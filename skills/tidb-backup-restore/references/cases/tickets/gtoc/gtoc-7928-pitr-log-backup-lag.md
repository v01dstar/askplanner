# GTOC-7928: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7928
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-09-30T08:47:51.438+0800
- Updated: 2025-10-30T08:56:50.792+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

**Problem background**  
The customer [REDACTED_CUSTOMER]**Object Lock** on an S3 bucket with a retention period of 30 days.  
After enabling, both **log backup** and **snapshot backup** started reporting errors.  
Typical S3 error:

```
InvalidRequest: Content-MD5 OR x-amz-checksum-* HTTP header is required 
for Put Object requests with Object Lock parameters
```

**Log backup**  
After a reset, log backup has resumed normal operation. Reset guide:  
<custom data-type="smartlink" data-id="id-0">https://docs.google.com/document/d/1s1xqE_hDoFSdynXx6G8f3_yO0PJjqhmGRhJI1IvdCyQ/edit?tab=t.0#heading=h.pg747a5xfuiw</custom> 

**Snapshot backup**  
Still failing. BR logs are attached in the ticket.

## Recent Comments Excerpt

### 2025-09-30T08:48:04.365+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b4286c2f0e4cc0f14ffb845d1f3e) by lark

### 2025-09-30T08:49:41.136+0800 [REDACTED_USER]

More detail  backup log

cluster [REDACTED_CLUSTER]/[REDACTED_RESOURCE_NAME], wait pipe message failed, errMsg [2025/09/30 00:01:25.756 +00:00] [ERROR] [client.go:1245] ["TiKV encountered an error, interrupting the backup."] ["error message"="Io(Custom { kind: Other, error │
│ : \"failed to put object aws-sdk error: ServiceError(ServiceError { source: Unhandled(Unhandled { source: ErrorMetadata { code: Some(\\\"InvalidRequest\\\"), message: Some(\\\"Content-MD5 OR x-amz-checksum- HTTP header is required for Put Object requests with Object Lock parameters\\\"), extras: Some({\\\"s3_ex │
│ tended_request_id\\\": \\\"tNQC5OiW44Y5Haa3V28eHfkE4r0s84Olxw8+fBgTi8egql5n4RGdV6SxGiCEz9T9KAOUF6T3l0M=\\\", \\\"aws_request_id\\\": \\\"MRXP659WR1PK1X9E\\\"}) }, meta: ErrorMetadata { code: Some(\\\"InvalidRequest\\\"), message: Some(\\\"Content-MD5 OR x-amz-checksum- HTTP header is required for Put Object req │
│ uests with Object Lock parameters\\\"), extras: Some({\\\"s3_extended_request_id\\\": \\\"tNQC5OiW44Y5Haa3V28eHfkE4r0s84Olxw8+fBgTi8egql5n4RGdV6SxGiCEz9T9KAOUF6T3l0M=\\\", \\\"aws_request_id\\\": \\\"MRXP659WR1PK1X9E\\\"}) } }), raw: Response { status: StatusCode(400), headers: Headers { headers: {\\\"x-amz-req │
│ uest-id\\\": HeaderValue { _private: H0(\\\"MRXP659WR1PK1X9E\\\") }, \\\"x-amz-id-2\\\": HeaderValue { _private: H0(\\\"tNQC5OiW44Y5Haa3V28eHfkE4r0s84Olxw8+fBgTi8egql5n4RGdV6SxGiCEz9T9KAOUF6T3l0M=\\\") }, \\\"content-type\\\": HeaderValue { _private: H0(\\\"application/xml\\\") }, \\\"transfer-encoding\\\": Hea │
│ derValue { _private: H0(\\\"chunked\\\") }, \\\"date\\\": HeaderValue { _private: H0(\\\"Tue, 30 Sep 2025 00:01:25 GMT\\\") }, \\\"connection\\\": HeaderValue { _private: H0(\\\"close\\\") }, \\\"server\\\": HeaderValue { _private: H0(\\\"AmazonS3\\\") }} }, body: SdkBody { inner: Once(Some(b\\\"<?xml version=\ │

### 2025-09-30T11:58:47.293+0800 [REDACTED_USER]

Summary:
Backup will check whether object lock is enabled before initializing the backup.
If object lock enabled, it will set a “ObjectLockEnabled` flag in the external storage configuration passed to TiKV.
When that flag set, TiKV calcuates MD5 and set the 
Content-MD5
 header for each object it uploads.
In this scenario, object lock was enabled after backup initialized. So the rest of requests in this backup fails.
The reason of the following snapshot backup keep failing is still not clear, waiting for more BR log to troubleshooting.

### 2025-10-22T00:48:15.149+0800 [REDACTED_USER]

This is the latest log from br pod. I don’t think it’s related with object lock. But I don’t understand the root cause of it.
[REDACTED_MEDIA]

### 2025-10-30T08:56:50.792+0800 [REDACTED_USER]

This ticket can be closed now.
