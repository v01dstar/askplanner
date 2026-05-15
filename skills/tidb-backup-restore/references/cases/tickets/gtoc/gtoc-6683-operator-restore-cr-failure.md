# GTOC-6683: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6683
- Status: Canceled
- Resolution: Cancel
- Priority: P1
- Issue type: Incident
- Created: 2024-02-08T06:22:27.000+0800
- Updated: 2024-07-02T11:59:03.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Another result from our restore testing. We saw a restore fail after \~12hrs from a successful backup on [REDACTED_ENV_NAME]. I’ve attached CRs for the vbk, bks, vrt, and rts.

will upload metrics for backup and restore to clinic once available. lmk if any logs would be useful as well

## Recent Comments Excerpt

### 2024-02-09T01:54:17.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Feb/24 5:54 PM

I’ve confirmed that the restore and tikv logs are correct. However we believe an infra-based disruption may have caused the pod to terminate unexpectedly, we are investigating and will update with more details

### 2024-02-09T02:56:57.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Feb/24 6:56 PM

Hi, Michael:
Ok, got it~ Waiting for you to update more details, and I will do further investigation.

### 2024-02-09T03:26:57.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Feb/24 7:26 PM

We’ve confirmed that the restore-data-fed job in zone c was killed due to infra-based pod eviction. To resolve this we plan to protect these restore pods with a pdb.
However, this restore had been running for ~5hrs when killed, so this appears to another slow restore related to: 
[REDACTED_SUPPORT_URL]
 
happy to merge it with the existing ticket or to continue debugging here if there’s any helpful info even in the incomplete logs/metrics

### 2024-02-09T04:54:27.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Feb/24 8:54 PM

OK, we can conduct further investigation in 
https://pingcap-ticket.atlassian.net/browse/[REDACTED_TICKET_ID]
Thx~

### 2024-02-15T00:21:54.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 14/Feb/24 4:21 PM

@[REDACTED_USER] as discussed, we will merge the conversation in another ticket to prevent context missing in multiple threads, will close this one.
