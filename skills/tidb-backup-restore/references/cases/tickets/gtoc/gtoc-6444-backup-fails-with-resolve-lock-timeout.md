# GTOC-6444: Backup fails with resolve lock timeout

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6444
- Status: Canceled
- Resolution: Cancel
- Priority: P2
- Issue type: Incident
- Created: 2023-09-20T12:16:37.000+0800
- Updated: 2024-05-20T13:30:47.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Error: resolve lock timeout. CR attached. Please let me know if you want anything else.

## Recent Comments Excerpt

### 2023-09-20T12:16:39.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 14/Sep/23 4:41 PM

Talked to Brian Zhang.
escalate this one to L3

### 2023-09-26T02:20:41.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Sep/23 6:20 PM

Any update of this ticket?

### 2023-10-05T10:59:13.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 05/Oct/23 2:58 AM

Hey @[REDACTED_USER] , there are multiple possibilities regarding this, such as network jitter, unable to fetch region info from PD etc, Can you collect following information? Thanks
full BR log
the tikv log for store 1942129 from 
2023/09/11 00:00:00.209 +00:00 to 2023/09/11 00:16:00.209 +00:00
PD log
the clinic

### 2023-11-08T04:27:29.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 07/Nov/23 8:27 PM

Hey @[REDACTED_USER], checking in to see if you are able to collect the information that Hua requested earlier.
Can you update us?
Thank you,
Feran

### 2023-11-09T05:07:17.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Nov/23 9:07 PM

We are switching to using EBS BR. If we need logical snapshot Backup again, we’ll reopen the ticket. We can close this for now.
