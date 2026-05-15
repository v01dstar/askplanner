# GTOC-6478: Log backup checkpoint lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6478
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2023-10-24T06:43:28.000+0800
- Updated: 2024-05-20T10:11:21.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: PiTR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: change-p2

## Symptom / Description Excerpt

Hi [REDACTED_USER],

We just had a SEV0 that the log backup checkpoint_ts could not advance and we need some help on the root cause.

Timeline:

The checkpoint_ts started to lag from 10-22 18:23:00 UTC. The first related error we found was around 18:25:00 UTC:

```
[2023/10/22 18:24:59.973 +00:00] [WARN] [advancer.go:428] ["[log backup advancer] option tick failed."] [error="store 63669537: context deadline exceeded"]
```

We manually evict all leaders of that store 63669537 (pod name{{[REDACTED_RESOURCE_NAME]}}) around  19:14:00 UTC and the issue was resolved.

We looked at the log of `[REDACTED_RESOURCE_NAME]` and `[REDACTED_RESOURCE_NAME]` (task owner) and could not find any related error (other than the error above). All metrics of that TiKV node looks normal. So we would like your help to investigate on the root cause of the log backup lag.

We’ve attached metrics dashboard, logs from `[REDACTED_RESOURCE_NAME]`, `[REDACTED_RESOURCE_NAME]`, `[REDACTED_RESOURCE_NAME]` (owner) and `[REDACTED_RESOURCE_NAME]` (pd leader). Let me know if you need more information. Thanks!

Thanks,  
Sicheng

## Recent Comments Excerpt

### 2023-11-05T00:59:53.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 04/Nov/23 4:59 PM

ignore the 2nd log above

### 2023-11-05T06:22:09.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 04/Nov/23 10:22 PM

I have forwarded the info to engineering team. Will update as soon as there is any news.

### 2023-11-05T10:12:30.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 05/Nov/23 2:12 AM

The engineering team reviewed the log file and found at PDT 09:37(16:37 UTC), flush is still normal ( The flush was stuck on Oct 24 occurrence). Can you also send two more hours tikv log after 16:37 UTC (16:37 - 18:37 UTC). Thanks.

### 2023-11-07T05:45:21.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Nov/23 9:45 PM

Hi, @[REDACTED_USER] the requested tikv log still available? And do we know the cause why the pod was stuck and kubectl was not able to connect to it?

### 2024-02-23T01:06:40.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 22/Feb/24 5:06 PM

This issue seems no longer reproducing; I am resolving this ticket for now. If the same problem happens again, please try getting the logs and info requested on Oct/26 and open a new ticket. Thanks.
