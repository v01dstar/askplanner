# GTOC-6697: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6697
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-02-10T09:01:55.000+0800
- Updated: 2025-05-29T14:42:31.488+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Tikv-17-1b stuck in crash loop

\[2024/02/09 22:14:37.241 +00:00\] \[ERROR\] \[init_cluster.rs:309\] \["error while open kvdb: Storage Engine Status { code: IoError, sub_code: None, sev: NoError, state: \\"Corruption: SST file is ahead of WALs in CF lock\\" }"\]

backup successful on source cluster with no tikv restarts

sharing:

* backup

    * volumebackup CR
    * backup-b CR
    * backup logs from all jobs
    * logs from tikv that crashes in restore (tikv-17-1b)
    
* restore

    * volumerestore CR
    * restore-b CR
    * logs from crashing tikv (tikv-17-1b)
    

am working on uploading metrics from source (backup) cluster to clinic and will update when done

am also working on restoring the backup again into a new cluster to see if we can repro the issue, will update when done

## Recent Comments Excerpt

### 2024-05-03T01:03:06.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/May/24 5:02 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-05-06T01:02:22.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 05/May/24 5:01 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-05-07T05:01:18.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/May/24 9:01 PM

yes, please go ahead and close this ticket

### 2025-05-29T13:33:54.137+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b4c4b52d825640eca9d9b2d41564) by lark

### 2025-05-29T14:42:30.998+0800 [REDACTED_USER]

This should be a RocksDB problem which may lead to WAL lost when the whole disk crashes.
https://github.com/tikv/rocksdb/pull/357
