# GTOC-6984: Backup fails with index out of range [0] with length 0

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6984
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-06-24T09:55:29.000+0800
- Updated: 2025-03-06T18:09:42.299+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, storage-credential, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello, we saw a ebs volumebackup failure due to one backup member failed due to 

```
panic: runtime error: index out of range [0] with length 0
```

This failed backup member got auto deleted after retention period but left some snapshots leaking. <custom data-type="smartlink" data-id="id-0">https://gist.github.com/olivia-chen-github/e10465f987bca8d074b41e8f4057a570</custom> 

Seems the backup created some snapshots, but didn’t create the `backupmeta`

failed backup log: <custom data-type="smartlink" data-id="id-1">https://gist.github.com/olivia-chen-github/0c93c5d4aaee6bf1b54df2255d5caf00</custom> 

Can you pls help understand the failure? thanks

## Recent Comments Excerpt

### 2024-07-09T03:56:40.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Jul/24 7:56 PM

The status for this ticket was "Escalate to L3" with no update for 7 days, please take a look.

### 2024-08-01T09:40:15.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/Aug/24 1:40 AM

Is this still happening?  Please send us the failed EBS volume backup CR as in previous update if this is recurring and we need to investigate it further.

### 2024-08-08T03:56:51.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 07/Aug/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-08-08T21:01:58.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Aug/24 1:01 PM

No response. Add auto-close.

### 2024-08-10T01:01:08.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/Aug/24 5:01 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.
