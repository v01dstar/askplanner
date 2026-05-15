# GTOC-7536: Restore fails with [BR:KV:ErrKVEpochNotMatch\]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7536
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2025-04-18T00:42:28.115+0800
- Updated: 2025-05-16T08:28:13.964+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

* Error says:  `import sst file failed after retry, stop the whole progress`
* Stack Trace: 

> tags.subDir:tidb-restore instanceId:[REDACTED_RESOURCE_NAME] messageText:I0416 10:50:20.966911 9 restore.go:179\] \[2025/04/16 10:50:20.966 +00:00\] \[ERROR\] \[import.go:590\] \["import sst file failed after retry, stop the whole progress"\] \[files="{total=1,files=\\"\[1040963_470638_268_4455345999825012e117c250f889b713df906e0b9b4112696c220eff588766e7_1744762604761_write.sst\]\\",totalKVs=322238,totalBytes=14500710,totalSize=8624955}"\] \[error="\[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match; \[BR:KV:ErrKVEpochNotMatch\]epoch not match"\] \[errorVerbose="the following errors occurred:\\n - \[BR:KV:ErrKVEpochNotMatch\]epoch not match\\n [github.com/pingcap/errors.AddStack\\n](http://github.com/pingcap/errors.AddStack%5Cn) \\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/errors.go:174\\n [github.com/pingcap/errors.Trace\\n](http://github.com/pingcap/errors.Trace%5Cn) \\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/juju_adaptor.go:15\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ingest\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:885\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ImportSSTFiles.func1\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:572\\n [github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\\n](http://github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1%5Cn) \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:217\\n \[github.com/pingcap/tidb/br/pkg/utils.WithRetryV2\[...\]\\n|[http://github.com/pingcap/tidb/br/pkg/utils.WithRetryV2](http://github.com/pingcap/tidb/br/pkg/utils.WithRetryV2)\[...\]\\n\] \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:235\\n [github.com/pingcap/tidb/br/pkg/utils.WithRetry\\n](http://github.com/pingcap/tidb/br/pkg/utils.WithRetry%5Cn) \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:216\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ImportSSTFiles\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:528\\n [github.com/pingcap/tidb/br/pkg/restore.(\*Client](http://github.com/pingcap/tidb/br/pkg/restore.(*Client)).RestoreSSTFiles.func2.1\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1459\\n [github.com/pingcap/tidb/br/pkg/restore.(\*Client](http://github.com/pingcap/tidb/br/pkg/restore.(*Client)).RestoreSSTFiles.func2\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1460\\n [github.com/pingcap/tidb/br/pkg/utils.(\*WorkerPool](http://github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool)).ApplyOnErrorGroup.func1\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\\n [golang.org/x/sync/errgroup.(\*Group](http://golang.org/x/sync/errgroup.(*Group)).Go.func1\\n \\t/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\\n runtime.goexit\\n \\t/usr/local/go/src/runtime/asm_amd64.s:1650\\n - \[BR:KV:ErrKVEpochNotMatch\]epoch not match\\n [github.com/pingcap/errors.AddStack\\n](http://github.com/pingcap/errors.AddStack%5Cn) \\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/errors.go:174\\n [github.com/pingcap/errors.Trace\\n](http://github.com/pingcap/errors.Trace%5Cn) \\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/juju_adaptor.go:15\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ingest\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:885\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ImportSSTFiles.func1\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:572\\n [github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\\n](http://github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1%5Cn) \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:217\\n \[github.com/pingcap/tidb/br/pkg/utils.WithRetryV2\[...\]\\n|[http://github.com/pingcap/tidb/br/pkg/utils.WithRetryV2](http://github.com/pingcap/tidb/br/pkg/utils.WithRetryV2)\[...\]\\n\] \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:235\\n [github.com/pingcap/tidb/br/pkg/utils.WithRetry\\n](http://github.com/pingcap/tidb/br/pkg/utils.WithRetry%5Cn) \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:216\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ImportSSTFiles\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:528\\n [github.com/pingcap/tidb/br/pkg/restore.(\*Client](http://github.com/pingcap/tidb/br/pkg/restore.(*Client)).RestoreSSTFiles.func2.1\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1459\\n [github.com/pingcap/tidb/br/pkg/restore.(\*Client](http://github.com/pingcap/tidb/br/pkg/restore.(*Client)).RestoreSSTFiles.func2\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/client.go:1460\\n [github.com/pingcap/tidb/br/pkg/utils.(\*WorkerPool](http://github.com/pingcap/tidb/br/pkg/utils.(*WorkerPool)).ApplyOnErrorGroup.func1\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/worker.go:76\\n [golang.org/x/sync/errgroup.(\*Group](http://golang.org/x/sync/errgroup.(*Group)).Go.func1\\n \\t/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\\n runtime.goexit\\n \\t/usr/local/go/src/runtime/asm_amd64.s:1650\\n - \[BR:KV:ErrKVEpochNotMatch\]epoch not match\\n [github.com/pingcap/errors.AddStack\\n](http://github.com/pingcap/errors.AddStack%5Cn) \\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/errors.go:174\\n [github.com/pingcap/errors.Trace\\n](http://github.com/pingcap/errors.Trace%5Cn) \\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/juju_adaptor.go:15\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ingest\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:885\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ImportSSTFiles.func1\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:572\\n [github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1\\n](http://github.com/pingcap/tidb/br/pkg/utils.WithRetry.func1%5Cn) \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:217\\n \[github.com/pingcap/tidb/br/pkg/utils.WithRetryV2\[...\]\\n|[http://github.com/pingcap/tidb/br/pkg/utils.WithRetryV2](http://github.com/pingcap/tidb/br/pkg/utils.WithRetryV2)\[...\]\\n\] \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:235\\n [github.com/pingcap/tidb/br/pkg/utils.WithRetry\\n](http://github.com/pingcap/tidb/br/pkg/utils.WithRetry%5Cn) \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/retry.go:216\\n [github.com/pingcap/tidb/br/pkg/restore.(\*FileImporter](http://github.com/pingcap/tidb/br/pkg/restore.(*FileImporter)).ImportSSTFiles\\n \\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:528\\n [github.com/pingcap/tidb/br/pkg/restore.(\*Client](http://github.com/pingcap/tid

_Trimmed; see Jira for full context._

## Recent Comments Excerpt

### 2025-04-18T00:42:45.139+0800 [REDACTED_USER]

notified (Wenqi Mou([REDACTED_EMAIL]), om_x100b4f26b6f384b80f17b293fd3ce30) by lark

### 2025-04-18T00:48:09.689+0800 [REDACTED_USER]

Summary so far: 
The same issue was reported 
https://github.com/pingcap/tidb/issues/42924
, but was closed as “From BR 7.6 and above, full restore sst download/ingest phase is after region split/scatter, such issue won't reoccur.” and “given current situation, we won't fix it.”.
There is another report on 7.5.5 release test (lark Ask BR Dec 23 2024) and the last update was “
从 7.6 整个恢复架构更新了，不会有这样的问题了
".
Given this is Databricks production issue, we need to figure out solution:

### 2025-05-12T18:53:21.671+0800 [REDACTED_USER]

it’s a known limitation at corner case and awaits feedback on the solution of auto retry.

### 2025-05-16T07:50:48.753+0800 [REDACTED_USER]

I have discussed the case with customer. This oncall can be closed.  Thanks for the detail explanation.
