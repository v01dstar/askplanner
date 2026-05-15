# GTOC-7038: Backup fails with nil pointer

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7038
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-07-29T09:57:12.000+0800
- Updated: 2025-03-06T18:08:10.358+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: storage-credential, performance-resource
- Labels: N/A

## Symptom / Description Excerpt

Hello,

One of our tidb cluster ran into the following backup failure. 

```
│ error: cluster [REDACTED_CLUSTER]/fed-skd-2024-07-28t14-15-00, wait pipe message failed, errMsg panic: runtime error: invalid memory address or nil pointer dereference                                                              │
│ [signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x4474931]                                                                                                                                                                  │
│                                                                                                                                                                                                                                          │
│ goroutine 1 [running]:                                                                                                                                                                                                                   │
│ github.com/pingcap/tidb/br/pkg/aws.(*EC2Session).WaitSnapshotsCreated(0xc0157a95e0, 0xc015934480, {0x5c81370, 0xc0157b1e00})                                                                                                             │
│     /tidb/br/pkg/aws/ebs.go:255 +0xa71                                                                                                                                                                                                   │
│ github.com/pingcap/tidb/br/pkg/task.RunBackupEBS({0x5c814f8, 0xc00087af50}, {0x5c940b8?, 0x86bcdc0?}, 0xc000a1bc00)                                                                                                                      │
│     /tidb/br/pkg/task/backup_ebs.go:255 +0x1c8a                                                                                                                                                                                          │
│ main.runBackupCommand(0xc000aa2300, {0x53bfc8f, 0xb})                                                                                                                                                                                    │
│     /tidb/br/cmd/br/backup.go:36 +0x1d4                                                                                                                                                                                                  │
│ main.newFullBackupCommand.func1(0xc0003ad200?, {0xc000af00c0?, 0x4?, 0x53adfc5?})                                                                                                                                                        │
│     /tidb/br/cmd/br/backup.go:117 +0x1f                                                                                                                                                                                                  │
│ github.com/spf13/cobra.(*Command).execute(0xc000aa2300, {0xc0001f2030, 0xc, 0xc})                                                                                                                                                        │
│     /go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:916 +0x87c                                                                                                                                                                      │
│ github.com/spf13/cobra.(*Command).ExecuteC(0xc000004300)                                                                                                                                                                                 │
│     /go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:1044 +0x3a5                                                                                                                                                                     │
│ github.com/spf13/cobra.(*Command).Execute(...)                                                                                                                                                                                           │
│     /go/pkg/mod/github.com/spf13/cobra@v1.6.1/command.go:968                                                                                                                                                                             │
│ main.main()                                                                                                                                                                                                                              │
│     /tidb/br/cmd/br/main.go:36 +0x212                                                                                                                                                                                                    │
│ , err: exit status 2
```

## Recent Comments Excerpt

### 2024-07-29T10:50:33.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/Jul/24 2:50 AM
It’s should be a duplicate issue of 
https://github.com/pingcap/tidb/issues/54511
 
please check with michael deng @airbnb to see if he cherry-picked the pr to the affected cluster. Thanks.
Regards
Jiamin Li

### 2024-07-29T12:06:34.000+0800 [REDACTED_USER]

commented by [REDACTED_EMAIL] - 29/Jul/24 4:06 AM

Great! Thank you! Will check with Michael

### 2024-07-29T12:41:18.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/Jul/24 4:41 AM

Welcome. OK.

### 2024-07-30T06:08:11.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/Jul/24 10:08 PM

We requested it to be cherrypicked to different release branches, so please nudge those. For now, we have cherrypicked the PR internally. So its ok to close this ticket.

### 2024-07-30T12:58:22.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/Jul/24 4:58 AM

Thanks for the update, Naman.
