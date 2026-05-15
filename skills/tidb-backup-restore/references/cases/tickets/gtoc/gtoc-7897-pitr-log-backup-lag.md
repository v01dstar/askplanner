# GTOC-7897: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7897
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-09-11T06:16:28.395+0800
- Updated: 2025-09-29T17:02:16.747+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PD
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

PD tso spike while customer [REDACTED_CUSTOMER]

It not expect to impact query while delete PD follower.

 

From log below, it shows PD leader failed first, and follower delete happen 5mins after that. The tso slow also in this time. From the two information, it point the issue to check why etcd is failed.

```
{"level":"ERROR","time":"2025/09/10 21:12:08.804 +00:00","caller":"etcd_kv.go:111","message":"save to etcd meet error","key":"/pd/[REDACTED_LONG_ID]/gc/safe_point/service/backup-stream-pitr-106911","value":"{\"service_id\":\"backup-stream-pitr-106911\",\"expired_at\":1757545928,\"safe_point\":[REDACTED_LONG_ID]}","error":"[PD:etcd:ErrEtcdKVPut]rpc error: code = Unknown desc = raft: stopped: rpc error: code = Unknown desc = raft: stopped","errorVerbose":"[PD:etcd:ErrEtcdKVPut]rpc error: code = Unknown desc = raft: stopped: rpc error: code = Unknown desc = raft: stopped

{"level":"INFO","time":"2025/09/10 21:12:08.884 +00:00","caller":"server.go:1815","message":"no longer a leader because lease has expired, pd leader will step down"}

{"level":"ERROR","time":"2025/09/10 21:12:09.029 +00:00","caller":"server.go:1712","message":"campaign PD leader meets error due to etcd error","campaign-leader-name":"pd-[REDACTED_ENV_NAME]","error":"[PD:etcd:ErrEtcdTxnInternal]rpc error: code = Unknown desc = raft: stopped: rpc error: code = Unknown desc = raft: stopped","errorVerbose":"[PD:etcd:ErrEtcdTxnInternal]rpc error: code = Unknown desc = raft: stopped: rpc error: code = Unknown desc = raft: stopped

{"level":"INFO","time":"2025/09/10 21:12:09.058 +00:00","caller":"member.go:356","message":"try to resign etcd leader to next pd-server","from":"pd-[REDACTED_ENV_NAME]","to":""}
{"level":"INFO","time":"2025/09/10 21:12:09.064 +00:00","caller":"server.go:1519","message":"leadership transfer starting","local-member-id":"cc33ef0f9744a578","current-leader-member-id":"cc33ef0f9744a578","transferee-member-id":"7da6ad8f93d201e3"}
{"level":"INFO","time":"2025/09/10 21:12:10.522 +00:00","caller":"server.go:1540","message":"leadership transfer finished","local-member-id":"cc33ef0f9744a578","old-leader-member-id":"cc33ef0f9744a578","new-leader-member-id":"7da6ad8f93d201e3","took":"500.201515ms"}


{"level":"ERROR","time":"2025/09/10 21:12:10.522 +00:00","caller":"server.go:1712","message":"campaign PD leader meets error due to etcd error","campaign-leader-name":"pd-[REDACTED_ENV_NAME]","error":"[PD:server:ErrLeaderFrequentlyChange]leader pd-[REDACTED_ENV_NAME] frequently changed, leader-key is [/pd/[REDACTED_LONG_ID]/leader]"}

{"level":"INFO","time":"2025/09/10 21:12:15.014 +00:00","caller":"leadership.go:191","message":"write leaderData to leaderPath ok","leader-key":"/pd/[REDACTED_LONG_ID]/leader","purpose":"leader election"}
{"level":"INFO","time":"2025/09/10 21:12:15.014 +00:00","caller":"server.go:1732","message":"campaign PD leader ok","campaign-leader-name":"pd-[REDACTED_ENV_NAME]"}
{"level":"INFO","time":"2025/09/10 21:12:15.917 +00:00","caller":"server.go:1806","message":"PD leader is ready to serve","leader-name":"pd-[REDACTED_ENV_NAME]"}


{"level":"INFO","time":"2025/09/10 21:17:26.570 +00:00","caller":"audit.go:126","message":"audit log","service-info":"{ServiceLabel:DeleteMemberByName, Method:HTTP/2.0/DELETE:/pd/api/v1/members/name/[REDACTED_RESOURCE_NAME], CallerID:pd-ctl, IP:[REDACTED_IP], Port:58776, StartTime:2025-09-10 21:17:26 +0000 UTC, URLParam:{}, BodyParam:}"}

## Recent Comments Excerpt

### 2025-09-11T06:16:41.051+0800 [REDACTED_USER]

notified (蒋先杰([REDACTED_EMAIL]), om_x100b432bc24a20900f217dec0d8e8fc) by lark

### 2025-09-11T11:21:19.221+0800 [REDACTED_USER]

https://tidb.atlassian.net/browse/GTOC-7689
 
This issue was also encountered in another oncall. We filed an 
issue
 with etcd, but it was rejected by etcd team due to the outdated version. Let me briefly describe the situation in previous oncall:
A user was performing Kubernetes node maintenance and performed some operations on the PD cluster: [REDACTED_CLUSTER] out 3 -> 5, deleting a non-leader PD pod, and scaling in 5 -> 3.
When deleting a PD follower, the same error message occurred, and a leader election occurred.
We suspect frequent changes to etcd members caused this issue, but we haven't yet identified the root cause.

### 2025-09-11T14:56:41.621+0800 [REDACTED_USER]

I also noticed that before the second leader election at 21:12, there was actually a member delete, which means that two deletes were initiated. 
So the key issue is also that deleting the follower caused the 
raft: stopped
 error in etcd.

{"level":"INFO","time":"2025/09/10 21:12:07.482 +00:00","caller":"audit.go:126","message":"audit log","service-info":"{ServiceLabel:DeleteMemberByName, Method:HTTP/1.1/DELETE:/pd/api/v1/members/name/[REDACTED_RESOURCE_NAME], CallerID:pd-ctl, IP:[REDACTED_IP], Port:55508, StartTime:2025-09-10 21:12:07 +0000 UTC, URLParam:{}, BodyParam:}"}

### 2025-09-12T04:47:40.967+0800 [REDACTED_USER]

What was the user's purpose for deleting the member?
Did the user scale the PD cluster in/out before deleting the member? (Is there any similarity with the previous ticket?)

Customer [REDACTED_CUSTOMER]ce type so he delete one and add a new one, so this is similar with node maintenance action as  you mention.

### 2025-09-15T11:36:39.390+0800 [REDACTED_USER]

@[REDACTED_USER]
 The etcd team's advice to us is to upgrade to the new version. I think we can also recommend users to upgrade to v8.5? Because etcd in v8.5 is v3.5. ref 
https://github.com/etcd-io/etcd/discussions/20337#discussioncomment-13762201
