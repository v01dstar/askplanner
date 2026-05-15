# GTOC-6935: PITR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6935
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-05-23T10:32:47.000+0800
- Updated: 2025-03-07T10:55:32.035+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, sync-diff-inspector
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello PingCAP, 

1\. After PITR restore, what is recommended way to do data validation?

2\. Does it have some automatic checksum mechanism that guarantees data restored is valid?

```
INFO] [collector.go:77] ["restore log success summary"] [total-take=22m39.091851295s] [restore-from=[REDACTED_LONG_ID] [restore-to=[REDACTED_LONG_ID] [restore-from="2024-05-14 00:00:03.274 +0000"] [restore-to="2024-05-14 11:00:00 +0000"] [total-kv-count=53125269] [skipped-kv-count-by-checkpoint=0] [total-size=25.48GB] [skipped-size-by-checkpoint=0B] [average-speed=18.74MB/s]
```

3\. Or should I use `sync_diff_inspector`?   
If so, what TSO values are needed source and target `snapshot` field?  
Is it `restore-to=[REDACTED_LONG_ID]` from  log restore?

4\. If I setup TiCDC replication, I was able to use “usual” `sync_diff_inspector` to do data validation (it showed no differences)

3\. Without TiCDC this didn’t work. I increased GC lifetime on both source and target clusters, did PITR restore and tried using `sync_diff_inspector` with same `restore-to}}TSO and it failed as shown below. I checked both clusters had {{taxify_admin_user._meta` table.

```
pitr restore
...
[2024/05/18 01:21:50.178 +00:00] [INFO] [collector.go:77] ["restore log success summary"] [total-take=3h9m5.08878665s] [restore-from=[REDACTED_LONG_ID] [restore-to=[REDACTED_LONG_ID] [restore-from="2024-05-14 00:00:03.274 +0000"] [restore-to="2024-05-17 19:00:00 +0000"] [total-kv-count=508661661] [skipped-kv-count-by-checkpoint=0] [total-size=220.4GB] [skipped-size-by-checkpoint=0B] [average-speed=19.43MB/s]

# sync diff 
leandro@ti-manager:~$ cat pitr-sync-diff-config.toml  | grep -v "#" | grep -v password | tr -s '\n' '\n'

check-thread-count = 4
export-fix-sql = true

## Recent Comments Excerpt

### 2024-05-29T15:28:57.000+0800 [REDACTED_USER]

About your first 3 questions:
1. For now, you may use 
sync_diff_inspector
. That is the best practice for now and we are also using it in internal testing. You may also use the 
ADMIN CHECKSUM TABLE
 statement with 
reading historical data
.

### 2024-05-29T18:24:42.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/May/24 10:24 AM

hi @[REDACTED_USER] your first 3 questions:
For now, you may use 
sync_diff_inspector
. That is the best practice for now and we are also using it in internal testing. You may also use the 
ADMIN CHECKSUM TABLE

### 2024-05-29T18:55:18.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/May/24 10:55 AM

Hello Haifeng,
Thanks for the answers. 
Regarding the 
sync_diff_inspector
, was speaking with Daniel and we found a bug:

### 2024-05-30T13:55:41.000+0800 [REDACTED_USER]

Oops... After checking with 
@[REDACTED_USER]
, I have noticed that we 
should not
 use snapshot reading in the downstream... (i.e. we need to remove the "snapshot" option in the 
data-sources.tidb0
)
I also agree that printing

### 2024-05-30T14:14:33.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/May/24 6:14 AM

hi  @[REDACTED_USER] checking , I have noticed that we 
should not
 use snapshot reading in the downstream... (i.e. we need to remove the "snapshot" option in the 
data-sources.tidb0
)
