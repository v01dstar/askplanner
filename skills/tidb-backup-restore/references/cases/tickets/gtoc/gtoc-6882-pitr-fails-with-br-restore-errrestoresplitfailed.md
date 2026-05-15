# GTOC-6882: PITR fails with [BR:Restore:ErrRestoreSplitFailed]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6882
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-04-30T00:33:51.000+0800
- Updated: 2025-03-06T18:13:16.512+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

The import failed on the TiDB cluster with the following error messages:

```
[2024/04/28 03:27:44.898 +00:00] [ERROR] [pipeline_items.go:325] ["failed on split range"] [ranges="{total=1024,ranges=\"[\\\"[7480000000000000045F69800000000000000100, 7480000000000000045F698000000000000001FB)\\\",\\\"(skip 1022)\\\",\\\"[74800000000000006C5F72014965356339633461FF3362633830346530FF6639613435633539FF3961633361336636FF3100000000000000F8, 74800000000000006C5F72014A30346661313034FF3033666139346333FF3762393230656165FF6264313630623263FF3800000000000000F8)\\\"]\",totalFiles=1024,totalKVs=1360093912,totalBytes=[REDACTED_LONG_ID],totalSize=[REDACTED_LONG_ID]}"] [error="split region failed: err=message:\"EpochNotMatch [region 603112632] 603113276 epoch changed conf_ver: 465125 version: 8804259 != conf_ver: 465125 version: 8803235, retry later\" epoch_not_match:<current_regions:<id:603112632 start_key:\"t\\200\\000\\000\\000\\000\\000\\001\\377\\307_r\\001\\0356b9\\377db4f\\3774a3\\37700444\\37748\\377296a16\\3779\\3779c2cee9\\377\\3774\\000\\000\\000\\000\\000\\000\\000\\377\\370\\000\\000\\000\\000\\000\\000\\000\\370\" end_key:\"x\\000\\000\\000\\000\\000\\000\\000\\373\" region_epoch:<conf_ver:465125 version:8804259 > peers:<id:603113276 store_id:349848090 > peers:<id:603113275 store_id:453795301 > peers:<id:606886396 store_id:453682591 > > > : [BR:Restore:ErrRestoreSplitFailed]fail to split region"] [errorVerbose="[BR:Restore:ErrRestoreSplitFailed]fail to split region\nsplit region failed: err=message:\"EpochNotMatch [region 603112632] 603113276 epoch changed conf_ver: 465125 version: 8804259 != conf_ver: 465125 version: 8803235, retry later\" epoch_not_match:<current_regions:<id:603112632 start_key:\"t\\200\\000\\000\\000\\000\\000\\001\\377\\307_r\\001\\0356b9\\377db4f\\3774a3\\37700444\\37748\\377296a16\\3779\\3779c2cee9\\377\\3774\\000\\000\\000\\000\\000\\000\\000\\377\\370\\000\\000\\000\\000\\000\\000\\000\\370\" end_key:\"x\\000\\000\\000\\000\\000\\000\\000\\373\" region_epoch:<conf_ver:465125 version:8804259 > peers:<id:603113276 store_id:349848090 > peers:<id:603113275 store_id:453795301 > peers:<id:606886396 store_id:453682591 > > > \ngithub.com/pingcap/tidb/br/pkg/restore/split.sendSplitRegionRequest\n\t/mnt/tidb/sql/br/pkg/restore/split/client.go:370\ngithub.com/pingcap/tidb/br/pkg/restore/split.(*pdClient).sendSplitRegionRequest\n\t/mnt/tidb/sql/br/pkg/restore/split/client.go:315\ngithub.com/pingcap/tidb/br/pkg/restore/split.(*pdClient).BatchSplitRegionsWithOrigin\n\t/mnt/tidb/sql/br/pkg/restore/split/client.go:413\ngithub.com/pingcap/tidb/br/pkg/restore/split.(*pdClient).BatchSplitRegions\n\t/mnt/tidb/sql/br/pkg/restore/split/client.go:452\ngithub.com/pingcap/tidb/br/pkg/restore.(*RegionSplitter).splitAndScatterRegions\n\t/mnt/tidb/sql/br/pkg/restore/split.go:265\ngithub.com/pingcap/tidb/br/pkg/restore.(*RegionSplitter).Split\n\t/mnt/tidb/sql/br/pkg/restore/split.go:105\ngithub.com/pingcap/tidb/br/pkg/restore.SplitRanges\n\t/mnt/tidb/sql/br/pkg/restore/util.go:507\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).SplitRanges\n\t/mnt/tidb/sql/br/pkg/restore/client.go:1315\ngithub.com/pingcap/tidb/br/pkg/restore.(*tikvSender).splitWorker.func3\n\t/mnt/tidb/sql/br/pkg/restore/pipeline_items.go:323\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/mnt/tidb/sql/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.2.0/errgroup/errgroup.go:75\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1598"] [stack="github.com/pingcap/tidb/br/pkg/restore.(*tikvSender).splitWorker.func3\n\t/mnt/tidb/sql/br/pkg/restore/pipeline_items.go:325\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/mnt/tidb/sql/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.2.0/errgroup/errgroup.go:75"]
```

The backup was initiated using command:

```
[__command="br restore full"] [ca=/var/lib/normandie/fuse/ca/root] [cert=/var/lib/normandie/fuse/chain/generic] [checksum=false] [concurrency=1024] [key=/var/lib/normandie/fuse/key/generic] [log-file=/var/log/tidb/br.log] [pd="[[REDACTED_ENV_NAME].ec2.pin220.com:2379]"] [ratelimit=0] [s3.region=us-east-1] [send-credentials-to-tikv=false] [storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
```

Backup start time: \[2024/04/28 03:26:59.118 +00:00\]

## Recent Comments Excerpt

### 2024-05-30T16:13:06.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/May/24 8:12 AM

This ticket has been updated by L3 team, please take a look

### 2024-06-07T00:23:49.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Jun/24 4:23 PM

The root cause was unable to determine as the logs were rotated form the hosts.

### 2024-06-08T01:03:39.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 07/Jun/24 5:03 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-06-11T01:06:36.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 10/Jun/24 5:06 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-06-14T01:04:46.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/Jun/24 5:04 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
