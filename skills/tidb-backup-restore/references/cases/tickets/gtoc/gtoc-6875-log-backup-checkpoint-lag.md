# GTOC-6875: Log backup checkpoint lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6875
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-04-25T06:11:58.000+0800
- Updated: 2025-03-06T18:13:27.451+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

While restoring the database on v7.5, it needs the target database empty. The restore fails with the following error messages:

```
the target cluster is not fresh, cannot restore. # you can drop existing databases and tables and start restore again #######################################################################
```

Can this be avoided, as sometimes the customer [REDACTED_CUSTOMER]itional tables for testing purposes?

## Recent Comments Excerpt

### 2024-04-27T03:11:33.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 7:11 PM

okay - Thanks Cheng!

### 2024-04-27T03:14:13.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 7:14 PM

The check will skip if user specify the filter parameter. 
https://github.com/pingcap/tidb/pull/51041
 

This PR is already merged into br v7.5.1. you can try this version of BR.

### 2024-05-21T01:02:45.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 20/May/24 5:02 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-05-24T01:07:56.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 23/May/24 5:07 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-05-27T01:01:43.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/May/24 5:01 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
