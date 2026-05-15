# GTOC-7785: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7785
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-07-21T08:08:32.738+0800
- Updated: 2025-07-31T16:50:55.443+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

TiKV crashed on our Matcha cluster [REDACTED_CLUSTER] 5% error rate at second level p99 latency for one minute interval.

Here is a k8s pod describe:

```
State:          Running
      Started:      Fri, 18 Jul 2025 13:17:33 -0700
    Last State:     Terminated
      Reason:       Error
      Exit Code:    139
      Started:      Thu, 17 Jul 2025 23:48:22 -0700
      Finished:     Fri, 18 Jul 2025 13:17:32 -0700
```

Here is the last few minutes log on this storage node:

```
...
[2025/07/18 20:15:15.184 +00:00] [INFO] [scheduler.rs:776] ["get snapshot failed"] [cmd="kv::command::acquirepessimisticlock keys([(?, false)]) @ [REDACTED_LONG_ID] 20000 45950427
8613000238 Some(Millis(50000)) [REDACTED_LONG_ID] true false | region_id: 61959146 region_epoch { conf_ver: 88607 version: 854 } peer { id: 542382764 store_id: 63759370 } max_exec
ution_duration_ms: 20000 resource_group_tag: ? is_retry_request: true request_source: \"external_Select\" resource_control_context { resource_group_name: \"default\" penalty { r_r
_u: 3.[REDACTED_LONG_ID] w_r_u: 5.[REDACTED_LONG_ID] read_bytes: 1868 total_cpu_time_ms: 0.[REDACTED_LONG_ID] kv_read_rpc_count: 7 kv_write_rpc_count: 1 } override_priority: 8 } keyspace
_id: 4294967295 source_stmt { connection_id: 2196263884 } cluster_id: [REDACTED_LONG_ID] heap_size: 342"] [err="Error(Request(message: \"peer is not leader for region 61959146, l
eader may Some(id: 542240882 store_id: 198)\" not_leader { region_id: 61959146 leader { id: 542240882 store_id: 198 } }))"] [cid=2209188] [thread_id=132]
[2025/07/18 20:15:29.816 +00:00] [INFO] [scheduler.rs:776] ["get snapshot failed"] [cmd="kv::command::acquirepessimisticlock keys([(?, false)]) @ [REDACTED_LONG_ID] 20006 45950428
2440302650 Some(Millis(50000)) [REDACTED_LONG_ID] true false | region_id: 98547 region_epoch { conf_ver: 62 version: 913 } peer { id: 149370103 store_id: 63759370 } max_execution_
duration_ms: 20000 resource_group_tag: ? is_retry_request: true request_source: \"external_Update\" resource_control_context { resource_group_name: \"default\" penalty { r_r_u: 36
5.[REDACTED_LONG_ID] w_r_u: 47.[REDACTED_LONG_ID] read_bytes: 209235 write_bytes: 474 total_cpu_time_ms: 50.[REDACTED_LONG_ID] kv_read_rpc_count: 727 kv_write_rpc_count: 9 } override_priority

## Recent Comments Excerpt

### 2025-07-21T08:09:40.601+0800 [REDACTED_USER]

We can request token to have 24 hours metrics access if needed. I am also checking with customer [REDACTED_CUSTOMER]there is any call stack. Let us know if you need anything else.

### 2025-07-21T11:00:16.573+0800 [REDACTED_USER]

@[REDACTED_USER]
 Did we enable coredump? We need it to get more context.

### 2025-07-22T19:30:29.731+0800 [REDACTED_USER]

We sent the SOP 
https://pingcap.feishu.cn/wiki/B6Diw1tNriT0cQkXGBTc43O6nGg
 to the customer [REDACTED_CUSTOMER]ons: 
1 <related to SOP itself, answered already> 
2. I don’t think this will work well in our environment. We have 100s of TiKV nodes in our cluster and rotate EC2 instances. It will take some time to figure our what is the good way to setup it it in k8s to work transparently. Any help hear would be highly appreciated. I can also ask for the help our compute team once get a required commands in the question 1 above.


3. While we don’t have

### 2025-07-22T20:09:26.704+0800 [REDACTED_USER]

@[REDACTED_USER]
 
For how to enable coredump on this environment, I think the K8S team know better than me.
No. 
SIGSEGV
 is handled by the OS, TiKV does not handle it. 
In theory, TiKV can do handle 
SIGSEGV

### 2025-07-25T09:15:22.917+0800 [REDACTED_USER]

From customer: [REDACTED_CUSTOMER]ctly the same. I believe it will be a blocker for Match launch.


Regarding the core dump (
abort-on-panic
=true) vs backtracing in the code:
