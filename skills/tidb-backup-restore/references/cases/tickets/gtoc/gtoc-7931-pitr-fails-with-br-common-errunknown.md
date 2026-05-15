# GTOC-7931: PITR fails with [BR:Common:ErrUnknown]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7931
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-10-02T03:50:38.980+0800
- Updated: 2026-01-13T20:54:30.182+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We had an incident earlier this week in staging that required us to rebuild all of our TiDB clusters from scratch and restore them using backups. During this we ran into two different issues. The first one was a strange issue that seems to be a tidb internal issue:

```
cluster [REDACTED_CLUSTER]/[REDACTED_ENV_NAME], wait pipe message failed, errMsg [2025/10/01 19:25:57.974 +00:00] [ERROR] [restore.go:76] ["failed to restore"]
 [error="error during merging temporary tables into system tables, table: global_grants: [BR:Common:ErrUnknown]failed to execute REPLACE INTO `mysql`.`global_grants`(`user`,`host`,`priv`,`with_grant_option`) SELECT `user`,`hos
t`,`priv`,`with_grant_option` FROM `__tidb_br_temporary_mysql`.`global_grants`;: [schema:1146]Table '__tidb_br_temporary_mysql.global_grants' doesn't exist"] [errorVerbose="[BR:Common:ErrUnknown]failed to execute REPLACE INTO
`mysql`.`global_grants`(`user`,`host`,`priv`,`with_grant_option`) SELECT `user`,`host`,`priv`,`with_grant_option` FROM `__tidb_br_temporary_mysql`.`global_grants`;: [schema:1146]Table '__tidb_br_temporary_mysql.global_grants'
doesn't exist\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/errors.go:178\ngithub.com/pingcap/errors.(*Error).GenWithStack\n\t/go/pkg/mod/github.com/pingcap/
errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/normalize.go:166\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).replaceTemporaryTableToSystable.func1\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:236\
ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).replaceTemporaryTableToSystable\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:292\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).re
storeSystemSchema\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:147\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).RestoreSystemSchemas\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:105\n
github.com/pingcap/tidb/br/pkg/task.runSnapshotRestore\n\t/tidb/br/pkg/task/restore.go:1627\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/tidb/br/pkg/task/restore.go:949\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore
.go:75\nmain.newFullRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:181\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/
go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/tidb/br/cmd/br/main.go:38\nruntime.main\n\t/usr/lo
cal/go/src/runtime/proc.go:272\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1700\nerror during merging temporary tables into system tables, table: global_grants"] [stack="main.runRestoreCommand\n\t/tidb/br/cmd/br/r
estore.go:76\nmain.newFullRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:181\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).Execute
C\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/tidb/br/cmd/br/main.go:38\nruntime.main\n\t/
usr/local/go/src/runtime/proc.go:272"]
[2025/10/01 19:25:57.974 +00:00] [ERROR] [main.go:39] ["br failed"] [error="error during merging temporary tables into system tables, table: global_grants: [BR:Common:ErrUnknown]failed to execute REPLACE INTO `mysql`.`global_g
rants`(`user`,`host`,`priv`,`with_grant_option`) SELECT `user`,`host`,`priv`,`with_grant_option` FROM `__tidb_br_temporary_mysql`.`global_grants`;: [schema:1146]Table '__tidb_br_temporary_mysql.global_grants' doesn't exist"] [
errorVerbose="[BR:Common:ErrUnknown]failed to execute REPLACE INTO `mysql`.`global_grants`(`user`,`host`,`priv`,`with_grant_option`) SELECT `user`,`host`,`priv`,`with_grant_option` FROM `__tidb_br_temporary_mysql`.`global_gran
ts`;: [schema:1146]Table '__tidb_br_temporary_mysql.global_grants' doesn't exist\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/errors.go:178\ngithub.com/ping
cap/errors.(*Error).GenWithStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/normalize.go:166\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).replaceTemporaryTableToSystable
.func1\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:236\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).replaceTemporaryTableToSystable\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:292\n
github.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).restoreSystemSchema\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:147\ngithub.com/pingcap/tidb/br/pkg/restore/snap_client.(*SnapClient).RestoreSystemSc
hemas\n\t/tidb/br/pkg/restore/snap_client/systable_restore.go:105\ngithub.com/pingcap/tidb/br/pkg/task.runSnapshotRestore\n\t/tidb/br/pkg/task/restore.go:1627\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/tidb/br/pkg/tas
k/restore.go:949\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:75\nmain.newFullRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:181\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.
8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:104

## Recent Comments Excerpt

### 2025-10-02T09:19:16.546+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2025-10-02T13:04:19.085+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b42d433d2e8b80f1d43e9001194e) by lark

### 2025-10-02T13:04:27.058+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b42d4336d19500f1a80d354dcad4) by lark

### 2025-10-04T02:27:51.131+0800 [REDACTED_USER]

Restore
 YAML used:
apiVersion: pingcap.com/v1alpha1
kind: Restore
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
spec:

### 2025-10-11T02:00:07.828+0800 [REDACTED_USER]

@[REDACTED_USER]
 This ticket can be closed. Thanks.
