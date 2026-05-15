# GTOC-6846: Operator backup CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6846
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-04-16T13:28:56.000+0800
- Updated: 2025-03-06T18:14:16.601+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Happened twice on the same cluster in successive backups (15min apart). Same zone (a) failed both times.

Error log:

**Error from server (Conflict): Operation cannot be fulfilled on** [**backups.pingcap.com**](http://backups.pingcap.com) **"fed-skd-2024-04-13t00-45-00": the object has been modified; please apply your changes to the latest version and try again**

I’ve attached backup job, operator, and br-federation-manager logs from the first of these instances.

## Recent Comments Excerpt

### 2024-04-20T03:04:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 19/Apr/24 7:04 PM

@xiao : What updates the Backup CRD. I’m assuming its backup pod, and operator. Also What backoff is this. Is that configurable from the backup CRD.

### 2024-04-22T11:26:04.000+0800 [REDACTED_USER]

The backup pod updated the Backup CR, but the cache in the backup pod didn't be updated in time, which caused the conflict. The backoff is 10ms, and it can't be configurable. It's just a 
default retry
 in the k8s client-go libary.

### 2024-04-23T02:23:59.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 22/Apr/24 6:23 PM

Answers from engineering team: The backup pod updated the Backup CR, but the cache in the backup pod didn't be updated in time, which caused the conflict. The backoff is 10ms, and it can't be configurable. It's just a 
default retry
 in the k8s client-go libary.
Let us know if you have further questions.

### 2024-05-07T05:17:37.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/May/24 9:17 PM

dupe issue of 
[REDACTED_SUPPORT_URL]
please close this ticket

### 2024-05-07T06:35:47.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/May/24 10:35 PM

Thanks for the update. Close as duplicate.
