# GTOC-6842: Log backup checkpoint lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6842
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-15T23:01:44.000+0800
- Updated: 2025-03-06T18:14:24.225+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Currently, we are using BR v6.5.3 and normally it took 25-40 minutes to completed. However, for today we run BR backup along with TiKV rolling restart <custom data-type="smartlink" data-id="id-0">https://docs.pingcap.com/tidb-in-kubernetes/stable/[REDACTED_RESOURCE_NAME]</custom> which is confirmed by Jack(our Pingcap contact point) that restart shouldn’t impact on BR. Unfortunately, when we did, BR took more than 1 hour and still not finish

## Recent Comments Excerpt

### 2024-04-17T17:41:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 18/Jan/24 10:37 AM

Hi,
This issue appears to be caused by a previous TikV restart. A current workaround is to kill the br process and then re-run the br backup.

### 2024-04-17T17:41:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 18/Jan/24 10:46 AM

TiKV Backup CPU as requested. 
[REDACTED_MEDIA]

### 2024-04-17T17:41:27.000+0800 [REDACTED_USER]

commented by [REDACTED_EMAIL] - 18/Jan/24 10:53 AM

The TIKV-9 log and BR-Backup log as below attached files.
[REDACTED_MEDIA]

### 2024-04-17T17:41:27.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/Feb/24 3:19 AM

So actually we cannot restart during the BR process? Previously, I was informed from Pingcap that it shouldn’t related as it’s rolling restart

### 2024-04-17T17:41:27.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 04/Feb/24 3:26 AM

Hi,
From the log provided , the reason is that tikv restart caused br to enter an abnormal state. 
From the log, it can also be seen that the cluster is using the v5.1.5 version, which is relatively low. 
Therefore, in the current environment, it is not recommended to restart tikv during the br backup process.
[2024/01/18 07:54:27.439 +00:00] [WARN] [backup.go:359] ["unable to use checkpoint mode, fall back to normal mode"] [error="TiKV node [REDACTED_RESOURCE_NAME].[REDACTED_RESOURCE_NAME].[REDACTED_ENV_NAME].svc:20160 version 5.1.5 is too low when use checkpoint, please update tikv's version to at least v6.5.0
