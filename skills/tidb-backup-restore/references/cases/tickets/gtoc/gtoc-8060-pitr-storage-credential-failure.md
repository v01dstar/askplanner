# GTOC-8060: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8060
- Status: Todo
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-11-25T10:03:54.255+0800
- Updated: 2026-01-13T20:50:48.235+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We’re required to have object lock enabled on our backup S3 buckets (both for snapshot and log based backups). This seems to be fine other than the fact that when a PITR happens (utilizing the log backup) a lockfile has to be written if I understand correctly. This is incompatible with object lock on an S3 bucket. If we can provide a separate S3 bucket for this lockfile to be stored in (apart from the actual backup data) we can keep object lock off of that bucket.

## Recent Comments Excerpt

### 2025-11-25T10:03:58.554+0800 [REDACTED_USER]

fail to find L2 assignee: please escalate to L3

### 2025-11-25T10:04:00.834+0800 [REDACTED_USER]

assign to 钟瀚震([REDACTED_EMAIL])

### 2025-11-25T10:04:02.448+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100b5d64a7d64cbcc49a130ad4f1270) by lark

### 2025-11-25T10:05:18.786+0800 [REDACTED_USER]

给研发的需求
现状（研发已确认）
无论是 snapshot restore 还是 PITR restore，只要目标集群配置过 log-backup，BR 在执行 restore 时都会在 
log-backup 所在的 S3 bucket
 写入一个 
临时 lockfile
，并在 restore 结束后删除。
客户的问题
