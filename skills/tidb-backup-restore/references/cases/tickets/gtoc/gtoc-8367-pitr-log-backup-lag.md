# GTOC-8367: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8367
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2026-04-14T08:58:11.997+0800
- Updated: 2026-04-24T07:41:04.331+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Customer [REDACTED_CUSTOMER]**log backup RPO continuously increases (up to hours or even >1 day)**.  
Previously, incidents were mitigated via workarounds due to urgency, but no root cause analysis was completed.

In this case, we have collected **complete clinic + PD/TiKV/TiDB logs covering before, during, and after the issue window**.

## Recent Comments Excerpt

### 2026-04-14T09:05:25.202+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b52ed638bfcb4c1093f19ede4b9e) by lark

### 2026-04-14T11:34:11.040+0800 [REDACTED_USER]

From tidb log, here are many logs show that the region (id=1008) has no leader.
[2026/04/12 21:58:57.656 +00:00] [INFO] [advancer.go:313] [\"current last region\"] [category=\"log backup advancer hint\"] [min=\"([?, ?), 0)\"] [for-polling=1] [min-ts=1970-01-01T00:00:00Z] [region-hint=\"ID=1008,Leader=0,ConfVer=5,Version=7,Peers=[1001 1012 1030],RealRange=[?, ?)\"]
From tikv-1 log, here are many logs show that the region (id=1008) has tombstone peer.
[2026/04/12 23:14:45_793 +00:00] [INFO] [store_rs:2229] [\\\"tombstone peer receives a stale message, local_peer_id >\":\"to_peer_id\",\"[local_peer_id\":\"1014]\",\"[region_id\":\"1008]\",\"[thread_id\":\"148]\",\"[to_peer_id\":\"1014]\",\"_noise\":false,\"az\":\"ap-southeast-2b\",\"cluster_uid\":\"whqs\",\"csp\":\"aws\",\"customer\":\"sql-platform\",\"ec2_instance_id\":\"i-0f11f86f5971247bb\",\"ec2_instance_type\":\"m7g.4xlarge\",\"env\":\"prod\",\"host_type\":\"k8s\",\"hostname\":\"ip-10-21-172-208.ap-southeast-2.compute.internal\",\"in msg\\\"] [msg_type\":\"MsgRequestPreVote]\"

### 2026-04-22T03:40:41.429+0800 [REDACTED_USER]

Root Cause Analysis: Why Regions 1002, 1006, 1008 Cannot Elect a Leader
Based on TiKV logs (2026-04-12 20:15–23:14 UTC) and pd-ctl output (2026-04-22).

Peer Distribution and Current State
Region
Store 1001 (missing)
Store 1012 / tikv-1
Store 1030 / tikv-0

### 2026-04-23T08:02:27.927+0800 [REDACTED_USER]

The linked ticket has been resolved.

### 2026-04-24T07:29:33.155+0800 [REDACTED_USER]

The issue has been resolved.
Root cause: Three system-metadata regions (1002, 1006, 1008) were permanently leaderless due to a broken Raft group — store 1001 no longer exists, and store 1012's peers for these regions were already tombstone. This left tikv-0 (store 1030) as the only candidate, with only 1/3 votes — below the 2/3 quorum needed for leader election. As a result, log backup checkpoint advancement was permanently blocked by these regions, causing RPO to grow continuously.
Resolution (2026-04-22): Stopped tikv-0 pod, ran the following on its data directory:
tikv-ctl --data-dir /var/lib/tikv unsafe-recover remove-fail-stores -s 1001 -r 1002,1006,1008
tikv-ctl --data-dir /var/lib/tikv unsafe-recover remove-fail-stores -s 1012 -r 1002,1006,1008
All three regions elected a leader on store 1030. Log backup was restarted and checkpoint lag returned to ~2.5 minutes, consistent with other healthy clusters.
This is not a product bug. The root cause was an improper TiKV lifecycle operation that left the cluster in a partially inconsistent state. Customer [REDACTED_CUSTOMER]d procedures for future TiKV scale-in/out/replacement operations, and an RPO alert is now in place for early detection.
Linked ticket [REDACTED_TICKET_ID] has been confirmed resolved by the customer.
