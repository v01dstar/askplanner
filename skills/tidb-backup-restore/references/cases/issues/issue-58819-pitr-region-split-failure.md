# Issue 58819: PITR region split failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/58819
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-01-09T06:45:45Z
- Updated: 2025-01-22T04:07:06Z
- Closed: 2025-01-17T02:41:46Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiDB, TiKV, BR
- Categories: pitr-log-restore, region-split-scatter
- Labels: affects-8.5, component/br, feature/developing, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/critical, type/bug
- Affected versions: affects-8.5, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `PITR region split failure`
- Search terms: BR; PITR; TiDB; TiKV; pitr-log-restore; region-split-scatter

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
 restore point with full backup and snapshot restore data
<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
restore point is ok
### 3. [REDACTED_USER]
```
[2025/01/08 17:11:02.647 +00:00] [FATAL] [splitter.go:71] ["[unreachable] no table id matched"] [tableID=4358749] [stack="github.com/pingcap/tidb/br/pkg/restore/split.(*BaseSplitStrategy).GetAccumulations\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/split/splitter.go:71\ngithub.com/pingcap/tidb/br/pkg/restore/log_client.(*LogClient).WrapCompactedFilesIterWithSplitHelper.(*PipelineRestorerWrapper[...]).WithSplit.func2\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/restorer.go:366\ngithub.com/pingcap/tidb/br/pkg/utils/iter.tryMap[...].TryNext\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/utils/iter/combinator_types.go:140\ngithub.com/pingcap/tidb/br/pkg/restore/log_client.(*LogClient).RestoreCompactedSstFiles\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/log_client/client.go:301\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream.func6\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:1566\ngithub.com/pingcap/tidb/br/pkg/task.withProgress\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:1748\ngithub.com/pingcap/tidb/br/pkg/task.restoreStream\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:1547\ngithub.com/pingcap/tidb/br/pkg/task.RunStreamRestore\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/stream.go:1311\ngithub.com/pingcap/tidb/br/pkg/task.RunRestore\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/task/restore.go:721\nmain.runRestoreCommand\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/restore.go:80\nmain.newStreamRestoreCommand.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/restore.go:254\ngithub.com/spf13/cobra.(*Command).execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:985\ngithub.com/spf13/cobra.(*Command).ExecuteC\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1117\ngithub.com/spf13/cobra.(*Command).Execute\n\t/go/pkg/mod/github.com/spf13/cobra@v1.8.1/command.go:1041\nmain.main\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/cmd/br/main.go:36\nruntime.main\n\t/go/pkg/mod/golang.org/[REDACTED_EMAIL]-amd64/src/runtime/proc.go:272"]
```

### 4. [REDACTED_USER]
master
<!-- Paste the output of SELECT tidb_version() -->
