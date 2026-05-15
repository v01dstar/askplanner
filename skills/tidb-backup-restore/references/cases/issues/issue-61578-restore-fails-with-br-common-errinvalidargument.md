# Issue 61578: Restore fails with [BR:Common:ErrInvalidArgument]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61578
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-06-09T04:02:26Z
- Updated: 2025-11-27T02:45:43Z
- Closed: 2025-06-16T23:20:13Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: restore-failure, schema-metadata, performance-resource
- Labels: affects-8.5, component/br, feature/developing, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Restore fails with [BR:Common:ErrInvalidArgument]`
- Search terms: BR; Restore; TiDB; TiKV; performance-resource; restore-failure; schema-metadata

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->
1. The br node with smaller CPU and memory starts a large data restore task, forcing the br oom
2. Expand the capacity of the br node and restart restore task

### 2. [REDACTED_USER]
restore success

### 3. [REDACTED_USER]
Restore failed! 
The task in `mysql.tidb_restore_registry` is still in running mode.

> mysql> select * from mysql.tidb_restore_registry;
> +----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+----------+-------------+---------------------+----------------+---------+--------------+----------------------------+----------------------------+
> | id | filter_strings                                                                                                                                                                                                                                                                      | filter_hash                      | start_ts | restored_ts | upstream_cluster_id | with_sys_table | status  | cmd          | task_start_time            | last_heartbeat_time        |
> +----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+----------+-------------+---------------------+----------------+---------+--------------+----------------------------+----------------------------+
> |  1 | *.*!__TiDB_BR_Temporary_*.*!mysql.*mysql.bind_infomysql.usermysql.dbmysql.tables_privmysql.columns_privmysql.global_privmysql.global_grantsmysql.default_rolesmysql.role_edges!sys.*!INFORMATION_SCHEMA.*!PERFORMANCE_SCHEMA.*!METRICS_SCHEMA.*!INSPECTION_SCHEMA.* | 2688546865cf9b7f4c35bebfdfc7e5e5 |        0 |           0 | [REDACTED_LONG_ID] |              1 | running | Full Restore | 2025-06-09 03:23:34.652232 | 2025-06-09 03:23:34.660559 |
> +----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+----------+-------------+---------------------+----------------+---------+--------------+----------------------------+----------------------------+

`[2025/06/09 03:33:28.025 +00:00] [ERROR] [main.go:38] ["br failed"] [error="task with ID 1 already exists and is running: [BR:Common:ErrInvalidArgument]invalid argument"] [errorVerbose="[BR:Common:ErrInvalidArgument]invalid argument\ntask with ID 1 already exists and is running\ngithub.com/pingcap/tidb/br/pkg/registry.(*Registry).ResumeOrCreateRegistration.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/registry/registration.go:233\ngithub.com/pingcap/tidb/br/pkg/registry.(*Registry).executeInTransaction\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/registry/registration.go:178\ngithub.com/pingcap/tidb/br/pkg/registry.(*Registry).ResumeOrCreateRegistration\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/registry/registration.go:210\ngithub.com/pingcap/tidb/br/pkg/task.RegisterRestoreIfNeeded\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:2148\ngithub.com/pingcap/tidb/br/pkg/task.runSnapshotRestore\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/restore.go:1162\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/restore.go:938\nmain.runRestoreCommand\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/restore.go:75\nmain.newFullRestoreCommand.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/restore.go:181\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1700"] [stack="main.main\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/main.go:38\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272"]`


### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
Release Version: v8.5.0-20250609-a850b6f
Edition: Community
Git Commit Hash: a850b6f2634ee51c32b2ab8623c78035186e1278
Git Branch: heads/refs/tags/v8.5.0-20250609-a850b6f
UTC Build Time: 2025-06-09 02:24:01
GoVersion: go1.23.3
Race Enabled: false
Check Table Before Drop: false
Store: tikv
