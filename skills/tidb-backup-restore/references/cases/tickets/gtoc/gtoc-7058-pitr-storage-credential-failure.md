# GTOC-7058: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7058
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-08-07T06:12:17.000+0800
- Updated: 2025-03-06T18:07:34.457+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi,

The PITR log backup is not working on the TiDB cluster. 

PITR status: 

```
sudo docker exec -it tidb-pd br log status --task-name=pitr_2  --pd=[REDACTED_ENV_NAME].ec2.pin220.com:2379 --ca /var/lib/normandie/fuse/ca/root --cert /var/lib/normandie/fuse/chain/generic --key /var/lib/normandie/fuse/key/generic 
Detail BR log in /tmp/br.log.2024-08-02T03.14.07Z 
● Total 1 Tasks.
> #1 <
              name: pitr_2
            status: ● NORMAL
             start: 2024-08-01 23:51:43.627 +0000
               end: 2090-11-18 14:07:45.624 +0000
           storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
       speed(est.): 33.46 ops/s
checkpoint[global]: 2024-08-01 23:51:43.627 +0000; gap=3h22m25s
```

Clinic: <custom data-type="smartlink" data-id="id-0">[REDACTED_CLINIC_URL]> 

Also, attached the log files to the ticket.

## Recent Comments Excerpt

### 2024-08-15T00:42:13.000+0800 [REDACTED_USER]

attached logs for all the TiKV stores

### 2024-08-15T14:45:22.000+0800 [REDACTED_USER]

OK, from the latest provided logs, it has been determined that this is caused by the above known issue.
 
But sorry, you provided logs are still not from 08/02 to 08/05.
At the 2024-08-02 07:16:00, the backup stream scheduler of TiKV 0a03b7ee is stuck.
[REDACTED_MEDIA]
At the 2024-08-07 02:50:30, the backup stream scheduler of any TiKV is stuck.
[REDACTED_MEDIA]
Therefore, I wonder what happened during this time. TiKV logs from 08/02 to 08/05 are needed to check.

### 2024-08-16T11:05:46.000+0800 [REDACTED_USER]

Update: before use cherry-picked version, you can just adjust the TiKV config `log-backup.initial-scan-pending-memory-quota` to 4 GiB. Maybe it can solve the problem.
https://docs.pingcap.com/tidb/v7.1/tikv-configuration-file#initial-scan-[REDACTED_ENV_NAME]

### 2024-09-06T09:10:35.000+0800 [REDACTED_USER]

Can it be closed? If there is any new issue, maybe we can open another one.

### 2024-09-13T06:56:59.000+0800 [REDACTED_USER]

Yes, close the ticket. The patch seems to worked and fixed the issue.
