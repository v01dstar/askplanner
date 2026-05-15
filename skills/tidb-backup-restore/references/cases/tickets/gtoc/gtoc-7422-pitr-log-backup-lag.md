# GTOC-7422: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7422
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-02-25T08:32:51.151+0800
- Updated: 2025-04-01T14:08:17.647+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We would like to understand the specific steps that are occurring in a PITR, specifically those that are occurring in the log replay portion of PITR, their purpose, and if there are any other opportunities to improve PITR performance. For this examination, I’m using the attached restore CR and restore logs as an example, but these pertain to any PITR instance that we run. This example is a PITR of a snapshot and 1d of logs from the full-shadow cluster.

First, from the restore CR, we observe the following status progresses:

```
  progresses:
  - lastTransitionTime: "2025-02-22T18:08:08Z"
    progress: 100
    step: Full Restore
  - lastTransitionTime: "2025-02-22T18:42:39Z"
    progress: 100
    step: Restore Meta Files
  - lastTransitionTime: "2025-02-22T19:59:51Z"
    progress: 100
    step: Restore KV Files
```

These map to progress printers in the restore pod/BR kernel. However, they appear to only show the progress completion time, without indication of when that progress began. We can see the detailed progress from the restore logs themselves.

```
I0222 17:05:36.104830       9 restore.go:176] [2025/02/22 17:05:36.098 +00:00] [INFO] [progress.go:160] [progress] [step="Full Restore"] [progress=4.92%] [count="120748 / 2452643"] [speed="? p/s"] [elapsed=2m0s] [remaining=?]
I0222 18:08:08.751726       9 restore.go:176] [2025/02/22 18:08:08.745 +00:00] [INFO] [progress.go:160] [progress] [step="Full Restore"] [progress=100.00%] [count="2452643 / 2452643"] [speed="654 p/s"] [elapsed=1h4m33s] [remaining=1h4m33s]
...
I0222 18:36:32.321106       9 restore.go:176] [2025/02/22 18:36:32.314 +00:00] [INFO] [progress.go:160] [progress] [step="Restore Meta Files"] [progress=0.00%] [count="0 / 2374"] [speed="? p/s"] [elapsed=2m0s] [remaining=?]
I0222 18:42:39.451627       9 restore.go:176] [2025/02/22 18:42:39.445 +00:00] [INFO] [progress.go:160] [progress] [step="Restore Meta Files"] [progress=100.00%] [count="2374 / 2374"] [speed="6 p/s"] [elapsed=8m7s] [remaining=8m7s]
...
I0222 18:56:56.185626       9 restore.go:176] [2025/02/22 18:56:56.179 +00:00] [INFO] [progress.go:160] [progress] [step="Restore KV Files"] [progress=0.15%] [count="62251 / 40972099"] [speed="? p/s"] [elapsed=2m0s] [remaining=?]
I0222 19:59:51.330367       9 restore.go:176] [2025/02/22 19:59:51.322 +00:00] [INFO] [progress.go:160] [progress] [step="Restore KV Files"] [progress=100.00%] [count="40972099 / 40972099"] [speed="10853 p/s"] [elapsed=1h4m55s] [remaining=1h4m55s]

## Recent Comments Excerpt

### 2025-02-25T15:45:01.278+0800 [REDACTED_USER]

Are all of the above steps post-Full Restore considered part of the log restore phase? Including the operations discussed in the gap periods that are not covered by the progress? So in this case, we can consider the duration of the log replay phase to occur from 18:08-19:59 (1hr51m)

Yes, and from the summary log, it shows ["restore log success summary"] [total-take=
1h51m45.607640914s
]

### 2025-02-25T15:50:00.619+0800 [REDACTED_USER]

And if so, how do these relate to PingCAP’s estimates of log replay throughput as 30GB/hr/tikv under optimal conditions? Does the performance estimate entail all stages of log replay? Or does it specifically pertain to the expected performance during the “Restore KV Files” stage? Given that this PITR replays 315GiB of S3 log data, should we estimate the log replay performance as 315GiB/135tikvs/1h51m? Or as 315GiB/135tikvs/65min?

Actually we estimate by real time(1h51m), but this is a good question, we may need to split the stage if other stage consume a lot of time. we may need much more details log of other stage.

### 2025-02-25T16:41:01.185+0800 [REDACTED_USER]

For the post meta restore gap, it appears the slow operation is 
client.RangeFilterFromIngestRecorder
 (
https://github.com/pingcap/tidb/blob/v8.1.1/br/pkg/task/stream.go#L1404
), which iterates the tables and rewrites the table IDs to the newly restored versions. However, I’m unable to confirm this from the logs, but from perusal of the code it doesn’t appear that any other calls made 
between the “Restore Meta Files” and “Restore KV Files” steps
 would require 8mins. 
Could this be the long-running operation and are there any easy ways to improve its performance?

### 2025-02-28T07:00:26.331+0800 [REDACTED_USER]

Airbnb Rishabh added one more question:  why it need to set start_ts as min_begin_ts of a file. Can’t tikv just ignore the partial content of a file ?

### 2025-02-28T09:22:45.558+0800 [REDACTED_USER]

When determine a [start-ts, restore-ts] range of restore. which means determine commit ts in this range. but the txn start before start-ts, which is min_begin_ts. 

So BR will find out all possible txn with min_begin_ts to make sure no data loss.
