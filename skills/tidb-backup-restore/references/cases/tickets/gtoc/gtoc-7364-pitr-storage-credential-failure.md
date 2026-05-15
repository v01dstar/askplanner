# GTOC-7364: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7364
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-01-23T07:51:11.625+0800
- Updated: 2025-03-06T17:38:41.567+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Now that we think we’ve resolved <custom data-type="smartlink" data-id="id-0">[REDACTED_SUPPORT_URL]>/[GTOC-7320](https://jira.tidbcloud.com/browse/GTOC-7320) and after we have resolved <custom data-type="smartlink" data-id="id-1">[REDACTED_SUPPORT_URL]>/GTOC-7347, we’d like to return to the issue of slow log replay performance during PITR.

I’ve included clinic metrics (<custom data-type="smartlink" data-id="id-2">[REDACTED_CLINIC_URL]>), logs, and CR from a recent PITR that we ran for 3d of logs. The restore runs w/ the following config:

```
br.pitr-concurrency: 2048
import.num-threads: 28

# defaults
import.import-mode-timeout: 10m
import.memory-use-ratio: 0.3
import.stream-channel-window: 128
```

The log restore phase took 4hrs, implying throughput of 2GB/tikv/hr. Extrapolating this performance to 1d of logs translates to an RTO of roughly 4hrs, just barely meeting our requirements for a UDS workload that does not have high write throughput. This remains pretty slow compared to our expectations.

I checked node network metrics and don’t see any meaningful BW throttling that we previously observed during the log apply phase either. However, I do see some EBS throttling due to throughput, where an individual TiKV node uses the full 800MB/s of EBS throughput for about \~5min before dropping back down. This happens cyclically every \~30min on the top of every hour and half hour (however we actually see this pattern across many of our TiDB clusters – could this be some regular background operation like GC?). This only affects a couple of tikvs at a time, and the large majority of tikvs for the majority of time are not EBS throughput throttled.

I also observe the period 22:06Z- 22:24Z where no tikvs are performing any meaningful import work. Could this be a period where a single slow tikv became the bottleneck and slowed down the rest of the log restore processes? I observe the following log from restore:

```
I0121 22:24:25.645585       9 restore.go:176] [2025/01/21 22:24:25.645 +00:00] [INFO] [split.go:671] ["end to split the regions"] [takes=19m35.17279039s]
```

It appears a split-scatter operation took almost 20min corresponding w/ the period where no restore work is being done. Can we also debug what was happening during this period? Don’t see anything obvious from Scatter and Splitter section on the PD dashboard.

I’d also like to discuss the effect of `br.pitr-concurrency`. We ran another PITR over the same period of logs w/ 512 concurrency and observed the log apply phase take \~5hrs, so we do see some performance improvement w/ higher concurrency but it also appears to be diminishing returns/non-linear increase. Would you expect further improved performance by bumping pitr-concurrency even higher?

## Recent Comments Excerpt

### 2025-02-26T06:01:26.800+0800 [REDACTED_USER]

We have run subsequent PITR tests with updated raft log GC settings to see if it improves restore performance. 
[REDACTED_CLINIC_URL]
  Relevant configs.
BR
concurrency=256
[REDACTED_RESOURCE_NAME]=64
pitr-batch-count=128
pitr-concurrency=4096

### 2025-02-26T16:15:58.529+0800 [REDACTED_USER]

Is there a better balance of configs we can set here? It seems the desire to retain more raft logs increases memory usage on the tikv, which slows down restore apply requests, so these configs are in tension. Ie. any improvements we make to reduce sent snapshots also hurts performance in via tikv flow control.
could the high disk usage and EBS throttling be related to compaction

There maybe one more thing to control L0 files and help increase the write heavy scenario, it to set memtable related rocksdb config.
Here is 3 useful rocksdb configurations:
write-buffer-size
: control the max size of a memtable.
storage.flow-control.memtables-threshold

### 2025-02-26T16:19:40.185+0800 [REDACTED_USER]

From another issue, I saw samiliar restore logs.
 ["import files done"] [batch-count=128] xxx
 ["import files done"] [batch-count=1] [batch-size=
298826455
] [take=2m51.522378979s] [files="[\"v1/20250216/11/30565823/[REDACTED_LONG_ID]-[REDACTED_UUID].log, \"]"]
 ["import files done"] [batch-count=128] xxx

that large size of log file is likely the cause of write skew. which implies upstream has a hot spot write on one region in a flush time.

### 2025-03-05T04:30:08.260+0800 [REDACTED_USER]

Here is 3 useful rocksdb configurations:
Do we apply these on the source (backup) cluster or on the restore side? If backup, then these would affect online serving, we have limited ability to make any changes there. If restore, then yes we could update them, but we’d customize them for the duration of the PITR and then reset them back to their original values to get the cluster in a serving state.
Can you upload the screenshot of this metrics?
[REDACTED_MEDIA]
that large size of log file is likely the cause of write skew. which implies upstream has a hot spot write on one region in a flush time.
I ran a quick script to analyze the distributions of log import sizes and durations. Here’s a scatter of the data from this restore’s logs
               size         count      duration
count  1.126972e+06  1.126972e+06  1.126972e+06

### 2025-03-05T17:26:05.160+0800 [REDACTED_USER]

Do we apply these on the source (backup) cluster or on the restore side?

on the restore side.



There appear to be large batches w/ very little data that take a long time to import (spike on left of plot). Otherwise it appears to smaller batches and smaller data sizes that take the longest to import.
Given the batch size distribution is bimodal w/ many 1 file batches and many 128-file batches, is there any tuning we should do with
