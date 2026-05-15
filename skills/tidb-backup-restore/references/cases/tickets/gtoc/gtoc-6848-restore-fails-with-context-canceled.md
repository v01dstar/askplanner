# GTOC-6848: Restore fails with context canceled

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6848
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-16T14:02:09.000+0800
- Updated: 2025-05-29T00:28:14.651+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: restore-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER], we are trying to restore the backup into a new cluster and it failed at the end with an error

```
I0415 22:53:27.601436       9 restore.go:164] [2024/04/15 22:53:27.601 +05:30] [WARN] [client.go:493] ["failed to get TS, retry it"] ["retry time"=1] [error="context canceled"]
I0415 22:53:27.601570       9 restore.go:164] [2024/04/15 22:53:27.601 +05:30] [ERROR] [client.go:499] ["failed to get TS"] [error="context canceled"] [errorVerbose="context canceled\ngithub
.com/tikv/pd/client.(*tsoRequest).Wait\n\t/go/pkg/mod/github.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-80f0d8ca4d07/client.go:1325\ngithub.com/tikv/pd/client.(*client).GetTS\n\t/go/pkg/mod/gi
thub.com/tikv/pd/client@v0.0.0-[REDACTED_LONG_ID]-80f0d8ca4d07/client.go:1333\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).GetTS\n\t/home/jenkins/agent/workspace/build-common/go/src/github.
com/pingcap/br/br/pkg/restore/client.go:467\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).GetTSWithRetry.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/
br/pkg/restore/client.go:484\ngithub.com/pingcap/tidb/br/pkg/utils.WithRetry\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:56\ngithub.com/p
ingcap/tidb/br/pkg/restore.(*Client).GetTSWithRetry\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:483\ngithub.com/pingcap/tidb/br/pkg/re
store.(*Client).execChecksum\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1416\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).GoVali
dateChecksum.func2.2\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1375\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnError
Group.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/syn
c@v0.1.0/errgroup/errgroup.go:75\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1594"] [stack="github.com/pingcap/tidb/br/pkg/restore.(*Client).GetTSWithRetry\n\t/home/jenkins/agen
t/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:499\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).execChecksum\n\t/home/jenkins/agent/workspace/build-commo
n/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1416\ngithub.com/pingcap/tidb/br/pkg/restore.(*Client).GoValidateChecksum.func2.2\n\t/home/jenkins/agent/workspace/build-common/go/src
/github.com/pingcap/br/br/pkg/restore/client.go:1375\ngithub.com/pingcap/tidb/br/pkg/utils.(*WorkerPool).ApplyOnErrorGroup.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.c
om/pingcap/br/br/pkg/utils/worker.go:76\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.1.0/errgroup/errgroup.go:75"]
```

Also attached are tail logs which captures the error

## Recent Comments Excerpt

### 2024-04-17T13:54:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 5:54 AM

I was waiting for the confirmation.

### 2024-04-17T14:29:14.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 6:29 AM
Currently, source cluster [REDACTED_CLUSTER] on v6.5.3. Is it okay to take upgrade the BR version to v6.5.4 for both backup and restore?
The main difference between small versions like v6.5. x is fixing some bugs and the functionality remains unchanged; So, theoretically speaking, it should be completely compatible.
so , you can run br:v6.5.4 on cluster [REDACTED_CLUSTER]

### 2024-04-17T19:40:42.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 11:40 AM

Sure, I m running restoration, will get back to you if any other issues faced.

### 2024-04-17T22:51:12.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 2:51 PM

Restore was successful with BR version v6.5.4

### 2024-04-17T23:05:07.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 3:04 PM

hi @[REDACTED_USER] 
I am so glad to hear this message. 
I will close this ticket.
If you has any other question later, you can create new ticket.
thanks
