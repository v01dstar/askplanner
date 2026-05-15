# GTOC-8392: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8392
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2026-04-21T04:47:33.499+0800
- Updated: 2026-04-21T05:12:12.603+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We’ve been having issues with the log backup lockfile for awhile. We know how to remedy those issues, but today I’ve encountered something slightly different and want to double check before proceeding.

---

Instead of the normal `LOCK.WRIT` file that normally gets stuck and we have to manually remove, today I see:

```
bash-4.2# aws s3 ls s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] | grep LOCK.WRIT
2026-04-15 00:13:43        212 APPEND_LOCK.WRIT
```

is this file also fine for me to manually remove to fix this issue? I will update our runbook if so.

## Recent Comments Excerpt

### 2026-04-21T04:47:38.271+0800 [REDACTED_USER]

fail to find L2 assignee, retry of choosing L2 assignee will be triggered 2 hours later.

if the issue is urgent, please escalate to L3 directly

### 2026-04-21T04:48:24.375+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), om_x100b515d5fb9b8a4c2c0b0e57151e62) by lark

### 2026-04-21T04:59:21.267+0800 [REDACTED_USER]

if there is 
no
 
previous PiTR running task
. this lock file can be deleted. 

And It’s better to know why the lock file not removed automatically, Does previous pitr failed? or previous log have such (
you may need to manually delete it
