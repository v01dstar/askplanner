# GTOC-6828: Restore fails with [BR:PD:ErrPDUpdateFailed]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6828
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-09T08:21:13.000+0800
- Updated: 2025-03-06T18:14:49.767+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR, PD
- Categories: restore-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Some restores are failing w/ BR:PD:ErrPdUpdateFailed. Fails during restore data phase in a specific zone (b)

Attaching:

* volumerestore cr yaml
* restore logs
* pd-0 and pd-1 logs from that zone
* operator logs from that zone
* br-federation-manager logs

## Recent Comments Excerpt

### 2024-04-16T12:24:15.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 16/Apr/24 4:24 AM

The main issue here is likely related to that DNS unable to resolve the correct host during the problem period. There are a lot of log entries like the following in external dns:
"time=\"2024-04-08T09:36:47Z\" level=debug msg=\"Skipping endpoint [REDACTED_ENV_NAME].[REDACTED_ENV_NAME].[REDACTED_ENV_NAME].svc.us-east-1a.shared.tidb.musta.ch 300 IN A  [REDACTED_IP] [] because owner id does not match, found: \\\"[REDACTED_ENV_NAME]\\\", required: \\\"[REDACTED_ENV_NAME]\\\"\"" 
"time=\"2024-04-08T09:41:24Z\" level=debug msg=\"Skipping endpoint rp-[REDACTED_ENV_NAME].rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME].svc.us-east-1a.shared.tidb.musta.ch 300 IN A  [REDACTED_IP] [] because owner id does not match, found: \\\"[REDACTED_ENV_NAME]\\\", required: \\\"[REDACTED_ENV_NAME]\\\"\""
What is the external DNS version? We noticed there is a similar issue reported:
https://github.com/kubernetes-sigs/external-dns/issues/583
  .

### 2024-04-27T04:50:59.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 8:50 PM

@xiao: We did further debugging. PDs are restarting due to delay in dns propogation to route 53 (This is could happen due to whatever reason, maybe slow route 53, external dns unavailability etc). And then even when PD starts (after validating dns propogation), we still have a initialDelaySeconds of 120 seconds. During this time, we cannot resolve “{{rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]}}". This is what restore tries to use, so the failure is expected. Eventually after 120 seconds have passed, after the pd restart, 
rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]
 now has a valid dns resolution. 
Proposed solution: 
Restore retries for atleast upto 5 mins to avoid delay in dns propogation, and initialDelay. And if fact, we see pd already has retries, when trying to connect to other PDs. But seems like restore doesn’t. Infact, we have seen backups also failing due to same error. So worth adding retries during bakcup as well

### 2024-04-27T04:59:23.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 8:59 PM

Right now, based on restore pod logs. 
I0424 18:40:13.390696       8 restore.go:176] [2024/04/24 18:40:13.390 +00:00] [INFO] [info.go:49] ["Welcome to Backup & Restore (BR)"] [release-version=v6.5.4-v14.8-abnb] [git-hash=ce590a5ee7c670c154ba71b605fd7c30681c60d9] [git-branch=heads/v6.5.4-v14.8-abnb] [go-version=go1.20.14] [utc-build-time="2024-03-28 21:36:08"] [race-enabled=false]
I0424 18:40:13.390723       8 restore.go:176] [2024/04/24 18:40:13.390 +00:00] [INFO] [common.go:744] [arguments] [__command="br restore full"] [ca=/var/lib/cluster-client-tls/ca.crt] [cert=/var/lib/cluster-client-tls/tls.crt] [check-requirements=false] [key=/var/lib/cluster-client-tls/tls.key] [output-file=/var/lib/br-bin/csb_restore.json] [pd="[rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379]"] [prepare=true] [s3.provider=aws] [s3.region=us-east-1] [send-credentials-to-tikv=false] [storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] [target-az=] [type=aws-ebs] [use-fsr=false] [volume-encrypted=true] [volume-iops=8000] [volume-throughput=800] [volume-type=gp3]
I0424 18:40:13.533930       8 restore.go:176] [2024/04/24 18:40:13.533 +00:00] [INFO] [s3.go:398] ["succeed to get bucket region from s3"] ["bucket region"=us-east-1]
I0424 18:40:13.586851       8 restore.go:176] [2024/04/24 18:40:13.586 +00:00] [ERROR] [restore_ebs_meta.go:137] ["fail to create pd controller"] [error="pd address (rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379) not available, error is Get \"https://rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379/pd/api/v1/config/cluster-version\": dial tcp: lookup rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME] on [REDACTED_IP]:53: no such host, please check network: [BR:PD:ErrPDUpdateFailed]failed to update PD"] [errorVerbose="[BR:PD:ErrPDUpdateFailed]failed to update PD\npd address (rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379) not available, error is Get \"https://rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME]:2379/pd/api/v1/config/cluster-version\": dial tcp: lookup rp-[REDACTED_ENV_NAME].[REDACTED_ENV_NAME] on [REDACTED_IP]:53: no such host, please check network\ngithub.com/pingcap/tidb/br/pkg/pdutil.NewPdController\n\t/tidb/br/pkg/pdutil/pd.go:282\ngithub.com/pingcap/tidb/br/pkg/task.(*restoreEBSMetaHelper).preRestore\n\t/tidb/br/pkg/task/restore_ebs_meta.go:135\ngithub.com/pingcap/tidb/br/pkg/task.(*restoreEBSMetaHelper).restore\n\t/tidb/br/pkg/task/restore_ebs_meta.go:177\ngithub.com/pingcap/tidb/br/pkg/task.RunRestoreEBSMeta\n\t/tidb/br/pkg/task/restore_ebs_meta.go:85\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:45\nmain.newFullRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:143\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968\nmain.main\n\t/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1598"] [stack="github.com/pingcap/tidb/br/pkg/task.(*restoreEBSMetaHelper).preRestore\n\t/tidb/br/pkg/task/restore_ebs_meta.go:137\ngithub.com/pingcap/tidb/br/pkg/task.(*restoreEBSMetaHelper).restore\n\t/tidb/br/pkg/task/restore_ebs_meta.go:177\ngithub.com/pingcap/tidb/br/pkg/task.RunRestoreEBSMeta\n\t/tidb/br/pkg/task/restore_ebs_meta.go:85\nmain.runRestoreCommand\n\t/tidb/br/cmd/br/restore.go:45\nmain.newFullRestoreCommand.func1\n\t/tidb/br/cmd/br/restore.go:143\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968\nmain.main\n\t/tidb/br/cmd/br/main.go:36\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250"]
I0424 18:40:13.586867       8 restore.go:176] [2024/04/24 18:40:13.586 +00:00] [INFO] [collector.go:259] ["EBS restore failed, please check the log for details."]

### 2024-05-01T09:57:14.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/May/24 1:57 AM

Hi, @[REDACTED_USER] , 
https://github.com/pingcap/tidb/pull/53005
  is merged. This pr should address both 
https://pingcap-ticket.atlassian.net/browse/[REDACTED_TICKET_ID]#icft=[REDACTED_TICKET_ID]
 and 10426. Please cherry pick the PR and let us know the result.
Thanks.

### 2024-05-30T03:48:14.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/May/24 7:48 PM

Close the ticket as PR is merged. Please feel free to reopen or open a new ticket if there is any concerns. Thanks
