# GTOC-7413: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7413
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-02-21T13:54:11.578+0800
- Updated: 2025-03-25T15:01:01.573+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We have one tidb cluster `[REDACTED_ENV_NAME]` having issue with back up log task checkpoint TS not advancing since the task was created.

```
[root@[REDACTED_ENV_NAME]:~]# br log status
Detail BR log in /tmp/br.log.2025-02-19T07.47.14Z 
● Total 1 Tasks.
> #1 <
              name: pitr3
            status: ● NORMAL
             start: 2025-02-19 07:31:39.165 +0000
               end: 2090-11-18 14:07:45.624 +0000
           storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
                    s-prod/pitr3
       speed(est.): 174385.44 ops/s
checkpoint[global]: 2025-02-19 07:31:39.165 +0000; gap=15m39s
```

You can check the S3 path and find logs are actually keeping updated there, so I think it is a bug in the checkpoint side.

Here is one example:  

```
[root@[REDACTED_ENV_NAME]:~]# aws s3 ls s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
2025-02-19 07:39:15   45012822 [REDACTED_LONG_ID]-[REDACTED_UUID].log
2025-02-19 07:39:16       3355 [REDACTED_LONG_ID]-[REDACTED_UUID].log
2025-02-19 07:46:42   15564189 [REDACTED_LONG_ID]-[REDACTED_UUID].log
2025-02-19 07:41:42   14462584 [REDACTED_LONG_ID]-[REDACTED_UUID].log
2025-02-19 07:44:12   15256382 [REDACTED_LONG_ID]-[REDACTED_UUID].log

## Recent Comments Excerpt

### 2025-02-21T19:02:36.253+0800 [REDACTED_USER]

After the log backup task pitr3 was created, the TiDB advancer owner was unable to complete any global checkpoint update. It always failed in the process of scanning regions. We can see a large number of failure logs in the TiDB log until 
2025/02/20 09:00:07.375 +00:00
.
"caller":"regioniter.go:138","message":"failed with trying to scan regions","error":"rpc error: code = DeadlineExceeded desc = context deadline exceeded"
PD received much GetRegion PRC requests at that time.

### 2025-02-24T10:45:13.513+0800 [REDACTED_USER]

https://github.com/tikv/tikv/issues/18243

### 2025-03-11T09:42:08.422+0800 [REDACTED_USER]

https://github.com/tikv/tikv/pull/18290
  wil fix the issue 
https://github.com/tikv/tikv/issues/18243

### 2025-03-11T11:13:24.596+0800 [REDACTED_USER]

https://github.com/pingcap/tidb/pull/59996
  will fix the issue that scan regions timeout

### 2025-03-25T15:00:46.419+0800 [REDACTED_USER]

https://github.com/pingcap/tidb/pull/59559
  can fix the issue that get region checkpoint ts timeout.
