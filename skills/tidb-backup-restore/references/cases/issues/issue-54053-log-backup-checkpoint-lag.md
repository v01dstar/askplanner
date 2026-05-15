# Issue 54053: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/54053
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2024-06-17T07:53:05Z
- Updated: 2024-06-19T08:56:49Z
- Closed: 2024-06-19T08:56:49Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Import
- Components: TiDB, TiKV, BR, Lightning
- Categories: restore-failure, region-split-scatter, sst-ingest-import, checkpoint-retry
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Import; Lightning; TiDB; TiKV; checkpoint-retry; region-split-scatter; restore-failure; sst-ingest-import

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br restore
2、inject network partition between one of tikv and other pods last for 3mins

### 2. [REDACTED_USER]
br restore can success

### 3. [REDACTED_USER]
br restore failed when injection network partition between one of tikv and other pods

`"download file failed"] [files="{total=1,files=\"[4_44722_1354_b077a553d62445e72046f59e7616693bf929d6284e7895610f0ebea47059ec57_1638173205994_write.sst]\",totalKVs=410870,totalBytes=88747920,totalSize=40516977}"] [region="{ID=7888,startKey=7480000000000000FFFA5F728000000001FFE62B060000000000FA,endKey=7480000000000000FFFA5F728000000001FFEC97DA0000000000FA,epoch=\"conf_ver:23 version:845 \",peers=\"id:7889 store_id:1 ,id:7891 store_id:4 ,id:8040 store_id:8 \"}"] [startKey=7480000000000000FFFA5F728000000001FFE62B060000000000FA] [endKey=7480000000000000FFFA5F728000000001FFEC97DA0000000000FA] [error="rpc error: code = Unavailable desc = error reading from server: read tcp [[REDACTED_IP]:38220](http://[REDACTED_IP]:38220/)->[[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): read: connection timed out; rpc error: code = Unavailable desc = connection error: desc = \"transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): i/o timeout\"; rpc error: code = Unavailable desc = connection error: desc = \"transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): i/o timeout\"; rpc error: code = Unavailable desc = connection error: desc = \"transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): i/o timeout\"; rpc error: code = Unavailable desc = connection error: desc = \"transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): i/o timeout\"; rpc error: code = Unavailable desc = connection error: desc = \"transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): i/o timeout\"; rpc error: code = Unavailable desc = connection error: desc = \"transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): i/o timeout\"; rpc error: code = Unavailable desc = connection error: desc = \"transport: error while dialing: dial tcp [[REDACTED_IP]:20160](http://[REDACTED_IP]:20160/): i/o timeout\""] [stack="[github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:523\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:216\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:234\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:215\ngithub.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:492\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1183\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.7.0/errgroup/errgroup.go:78](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles.func1/n/t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:523/ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry.func1/n/t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:216/ngithub.com/pingcap/tidb/br/pkg/utils.WithRetryV2[...]/n/t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:234/ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry/n/t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:215/ngithub.com/pingcap/tidb/br/pkg/restore.(*FileImporter).ImportSSTFiles/n/t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:492/ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).RestoreSSTFiles.func2/n/t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1183/ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1/n/t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76/ngolang.org/x/sync/errgroup.(*Group).Go.func1/n/t/go/pkg/mod/golang.org/x/sync@v0.7.0/errgroup/errgroup.go:78)"]`

### 4. [REDACTED_USER]
./tidb-server -V
Release Version: v6.5.10
Edition: Community
Git Commit Hash: https://github.com/pingcap/tidb/commit/23062507bab86d03a616c2793607c3f4dd349235
Git Branch: heads/refs/tags/v6.5.10
UTC Build Time: 2024-06-12 08:25:43
GoVersion: go1.19.13
Race Enabled: false
TiKV Min Version: 6.2.0-alpha
Check Table Before Drop: false
Store: unistore
2024-06-13T06:58:24.395+0800
