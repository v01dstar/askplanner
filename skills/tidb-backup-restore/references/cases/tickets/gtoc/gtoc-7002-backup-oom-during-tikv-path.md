# GTOC-7002: Backup OOM during TiKV path

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7002
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2024-07-04T06:58:00.000+0800
- Updated: 2025-03-06T18:09:10.349+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiKV
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hey team, we are observing increased tikv memory usage and OOM during backups on our largest [REDACTED_ENV_NAME] cluster. These OOMs have occurred for two problematic tikvs (tikv-2-e and tikv-27-e) consistently over 3 consecutive backups. The backups complete successfully, but the tikv restart due to OOM causes errors and increased latency in serving online traffic.

We only observe these memory increases at regular cadence aligning w/ our backup schedule, which runs for this cluster runs every 30mins at xx:05 and xx:35.

Our initial hunch is that region scheduling/gc is paused for a longer period of time during recent backups which causes these tikvs to accumulate too much memory and OOM.

I’ve attached volume backup CRs, tikv logs. I will share clinic metrics shortly

## Recent Comments Excerpt

### 2024-07-06T08:40:06.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Jul/24 12:39 AM

Thanks for the update. Please keep us posted on the progress.

### 2024-07-13T03:56:20.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 12/Jul/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-07-13T06:53:42.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 12/Jul/24 10:53 PM

Hi, Rishabh,  as discussed in today’s call, the following is the recommended setting (see July 4, 2024 at 11:45 AM update)
Config `readpool.unified.max-tasks-per-worker` set the max number of tasks for 1 thread, so the total number of tasks is `readpool.unified.max-tasks-per-worker` * `readpool.unified.max-thread-count`.
In general, set the maximum of total number of tasks to a too large number is not very useful. In my experience, set it to around 10k~100k is enough.

### 2024-07-20T02:17:41.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 19/Jul/24 6:17 PM

thanks.

### 2024-07-22T23:31:04.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 22/Jul/24 3:30 PM

I am closing this ticket as this is an AWS issue. Please feel free to reopen if there is any concerns.
