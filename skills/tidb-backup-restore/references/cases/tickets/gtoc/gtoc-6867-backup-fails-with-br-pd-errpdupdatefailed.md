# GTOC-6867: Backup fails with [BR:PD:ErrPDUpdateFailed]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6867
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-23T11:51:40.000+0800
- Updated: 2025-03-06T18:13:41.599+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello, we have multiple backups failed in prod due to pd update failure. We saw init job completed and backup in a data plane failed due to 

```
"I0331 11:13:57.851382       9 backup.go:302] [2024/03/31 11:13:57.851 +00:00] [ERROR] [conn.go:152] [\"fail to create pd controller\"] [error=\"pd address ([REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379) not available, error is Get \\\"https://[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379/pd/api/v1/config/cluster-version\\\": dial tcp: lookup [REDACTED_ENV_NAME].[REDACTED_ENV_NAME] on [REDACTED_IP]:53: no such host, please check network: [BR:PD:ErrPDUpdateFailed]failed to update PD\"] [errorVerbose=\"[BR:PD:ErrPDUpdateFailed]failed to update PD\\npd address ([REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379) not available, error is Get \\\"https://[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379/pd/api/v1/config/cluster-version\\\": dial tcp: lookup [REDACTED_ENV_NAME].[REDACTED_ENV_NAME] on [REDACTED_IP]:53: no such host, please check network\\ngithub.com/pingcap/tidb/br/pkg/pdutil.NewPdController\\n\\t/tidb/br/pkg/pdutil/pd.go:282\\ngithub.com/pingcap/tidb/br/pkg/conn.NewMgr\\n\\t/tidb/br/pkg/conn/conn.go:150\\ngithub.com/pingcap/tidb/br/pkg/task.NewMgr\\n\\t/tidb/br/pkg/task/common.go:639\\ngithub.com/pingcap/tidb/br/pkg/task.RunBackupEBS\\n\\t/tidb/br/pkg/task/backup_ebs.go:116\\nmain.runBackupCommand\\n\\t/tidb/br/cmd/br/backup.go:36\\nmain.newFullBackupCommand.func1\\n\\t/tidb/br/cmd/br/backup.go:117\\ngithub.com/spf13/cobra.(*Command).execute\\n\\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916\\ngithub.com/spf13/cobra.(*Command).ExecuteC\\n\\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044\\ngithub.com/spf13/cobra.(*Command).Execute\\n\\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968\\nmain.main\\n\\t/tidb/br/cmd/br/main.go:36\\nruntime.main\\n\\t/usr/local/go/src/runtime/proc.go:250\\nruntime.goexit\\n\\t/usr/local/go/src/runtime/asm_amd64.s:1598\"] [stack=\"github.com/pingcap/tidb/br/pkg/conn.NewMgr\\n\\t/tidb/br/pkg/conn/conn.go:152\\ngithub.com/pingcap/tidb/br/pkg/task.NewMgr\\n\\t/tidb/br/pkg/task/common.go:639\\ngithub.com/pingcap/tidb/br/pkg/task.RunBackupEBS\\n\\t/tidb/br/pkg/task/backup_ebs.go:116\\nmain.runBackupCommand\\n\\t/tidb/br/cmd/br/backup.go:36\\nmain.newFullBackupCommand.func1\\n\\t/tidb/br/cmd/br/backup.go:117\\ngithub.com/spf13/cobra.(*Command).execute\\n\\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916\\ngithub.com/spf13/cobra.(*Command).ExecuteC\\n\\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044\\ngithub.com/spf13/cobra.(*Command).Execute\\n\\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968\\nmain.main\\n\\t/tidb/br/cmd/br/main.go:36\\nruntime.main\\n\\t/usr/local/go/src/runtime/proc.go:250\"]",
```

I do see pd pod in this az restarted around the backup time. wondering what does this pd connection trying to do during backup process? and do we have a retry waiting for pd to come back to live? thanks.

pd pod restart: <custom data-type="smartlink" data-id="id-0">https://gist.github.com/olivia-chen-github/7e513849540af361d1f1bce741f3f0c0</custom> 

init log: <custom data-type="smartlink" data-id="id-1">https://gist.github.com/olivia-chen-github/de84d12c40b0086b905effa35e04ed44</custom> 

failed backup log: <custom data-type="smartlink" data-id="id-2">https://gist.github.com/olivia-chen-github/261b05d609d0967e0e762a7b73805eee</custom>

## Recent Comments Excerpt

### 2024-05-01T01:19:03.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/Apr/24 5:18 PM

cool. thanks Hua. Do you plan to merge this pr sometime recently? thx
https://github.com/pingcap/tidb/pull/53005/files

### 2024-05-01T02:46:48.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/Apr/24 6:46 PM

@[REDACTED_USER] understanding is Airbnb manages your own repo and has been cherry picked the PRs by yourselves. This PR will be added to the next official 6.5.x releases, but if you need it to be added to your current version, I need to raise a hotfix request, let me know which way you prefer, thanks

### 2024-05-03T06:39:03.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/May/24 10:38 PM

Yes we typically pick up commit from upstream after the pr is merged. so wondering do we have rough estimation about when it’s going to get merged? thx

### 2024-05-07T23:14:37.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 07/May/24 3:14 PM

Hey @[REDACTED_USER] , the pull request has been successfully merged into the release-6.5 branch. Should there be no further issues, may I proceed to close this ticket? Thank you.

### 2024-05-16T04:17:06.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 15/May/24 8:16 PM

As we haven't received any responses for some time, we will proceed to close this ticket temporarily. Should you require further assistance, please don't hesitate to reopen it.
