# GTOC-7418: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7418
- Status: Canceled
- Resolution: Cancel
- Priority: P2
- Issue type: Incident
- Created: 2025-02-24T13:29:31.603+0800
- Updated: 2025-05-28T17:35:51.696+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV, TiKV BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

**– From Customer**

we were paged by the `TiDB_TiDB_log_backup_rpo_lag` alert recently. I noticed that the "Max Leader Resolved TS gap" graph showed a large gap in `resolved_ts` in the tikv node `[REDACTED_RESOURCE_NAME]`, which matched the "Abnormal Checkpoint TS Lag" graph.

We found these log messages when searching for "the max gap of leader resolved-ts is large",

```
we were paged by the TiDB_TiDB_log_backup_rpo_lag alert recently. I noticed that the "Max Leader Resolved TS gap" graph showed a large gap in resolved_ts in the tikv node [REDACTED_RESOURCE_NAME], which matched the "Abnormal Checkpoint TS Lag" graph.

We found these log messages when searching for "the max gap of leader resolved-ts is large",
```

The `gap` in the log messages were large, which confirmed the `resolved_ts` gap. The `key` was the same in these two log [messages. ](http://messages.my/)The slowest commit was about 1min around that time. [My](http://messages.my/) questions are:

1. Was the key locked because of pessimistic locking or something else?
2. If I begins a pessimistic transaction with select-for-update, and the transaction is a long running one, would the transaction hold the `resolved_ts` of the region?
3. What's the recommendation to mitigate this kind of rpo lag?

‌

I couldn’t reproduce the resolved_ts lag with either select-for-update or a long open transaction. For example, I began a transaction, insert 1 row, but left it open. The `resolved_ts` advanced to now.

```
$ curl http://[REDACTED_IP]:10080/mvcc/key/test/tt/5
{
 "key": "7480000000000000535F728000000000000005",
 "region_id": 10,
 "value": {

## Recent Comments Excerpt

### 2025-02-24T13:29:46.294+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), ) by lark

### 2025-02-24T17:55:02.707+0800 [REDACTED_USER]

for now we’ll track in 
https://pingcap-ticket.atlassian.net/browse/[REDACTED_TICKET_ID]
.
