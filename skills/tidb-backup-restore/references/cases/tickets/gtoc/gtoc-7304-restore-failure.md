# GTOC-7304: Restore failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7304
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-12-13T09:15:03.000+0800
- Updated: 2025-03-07T10:55:18.324+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

On a 70GB database we’re seeing restore speeds as slow as 150mbps and backup speeds as fast as 350mbps. Logs attached.

## Recent Comments Excerpt

### 2024-12-13T09:15:16.000+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), ) by lark

### 2024-12-13T17:15:06.000+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), ) by lark

### 2024-12-13T20:52:24.000+0800 [REDACTED_USER]

According to the log it seems the restore speed is 
average-speed=292MB/s
. 
Backup scans data from leaders only, while restoring requires rebuild all peers (usually 3 duplicates), so resotring may be slower than backing up.
Also it seems we cannot reuse the table ID from upstream because we are restoring to an existing cluster: 
[REDACTED_CLUSTER] 19:43:42.845644 9 restore.go:176] [2024/12/12 19:43:42.845 +00:00] [INFO] [client.go:286] ["registering the table IDs"] [ids="ID:empty(end=195)"]
This requires us to rebuild the SST files which will slow down the restoration. You may try to restore to a brand new cluster.

### 2025-03-02T11:04:12.332+0800 [REDACTED_USER]

@[REDACTED_USER]
 This ticket can be closed now. Thanks.
