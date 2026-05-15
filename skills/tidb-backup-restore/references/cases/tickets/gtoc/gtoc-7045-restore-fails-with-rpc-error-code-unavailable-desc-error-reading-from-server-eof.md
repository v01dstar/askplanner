# GTOC-7045: Restore fails with rpc error: code = Unavailable desc = error reading from server: EOF

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7045
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-08-01T20:05:18.000+0800
- Updated: 2025-03-06T18:07:57.990+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

During restore, for very high concurrency values the `rateLimit` parameter doesn’t seem to have any effect.  
This issue was also discussed in a previous ticket - <custom data-type="smartlink" data-id="id-0">[REDACTED_SUPPORT_URL]> 

During the experiments, we tried restore by varying the `rateLimit` and the `concurrency` parameters. (The logs are attached in the previous ticket).

When we change the `concurrency` from 64 → 128, there is almost no impact on the overall performance and the time taken to perform the restore. The `rateLimit` parameter also seems to be respected.

However, when we go from 128 → 512, irrespective of the `rateLimit` value the restores always take the same amount of time.  
Our guess is that when we go above the default value of concurrency, i.e. 128, the `rateLimit` parameter is simply ignored.

Is it possible to investigate this?

## Recent Comments Excerpt

### 2024-08-06T18:37:12.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Aug/24 10:36 AM

Hi [REDACTED_USER],
For 
"When we change the
 
concurrency

### 2024-08-06T19:08:37.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Aug/24 11:08 AM

Are you planning to fix this error in the next release?

### 2024-08-06T21:45:27.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Aug/24 1:45 PM

You means this “We don't recommend the concurrency too high ( such as 512 ) , because it may lead too some unexpected TiKV problems”？

### 2024-08-06T23:31:08.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Aug/24 3:31 PM

> You means this “We don't recommend the concurrency too high ( such as 512 ) , because it may lead too some unexpected TiKV problems”？
Yes
And also why this error came ?
I0606 05:04:45.893027 9 restore.go:176] [2024/06/06 05:04:45.892 +00:00] [WARN] [backoff.go:170] ["retry to import ssts"] [attempt=8] [error="rpc error: code = Unavailable desc = error reading from server: EOF"] [errorVerbose="rpc error: code = Unavailable desc = error reading from server: EOF\ngithub.com/pingcap/errors.AddStack\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/errors.go:174\ngithub.com/pingcap/errors.Trace\n\t/go/pkg/mod/github.com/pingcap/errors@v0.11.5-0.[REDACTED_LONG_ID]-b66cddb77c32/juju_adaptor.go:15\ngithub.com/pingcap/tidb/br/pkg/restore.(*FileImporter).downloadSST.func1\n\t/home/jenkins/agent/workspace/build-common/go/src/github.com/pingcap/br/br/pkg/restore/import.go:724\ngolang.org/x/sync/errgroup.(*Group).Go.func1\n\t/go/pkg/mod/golang.org/x/sync@v0.3.0/errgroup/errgroup.go:75\nruntime.goexit\n\t/usr/local/go/src/runtime/asm_amd64.s:1650"]

### 2024-08-07T18:49:23.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 07/Aug/24 10:49 AM

Hi [REDACTED_USER], 
I don't think it is a particular issue but a boundary, but we should added some max value limitation, such as the max value of concurrency is 256. 
We suspect the cluster has restarted during restore from the 512 concurrency log , the restore task can’t connect to TiKV and has to retry import.
Regards
Jiamin Li
