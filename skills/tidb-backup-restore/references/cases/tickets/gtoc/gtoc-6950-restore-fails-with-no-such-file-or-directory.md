# GTOC-6950: Restore fails with No such file or directory

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6950
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2024-06-06T08:57:41.000+0800
- Updated: 2025-03-06T18:10:59.266+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiKV
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

from our side, we tried to restore the data to the empty TiDB cluster [REDACTED_CLUSTER] 6.5.7. The first time during the restore, it caused the issue that the load does not distribute across the TiKV pod, and one of TiKV OOM and the other 11 TiKV pod utilization did not grow up at all, and the second time we had restore also same issue and one of TiKV facing the disk out of space. So please help to investigate and find the root cause that why the load does not distribute across the TiKV.

```
[2024/05/31 16:19:49.972 +07:00] [WARN] [server.rs:584] ["failed to remove space holder on starting: No such file or directory (os error 2)"]
[2024/05/31 16:19:49.972 +07:00] [WARN] [server.rs:593] ["no enough disk space left to create the place holder file"]
[2024/05/31 16:19:49.972 +07:00] [INFO] [mod.rs:127] ["encryption: none of key dictionary and file dictionary are found."]
[2024/05/31 16:19:49.972 +07:00] [INFO] [mod.rs:529] ["encryption is disabled."]
[2024/05/31 16:19:51.124 +07:00] [INFO] [engine.rs:93] ["Recovering raft logs takes 1.151742231s"]
[2024/05/31 16:19:51.606 +07:00] [ERROR] [engine_factory.rs:164] ["failed to create kv engine"] [err="Engine(Status { code: IoError, sub_code: None, sev: NoError, state: \"IO error: No space left on device: While appending to file: /var/lib/tikv/db/MANIFEST-100682: No space left on device\" })"] [path=/var/lib/tikv/db]
[2024/05/31 16:19:51.606 +07:00] [FATAL] [server.rs:1917] ["failed to create kv engine: Storage Engine Status { code: IoError, sub_code: None, sev: NoError, state: \"IO error: No space left on device: While appending to file: /var/lib/tikv/db/MANIFEST-100682: No space left on device\" }"]
```

## Recent Comments Excerpt

### 2024-07-01T13:09:05.000+0800 [REDACTED_USER]

Any updates? If there is no feedback, the ticket will be closed within 2 days.

### 2024-07-01T15:06:13.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/Jul/24 7:05 AM

In summary, you confirmed that the unevenly distributed load come from the imbalance of zones. If we make sure that the nodes is balance for all zone. This issue will not reappear right?

### 2024-07-01T15:37:55.000+0800 [REDACTED_USER]

yes, please make sure that the nodes is balanced for all zone

### 2024-07-01T15:53:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/Jul/24 7:53 AM

Hi,
Yes, that's correct. If you encounter a similar situation next time, you could first check if the nodes are balanced for all zone.

### 2024-07-03T10:45:16.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 03/Jul/24 2:45 AM

Ok we will take note on that. Thank you for your support
