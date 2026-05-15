# GTOC-7544: Operator PITR CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7544
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-04-23T06:18:03.855+0800
- Updated: 2025-05-12T18:51:23.914+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], restore-failure, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello,

PingCAP documentation explains ([link](https://docs.pingcap.com/tidb/stable/br-checkpoint-restore/)) that TiDB logical restore process is able to handle failures (would recover starting from a restore checkpoint). However, we observe this is not happening: in the case of restore job pod preemption (e.g. due to k8s scaler), job is marked as failed and never retried.

Looking at the restore object spec, we see that restore is failing with following status:

```
"apiVersion": "pingcap.com/v1alpha1",
  "status": {
    "progresses": [
      {
        "lastTransitionTime": "2025-04-16T20:46:30Z",
        "progress": 100,
        "step": "Full Restore"
      }
    ],
    "conditions": [
      {
        "type": "Scheduled",
        "lastTransitionTime": "2025-04-16T19:20:54Z",
        "status": "True"
      },
      {
        "type": "Running",
        "lastTransitionTime": "2025-04-16T19:23:11Z",
        "status": "True"
      },
      {

## Recent Comments Excerpt

### 2025-04-23T06:18:18.301+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b4fb5145470b00ece2b0f76f9f44) by lark

### 2025-04-30T04:49:48.970+0800 [REDACTED_USER]

Customer [REDACTED_CUSTOMER]
https://github.com/pingcap/tidb-operator/pull/6092
 
Follow up question:  what is the expected for retries if PITR restore failed? Would it restart from the beginning?
My concern is the disk space exhaustion if restore job tries to re-apply the snapshot.

### 2025-05-07T19:56:24.776+0800 [REDACTED_USER]

what is the expected for retries if PITR restore failed? Would it restart from the beginning?
When a PiTR fails, restarting it with the same configuration starts from the last checkpoint unless 
--enable-checkpoint
 was set to 
false
.  It will restart from a near position to its failure.

### 2025-05-12T18:51:23.751+0800 [REDACTED_USER]

it’s a q&a ticket and is to be closed soon.
