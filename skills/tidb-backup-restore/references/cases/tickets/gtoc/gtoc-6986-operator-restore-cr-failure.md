# GTOC-6986: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6986
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2024-06-24T18:20:53.000+0800
- Updated: 2025-03-06T18:09:38.880+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR, TiDB Operator, TiKV
- Categories: backup-failure, tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER],

While doing PRDTMP restoration, the Jenkins has been failed with Low Disk space issue. we have tried deleting .sst file and trying to drop the databases but not working as .sst files are deleted successfully, but dropping database is not stucked and the process also and TIKV Pod is stuck with CrashLoopBackOff error. Can you please help with any other solution to fix CrashLoopBackOff error apart from recreate the cluster. 

Thanks and Regards,

Sivaraman.K

## Recent Comments Excerpt

### 2024-07-03T16:45:11.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 03/Jul/24 8:45 AM

Hi,
The official recommendation is at least three replicas, or an odd number of replicas greater than 3, to ensure high availability and disaster recovery capabilities.
Best regards,
Sam

### 2024-07-03T17:00:01.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 03/Jul/24 8:59 AM

Hi
You mean this value right? 
https://docs.pingcap.com/tidb/stable/pd-configuration-file#replication
 
Thanks
May

### 2024-07-03T17:35:04.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 03/Jul/24 9:34 AM

Yes, replication.max-replicas .

### 2024-07-04T17:34:47.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 04/Jul/24 9:34 AM

Hi [REDACTED_USER],
Thank you so much for your strongly support now we able to restore already
Thankyou 
May

### 2024-07-04T18:41:02.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 04/Jul/24 10:40 AM

Dear Customer,
Hello!
We are pleased to have resolved your issue. We plan to close the ticket in 24 hours. If you encounter any trouble or have any questions during this period, please feel free to contact us before the ticket is closed.
Thank you for your understanding and cooperation!
Best regards,
Sam
