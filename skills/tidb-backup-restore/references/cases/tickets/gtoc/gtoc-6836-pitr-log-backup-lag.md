# GTOC-6836: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6836
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-11T14:39:35.000+0800
- Updated: 2025-03-06T18:14:35.262+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

BR log truncate operation was failed.  
log message is below.  
BR version is v7.1 and TiDB cluster is v6.5.8

```
$ cat br-truncate-20240409-143001.log
[2024/04/09 14:30:01.333 +00:00] [INFO] [info.go:49] ["Welcome to Backup & Restore (BR)"] [release-version=v7.1.0] [git-hash=635a4362235e8a3c0043542e629532e3c7bb2756] [git-branch=heads/refs/tags/v7.1.0] [go-version=go1.20.3] [utc-build-time="2023-05-30 11:10:45"] [race-enabled=false]
[2024/04/09 14:30:01.334 +00:00] [INFO] [common.go:723] [arguments] [__command="br log truncate"] [log-file=/home/ec2-user/deploy/log/br-truncate-20240409-143001.log] [s3.region=ap-northeast-1] [send-credentials-to-tikv=false] [storage=s3://[REDACTED_ENV_NAME] [until=[REDACTED_LONG_ID] [yes=true]
[2024/04/09 14:30:01.388 +00:00] [INFO] [s3.go:402] ["succeed to get bucket region from s3"] ["bucket region"=ap-northeast-1]
[2024/04/09 14:30:01.436 +00:00] [INFO] [stream_mgr.go:316] ["use workers to speed up reading metadata files"] [workers=128]
[2024/04/09 14:38:53.461 +00:00] [WARN] [s3.go:986] ["failed to request s3, retrying"] [error="ServiceUnavailable: Service Unavailable\n\tstatus code: 503, request id: [REDACTED_REQUEST_ID], host id: [REDACTED_HOST_ID]"] [backoff=2.686144176s]
[2024/04/09 14:38:53.842 +00:00] [ERROR] [stream_mgr.go:328] ["failed to read file"] [file=v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta] [stack="github.com/pingcap/tidb/br/pkg/stream.FastUnmarshalMetaData.func1.1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/stream/stream_mgr.go:328\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.1.0/errgroup/errgroup.go:75"]
[2024/04/09 14:38:53.842 +00:00] [ERROR] [stream_mgr.go:328] ["failed to read file"] [file=v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta] [stack="github.com/pingcap/tidb/br/pkg/stream.FastUnmarshalMetaData.func1.1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/stream/stream_mgr.go:328\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.1.0/errgroup/errgroup.go:75"]
[2024/04/09 14:38:53.842 +00:00] [ERROR] [stream.go:530] ["failed to stream"] [command="log truncate"] [error="scanning metadata meets error RequestCanceled: request context canceled\ncaused by: context canceled: during reading meta file v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta from storage: unexpected EOF"] [errorVerbose="unexpected EOF\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/juju_adaptor.go:15\ngithub.com/pingcap/tidb/br/pkg/storage.(*S3Storage).ReadFile\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/storage/s3.go:534\ngithub.com/pingcap/tidb/br/pkg/stream.FastUnmarshalMetaData.func1.1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/stream/stream_mgr.go:326\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.1.0/errgroup/errgroup.go:75\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1598\nduring reading meta file v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta from storage\nscanning metadata meets error RequestCanceled: request context canceled\ncaused by: context canceled"] [stack="github.com/pingcap/tidb/br/pkg/task.RunStreamCommand\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:530\nmain.streamCommand\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/stream.go:232\nmain.newStreamTruncateCommand.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/stream.go:143\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968\nmain.main\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/main.go:58\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250"]
[2024/04/09 14:38:53.843 +00:00] [ERROR] [main.go:60] ["br failed"] [error="scanning metadata meets error RequestCanceled: request context canceled\ncaused by: context canceled: during reading meta file v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta from storage: unexpected EOF"] [errorVerbose="unexpected EOF\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/juju_adaptor.go:15\ngithub.com/pingcap/tidb/br/pkg/storage.(*S3Storage).ReadFile\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/storage/s3.go:534\ngithub.com/pingcap/tidb/br/pkg/stream.FastUnmarshalMetaData.func1.1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/stream/stream_mgr.go:326\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.1.0/errgroup/errgroup.go:75\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1598\nduring reading meta file v1/backupmeta/[REDACTED_LONG_ID]-[REDACTED_UUID].meta from storage\nscanning metadata meets error RequestCanceled: request context canceled\ncaused by: context canceled"] [stack="main.main\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/main.go:60\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250"]
```

Because this happens during daily log backup schedule, we will monitor next daily job. (It means not retry yet).  
Does error retry works properly?

## Recent Comments Excerpt

### 2024-04-11T15:11:59.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 11/Apr/24 7:11 AM

The actual error that brought down the 
br log truncate
 process is likely this:
unexpected EOF
github.com/pingcap/errors.AddStack
	/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/errors.go:174

### 2024-04-11T15:18:50.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 11/Apr/24 7:18 AM

等会儿整理给客户

### 2024-04-11T15:31:50.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 11/Apr/24 7:31 AM

Hi @[REDACTED_USER] ,
In the log, the BR versoin is v7.1.0.
The actual error that brought down the 
br log truncate
 process is likely this:
unexpected EOF

### 2024-04-11T16:12:05.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 11/Apr/24 8:12 AM

Thanks for explanation. Understand clearly.

We will consider to use the upper BR version which contains PR you shared.
Please close this ticket. Thanks for your support.

### 2024-04-11T16:27:50.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 11/Apr/24 8:27 AM

Hello:
I'm glad I was able to resolve this issue for you. We will close the ticket later.
Thanks
