# GTOC-8089: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8089
- Status: ESCALATE TO L3
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-12-11T12:21:56.506+0800
- Updated: 2025-12-11T13:34:25.024+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We’re experimenting with logical BR on [REDACTED_ENV_NAME] use cases (they use EBS backups in production), and face consistent backup failures, when default configuration is used (auto-tune enabled, 5MiB multi-part size). The failures happen due to TiKV failing to handle and retry HTTP 503 errors coming from AWS.

Example of TiKV error:

```
[2025/12/09 20:01:14.321 +00:00] [WARN] [util.rs:110] ["aws request fails"] [uuid=[REDACTED_UUID] [context=upload_part] [retry?=false] [err="aws-sdk error: ServiceError(ServiceError { source: Unhandled(Unhandled { source: ErrorMetadata { code: Some(\"SlowDown\"), message: Some(\"Please reduce your request rate.\"), extras: Some({\"s3_extended_request_id\": \"1DN8G8mhPNnr0CEbJGCobzZEewXR4V/cH0+2HzHUYCYNBlVgWUAIehhio1u/VHbbyk2mZEGQ6aQu1k1wGg3i8KWyAcM7zfvWvS8X8V46Te0=\", \"aws_request_id\": \"SJXZKJWX81CSG8J2\"}) }, meta: ErrorMetadata { code: Some(\"SlowDown\"), message: Some(\"Please reduce your request rate.\"), extras: Some({\"s3_extended_request_id\": \"1DN8G8mhPNnr0CEbJGCobzZEewXR4V/cH0+2HzHUYCYNBlVgWUAIehhio1u/VHbbyk2mZEGQ6aQu1k1wGg3i8KWyAcM7zfvWvS8X8V46Te0=\", \"aws_request_id\": \"SJXZKJWX81CSG8J2\"}) } }), raw: Response { status: StatusCode(503), headers: Headers { headers: {\"x-amz-request-id\": HeaderValue { _private: H0(\"SJXZKJWX81CSG8J2\") }, \"x-amz-id-2\": HeaderValue { _private: H0(\"1DN8G8mhPNnr0CEbJGCobzZEewXR4V/cH0+2HzHUYCYNBlVgWUAIehhio1u/VHbbyk2mZEGQ6aQu1k1wGg3i8KWyAcM7zfvWvS8X8V46Te0=\") }, \"content-type\": HeaderValue { _private: H0(\"application/xml\") }, \"transfer-encoding\": HeaderValue { _private: H0(\"chunked\") }, \"date\": HeaderValue { _private: H0(\"Tue, 09 Dec 2025 20:01:13 GMT\") }, \"connection\": HeaderValue { _private: H0(\"close\") }, \"server\": HeaderValue { _private: H0(\"AmazonS3\") }} }, body: SdkBody { inner: Once(Some(b\"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?>\\n<Error><Code>SlowDown</Code><Message>Please reduce your request rate.</Message><RequestId>SJXZKJWX81CSG8J2</RequestId><HostId>1DN8G8mhPNnr0CEbJGCobzZEewXR4V/cH0+2HzHUYCYNBlVgWUAIehhio1u/VHbbyk2mZEGQ6aQu1k1wGg3i8KWyAcM7zfvWvS8X8V46Te0=</HostId></Error>\")), retryable: true }, extensions: Extensions { extensions_02x: Extensions, extensions_1x: Extensions } } })"] [thread_id=326]
```

Note that AWS classifies the error as retryable (`retryable: true`), and API wraps it in ServiceError, while tikv marks the error as non-retryable (`retry?=false`)

Failed log backup CR is attached.

We did check TiKV code and believe there is a bug, where ServiceError returned by AWS APIs are not handled as retryable errors. I have submitted tikv issue <custom data-type="smartlink" data-id="id-0">https://github.com/tikv/tikv/issues/19196</custom>  and potential fix <custom data-type="smartlink" data-id="id-1">https://github.com/tikv/tikv/pull/19197</custom>  , asking BR team to take a look.

## Recent Comments Excerpt

### 2025-12-11T12:22:03.088+0800 [REDACTED_USER]

assign to 陈青璟([REDACTED_EMAIL])

### 2025-12-11T12:22:05.610+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), om_x100b5c9020058934c2f52d95819fef8) by lark

### 2025-12-11T13:33:59.972+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), om_x100b5c9132bb48a8c1033379a9a5ce6) by lark

### 2025-12-11T13:34:24.850+0800 [REDACTED_USER]

PTAL about the GitHub issue and PR.
