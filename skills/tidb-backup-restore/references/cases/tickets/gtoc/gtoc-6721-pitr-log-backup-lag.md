# GTOC-6721: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6721
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-02-22T05:07:58.000+0800
- Updated: 2024-06-26T01:01:12.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: change-p2

## Symptom / Description Excerpt

After rolling restart all pods in a TiDB cluster, the PiTR checkpoint can not advance with “no-leader” error:

```
{
    "level": "INFO",
    "time": "2024/02/21 20:25:42.708 +00:00",
    "caller": "region_request.go:1285",
    "message": "throwing pseudo region error due to no replica available",
    "req-ts": [REDACTED_LONG_ID],
    "req-type": "Cop",
    "region": "{ region id: 160261, ver: 312, confVer: 206895 }",
    "region-is-valid": "true",
    "retry-times": 1,
    "replica-read-type": "leader",
    "replica-selector-state": "invalidStore",
    "stale-read": false,
    "replica-status": "peer: 160262, store: 188, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160263, store: 94, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160264, store: 282, isEpochStale: false, attempts: 1, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160265, store: 1, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable; peer: 160266, store: 141, isEpochStale: false, attempts: 0, replica-epoch: 0, store-epoch: 0, store-state: resolved, store-liveness-state: reachable",
    "total-backoff-ms": 0,
    "total-backoff-times": 0,
    "total-region-errors": "not_leader:1"
}
```

This is impacting our backup SLA.

## Recent Comments Excerpt

### 2024-06-18T04:00:00.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Jun/24 7:59 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-06-18T04:16:38.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Jun/24 8:16 PM

Add ‘auto-close’ label.

### 2024-06-20T01:01:47.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 19/Jun/24 5:01 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-06-23T01:00:52.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 22/Jun/24 5:00 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-06-26T01:01:12.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Jun/24 5:01 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
