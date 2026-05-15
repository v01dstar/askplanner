# GTOC-8048: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8048
- Status: Pending for fixes/proactive actions
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-11-19T11:25:25.523+0800
- Updated: 2026-01-13T20:51:17.321+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

Hello,

We run daily snapshot backups using `br` tool. We are consistently able to reproduce this with one of our large clusters (about 13 TiB in size) the backup is corrupted / incomplete.

1. We ran restore command to restore the snapshot backup to a new cluster, and the restore process fails. Error details below.
2. The `br` checksum process also fails for these snapshot backups with the same error.

## Restore Failure

```
[2025/11/17 23:52:23.625 +00:00] [ERROR] [import.go:604] ["import sst file failed after retry, stop the whole progress"] [files="{total=1,files=\"[1114391333/2325890_143_7dee66d1b199e5721751f1dc33aff364b47488be3d1c0b03d5e7917423d5658f_1763337917577_write.sst]\",totalKVs=13966
restore [2025/11/17 23:52:23.627 +00:00] [ERROR] [client.go:1480] ["restore files failed"] [error="Cannot read https://s3-fips.us-east-1.amazonaws.com/db-tidb-foo/snapshot-webapp/webapp-pd.tidb-2379-2025-11-17t00-00-24/1114391333/2325890_143_7dee66d1b199e5721751f1dc33aff364b47488be3d1c0b03d5e7917423d5658f_1763337917577_write.sst into ...
restore [2025/11/17 23:52:23.629 +00:00] [ERROR] [pipeline_items.go:394] ["restore batch meet error"] [error="Cannot read https://s3-fips.us-east-1.amazonaws.com/db-tidb-foo/snapshot-webapp/webapp-pd.tidb-2379-2025-11-17t00-00-24/1114391333/2325890_143_7dee66d1b199e5721751f1dc33aff364b47488be3d1c0b03d5e7917423d5658f_1763337917577_write.sst ...
restore [2025/11/17 23:52:24.203 +00:00] [ERROR] [advancer.go:399] ["listen task meet error, would reopen."]
```

## BR Checksum Failure

```
[root@[REDACTED_RESOURCE_NAME] br-run]# /tmp/br-run/br debug checksum --storage "s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]" --s3.region "us-east-1"
Detail BR log in /tmp/br.log.2025-11-17T22.09.51Z
Error: failed to read s3 file, file info: input.bucket='db-tidb-foo', input.key='snapshot-webapp/webapp-pd.tidb-2379-2025-11-17t00-00-24/1114391333/2325890_143_7dee66d1b199e5721751f1dc33aff364b47488be3d1c0b03d5e7917423d5658f_1763337917577_write.sst': NoSuchKey: The specified key does not exist.
        status code: 404, request id: [REDACTED_REQUEST_ID], host id: [REDACTED_HOST_ID]
```

We are using TiDB v7.5.6. Could you please help us debug this error?

Thank you

## Recent Comments Excerpt

### 2025-11-20T14:01:30.004+0800 [REDACTED_USER]

Oops. This should need a KB.

### 2025-11-21T14:15:38.856+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b5d3476b134a8c49e27930c4e4fc) by lark and phone

### 2025-11-21T14:15:40.714+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2025-11-21T14:16:44.393+0800 [REDACTED_USER]

this PR will fix the issue 
https://github.com/tikv/tikv/pull/19125

### 2025-11-21T14:18:08.053+0800 [REDACTED_USER]

Response(not ack for Critical alert) in lark: om_x100b5d3476b134a8c49e27930c4e4fc
