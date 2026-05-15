# GTOC-7248: PITR fails with Permission denied (os error 13)

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7248
- Status: Resolved
- Resolution: Done
- Priority: P0
- Issue type: Incident
- Created: 2024-11-15T12:29:01.000+0800
- Updated: 2025-03-06T17:52:10.082+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

pitr report following error:

```java
bash-5.1$  /br log status --pd http://[REDACTED_ENV_NAME]:2379
Detail BR log in /tmp/br.log.2024-11-13T13.54.09+0530
● Total 1 Tasks.
> #1 <
                    name: [REDACTED_RESOURCE_NAME]
                  status: ○ ERROR
                   start: 2024-11-13 13:05:09.814 +0530
                     end: 2090-11-18 19:37:45.624 +0530
                 storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
             speed(est.): 0.00 ops/s
      checkpoint[global]: 2024-11-13 13:05:09.814 +0530; gap=49m1s
          error[store=7]: KV:LogBackup:Io
error-happen-at[store=7]: 2024-11-13 13:05:10.827 +0530; gap=49m0s
  error-message[store=7]: I/O Error: Permission denied (os error 13)
          error[store=8]: KV:LogBackup:Io
error-happen-at[store=8]: 2024-11-13 13:05:10.825 +0530; gap=49m0s
  error-message[store=8]: I/O Error: Permission denied (os error 13)
```

the two pitr error tikv store keep print the following error:

```java
[2024/11/13 14:09:33.341 +05:30] [INFO] [logger.rs:14] ["EVENT_LOG_v1 {\"time_micros\": [REDACTED_LONG_ID], \"job\": 1773552, \"event\": \"flush_started\", \"num_memtables\": 1, \"num_entries\": 66789, \"num_deletes\": 0, \"total_data_size\": 131301856, \"memory_usage\": 133964144, \"flush_reason\": \"Write Buffer Full\"}"] [thread_id=0x4]
[2024/11/13 14:09:33.341 +05:30] [FATAL] [mod.rs:419] ["logger encountered error"] [err="Permission denied (os error 13)"]
[2024/11/13 14:09:33.341 +05:30] [INFO] [logger.rs:14] ["[db/flush_job.cc:857] [default] [JOB 1773552] Level-0 flush table #15741742: started"] [thread_id=0x4]

## Recent Comments Excerpt

### 2024-11-15T12:45:22.000+0800 [REDACTED_USER]

notified (高磊([REDACTED_EMAIL]), om_d458ac33c973572edcc3d3ca92105333) by lark and phone

### 2024-11-15T12:45:55.000+0800 [REDACTED_USER]

acked msg index: om_d6abc35eb47142d1ecc3bddafd09ebad

### 2024-11-15T12:45:55.000+0800 [REDACTED_USER]

acked msg index: om_6897ca022b4507a59972fd6fd56df55a

### 2024-11-15T12:45:56.000+0800 [REDACTED_USER]

ack by completing reading the Feishu message

### 2024-11-15T12:45:57.000+0800 [REDACTED_USER]

acked msg index: om_d458ac33c973572edcc3d3ca92105333
