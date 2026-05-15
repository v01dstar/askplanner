# GTOC-6893: PITR fails with [BR:ExternalStorage:ErrStorageInvalidConfig]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6893
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-05-02T10:15:43.000+0800
- Updated: 2025-03-06T18:12:38.860+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: change-p2

## Symptom / Description Excerpt

Looks like my last request was missing, resending this request.

We recently upgrade our tidb from v.6.5.8 to v6.5.9 to staging, all of those regions experienced PiTR issues like below.

alert name: [REDACTED_RESOURCE_NAME]

```
# ./br log status --pd=https://jobs-pd.tidb:2379 --ca=/var/lib/tidb-tls/ca.crt --cert=/var/lib/tidb-tls/tls.crt --key=/var/lib/tidb-tls
/tls.key
Detail BR log in /tmp/br.log.2024-04-23T20.33.22Z
● Total 1 Tasks.
> #1 <
              name: [REDACTED_RESOURCE_NAME]
            status: ● PAUSE
             start: 2023-05-28 21:43:51.353 +0000
               end: 2090-11-18 14:07:45.624 +0000
           storage: azure://backup-data/log-jobs/log-2023-05-28t21-43-44
       speed(est.): 0.00 ops/s
checkpoint[global]: 2024-04-22 19:37:33.698 +0000; gap=24h55m50s
```

```
./br log metadata --pd=https://jobs-pd.tidb:2379 --ca=/var/lib/tidb-tls/ca.crt --cert=/var/lib/tidb-tls/tls.crt --key=/var/lib/tidb-t
ls/tls.key
Detail BR log in /tmp/br.log.2024-04-23T20.35.03Z
[2024/04/23 20:35:03.250 +00:00] [INFO] [collector.go:73] ["log metadata failed summary"] [total-ranges=1] [ranges-succeed=0] [ranges-failed=1] [unit-name="log metadata"] [error="empty store is not allowed: [BR:ExternalStorage:ErrStorageInvalidConfig]invalid external storage config"] [errorVerbose="[BR:ExternalStorage:ErrStorageInvalidConfig]invalid external storage config\nempty store is not allowed\ngithub.com/pingcap/tidb/br/pkg/storage.ParseBackend\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/storage/parse.go:42\ngithub.com/pingcap/tidb/br/pkg/task.GetStorage\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/common.go:625\ngithub.com/pingcap/tidb/br/pkg/task.getLogRange\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:1372\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamMetadata\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:647\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamCommand\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:506\nmain.streamCommand\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/stream.go:231\nmain.newStreamCheckCommand.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/stream.go:156\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968\nmain.main\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/main.go:57\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"]
Error: empty store is not allowed: [BR:ExternalStorage:ErrStorageInvalidConfig]invalid external storage config
```

## Recent Comments Excerpt

### 2024-06-25T03:56:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 24/Jun/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-06-25T20:14:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Jun/24 12:14 PM

add auto-close-start label

### 2024-06-26T01:01:17.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Jun/24 5:01 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-06-29T01:01:28.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 28/Jun/24 5:01 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-07-02T01:01:10.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/Jul/24 5:00 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
