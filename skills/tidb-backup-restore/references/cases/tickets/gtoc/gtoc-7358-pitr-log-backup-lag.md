# GTOC-7358: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7358
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-01-20T10:36:23.420+0800
- Updated: 2025-03-06T17:38:46.955+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We saw another instance of the log backup on the full-shadow cluster [REDACTED_CLUSTER] due to tidb rolling restart and specifically advancer restart.

Metrics indicate the initial advancer was tidb-9-1a, which restarted at \~06:22Z, transitioning to the new advancer tidb-11-1e. The last log checkpoint from the log backup status status is 2025-01-17 06:16:40Z.

This behavior is unexpected given that we have cherry-picked [pingcap/tidb#58135](https://github.com/pingcap/tidb/issues/58135) to our 8.1.1 release. Is there another possible issue causing log backup pause during tidb advancer restart?

Once again, we see that the log backup CR status shows running as well, even though the actual log backup is paused. Is there a tidb-operator fix we should look to cherry-pick as well?

Given that we were able to detect this issue \~12hrs later, we were able to resume the log backup and it took \~30min to catch up the 12hrs of logs.

I’ve included BR logs of the status and resume commands as well as logs from the tidb pods during the restart period.

## Recent Comments Excerpt

### 2025-01-20T10:42:11.023+0800 [REDACTED_USER]

We didn’t perform any manual operations to pause the log, and only saw it paused after the advancer restart. only when we noticed it was paused did we take manual action to resume
here are the clinic metrics from that time frame: 
[REDACTED_CLINIC_URL]
https://jira.tidbcloud.com/browse/GTOC-7310
 is similar where PiTR paused during TiKV restart.

### 2025-01-20T12:03:23.264+0800 [REDACTED_USER]

We find these logs in tidb-11-1e:
The log shows that the global checkpoint ts was 
2025-01-17 06:16:40.756 +0000
 while the TiDB advancer recorded checkpoint ts was 
2025-01-14 21:34:43.579 +0000
. However, it still used the TiDB advancer recorded checkpoint ts to calculate the checkpoint lag. Therefore, we guess this commit is not cherry-picked back to TiDB (Notice that 
NOT
 BR).

### 2025-01-22T02:25:45.543+0800 [REDACTED_USER]

From Airbnb: Thanks for the analysis. We investigated on our side and can also confirm that tikv-11-1e doesn’t have the cherry-pick at this time. In this case, the tidb restart is triggered by a rolling restart that deploys the fix. The rolling restart proceeds by AZ (1a, 1b, then 1e), so when 1a restarts and triggers advancer switch to 1e, the tidbs in 1e haven’t yet restarted w/ update code/fix.
To confirm, will this global checkpoint lag check/comparison first occur during advancer startup? or does it occur during the tidb startup phase?

### 2025-01-22T10:30:48.944+0800 [REDACTED_USER]

The global checkpoint lag check/comparison first occur during advancer 
owner-tick
. There is only one advancer owner in TiDB nodes, so the TiDB-1e became new advancer owner after the TiDB-1a (old advancer owner) was down. Then, the new advancer owner in TiDB-1e triggered 
owner-tick 
to collect region-level checkpoint ts from TiKV nodes and finally try to summary and calculate new global checkpoint ts. However, it failed and couldn’t get the newest global checkpoint ts. Therefore, it should get the global checkpoint ts from PD and do global checkpoint lag check/comparison.
