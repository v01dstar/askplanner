# GTOC-7551: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7551
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-04-24T09:06:49.689+0800
- Updated: 2025-11-28T10:28:43.638+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

I’m validating TiDB PITR restore functionality on UDS full shadow cluster (at scale we expect to run workload in productions) and observe OOM errors in the br process. OOM happens during the “Restore KV Files” phase of the process. BR process' RSS grows rapidly and hits 94GiB (our current container limit) before being killed by Linux kernel (due to cgroup memory limit).

Attached are:

* Full BR process logs
* Restore container memory usage (working set is shown, but RSS is strictly following working set usage)
* Restore container CPU usage
* k8s restore object showing the failure

When looking into the issue, I make following observations:

There is a gap (close to an hour) between generating rewrite rules and starting KV restore, relevant log snippet.

```
Apr 22, 2025 @ 04:09:41.123	I0422 11:09:41.123899       9 restore.go:176] [2025/04/22 11:09:41.117 +00:00] [INFO] [progress.go:176] [progress] [step="Restore KV Files"] [progress=0.00%] [count="0 / 291937359"] [speed="? p/s"] [elapsed=2m0s] [remaining=?]
	Apr 22, 2025 @ 03:14:49.197	I0422 10:14:49.197168       9 restore.go:176] [2025/04/22 10:14:49.193 +00:00] [INFO] [stream.go:1778] ["add rewrite rule"] [tableName=[REDACTED_RESOURCE_NAME] [oldID=41242] [newID=41242]
```

While it is not related to OOM, I want to understand what exactly br process is doing here. I believe it is scanning backup files through the iterator, filtering out data files which are earlier that startTS. Can you confirm that?

11:09:49 – 11:25:41, BR process is using a lot of CPU, but is not making any progress:

```
Apr 22, 2025 @ 04:27:41.124	I0422 11:27:41.124089       9 restore.go:176] [2025/04/22 11:27:41.117 +00:00] [INFO] [progress.go:176] [progress] [step="Restore KV Files"] [progress=0.08%] [count="222800 / 291937359"] [speed="143 p/s"] [elapsed=20m0s] [remaining=568h30m34s]
	Apr 22, 2025 @ 04:25:41.123	I0422 11:25:41.123347       9 restore.go:176] [2025/04/22 11:25:41.117 +00:00] [INFO] [progress.go:176] [progress] [step="Restore KV Files"] [progress=0.00%] [count="3133 / 291937359"] [speed="26 p/s"] [elapsed=18m0s] [remaining=3104h45m37s]
	Apr 22, 2025 @ 04:23:41.177	I0422 11:23:41.177027       9 restore.go:176] [2025/04/22 11:23:41.165 +00:00] [INFO] [progress.go:176] [progress] [step="Restore KV Files"] [progress=0.00%] [count="0 / 291937359"] [speed="? p/s"] [elapsed=16m0s] [remaining=?]
	Apr 22, 2025 @ 04:21:41.123	I0422 11:21:41.123793       9 restore.go:176] [2025/04/22 11:21:41.117 +00:00] [INFO] [progress.go:176] [progress] [step="Restore KV Files"] [progress=0.00%] [count="0 / 291937359"] [speed="? p/s"] [elapsed=14m0s] [remaining=?]
	Apr 22, 2025 @ 04:19:41.124	I0422 11:19:41.124099       9 restore.go:176] [2025/04/22 11:19:41.117 +00:00] [INFO] [progress.go:176] [progress] [step="Restore KV Files"] [progress=0.00%] [count="0 / 291937359"] [speed="? p/s"] [elapsed=12m0s] [remaining=?]

## Recent Comments Excerpt

### 2025-11-27T12:14:56.097+0800 [REDACTED_USER]

Noticed many “txn entry is null” in the log file.
~> cat [REDACTED_ENV_NAME].log | rg 'txn entry is null' | wc -l
89976
Check 
goroutine
 again, I noticed:
github.com/pingcap/tidb/br/pkg/stream.(*MetadataHelper).ReadFile(0xc1abb84510, {0x7644810, 0xc00404d630}, {0xc3bbbadc20, 0x5f}, 0x0, 0x193e6ec1, 0x3, {0x766a860, 0xc0c36f1d70}, ...)
The arguments of

### 2025-11-27T12:25:28.381+0800 [REDACTED_USER]

Memo: also it seems there are some keys presenting many times in the 
txn entry is null
 log:
    279 "mDB:80\u0000\u0000\ufffd\u0000\ufffd\u0000\u0000\u0000\u0000\u0000\u0000\ufffd\u0000hTID:36\ufffd24\ufffd4\u0000\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\u0000\ufffd\ufffd\ufffd\ufffd_\ufffd\ufffd\ufffd\ufffd"
    286 "mDB:80\u0000\u0000\ufffd\u0000\ufffd\u0000\u0000\u0000\u0000\u0000\u0000\ufffd\u0000hTID:36\ufffd24\ufffd4\u0000\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\u0000\ufffd\ufffd\ufffd\u0013k\ufffd\ufffd\ufffd\ufffd"
    303 "mDB:80\u0000\u0000\ufffd\u0000\ufffd\u0000\u0000\u0000\u0000\u0000\u0000\ufffd\u0000hTID:36\ufffd24\ufffd4\u0000\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\u0000\ufffd\ufffd\ufffd\ufffdb\ufffd\ufffd\ufffd\ufffd"
    328 "mDB:80\u0000\u0000\ufffd\u0000\ufffd\u0000\u0000\u0000\u0000\u0000\u0000\ufffd\u0000hTID:36\ufffd24\ufffd4\u0000\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\u0000\ufffd\ufffd\ufffd\u000fG\ufffd\ufffd\ufffd\ufffd"
    370 "mDB:80\u0000\u0000\ufffd\u0000\ufffd\u0000\u0000\u0000\u0000\u0000\u0000\ufffd\u0000hTID:36\ufffd24\ufffd4\u0000\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\ufffd\u0000\u0000\u0000\u0000\ufffd\ufffd\ufffd\u0013g\ufffd\ufffd\ufffd\ufffd"

### 2025-11-27T12:31:01.494+0800 [REDACTED_USER]

Memo': The batch
github.com/pingcap/tidb/br/pkg/restore/log_client.(*LogClient).RestoreBatchMetaKVFiles(0xc04e9c77a0, {0x7644810, 0xc00404d630}, {0xc0700b7810, 0x564, 0x59c7305?}, 0xc08287dc70, {0xc03aade000, 0x67a7, 0x6c00}, ...)
Arguments:
github.com/pingcap/tidb/br/pkg/restore/log_client.(*LogClient).RestoreBatchMetaKVFiles(
  0xc04e9c77a0,                                   // LogClient receiver (this pointer)
  {0x7644810, 0xc00404d630},                      // ctx context.Context (interface fat pointer)
  {0xc0700b7810, 0x564, 0x59c7305?},              // files []*backuppb.DataFileInfo (data ptr, len=1380, cap≈0x59c7305)
  0xc08287dc70,                                   // schemasReplace *stream.SchemasReplace mapper

### 2025-11-27T21:32:04.245+0800 [REDACTED_USER]

@[REDACTED_USER]
 , Airbnb is working on cherry-picking log compaction feature to their branch to see if that would address OOM issue. The purpose of the uploaded files is to see if OOM was caused by something else, i.e,   some other causes that are not addressed by log compaction.

### 2025-11-28T10:28:43.638+0800 [REDACTED_USER]

@[REDACTED_USER]
  IMO this can be a new issue. It seems a huge batch was made during restoring.
