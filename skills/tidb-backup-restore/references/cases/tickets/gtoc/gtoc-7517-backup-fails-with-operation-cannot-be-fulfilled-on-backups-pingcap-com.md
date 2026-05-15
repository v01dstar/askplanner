# GTOC-7517: Backup fails with Operation cannot be fulfilled on backups.pingcap.com

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7517
- Status: Canceled
- Resolution: Cancel
- Priority: P2
- Issue type: Incident
- Created: 2025-04-07T11:21:41.349+0800
- Updated: 2025-05-26T13:39:21.596+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR, TiDB Operator
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We are seeing an elevated rate of backup failures on our prod [REDACTED_ENV_NAME] after our most recent release. Previously we saw backups succeeding at a \~99% rate and it is \~92% over the last week.

Recent backup failures show the same symptom, which is one of the federated data plane backup jobs fails with the following logs:

```
Defaulted container "backup" out of: backup, logging, br (init)
Create rclone.conf file.
/[REDACTED_RESOURCE_NAME] backup --namespace=[REDACTED_NAMESPACE] --backupName=[REDACTED_RESOURCE_NAME] --tikvVersion=v6.5.4-v16.6-abnb --mode=volume-snapshot --cluster-tls=true
I0404 00:41:23.005769       9 backup.go:78] start to process backup [REDACTED_ENV_NAME]/fed-skd-2025-04-04t00-40-00
I0404 00:41:23.019101       9 backup_status_updater.go:128] Backup: [[REDACTED_ENV_NAME]/fed-skd-2025-04-04t00-40-00] updated successfully
E0404 00:41:23.023764       9 backup_status_updater.go:131] Failed to update backup [[REDACTED_ENV_NAME]/fed-skd-2025-04-04t00-40-00], error: Operation cannot be fulfilled on backups.pingcap.com "fed-skd-2025-04-04t00-40-00": the object has been modified; please apply your changes to the latest version and try again
E0404 00:41:23.039545       9 backup_status_updater.go:131] Failed to update backup [[REDACTED_ENV_NAME]/fed-skd-2025-04-04t00-40-00], error: Operation cannot be fulfilled on backups.pingcap.com "fed-skd-2025-04-04t00-40-00": the object has been modified; please apply your changes to the latest version and try again
E0404 00:41:23.055508       9 backup_status_updater.go:131] Failed to update backup [[REDACTED_ENV_NAME]/fed-skd-2025-04-04t00-40-00], error: Operation cannot be fulfilled on backups.pingcap.com "fed-skd-2025-04-04t00-40-00": the object has been modified; please apply your changes to the latest version and try again
E0404 00:41:23.071076       9 backup_status_updater.go:131] Failed to update backup [[REDACTED_ENV_NAME]/fed-skd-2025-04-04t00-40-00], error: Operation cannot be fulfilled on backups.pingcap.com "fed-skd-2025-04-04t00-40-00": the object has been modified; please apply your changes to the latest version and try again
E0404 00:41:23.086680       9 backup_status_updater.go:131] Failed to update backup [[REDACTED_ENV_NAME]/fed-skd-2025-04-04t00-40-00], error: Operation cannot be fulfilled on backups.pingcap.com "fed-skd-2025-04-04t00-40-00": the object has been modified; please apply your changes to the latest version and try again
Error from server (Conflict): Operation cannot be fulfilled on backups.pingcap.com "fed-skd-2025-04-04t00-40-00": the object has been modified; please apply your changes to the latest version and try again
Sleeping for 30 seconds to let sidecars upload metrics...
Sleeping for 30 seconds to let sidecars to terminates...
```

From the logs it appears that the backup isn’t failing due to issues with AWS or the EBS snapshots, but instead tidb-operator is failing to update the backup CR due to optimistic concurrency conflicts and it never attempts to perform volume snapshots. This issue appears to be sporadic/intermittent and causing the increased rate of backup failures.

Our latest tidb-operator release includes the following fixes/cherry-picks

* <custom data-type="smartlink" data-id="id-0">https://github.com/pingcap/tidb-operator/pull/5530</custom>  
* <custom data-type="smartlink" data-id="id-1">https://github.com/pingcap/tidb-operator/pull/6087</custom> 
* <custom data-type="smartlink" data-id="id-2">https://github.com/pingcap/tidb-operator/pull/5735</custom>

## Recent Comments Excerpt

### 2025-04-07T11:23:25.432+0800 [REDACTED_USER]

Customer’s Backup always failed as "the object has been modified" exceeds max internal retries.
Please L3 to check how to eliminate theses "the object has been modified" reconciling errors. Thanks.
Customer’s tidb-operator has been applied the following PRs:
https://github.com/pingcap/tidb-operator/pull/5530
https://github.com/pingcap/tidb-operator/pull/6087
https://github.com/pingcap/tidb-operator/pull/5735

### 2025-04-07T17:24:31.894+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2025-04-08T01:13:07.631+0800 [REDACTED_USER]

[REDACTED_MEDIA]
yaml output from the failed bk


current release (w/ 92% success rate): 
TiDB Operator Version: http://version.Info {GitVersion:"v1.5.1-v15.4-abnb", GitCommit:"76d4b3c6afcb36d69188cc2e3df687bc6e444491", GitTreeState:"clean", BuildDate:"2025-03-11T21:15:14Z", GoVersion:"go1.21.3", Compiler:"gc", Platform:"linux/amd64"}

### 2025-04-08T10:41:37.532+0800 [REDACTED_USER]

From customer [REDACTED_CUSTOMER]:
are there any other unofficial release version fixes
We have many other changes as we forked from v1.5.1 and have cherry-picked many upstream changes in the meantime. However in this specific release there are no other operator changes in the diff

### 2025-04-10T09:28:50.687+0800 [REDACTED_USER]

[REDACTED_MEDIA]
Please help me take a look. The customer [REDACTED_CUSTOMER]is code has existed for a long time, what changes in tidb-operator have caused this error to be reported more frequently? L1 guessed that it is unstable to reproduce. Now the system has increased the number of calls, so the frequency of occurrence has increased.
