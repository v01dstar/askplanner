# GTOC-6995: PITR log backup event loader failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6995
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-06-27T13:27:34.000+0800
- Updated: 2025-03-06T18:09:22.796+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, PiTR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

**Customer [REDACTED_CUSTOMER]**  
We were paged often by this alert, so we took a close look at this alert. One recent scenario was,

* the tikv tried to get the snapshot of a region that was assigned to the tikv instance recently, in initial_scan.do_initial_scan
* but the tikv lost the leadership of the region when do_initial_scan was called, which caused the snapshot to fail
* the failure was reported as a fatal error and tikv_log_backup_task_status was set to error  
  Is our understanding of the scenario correct?  
  Our questions are,
* the above failure looks like expected and transient as the region would be handled by the next leader.
* tikv_log_backup_task_status is shared by all regions of a tikv instance. Failure of any region would set the status to error. But success of any other region would reset the status to ok, which would mask the earlier failure. Is our understanding correct?
* what we do to handle the alert most of the time is simply run br log resume. Is it the best way to handle this alert? Does it make sense to auto resume this kind of failure?

**PingCAP answered；**  
1\. retry { do_initial_scan } --retry exhaustion--> task fatal.  From the function [https://github.com/tikv/tikv/blob/v6.5.9/components/backup-stream/src/subscription_manager.rs#L214](https://github.com/tikv/tikv/blob/v6.5.9/components/backup-stream/src/subscription_manager.rs#L214), （the code is for v6.5.9, but different versions have the same behavior here）, it would be stop to retry to start observer if the error is not retryable. Therefore, the fatal task means retrying exhaustion and the error is still retryable. The retryable error is usually unexpected. Besides, the total retry backoff time is about 5 minutes, so if retry exhaustion, the checkpoint will not advance for  5 minutes and RPO will be larger than 5 minutes.  
2\. the value \`tikv_log_backup_task_status\` is stored in the variable \`TASK_STATUS\`. It is changed to Running only when the log task is starting or resuming.  
3\. Yes, because currently, it cannot auto resume.

**Custom asked again：**  
The error in the br log status was

retry time exceeds: and error and error failed to get initial snapshot: failed to get the snapshot (region_id = 1149): Other Error: \[components/backup-stream/src/event_loader.rs:265\]: message 'CaptureChan  
ge' dropped for region 1149: oneshot canceled: failed to get initial snapshot: failed to get the snapshot (region_id = 1149): Other Error:

And we noticed another error message around the same time in the log

\["get snapshot failed"\] \[err="Error(Request(message:   
"peer is not leader for region 1149, leader may Some(id: 9354150 store_id: 7645543)  
" not_leader { region_id: 1149 leader { id: 9354150 store_id: 7645543 } }))"\]

## Recent Comments Excerpt

### 2024-06-27T14:05:25.000+0800 [REDACTED_USER]

Can you provide the entire error logs about region 1149? The error is `oneshot canceled`, which means the message is consumed by peer, but doesn't response to callback.
For the second question, it sleeps after each retry, 
https://github.com/tikv/tikv/blob/v6.5.9/components/backup-stream/src/subscription_manager.rs#L201
and the total duration is 345 seconds
https://github.com/tikv/tikv/blob/v6.5.9/components/backup-stream/src/subscription_manager.rs#L41-L54

### 2024-06-28T13:43:48.000+0800 [REDACTED_USER]

The error happens at 2024-06-19 19:11:32.813 from `br log status` command result. 

New peer was created at 2024-06-19 19:12:45 from tikv log provided.

```

[2024/06/19 19:12:45.493 +00:00] [INFO] [
raft.rs:388
