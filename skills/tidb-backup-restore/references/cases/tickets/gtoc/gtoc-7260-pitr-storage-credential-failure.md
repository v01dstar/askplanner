# GTOC-7260: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7260
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2024-11-19T22:05:09.000+0800
- Updated: 2025-03-06T17:51:48.549+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

I'm doing pitr test on a testing cluster in k8s. The cluster has 200k schema, 1 million tables. Snapshot backup and restore are working. However pitr fails.

Error message is:   
\[2024/11/16 08:54:29.887 +00:00\] \[ERROR\] \[restore.go:76\] \["failed to restore"\] \[error="failed to insert rows into gc_delete_range: \[domain:8027\]Information schema is out of date: schema failed to update in 1 lease, please make sure TiDB can connect to TiKV"\] \[errorVerbose="\[domain:8027\]Information schema is out of date: schema failed to update in 1 lease, please make sure TiDB can connect to TiKV\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*twoPhaseCommitter).checkSchemaValid\\n\\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-691e80ae0ea9/txnkv/transaction/2pc.go:2051\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*twoPhaseCommitter).calculateMaxCommitTS\\n\\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-691e80ae0ea9/txnkv/transaction/2pc.go:2056\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*twoPhaseCommitter).execute\\n\\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-691e80ae0ea9/txnkv/transaction/2pc.go:1741\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*KVTxn).Commit\\n\\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-691e80ae0ea9/txnkv/transaction/txn.go:760\\ngithub.com/pingcap/tidb/pkg/store/driver/txn.(\*tikvTxn).Commit\\n\\t/workspace/source/tidb/pkg/store/driver/txn/txn_driver.go:117\\ngithub.com/pingcap/tidb/pkg/session.(\*LazyTxn).Commit\\n\\t/workspace/source/tidb/pkg/session/txn.go:434\\ngithub.com/pingcap/tidb/pkg/session.(\*session).commitTxnWithTemporaryData\\n\\t/workspace/source/tidb/pkg/session/session.go:673\\ngithub.com/pingcap/tidb/pkg/session.(\*session).doCommit\\n\\t/workspace/source/tidb/pkg/session/session.go:553\\ngithub.com/pingcap/tidb/pkg/session.(\*session).doCommitWithRetry\\n\\t/workspace/source/tidb/pkg/session/session.go:795\\ngithub.com/pingcap/tidb/pkg/session.(\*session).CommitTxn\\n\\t/workspace/source/tidb/pkg/session/session.go:925\\ngithub.com/pingcap/tidb/pkg/session.autoCommitAfterStmt\\n\\t/workspace/source/tidb/pkg/session/tidb.go:290\\ngithub.com/pingcap/tidb/pkg/session.finishStmt\\n\\t/workspace/source/tidb/pkg/session/tidb.go:252\\ngithub.com/pingcap/tidb/pkg/session.runStmt\\n\\t/workspace/source/tidb/pkg/session/session.go:2322\\ngithub.com/pingcap/tidb/pkg/session.(\*session).ExecuteStmt\\n\\t/workspace/source/tidb/pkg/session/session.go:2153\\ngithub.com/pingcap/tidb/pkg/session.(\*session).ExecuteInternal\\n\\t/workspace/source/tidb/pkg/session/session.go:1526\\ngithub.com/pingcap/tidb/br/pkg/gluetidb.(\*tidbSession).ExecuteInternal\\n\\t/workspace/source/tidb/br/pkg/gluetidb/glue.go:203\\ngithub.com/pingcap/tidb/br/pkg/restore/log_client.(\*LogClient).InsertGCRows\\n\\t/workspace/source/tidb/br/pkg/restore/log_client/client.go:1553\\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream\\n\\t/workspace/source/tidb/br/pkg/task/stream.go:1482\\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\\n\\t/workspace/source/tidb/br/pkg/task/stream.go:1233\\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\\n\\t/workspace/source/tidb/br/pkg/task/restore.go:699\\nmain.runRestoreCommand\\n\\t/workspace/source/tidb/br/cmd/br/restore.go:75\\nmain.newStreamRestoreCommand.func1\\n\\t/workspace/source/tidb/br/cmd/br/restore.go:249\\ngithub.com/spf13/cobra.(\*Command).execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\\ngithub.com/spf13/cobra.(\*Command).ExecuteC\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\\ngithub.com/spf13/cobra.(\*Command).Execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\\nmain.main\\n\\t/workspace/source/tidb/br/cmd/br/main.go:36\\nruntime.main\\n\\t/usr/local/go/src/runtime/proc.go:272\\nruntime.goexit\\n\\t/usr/local/go/src/runtime/asm_amd64.s:1700\\ngithub.com/pingcap/errors.AddStack\\n\\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/errors.go:178\\ngithub.com/pingcap/errors.Trace\\n\\t/root/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-6bd07397691f/juju_adaptor.go:15\\ngithub.com/pingcap/tidb/pkg/store/driver/error.ToTiDBErr\\n\\t/workspace/source/tidb/pkg/store/driver/error/error.go:203\\ngithub.com/pingcap/tidb/pkg/store/driver/txn.extractKeyErr\\n\\t/workspace/source/tidb/pkg/store/driver/txn/error.go:166\\ngithub.com/pingcap/tidb/pkg/store/driver/txn.(\*tikvTxn).extractKeyErr\\n\\t/workspace/source/tidb/pkg/store/driver/txn/txn_driver.go:349\\ngithub.com/pingcap/tidb/pkg/store/driver/txn.(\*tikvTxn).Commit\\n\\t/workspace/source/tidb/pkg/store/driver/txn/txn_driver.go:118\\ngithub.com/pingcap/tidb/pkg/session.(\*LazyTxn).Commit\\n\\t/workspace/source/tidb/pkg/session/txn.go:434\\ngithub.com/pingcap/tidb/pkg/session.(\*session).commitTxnWithTemporaryData\\n\\t/workspace/source/tidb/pkg/session/session.go:673\\ngithub.com/pingcap/tidb/pkg/session.(\*session).doCommit\\n\\t/workspace/source/tidb/pkg/session/session.go:553\\ngithub.com/pingcap/tidb/pkg/session.(\*session).doCommitWithRetry\\n\\t/workspace/source/tidb/pkg/session/session.go:795\\ngithub.com/pingcap/tidb/pkg/session.(\*session).CommitTxn\\n\\t/workspace/source/tidb/pkg/session/session.go:925\\ngithub.com/pingcap/tidb/pkg/session.autoCommitAfterStmt\\n\\t/workspace/source/tidb/pkg/session/tidb.go:290\\ngithub.com/pingcap/tidb/pkg/session.finishStmt\\n\\t/workspace/source/tidb/pkg/session/tidb.go:252\\ngithub.com/pingcap/tidb/pkg/session.runStmt\\n\\t/workspace/source/tidb/pkg/session/session.go:2322\\ngithub.com/pingcap/tidb/pkg/session.(\*session).ExecuteStmt\\n\\t/workspace/source/tidb/pkg/session/session.go:2153\\ngithub.com/pingcap/tidb/pkg/session.(\*session).ExecuteInternal\\n\\t/workspace/source/tidb/pkg/session/session.go:1526\\ngithub.com/pingcap/tidb/br/pkg/gluetidb.(\*tidbSession).ExecuteInternal\\n\\t/workspace/source/tidb/br/pkg/gluetidb/glue.go:203\\ngithub.com/pingcap/tidb/br/pkg/restore/log_client.(\*LogClient).InsertGCRows\\n\\t/workspace/source/tidb/br/pkg/restore/log_client/client.go:1553\\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream\\n\\t/workspace/source/tidb/br/pkg/task/stream.go:1482\\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\\n\\t/workspace/source/tidb/br/pkg/task/stream.go:1233\\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\\n\\t/workspace/source/tidb/br/pkg/task/restore.go:699\\nmain.runRestoreCommand\\n\\t/workspace/source/tidb/br/cmd/br/restore.go:75\\nmain.newStreamRestoreCommand.func1\\n\\t/workspace/source/tidb/br/cmd/br/restore.go:249\\ngithub.com/spf13/cobra.(\*Command).execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\\ngithub.com/spf13/cobra.(\*Command).ExecuteC\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\\ngithub.com/spf13/cobra.(\*Command).Execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\\nmain.main\\n\\t/workspace/source/tidb/br/cmd/br/main.go:36\\nruntime.main\\n\\t/usr/local/go/src/runtime/proc.go:272\\nruntime.goexit\\n\\t/usr/local/go/src/runtime/asm_amd64.s:1700\\nfailed to insert rows into gc_delete_range"\] \[stack="main.runRestoreCommand\\n\\t/workspace/source/tidb/br/cmd/br/restore.go:76\\nmain.newStreamRestoreCommand.func1\\n\\t/workspace/source/tidb/br/cmd/br/restore.go:249\\ngithub.com/spf13/cobra.(\*Command).execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\\ngithub.com/spf13/cobra.(\*Command).ExecuteC\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\\ngithub.com/spf13/cobra.(\*Command).Execute\\n\\t/root/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\\nmain.main\\n\\t/workspace/source/tidb/br/cmd/br/main.go:36\\nruntime.main\\n\\t/usr/local/go/src/runtime/proc.go:272"\]  
\[2024/11/16 08:54:29.888 +00:00\] \[ERROR\] \[main.go:38\] \["br failed"\] \[error="failed to insert rows into gc_delete_range: \[domain:8027\]Information schema is out of date: schema failed to update in 1 lease, please make sure TiDB can connect to TiKV"\] \[errorVerbose="\[domain:8027\]Information schema is out of date: schema failed to update in 1 lease, please make sure TiDB can connect to TiKV\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*twoPhaseCommitter).checkSchemaValid\\n\\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-691e80ae0ea9/txnkv/transaction/2pc.go:2051\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*twoPhaseCommitter).calculateMaxCommitTS\\n\\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-691e80ae0ea9/txnkv/transaction/2pc.go:2056\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*twoPhaseCommitter).execute\\n\\t/root/go/pkg/mod/github.com/tikv/client-go/v2@v2.0.8-0.[REDACTED_LONG_ID]-691e80ae0ea9/txnkv/transaction/2pc.go:1741\\ngithub.com/tikv/client-go/v2/txnkv/transaction.(\*KVTxn).Commit\\n\\t/root

_Trimmed; see Jira for full context._

## Recent Comments Excerpt

### 2024-11-19T22:24:15.000+0800 [REDACTED_USER]

Also, I have checked data in target cluster. I believe log has already applied. It looks like some error happened after pitr is almost done.

### 2024-11-19T22:53:24.000+0800 [REDACTED_USER]

This is config
 

apiVersion: pingcap.com/v1alpha1

kind: Restore

metadata:

### 2024-11-25T10:48:58.000+0800 [REDACTED_USER]

1. Does TiKV restarted during that time?

2. How many "insert into the delete range" logs in restore.log

### 2024-11-25T10:58:38.000+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2024-11-27T04:19:51.000+0800 [REDACTED_USER]

reproduced locally using PR
https://github.com/pingcap/tidb/pull/57742
 
TL;DR, it happens in the cluster with large number of tables but minimal actual data. During PiTR restore infoSchema takes minutes to load the change, and since actual data restore finished within seconds, restore process tries to use infoSchema for insertGCRow before its reloading finished and thus causing the issue.
 
Fix could be explicitly wait for infoSchema to finish any loading before proceeding to the rest of the restore process.
