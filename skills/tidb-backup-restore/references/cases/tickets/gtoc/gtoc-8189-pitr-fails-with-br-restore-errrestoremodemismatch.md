# GTOC-8189: PITR fails with [BR:Restore:ErrRestoreModeMismatch]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8189
- Status: Todo
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2026-01-29T14:06:05.706+0800
- Updated: 2026-01-30T13:38:25.836+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi, we are currently onboarding onto logical backup and restore on the [REDACTED_ENV_NAME] cluster. When attempting a restore from a logical snapshot, it is blocked by the following error:

```
[2026/01/28 18:06:33.280 +00:00] [ERROR] [main.go:38] ["br failed"] [error="Clustered index option mismatch. Restored cluster's @@tidb_enable_clustered_index should be OFF (backup table = false, created table = true).: [BR:Restore:ErrRestoreModeMismatch]restore mode mismatch"] [errorVerbose="[BR:Restore:ErrRestoreModeMismatch]restore mode mismatch\nClustered index option mismatch. Restored cluster's @@tidb_enable_clustered_index should be OFF (backup table = false, created table = true).\ngithub.com/pingcap/tidb/br/pkg/task.PreCheckTableClusterIndex\n\t/tidb/br/pkg/task/restore.go:1525\ngithub.com/pingcap/tidb/br/pkg/task.runSnapshotRestore\n\t/tidb/br/pkg/task/restore.go:1005\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/tidb/br/pkg/task/restore.go:740\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:75\nmain.newFullRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:181\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/tidb/br/cmd/br/main.go:37\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1700"] [stack="main.main\n\t/tidb/br/cmd/br/main.go:38\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:272"]
```

This is saying that the table in the backup desires clustered indexes to be disabled but the destination cluster has it enabled (which is the default behavior)

However, when I checked the source cluster, the variable is set to ON:

```
SELECT @@global.tidb_enable_clustered_index;
+--------------------------------------+
| @@global.tidb_enable_clustered_index |
+--------------------------------------+
| ON                                   |
+--------------------------------------+
```

Is it possible that this is somehow encoded at the table level in the backup and corresponds to when the table was originally created (probably in an older version of tidb)? If so, any suggestions for how to work around it? We probably have tables that are both clustered and nonclustered index, so it sounds like the option _should_ be ON.

Full LogicalRestore CR:

```
% kubectl --context=m-[REDACTED_ENV_NAME] -n [REDACTED_ENV_NAME] get logrt [REDACTED_ENV_NAME] -o yaml
apiVersion: tidb.airbnb.com/v1
kind: LogicalRestore
metadata:

## Recent Comments Excerpt

### 2026-01-29T14:06:11.748+0800 [REDACTED_USER]

assign to 陈青璟([REDACTED_EMAIL])

### 2026-01-29T14:06:13.587+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), om_x100b589bc383c8a4c4dc3cbe20f8b8d) by lark
