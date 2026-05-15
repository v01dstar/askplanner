# GTOC-6919: Restore gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6919
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-05-14T11:24:59.000+0800
- Updated: 2025-03-07T10:55:33.936+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello,

We have a volumerstore completed ebs volume restore and warmup phase, it stuck in data restore for over 2d. We didn’t see any error reported in the data restore log and the data restore is still running

data restore log: <custom data-type="smartlink" data-id="id-0">https://gist.github.com/olivia-chen-github/0835bb0a04422631277e5bda681dc173</custom> 

volumerestore cr: <custom data-type="smartlink" data-id="id-1">https://gist.github.com/olivia-chen-github/7b84c9cba5e736429f54f4d9f51ebf36</custom> 

restore cr: <custom data-type="smartlink" data-id="id-2">https://gist.github.com/olivia-chen-github/99cb3b9b55af82a9918aab6d346cb6c5</custom> 

restore cr for the data restore data plane: <custom data-type="smartlink" data-id="id-3">https://gist.github.com/olivia-chen-github/03991de04a6a89b0c5a8823d3b8c768c</custom>  the backupmeta not found error is due to the backup is recycled with 1d maxreservetime

Could you help us understand what’s the problem? thx

## Recent Comments Excerpt

### 2024-05-15T06:16:46.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 14/May/24 10:16 PM

@[REDACTED_USER] can you also check troubleshooting #2 and upload the output? Thanks

### 2024-05-15T12:17:23.000+0800 [REDACTED_USER]

We have noticed that there are some errors happen during TLS handshaking:
[2024/05/10 19:33:44.649 +00:00] [ERROR] [<unknown>] [\"Handshake failed with fatal error SSL_ERROR_WANT_WRITE: error:00000000:lib(0):func(0):reason(0).\"]"
[2024/05/10 19:33:46.422 +00:00] [ERROR] [raft_client.rs:847] [\"wait connect timeout\"] [addr=[REDACTED_ENV_NAME].[REDACTED_ENV_NAME].[REDACTED_ENV_NAME].svc.us-east-1b.[REDACTED_ENV_NAME].tidb.musta.ch:20160] [store_id=198]"
Consequently, the raft connection between peers cannot be established. Hence we cannot elect any leader, the restore data step cannot be finished.
For troubleshooting the TLS problem, you may:
0. Check the network infrastructure. (Are all TiKVs are connected, can they ping each other?)

1. Check the openssl version that TiKV uses. (It depends on how you build it, in a default build, it should be a statically linked one, and when FIPS support enabled, it will be dynamically linked.)

### 2024-05-16T04:17:20.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 15/May/24 8:17 PM

Some more update: We have noticed that there are some errors happen during TLS handshaking:
[2024/05/10 19:33:44.649 +00:00] [ERROR] [<unknown>] [\"Handshake failed with fatal error SSL_ERROR_WANT_WRITE: error:00000000:lib(0):func(0):reason(0).\"]"
[2024/05/10 19:33:46.422 +00:00] [ERROR] [raft_client.rs:847] [\"wait connect timeout\"] [addr=[REDACTED_ENV_NAME].[REDACTED_ENV_NAME].[REDACTED_ENV_NAME].svc.us-east-1b.[REDACTED_ENV_NAME].tidb.musta.ch:20160] [store_id=198]"
Consequently, the raft connection between peers cannot be established. Hence we cannot elect any leader, the restore data step cannot be finished.
For troubleshooting the TLS problem, you may:
Check the network infrastructure. (Are all TiKVs are connected, can they ping each other?)

### 2024-05-18T06:12:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/May/24 10:12 PM

We root cause the issue to a large certificate, which breaks TLS. We just recreated the cluster with smaller certs (via smaller cluster name), and that restore worked fine. Thanks for sharing the log with the TLS error, that was very helpful. Feel free to close the ticket.

### 2024-05-18T08:07:39.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 18/May/24 12:07 AM

Thanks for letting us know. Close the ticket.
