# Issue 57447: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57447
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-11-18T03:25:52Z
- Updated: 2024-11-18T03:26:15Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR, Storage, PD
- Categories: backup-failure, storage-access, checkpoint-retry, performance-resource, observability-diagnosis
- Labels: component/br, severity/moderate, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; PD; Restore; Storage; TiDB; TiKV; backup-failure; checkpoint-retry; observability-diagnosis; performance-resource; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1. running br backup full command, and somehow it failed to connect to PD

### 2. [REDACTED_USER]
1. backup should fail, and error prompt should be accurate

### 3. [REDACTED_USER]
1. error information not accurate, it complains "running BR in incompatible version of cluster", actually br and tidb cluster is same version, and rerun the backup can be successful.

```
[2024/11/18 03:13:35.376 +00:00] [INFO] [meminfo.go:179] ["use cgroup memory hook because TiDB is in the container"]
[2024/11/18 03:13:35.376 +00:00] [INFO] [info.go:52] ["Welcome to Backup & Restore (BR)"] [release-version=v8.1.1] [git-hash=a7df4f9845d5d6a590c5d45dad0dcc9f21aa8765] [git-branch=HEAD] [go-version=go1.21.13] [utc-build-time="2024-08-22 05:51:39"] [race-enabled=false]
[2024/11/18 03:13:35.376 +00:00] [INFO] [common.go:755] [arguments] [__command="br backup full"] [checksum-concurrency=64] [concurrency=128] [ignore-stats=false] [pd="[http://downstream-pd:2379]"] [storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
[2024/11/18 03:13:35.378 +00:00] [INFO] [conn.go:159] ["new mgr"] [pdAddrs="[downstream-pd:2379]"]
[2024/11/18 03:13:35.381 +00:00] [INFO] [pd_service_discovery.go:991] ["[pd] update member urls"] [old-urls="[http://downstream-pd:2379]"] [new-urls="[http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379,http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379,http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379]"]
[2024/11/18 03:13:35.381 +00:00] [INFO] [pd_service_discovery.go:1016] ["[pd] switch leader"] [new-leader=http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379] [old-leader=]
[2024/11/18 03:13:35.381 +00:00] [INFO] [pd_service_discovery.go:498] ["[pd] init cluster id"] [cluster-id=[REDACTED_LONG_ID]
[2024/11/18 03:13:36.382 +00:00] [WARN] [pd_service_discovery.go:509] ["[pd] failed to check service mode and will check later"] [error="[PD:client:ErrClientGetClusterInfo]error:rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp: lookup [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc: i/o timeout\" target:[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379 status:TRANSIENT_FAILURE: error:rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp: lookup [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc: i/o timeout\" target:[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379 status:TRANSIENT_FAILURE"]
[2024/11/18 03:13:36.384 +00:00] [INFO] [collector.go:224] ["units canceled"] [cancel-unit=0]
[2024/11/18 03:13:36.384 +00:00] [INFO] [collector.go:78] ["Full Backup failed summary"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0]
[2024/11/18 03:13:36.384 +00:00] [WARN] [resource_manager_client.go:302] ["[resource_manager] get token stream error"] [error="rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp: lookup [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc: i/o timeout\""]
[2024/11/18 03:13:36.384 +00:00] [INFO] [resource_manager_client.go:290] ["[resource manager] exit resource token dispatcher"]
[2024/11/18 03:13:36.384 +00:00] [INFO] [pd_service_discovery.go:910] ["[pd] cannot update member from this url"] [url=http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379] [error="[PD:client:ErrClientGetMember]error:rpc error: code = Canceled desc = context canceled target:[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379 status:TRANSIENT_FAILURE: error:rpc error: code = Canceled desc = context canceled target:[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379 status:TRANSIENT_FAILURE"]
[2024/11/18 03:13:36.384 +00:00] [ERROR] [backup.go:57] ["failed to backup"] [error="running BR in incompatible version of cluster, if you believe it's OK, use --check-requirements=false to skip.: rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp: lookup [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc: i/o timeout\""] [errorVerbose="rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp: lookup [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc: i/o timeout\"\ngithub.com/tikv/pd/client.(*client).respForErr\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-10ecdbe92b55/client.go:1580\ngithub.com/tikv/pd/client.(*client).GetAllStores\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-10ecdbe92b55/client.go:1202\ngithub.com/pingcap/tidb/br/pkg/version.CheckClusterVersion\n\t/workspace/source/tidb/br/pkg/version/version.go:89\ngithub.com/pingcap/tidb/br/pkg/conn.NewMgr\n\t/workspace/source/tidb/br/pkg/conn/conn.go:176\ngithub.com/pingcap/tidb/br/pkg/task.NewMgr\n\t/workspace/source/tidb/br/pkg/task/common.go:651\ngithub.com/pingcap/tidb/br/pkg/task.RunBackup\n\t/workspace/source/tidb/br/pkg/task/backup.go:406\nmain.runBackupCommand\n\t/workspace/source/tidb/br/cmd/br/backup.go:56\nmain.newFullBackupCommand.func1\n\t/workspace/source/tidb/br/cmd/br/backup.go:148\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\nrunning BR in incompatible version of cluster, if you believe it's OK, use --check-requirements=false to skip."] [stack="main.runBackupCommand\n\t/workspace/source/tidb/br/cmd/br/backup.go:57\nmain.newFullBackupCommand.func1\n\t/workspace/source/tidb/br/cmd/br/backup.go:148\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267"]
[2024/11/18 03:13:36.384 +00:00] [ERROR] [pd_service_discovery.go:559] ["[pd] failed to update member"] [urls="[http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379,http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379,http://[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc:2379]"] [error="context canceled"] [errorVerbose="context canceled\ngithub.com/pingcap/errors.AddStack\n\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/errors.go:178\ngithub.com/pingcap/errors.Trace\n\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/juju_adaptor.go:15\ngithub.com/tikv/pd/client/retry.(*Backoffer).Exec\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-10ecdbe92b55/retry/backoff.go:94\ngithub.com/tikv/pd/client.(*pdServiceDiscovery).updateMemberLoop\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-10ecdbe92b55/pd_service_discovery.go:558\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650"] [stack="github.com/tikv/pd/client.(*pdServiceDiscovery).updateMemberLoop\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-10ecdbe92b55/pd_service_discovery.go:559"]
[2024/11/18 03:13:36.384 +00:00] [INFO] [pd_service_discovery.go:550] ["[pd] exit member loop due to context canceled"]
[2024/11/18 03:13:36.384 +00:00] [ERROR] [main.go:38] ["br failed"] [error="running BR in incompatible version of cluster, if you believe it's OK, use --check-requirements=false to skip.: rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp: lookup [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc: i/o timeout\""] [errorVerbose="rpc error: code = Unavailable desc = connection error: desc = \"transport: Error while dialing: dial tcp: lookup [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].svc: i/o timeout\"\ngithub.com/tikv/pd/client.(*client).respForErr\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-10ecdbe92b55/client.go:1580\ngithub.com/tikv/pd/client.(*client).GetAllStores\n\t/root/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-10ecdbe92b55/client.go:1202\ngithub.com/pingcap/tidb/br/pkg/version.CheckClusterVersion\n\t/workspace/source/tidb/br/pkg/version/version.go:89\ngithub.com/pingcap/tidb/br/pkg/conn.NewMgr\n\t/workspace/source/tidb/br/pkg/conn/conn.go:176\ngithub.com/pingcap/tidb/br/pkg/task.NewMgr\n\t/workspace/source/tidb/br/pkg/task/common.go:651\ngithub.com/pingcap/tidb/br/pkg/task.RunBackup\n\t/workspace/source/tidb/br/pkg/task/backup.go:406\nmain.runBackupCommand\n\t/workspace/source/tidb/br/cmd/br/backup.go:56\nmain.newFullBackupCommand.func1\n\t/workspace/source/tidb/br/cmd/br/backup.go:148\ngithub.com/spf13/cobra.(*Command).execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:983\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1115\ngithub.com/spf13/cobra.(*Command).Execute\n\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.0/command.go:1039\nmain.main\n\t/workspace/source/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650\nrunning BR in incompatible version of cluster, if you believe it's OK, use --check-requirements=false to skip."] [stack="main.main\n\t/workspace/source/tidb/br/cmd/br/main.go:38\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:267"]

```
### 4. [REDACTED_USER]

[release-version=v8.1.1]
[git-hash=a7df4f9845d5d6a590c5d45dad0dcc9f21aa8765]
