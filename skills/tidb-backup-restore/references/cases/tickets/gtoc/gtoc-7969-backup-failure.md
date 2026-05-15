# GTOC-7969: Backup failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7969
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-10-15T14:30:41.028+0800
- Updated: 2026-03-23T19:15:01.093+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiKV
- Categories: backup-failure, tikv-data-path, performance-resource, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

The issue is looks similar to the incident but different date and nodes.   
<custom data-type="smartlink" data-id="id-0">[REDACTED_SUPPORT_URL]> 

There are duration spikes twice in these days.  
10/13 00:30\~01:00 JST  
10/15 01:00\~01:30 JST

Evict-leader was running at both timing on different TiKV nodes.  
These incidents were occurred during BR backup, but BR backup is executed every night and not happened always.

Grafana file: <custom data-type="smartlink" data-id="id-1">https://drive.google.com/drive/folders/1hvUA0y7r1hekmrN5eNJNeaZnSjevsPny?usp=drive_link</custom> 

As per checked from my send, suspecting disk issue.

 

1. 10/13 00:30\~01:00 JST ( 10/12 23:30 \~ 10/13 00:00 UTC+8)  
  Node: [REDACTED_IP]

    1. CPU Spike
    
        [REDACTED_MEDIA]
    2. Leader drop observed
    
        [REDACTED_MEDIA]
    3. Uptime have no abnormality
    
        [REDACTED_MEDIA]

## Recent Comments Excerpt

### 2025-10-15T14:30:47.534+0800 [REDACTED_USER]

assign to 江红梅([REDACTED_EMAIL])

### 2025-10-16T11:28:44.161+0800 [REDACTED_USER]

notified (黄必胜([REDACTED_EMAIL]), om_x100b40322875b2200f1ee891bf3c1d7) by lark

### 2025-10-16T11:34:21.426+0800 [REDACTED_USER]

Currently, I mainly suspect that a series of problems are caused by disk long-tail issues. Analyze logic :
 disk jitter -> slow-store-> awake region -> region leader re-election -> leader drop and gRPC busy(tikv report unreachable and channel full ).
Another possibility is that there is something wrong with the EC2, both in the disk and in the network, when the backup starts up.
Escalate to L3 to double-check that.

### 2025-10-16T15:04:36.905+0800 [REDACTED_USER]

I think several observations on our side suggest the disk was slow at that time. Even though the IOPS limit wasn’t hit, it could still be due to disk pressure. Have we checked with the cloud vendor?
[REDACTED_MEDIA]
[REDACTED_MEDIA]
[REDACTED_MEDIA]
The leader drop could be caused by raftstore being stuck by certain events. The slowness could also come from slow disk I/O — raftstore performs I/O occasionally as well, and v6.5.8 doesn’t include some of the recent raftstore optimizations that reduce I/O. I also suspect it might be related to the awakening of hibernate regions, triggered by a sudden write spike across many regions. Can we get the TiKV logs of `[REDACTED_IP]` to double check?
[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2026-03-23T19:14:48.678+0800 [REDACTED_USER]

Based on the final investigation, this case was most likely caused by underlying hardware or disk-level issues during the BR backup window, rather than by a confirmed TiDB product defect. We will close this ticket for now. If similar symptoms appear again, please collect the latest system and cloud-vendor level evidence and submit a new ticket.
