# GTOC-8196: PITR fails with HTTP 411 Length Required

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8196
- Status: Resolved
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2026-02-02T12:43:42.977+0800
- Updated: 2026-03-04T17:50:06.107+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

**客户：Flipcart**

**[REDACTED_ENV_NAME]** 的备份任务已持续运行超过 \*15 天\*。  
请协助检查该问题，并提供\*详细的原因分析\*以及\*相应的解决方案\*，以便尽快恢复备份任务的正常状态。

[[REDACTED_CUSTOMER_CONSOLE_URL])

[https://br.noah.fkcloud.in/k8s/configs/[REDACTED_ENV_NAME]/rpos/](https://br.noah.fkcloud.in/k8s/configs/[REDACTED_ENV_NAME]/rpos/)

```
[
  {
    "name": "prod__643__tidb__2026-01-30__10-21-04__full",
    "RPO": {
      "type": "--full",
      "data": {
        "app_name": "rigelpc",
        "pod": "[REDACTED_ENV_NAME]",
        "controller_statefulset": "",
        "namespace": "[REDACTED_ENV_NAME]",
        "k8s_cluster_name": "prod-ch-3",
        "zone": "in-chennai-2"
      },
      "start_time": "2026-01-30 10:21:07",
      "end_time": "2026-01-30 10:22:00",
      "size": 0,
      "location": "",
      "status": "FAILED",

## Recent Comments Excerpt

### 2026-02-10T09:30:39.187+0800 [REDACTED_USER]

Full backups worked after setting the above config. But PITR backup gave the same error
31]: 
2026-02-09 18:16:45.438 +0530; gap=1h15m44s
  error-message[store=31]: 
[store = 31] I/O Error: failed to put object aws-sdk error: ServiceError(ServiceError { source: Unhandled(Unhandled { source: XmlDecodeError { kind: Custom("no root element") }, meta: ErrorMetadata { code: None, mes
                           sage: None, extras: None } }), raw: Response { status: StatusCode(411), headers: Headers { headers: {"content-type": HeaderValue { _private: H0("text/html; charset=UTF-8") }, "referrer-policy": HeaderValue { _privat
                           e: H0("no-referrer") }, "content-length": HeaderValue { _private: H0("1564") }, "date": HeaderValue { _private: H0("Mon, 09 Feb 2026 12:46:45 GMT") }} }, body: SdkBody { inner: Once(Some(b"<!DOCTYPE html>\n<html lan
                           g=en>\n  <meta charset=utf-8>\n  <meta name=viewport content=\"initial-scale=1, minimum-scale=1, width=device-width\">\n  <title>Error 411 (Length Required)!!1</title>\n  <style>\n    *{margin:0;padding:0}html,code{

### 2026-02-10T16:35:26.255+0800 [REDACTED_USER]

what config? i don’t see we’ve suggested any config 

 
the PiTR error is the same “Error 411”

### 2026-02-11T05:37:52.164+0800 [REDACTED_USER]

They changed
backup.s3-multi-part-size = '256MiB'
 and apparently this helped with the full backups? I think it was suggested by Subi or Jana

### 2026-02-11T12:12:36.698+0800 [REDACTED_USER]

Oh ok. Yeah this will make BR stop using Multi-part upload for files below 256 MiB and thus able to workaround the issue.
Unfortunately, as of v8.5.4, only “full backup task” 
respected
 
backup.s3-multi-part-size
, while all other usage of S3 within TiKV just assumed the default config:
Log backup 
https://github.com/tikv/tikv/blob/4855bdccc64e7a8551d30ebbbd5be75a42929265/components/backup-stream/src/router.rs#L1005-L1008

### 2026-03-04T13:50:54.237+0800 [REDACTED_USER]

@[REDACTED_USER]
 
@[REDACTED_USER]
 Hi, this issue has been solved and this ticket can be closed. Thank you for the effort.
