# GTOC-7739: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7739
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-07-04T03:27:32.293+0800
- Updated: 2025-12-05T01:14:18.482+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

The BR log backup job is paused when the TiDB SQL node ownership is changed. 

The information in the TiDB SQL logs:

```
{"level":"INFO","time":"2025/07/02 20:23:04.203 +00:00","caller":"advancer.go:315","message":"current last region","category":"log backup advancer hint","min":"([74, 7480000000000000DB5F720100221701A0000000FF6CF7CE011040AB07FF0000000000000000F7), 0)","for-polling":31965,"min-ts":"1970-01-01T00:00:00Z","region-hint":"ID=242782,Leader=568323518,ConfVer=81431,Version=286,Peers=[812665 568325652 568323518],RealRange=[72000001, 7480000000000000405F7280000000000D48F7)"}

{"level":"WARN","time":"2025/07/02 20:23:05.795 +00:00","caller":"advancer.go:709","message":"resolve locks failed, wait for next tick","category":"advancer","uuid":"log backup advancer","error":"unexpected scanlock error: error:<locked:<primary_lock:\"t\\200\\000\\000\\000\\000\\000\\000\\361_r\\202\\270%B<\\211\\362\\230\" lock_version:[REDACTED_LONG_ID] key:\"t\\200\\000\\000\\000\\000\\000\\000\\361_r\\202\\361\\304\\000\\233\\207\\247\\230\" lock_ttl:20003 txn_size:1 lock_for_update_ts:[REDACTED_LONG_ID] use_async_commit:true min_commit_ts:[REDACTED_LONG_ID] > > ","errorVerbose":"unexpected scanlock error: error:<locked:<primary_lock:\"t\\200\\000\\000\\000\\000\\000\\000\\361_r\\202\\270%B<\\211\\362\\230\" lock_version:[REDACTED_LONG_ID] key:\"t\\200\\000\\000\\000\\000\\000\\000\\361_r\\202\\361\\304\\000\\233\\207\\247\\230\" lock_ttl:20003 txn_size:1 lock_for_update_ts:[REDACTED_LONG_ID] use_async_commit:true min_commit_ts:[REDACTED_LONG_ID] > > \ngithub.com/tikv/client-go/v2/tikv.scanLocksInOneRegionWithStartKey\n\t/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-f8e321f39dd5/tikv/gc.go:258\ngithub.com/tikv/client-go/v2/tikv.(*BaseRegionLockResolver).ScanLocksInOneRegion\n\t/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-f8e321f39dd5/tikv/gc.go:134\ngithub.com/tikv/client-go/v2/tikv.ResolveLocksForRange\n\t/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-f8e321f39dd5/tikv/gc.go:189\ngithub.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).asyncResolveLocksForRanges.func1.2\n\t/mnt/tidb/sql/br/pkg/streamhelper/advancer.go:690\ngithub.com/tikv/client-go/v2/txnkv/rangetask.(*rangeTaskWorker).run\n\t/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-f8e321f39dd5/txnkv/rangetask/range_task.go:339\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\ngithub.com/tikv/client-go/v2/txnkv/rangetask.(*Runner).RunOnRange\n\t/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-f8e321f39dd5/txnkv/rangetask/range_task.go:272\ngithub.com/pingcap/tidb/br/pkg/streamhelper.(*CheckpointAdvancer).asyncResolveLocksForRanges.func1.3\n\t/mnt/tidb/sql/br/pkg/streamhelper/advancer.go:706\ngithub.com/pingcap/tidb/pkg/util.(*WorkerPool).Apply.func1\n\t/mnt/tidb/sql/pkg/util/worker_pool.go:63\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650"}

{"level":"INFO","time":"2025/07/02 20:23:05.795 +00:00","caller":"advancer.go:716","message":"finish resolve locks for checkpoint","category":"advancer","uuid":"log backup advancer","StartKey":"","EndKey":"","targets":2}

{"level":"WARN","time":"2025/07/02 20:23:06.215 +00:00","caller":"advancer_cliext.go:285","message":"skipping upload global checkpoint","category":"log backup advancer","old":[REDACTED_LONG_ID],"new":[REDACTED_LONG_ID]}

{"level":"WARN","time":"2025/07/02 20:23:06.215 +00:00","caller":"advancer.go:579","message":"checkpoint lag is too large","category":"log backup advancer","lag":"465h25m36.432s"}

{"level":"WARN","time":"2025/07/02 20:23:06.217 +00:00","caller":"advancer.go:676","message":"important tick failed.","category":"log backup advancer","error":"check point lagged too large: check point lagged too large"}

{"level":"INFO","time":"2025/07/02 20:23:06.218 +00:00","caller":"advancer.go:397","message":"Meet task event","category":"log backup advancer","event":"Pause(pitr1)"}
```

```
br log status

Detail BR log in /tmp/br.log.2025-07-03T18.39.08Z 

● Total 1 Tasks.

> #1 <

## Recent Comments Excerpt

### 2025-07-08T14:24:00.063+0800 [REDACTED_USER]

There is a cluster in cloud encountering similar problem. We have checked its heap profile and found that:
It seems during initial scanning, most of memory was used by the index and bloom filter blocks.
[REDACTED_MEDIA]
This symptom is also found at the compaction stack:
[REDACTED_MEDIA]
Though reading actual content of SSTs mainly allocates memory by 
UncompressBlock
…

### 2025-07-11T17:14:41.239+0800 [REDACTED_USER]

Regardless of the root cause, heap profiling clearly indicates that the majority of memory consumption is concentrated in the event_loader::fill_entries function（which is part of incremental scanning)

Current configuration parameters for incremental scanning primarily limit the volume of actual data being scanned. According to monitoring data, memory usage appears to remain within the 512MB limit. However, this does 
not fully represent total memory consumption
, especially considering the involvement of RocksDB, where indirect or unmanaged memory usage may not be accounted for.

Based on this, we believe there are two possible explanations:
Scenario 1: Code-level memory accounting or cleanup issue

### 2025-07-17T00:59:50.826+0800 [REDACTED_USER]

@[REDACTED_USER]
 Is there any Github issue link that can be shared with the customer?

### 2025-07-18T11:00:25.937+0800 [REDACTED_USER]

https://github.com/tikv/tikv/issues/18719

### 2025-07-18T13:34:22.959+0800 [REDACTED_USER]

@[REDACTED_USER]
 
https://github.com/tikv/tikv/issues/18719
  Juncen has filed an issue on github. PTAL
