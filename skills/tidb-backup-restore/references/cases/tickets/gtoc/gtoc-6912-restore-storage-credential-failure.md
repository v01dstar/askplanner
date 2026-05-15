# GTOC-6912: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6912
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2024-05-10T20:29:14.000+0800
- Updated: 2025-03-06T18:12:04.851+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB Lightning
- Categories: backup-failure, storage-credential, tikv-data-path, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

I am taking the full backup of tidb cluster and when i am trying to restore the backup on another cluster we are facing issue .

issue: while restoring view it is showing issue

backup command:  tiup dumpling -u datawarehouse_dev -pdatawarehouse654 -P 4000 -h [tidb.pntrzz.com](http://tidb.pntrzz.com) --filetype sql -t 8 -o 'gs://[REDACTED_ENV_NAME]/backup_tidb/full-backup' -r 200000 -F 256MiB --gcs.credentials-file tiup_svc_dev.json -W=false

restore file: file is attach in attachment

## Recent Comments Excerpt

### 2024-05-13T18:53:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/May/24 10:53 AM

i want to proceed with 3rd way should i move those 2 file to another s3 bucket and load other should it work?

### 2024-05-13T18:55:06.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/May/24 10:54 AM

Hi @[REDACTED_USER] ,
Please refer to the following documents

{{# Only import tables if these wildcard rules are matched. See the corresponding section for details. filter = ['
.
', '!mysql.

### 2024-05-13T19:01:06.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/May/24 11:00 AM

i want to proceed with 3rd way should i move those 2 file to another s3 bucket and load other should it work?
--Yes, Please try

### 2024-05-13T19:49:07.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/May/24 11:48 AM

thanks @[REDACTED_USER], thanks for support like we can go with filter and then we should manually recreate this view on new cluster.

### 2024-05-13T20:43:58.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/May/24 12:43 PM

Hi @[REDACTED_USER] two cluster diff variables.Please use TiUP to diff 
tiup dba diff --help
For example diff two cluster tidb variables.(TiKV,PD are same)

--diff-type
