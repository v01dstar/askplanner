# GTOC-7915: PITR fails with slice bounds out of range

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7915
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-09-20T00:58:25.577+0800
- Updated: 2025-09-26T11:27:03.320+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Around `2025-09-18T22:14:34+00:00` UTC we have created a 1G DB called `pitr_1gb` using the attached `sysbench_pitr_1gb.yaml`

Then we have added few more records and run the attached `restore_pitr_1gb.yaml` to restore the DB to the original state.

However the restore job `kubectl get job/restore-pitr-job-restore -n [REDACTED_ENV_NAME]` ended up with error. Attached is the complete log for the restore job.

## Recent Comments Excerpt

### 2025-09-20T00:58:38.306+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100b43ecf516ac8c0ec81f6bb8f49f7) by lark

### 2025-09-20T00:59:39.547+0800 [REDACTED_USER]

[REDACTED_MEDIA]
[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2025-09-22T17:15:01.494+0800 [REDACTED_USER]

I’ve created a new pr to fix it: 
https://github.com/pingcap/tidb/pull/63662
