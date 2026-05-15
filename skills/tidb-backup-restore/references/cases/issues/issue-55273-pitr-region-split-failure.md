# Issue 55273: PITR region split failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/55273
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-08-07T09:52:16Z
- Updated: 2024-08-28T04:28:48Z
- Closed: 2024-08-28T04:28:48Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: PITR
- Components: TiDB, TiKV, Operator, BR, Storage, PD
- Categories: pitr-log-restore, storage-access, region-split-scatter, observability-diagnosis
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `PITR region split failure`
- Search terms: BR; Operator; PD; PITR; Storage; TiDB; TiKV; observability-diagnosis; pitr-log-restore; region-split-scatter; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. Start a log backup task:
```console
$ tiup br:v8.1.0 log start -u upd-1:2379 --task-name fiolvit -s (s3altpath test)
Starting component `br`: /root/.tiup/components/br/v8.1.0/br log start -u upd-1:2379 --task-name fiolvit -s s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
Detail BR log in /tmp/br.log.2024-08-07T17.45.19+0800
[2024/08/07 17:45:19.859 +08:00] [INFO] [collector.go:77] ["log start"] [streamTaskInfo="{taskName=fiolvit,startTs=[REDACTED_LONG_ID],endTS=[REDACTED_LONG_ID],tableFilter=*.*}"] [pausing=false] [rangeCount=2]
[2024/08/07 17:45:23.269 +08:00] [INFO] [collector.go:77] ["log start success summary"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0] [backup-checksum=32.966226ms] [total-take=3.715794709s]
```

And then, check the TiDB log.
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
It shouldn't contain sensetive information.

### 3. [REDACTED_USER]
```
[2024/08/07 17:45:19.844 +08:00] [INFO] [advancer.go:399] ["added event"] [task="storage:<s3:<endpoint:\"http://minio:9000\" region:\"us-east-1\" bucket:\"astro\" prefix:\"test\" access_key:\"minioadmin\" secret_access_key:\"minioadmin\" force_path_style:true > > start_ts:[REDACTED_LONG_ID] end_ts:[REDACTED_LONG_ID] name:\"fiolvit\" table_filter:\"*.*\" compression_type:ZSTD "] [ranges="{[6D, 6E), [74, 75)}"] [current-checkpoint=[REDACTED_LONG_ID]
```

Notice here, our secret key was printed:

```
... access_key:\"minioadmin\" secret_access_key:\"minioadmin\" ...
```

### 4. [REDACTED_USER]
Current master.
<!-- Paste the output of SELECT tidb_version() -->

**Note**: It is always unsafe to enable `--send-credentials-to-tikv` when starting log backup because: it will store the credentials to PD, and won't rotate them. Then, when the session key expired, there is no way to refresh them(Also anyone that can access PD can query them...). Authorize by IAM roles or other context of the TiKV node are more recommended in productive environment.
