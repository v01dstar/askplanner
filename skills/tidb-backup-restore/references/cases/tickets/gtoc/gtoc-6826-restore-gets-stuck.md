# GTOC-6826: Restore gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6826
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-04-08T09:18:15.000+0800
- Updated: 2025-03-06T18:14:53.095+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: PD
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We run periodic restores, to test BR. And sometimes, we see restores are stuck 

`waiting for all PD members are ready in tidbcluster [REDACTED_CLUSTER]/rp-[REDACTED_ENV_NAME], requeuing`

`pd_member_manager.go:379] PD member: [[REDACTED_LONG_ID] doesn't have a name, and can't get it from clientUrls: [[]], memberHealth Info: [{ [REDACTED_LONG_ID] [] false}] in [[REDACTED_ENV_NAME]/rp-[REDACTED_ENV_NAME]I0404 21:27:30.528701       1 t`

And this doesn’t really recover.

## Recent Comments Excerpt

### 2024-04-27T04:56:04.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 8:55 PM

I posted a detailed analysis, and root cause and proposed solution in 
[REDACTED_SUPPORT_URL]
 . We need to add retries even in the operator code, which triggers the error “{{waiting for all PD members are ready in tidbcluster}}"

### 2024-04-27T04:56:28.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 8:56 PM

So please reopen the ticket, to align on the analysis, and fix.

### 2024-04-27T04:58:18.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 8:58 PM

Sorry. Rethinking about this. The symptom here is slightly different ie pds are stuck in crash loop. So they (pd) are genuinely are not available in the cluster.

### 2024-04-27T04:59:08.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 8:59 PM

Infact operator here does keep retrying.

### 2024-04-27T05:01:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 9:01 PM

Hi @[REDACTED_USER], this issue might be different. It could be related with configuration issue in TC_PD_spec.txt, as it only specify 2 PDs instead of 3. Can we close this ticket while keep 
https://pingcap-ticket.atlassian.net/browse/[REDACTED_TICKET_ID]
 open for further investigation?
