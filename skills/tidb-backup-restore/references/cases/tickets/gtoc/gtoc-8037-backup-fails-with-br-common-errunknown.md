# GTOC-8037: Backup fails with [BR:Common:ErrUnknown]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8037
- Status: Pending for fixes/proactive actions
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-11-15T03:24:43.728+0800
- Updated: 2026-01-13T20:51:38.533+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: storage-credential, tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We encountered an error where an improper IAM role was configured for a cluster. Due to this, when the backup was attempting to run, it was failing out. Although when checking the br.log, it was not immediately obvious what the issue was.

Upon investigating a random TiKV host, we then saw an error log being raised within the TiKV logs that told us about the bad IAM role configuration. It would have saved us a lot of time if that error was displayed within the br.log that gets produced.

<custom data-type="smartlink" data-id="id-0">https://pinterest.slack.com/archives/C01317HD0N7/p1759947156836679</custom> 

Final note – Cluster has been decommissioned and I can’t find the TiDB version for the life of me that was running… Sorry!

## Recent Comments Excerpt

### 2025-11-15T03:24:48.051+0800 [REDACTED_USER]

fail to find L2 assignee: please escalate to L3

### 2025-11-15T03:24:49.564+0800 [REDACTED_USER]

assign to 廖坚钧([REDACTED_EMAIL])

### 2025-11-15T03:24:51.450+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b5e4c6eeae8800ec399f19006689) by lark

### 2025-11-15T03:25:33.504+0800 [REDACTED_USER]

