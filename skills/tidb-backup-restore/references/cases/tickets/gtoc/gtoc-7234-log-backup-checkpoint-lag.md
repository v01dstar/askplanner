# GTOC-7234: Log backup checkpoint lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7234
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-11-09T09:02:50.000+0800
- Updated: 2025-03-06T17:52:35.406+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, performance-resource
- Labels: N/A

## Symptom / Description Excerpt

We have a daily BR job to backup TIDB, when it runs, the application query latency spike up to 20 seconds so we have to keep BR. How can we effectively tune the knobs to make BR run so guarantee RPO/RTO without interrupting application?

More details see: [https://docs.google.com/document/d/1KniDA-4BHRgJkt-lmz-KsllJ-es-FAkKID7Z4CKsSlw/edit?tab=t.0#heading=h.inscxq8y83uo](https://docs.google.com/document/d/1KniDA-4BHRgJkt-lmz-KsllJ-es-FAkKID7Z4CKsSlw/edit?tab=t.0#heading=h.inscxq8y83uo)

## Recent Comments Excerpt

### 2024-11-09T21:20:50.000+0800 [REDACTED_USER]

Seems the ratelimit didn't work when concurrency is larger than 1.
I suggest user to set backup.num_threads = 2 to control  CPU usage。

### 2024-11-10T02:07:37.000+0800 [REDACTED_USER]

Thanks Hanzhen for taking a look!
 
The customer [REDACTED_CUSTOMER] at around 70% and no IO progress is being made, and they wonder if the IO quota is exhausted. Progress bar stopping at 70% is very likely due to backup progress finished the upload and was doing checksum as we see many similar reports. There is an ongoing fix to make it better in this PR 
https://github.com/pingcap/tidb/pull/56612
As suggested by Hanzhen, we can probably tune the num threads to be 2. The rate limit seems not controlling the disk read during full backup, and it might be controlled by thread_num * batch size, I'm confirming with the rest of the team. If it's true it's definitely not ideal and we need to fix it.
Looks like user turns on the backup.enable-auto-tune, I'm afraid even if we tune thread down to 2 this auto tune might tune it up if some vCPU is available and thus impact the online traffic. We can probably turn that off as well. Will confirm with the team too.

### 2024-12-01T03:52:23.000+0800 [REDACTED_USER]

This ticket can be closed now. Thanks.
