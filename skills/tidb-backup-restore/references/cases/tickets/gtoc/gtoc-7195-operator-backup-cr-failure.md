# GTOC-7195: Operator backup CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7195
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-10-16T06:45:10.000+0800
- Updated: 2025-03-06T17:53:40.888+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: tikv-data-path, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello, we are testing tikv node replacement process following steps in [this doc https://docs.google.com/document/d/1lE3kkDE-zZmCia4luhFyhLddbTjzqt1uiFkonU7pkqw/edit?tab=t.0&n=Node_Replacement ](https://docs.google.com/document/d/1lE3kkDE-zZmCia4luhFyhLddbTjzqt1uiFkonU7pkqw/edit#bookmark=id.vee4pb1n6gjc). There’s a period of time that we have two stores mapping to the same tikv address, one old one with status `OFFLINE`, and one new store `UP`, as mentioned [here https://docs.google.com/document/d/1lE3kkDE-zZmCia4luhFyhLddbTjzqt1uiFkonU7pkqw/edit?tab=t.0&n=Node_Replacement](https://docs.google.com/document/d/1lE3kkDE-zZmCia4luhFyhLddbTjzqt1uiFkonU7pkqw/edit#bookmark=id.wdsz82yhkbhz). During this period of time we saw backups failing continuously due to the connection to new store failed. The backup init failed so no backup pod created. sample failure:  
 

```java
cluster [REDACTED_CLUSTER]/fed-skd-2024-10-14t23-05-00, wait pipe message failed, errMsg [2024/10/14 23:05:17.231 +00:00] [ERROR] [prepare.go:163] ["failed to prepare connections"] [error="failed to create and cache stream for store 128834219: failed to initialize the lease: EOF"] [stack="github.com/pingcap/tidb/br/pkg/backup/prepare_snap.(*Preparer).DriveLoopAndWaitPrepare\n\t/tidb/br/pkg/backup/prepare_snap/prepare.go:163\ngithub.com/pingcap/tidb/br/pkg/task/operator.pauseAdminAndWaitApply\n\t/tidb/br/pkg/task/operator/cmd.go:193\ngithub.com/pingcap/tidb/br/pkg/task/operator.AdaptEnvForSnapshotBackup.func3\n\t/tidb/br/pkg/task/operator/cmd.go:149\ngithub.com/pingcap/tidb/br/pkg/task/operator.(*AdaptEnvForSnapshotBackupContext).run.func1\n\t/tidb/br/pkg/task/operator/cmd.go:63\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.1.0/errgroup/errgroup.go:75"]
```

and meanwhile the tikv is up and running(the screenshot time in in PDT and the logs/errors is using UTC), but we saw tikv errors

 

```java
[2024/10/14 23:22:51.203 +00:00] [ERROR] [kv.rs:699] ["dispatch raft msg from gRPC to raftstore fail"] [err="RaftServer(StoreNotMatch \{ to_store_id: 112, my_store_id: 128834219 })"][2024/10/14 23:22:51.203 +00:00] [ERROR] [kv.rs:706] ["KvService::batch_raft send response fail"] [err=RemoteStopped]
```

is this related?

log for the replaced tikv pod and failed backup cr attached. could you pls help us understand what went wrong? thanks.

Also we found once the old store is removed the backups got completed. so wondering is backup process trying to connect the old store also? but in the log it says the new store connection failure.

## Recent Comments Excerpt

### 2024-10-16T10:46:47.000+0800 [REDACTED_USER]

BR can filter the `physically_destroyed` store in this case.
[REDACTED_MEDIA]

### 2024-10-16T18:15:50.000+0800 [REDACTED_USER]

I am afraid ebs br is hard to tolerate the inconsistency, and customer [REDACTED_CUSTOMER] pod phase of backup.  

The reason is that br operator saves backup metadata  at the beginning of backup, and the metadata contains the tidb cluster [REDACTED_CLUSTER] information including volumes attached to each tikv nodes. If there is co-exisistence of deleted tikv node and new added tikv node, backup won't hanlde the volumes for the new node at all.

### 2024-10-19T08:04:17.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 customer [REDACTED_CUSTOMER]: So during the period we have two stores, the previous tikv pod and corresponding pvcs are deleted already and we only have one new tikv pod in metadata. So wondering do we still expect old volumes attached to the new tikv pod?

### 2024-10-23T14:37:42.000+0800 [REDACTED_USER]

no, ebs br doesn't have the presumption that "old volumes attached to the new tikv pod" at the case. the point is that backup init phase can see the consistent view as br operator side sees at the beginning, either old pod with old volumes attached or new pod with new volumes attached.

### 2024-10-29T16:57:02.000+0800 [REDACTED_USER]

friendly ping, any update or cloud we close this ticket? 
@[REDACTED_USER]
