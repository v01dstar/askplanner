# GTOC-6838: PITR fails with [BR:Common:ErrUnknown]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6838
- Status: Todo
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-04-13T01:24:23.000+0800
- Updated: 2025-03-06T18:14:31.782+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER],

We are running a DDL job (add index) on a TiDB cluster with v7.1.1. The backup are running fine, although the log backup for the PITR job is failing to run:

```
[error="Unable to create log backup task. Please wait until the DDL jobs(add index with ingest method) are finished.: [BR:Common:ErrUnknown]internal error"] [errorVerbose="[BR:Common:ErrUnknown]internal error\nUnable to create log backup task. Please wait until the DDL jobs(add index with ingest method) are finished.\ngithub.com/pingcap/tidb/br/pkg/task.(*streamMgr).checkStreamStartEnable\n\t/mnt/tidb/sql/br/pkg/task/stream.go:471\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamStart\n\t/mnt/tidb/sql/br/pkg/task/stream.go:561\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamCommand\n\t/mnt/tidb/sql/br/pkg/task/stream.go:529\nmain.streamCommand\n\t/mnt/tidb/sql/br/cmd/br/stream.go:232\nmain.newStreamStartCommand.func1\n\t/mnt/tidb/sql/br/cmd/br/stream.go:70\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968\nmain.main\n\t/mnt/tidb/sql/br/cmd/br/main.go:58\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1598"]
```

## Recent Comments Excerpt

### 2024-05-10T04:19:41.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/May/24 8:19 PM

the cherry-pick is now available with v7.1.5.

### 2024-05-10T04:51:00.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/May/24 8:50 PM

We want the cherry pick for v7.5. It looks like it’s being still worked on.

### 2024-05-10T05:06:45.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/May/24 9:06 PM

okay. 
all tests of the v7.5 cherry-pick actually passed it just needs 1 more LGTM to be merged.

### 2024-05-12T01:00:52.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 11/May/24 5:00 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-05-15T01:01:32.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 14/May/24 5:01 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
