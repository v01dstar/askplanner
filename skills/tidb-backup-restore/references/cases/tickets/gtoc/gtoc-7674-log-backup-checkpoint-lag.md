# GTOC-7674: Log backup checkpoint lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7674
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-06-13T07:26:50.551+0800
- Updated: 2025-09-11T08:02:52.112+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We're observing a significant `resolved-ts` gap on a subset of TiKV nodes in our **prod green cluster** (`[REDACTED_ENV_NAME]`). This cluster is currently serving production traffic in shadow mode. The `resolved-ts` lag is leading to **backup job failures**.

We’ve checked for long-running transactions and long-held locks via `information_schema`, but found no evidence of either. Notably, the lagging TiKV nodes, especially `tikv-17-1e`, are reporting a high rate of `raftstore` errors, primarily of the `err_other` type. I couldn’t find clear clue about the error from the TiKV log though.

Yesterday, we attempted to mitigate the issue by restarting the affected TiKV pods. While this resolved the issue for a few nodes, **five nodes still show a continuously growing** `resolved-ts` **gap**.

Could you please help investigate this issue? Thank you!

## Recent Comments Excerpt

### 2025-06-18T05:31:33.657+0800 [REDACTED_USER]

^ log files for two other replicas of Region 
259482382
The host of three replicas:
1e [REDACTED_ENV_NAME]
1b [REDACTED_ENV_NAME]
1a [REDACTED_ENV_NAME]
[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2025-06-19T09:49:15.145+0800 [REDACTED_USER]

notified (徐锐([REDACTED_EMAIL]), om_x100b4a028768f4ac0ec2832241f6dd1) by lark

### 2025-06-19T10:01:25.154+0800 [REDACTED_USER]

No useful information found for Region 
259482382
 in the logs for the lag from 06-04 to 06-06

Similar phenomenon is reproduced in the test environment, investigating adding more logs.

### 2025-06-20T09:24:48.993+0800 [REDACTED_USER]

From the internal reproduction, 
https://pingcap.feishu.cn/docx/CwGIdXx1xon3RBxnv4KcaOP4nW3?from=auth_notice&hash=9a8b9c0ea8eacf8f436bd72bc29206a6
 the 06-04 ~ 06-06 lag is expected because of the network partition or delay bettween the related tikv-server nodes.

### 2025-06-27T05:36:26.558+0800 [REDACTED_USER]

I checked the logs and did notice some network issues at the very beginning of the cluster [REDACTED_CLUSTER] However, this still doesn’t seem to fully explain the issue our cluster [REDACTED_CLUSTER]

The large 
safe-ts
 gap persisted in our cluster. As you mentioned, this kind of issue should typically resolve itself once the network recovers. But in our case, the lag continued for nearly a week even after the network had stabilized.
Moreover, the affected TiKV nodes were still able to serve most traffic successfully. Only a small subset of regions on those nodes were impacted, which suggests that a general network issue is unlikely to be the root cause.
This also doesn’t explain why it’s always the ML cluster [REDACTED_CLUSTER] this issue, while other production clusters are unaffected.
If the current logs and metrics aren’t giving us enough insight, one thing we could try is leveraging a patched version of TiKV. The PingCAP TiKV team can prepare a release-6.5 patch with enhanced diagnostic messages and logging. We could cherry-pick this patch, build our own images, and attempt another cluster [REDACTED_CLUSTER] to try and reproduce the issue and gather more detailed debugging information.
