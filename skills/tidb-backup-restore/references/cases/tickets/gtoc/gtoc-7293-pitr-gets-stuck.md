# GTOC-7293: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7293
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-12-05T08:49:57.000+0800
- Updated: 2025-03-06T17:45:40.495+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

The log backup job is paused:

   
 {{}}

```java
sudo docker exec -it tidb-pd br log status  --pd=[REDACTED_ENV_NAME].ec2.pin220.com:2379 --ca /var/lib/normandie/fuse/ca/root --cert /var/lib/normandie/fuse/chain/generic --key /var/lib/normandie/fuse/key/generic  Detail BR log in /tmp/br.log.2024-12-04T21.15.37Z  ● Total 1 Tasks. > #1 <               name: pitr_1             status: ● PAUSE              start: 2024-11-29 05:17:51.31 +0000                end: 2090-11-18 14:07:45.624 +0000            storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]        speed(est.): 0.00 ops/s checkpoint[global]: 2024-12-02 14:17:02.16 +0000; gap=54h58m37s
```

 

   
   
 {{}}

```java
sudo docker exec -it tidb-pd br log resume --task-name=pitr_1  --pd=[REDACTED_ENV_NAME].ec2.pin220.com:2379 --ca /var/lib/normandie/fuse/ca/root --cert /var/lib/normandie/fuse/chain/generic --key /var/lib/normandie/fuse/key/generic --log-file=/var/log/tidb/br.log -L debug   Detail BR log in /var/log/tidb/br.log  [2024/12/04 21:12:43.228 +00:00] [INFO] [collector.go:77] ["log resume"] [streamTaskInfo="{taskName=pitr_1,startTs=[REDACTED_LONG_ID],endTS=[REDACTED_LONG_ID],tableFilter=*.*}"] [2024/12/04 21:12:43.230 +00:00] [INFO] [collector.go:77] ["log resume success summary"] [total-ranges=0] [ranges-succeed=0] [ranges-failed=0] [total-take=164.387739ms]
```

{{}}

 

 

While resuming the log backup job the TiDB SQL owner node reports:

```java

## Recent Comments Excerpt

### 2024-12-10T16:34:05.000+0800 [REDACTED_USER]

@[REDACTED_USER]
  what if pinterest applied 
https://github.com/pingcap/tidb/issues/57134
  and resume paused log backup as a workaround during the holiday season?

### 2024-12-12T04:08:31.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 

It looks like there are some test which are pending to be completed on the CP version for v8.1.1

https://github.com/pingcap/tidb/pull/57279

### 2024-12-12T07:54:25.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 we are working on the 8.1 cherry-pick, and pingcap is planning to release 8.1.2 around 12/20 before the holiday season.  pinterest can use that version if it's released in time.

### 2024-12-12T09:49:37.000+0800 [REDACTED_USER]

We don't want to go over the minor version upgrade process during the holiday season. Just to be clear it will be a cherry pick version on v8.1.1, right?

### 2024-12-13T22:18:38.000+0800 [REDACTED_USER]

the cherry-pick pr for 8.1 is 
https://github.com/pingcap/tidb/pull/58259