From TiKV shows:
{"level":"ERROR","caller":"endpoint.rs:259","message":"backup save file failed","time":"2025/10/08 18:23:09.629 +00:00","thread_id":211,"err_code":"KV:Unknown","err":"Io(Custom { kind: Other, error: \"failed to put object aws-sdk error: ServiceError(ServiceError { source: Unhandled(Unhandled { source: ErrorMetadata { code: Some(\\\"AccessDenied\\\"), message: Some(\\\"User: arn:aws:sts::[REDACTED_LONG_ID]:assumed-role/base/i-0b4ef6a5e3916356a is not authorized to perform: s3:PutObject on resource: \\\\\\\"arn:aws:s3:::pinterest-ipiales/dev/backups/data/pinventory_dev/FULL-1759947779/data/108504263/307404644_15481_bb58aaea560c3b24df29c4530bb4bf4b3ec0377a07ce01cb25f4e0b31988bb1a_1759947789019_default.sst\\\\\\\" with an explicit deny in a resource-based policy\\\"), extras: Some({\\\"s3_extended_request_id\\\": \\\"T2ymDL0DuEEE9e6scW4EWZ1H++egmcyWHxRGhRfTza0Rkj815wEv3ml2CHPifNweZ2SgvjfzqVc=\\\", \\\"aws_request_id\\\": \\\"T4SYYTKMCNZ2Y4YD\\\"}) }, meta: ErrorMetadata { code: Some(\\\"AccessDenied\\\"), message: Some(\\\"User: arn:aws:sts::[REDACTED_LONG_ID]:assumed-role/base/i-0b4ef6a5e3916356a is not authorized to perform: s3:PutObject on resource: \\\\\\\"arn:aws:s3:::pinterest-ipiales/dev/backups/data/pinventory_dev/FULL-1759947779/data/108504263/307404644_15481_bb58aaea560c3b24df29c4530bb4bf4b3ec0377a07ce01cb25f4e0b31988bb1a_1759947789019_default.sst\\\\\\\" with an explicit deny in a resource-based policy\\\"), extras: Some({\\\"s3_extended_request_id\\\": \\\"T2ymDL0DuEEE9e6scW4EWZ1H++egmcyWHxRGhRfTza0Rkj815wEv3ml2CHPifNweZ2SgvjfzqVc=\\\", \\\"aws_request_id\\\": \\\"T4SYYTKMCNZ2Y4YD\\\"}) } }), raw: Response { status: StatusCode(403), headers: Headers { headers: {\\\"x-amz-request-id\\\": HeaderValue { _private: H0(\\\"T4SYYTKMCNZ2Y4YD\\\") }, \\\"x-amz-id-2\\\": HeaderValue { _private: H0(\\\"T2ymDL0DuEEE9e6scW4EWZ1H++egmcyWHxRGhRfTza0Rkj815wEv3ml2CHPifNweZ2SgvjfzqVc=\\\") }, \\\"content-type\\\": HeaderValue { _private: H0(\\\"application/xml\\\") }, \\\"transfer-encoding\\\": HeaderValue { _private: H0(\\\"chunked\\\") }, \\\"date\\\": HeaderValue { _private: H0(\\\"Wed, 08 Oct 2025 18:23:08 GMT\\\") }, \\\"server\\\": HeaderValue { _private: H0(\\\"AmazonS3\\\") }} }, body: SdkBody { inner: Once(Some(b\\\"<?xml version=\\\\\\\"1.0\\\\\\\" encoding=\\\\\\\"UTF-8\\\\\\\"?>\\\\n<Error><Code>AccessDenied</Code><Message>User: arn:aws:sts::[REDACTED_LONG_ID]:assumed-role/base/i-0b4ef6a5e3916356a is not authorized to perform: s3:PutObject on resource: \\\\\\\"arn:aws:s3:::pinterest-ipiales/dev/backups/data/pinventory_dev/FULL-1759947779/data/108504263/307404644_15481_bb58aaea560c3b24df29c4530bb4bf4b3ec0377a07ce01cb25f4e0b31988bb1a_1759947789019_default.sst\\\\\\\" with an explicit deny in a resource-based policy</Message><RequestId>T4SYYTKMCNZ2Y4YD</RequestId><HostId>T2ymDL0DuEEE9e6scW4EWZ1H++egmcyWHxRGhRfTza0Rkj815wEv3ml2CHPifNweZ2SgvjfzqVc=</HostId></Error>\\\")), retryable: true }, extensions: Extensions { extensions_02x: Extensions, extensions_1x: Extensions } } })\" })"}
EditDelete
Jack Ma 
2 minutes ago
[2025/10/08 19:14:23.725 +00:00] [ERROR] [main.go:38] ["br failed"] [error="at fine-grained backup, remained ranges = 0: backoff exceeds the max backoff time 1h0m0s: [BR:Common:ErrUnknown]internal error"] [errorVerbose="[BR: Common:ErrUnknown]internal error\nbackoff exceeds the max backoff time 1h0m0s\ngithub.com/pingcap/tidb/br/pkg/utils.(*RetryWithBackoffer).BackOff\n\t/mnt/tidb/sql/br/pkg/utils/retry.go:348\ngithub.com/pingcap/tidb/br/pkg/bac 119631 kup.(*Client).fineGrainedBackup\n\t/mnt/tidb/sql/br/pkg/backup/client.go:1247\ngithub.com/pingcap/tidb/br/pkg/ba 119631 ckup.(*Client).BackupRange\n\t/mnt/tidb/sql/br/pkg/backup/client.go:995\ngithub.com/pingcap/tidb/br/pkg/backup.(*Client).BackupRanges.func2\n\t/mnt/tidb/sql/br/pkg/backup/client.go:901\ngithub.com/pingcap/tidb/pkg/util.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/mnt/tidb/sql/pkg/util/worker_pool.go:81\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.7.0/errgroup/errgroup.go:78\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\nat fine-grained backup, remained ranges = 0"] [stack="main.main\n\t/mnt/tidb/sql/br/cm 119631 d/br/main.go:38\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267"]
EditDelete
Jack Ma

### 2025-11-15T12:39:45.677+0800 [REDACTED_USER]

fixed by 
https://github.com/pingcap/tidb/pull/58671
 in v9.0.0. Maybe it can be cherry-picked back.
