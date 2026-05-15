# GTOC-6458: BR panic during restore

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6458
- Status: Canceled
- Resolution: Cancel
- Priority: P1
- Issue type: Incident
- Created: 2023-10-09T17:03:11.000+0800
- Updated: 2026-05-09T12:15:06.410+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: restore-failure, tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello,

We are doing ebs restore on a 70TB cluster. During restore process, the volume restore, warmup and tikv start phase completed. But we got one tikv replica crashed during data restore phase due to 

```
[FATAL] [lib.rs:509] ["unstable.slice[28051, 28055] out of bound[28051, 28051], raft_id: 2010234007, region_id: 2010234004"]
```

in this test we have 45 tikv replicas spread evenly across 3 azs. We believe this is not a transient error cause we saw same error multiple times. wondering do you have any insights why did this tikv crash? thx.  
restore full log:<custom data-type="smartlink" data-id="id-0">https://gist.github.com/oliviachenairbnb/2224240147b0c4f1f500f4a7b79cae7d</custom> 

tikv full log: [https://gist.githubusercontent.com/oliviachenairbnb/699a6ba18b0c8ea62a6577766afb85b7/raw/5c86867be3fa198688237716b47bc23b7ad35f29/tikv%2520crash](https://gist.githubusercontent.com/oliviachenairbnb/699a6ba18b0c8ea62a6577766afb85b7/raw/5c86867be3fa198688237716b47bc23b7ad35f29/tikv%2520crash)

tikv version: 6.5.4

## Recent Comments Excerpt

### 2023-10-10T10:22:03.000+0800 [REDACTED_USER]

The panic is caused by ebs backup break region merge assumption: when proposing commit merge, all source peers must have raft logs that is large than or equal to prepare merge min index. But in ebs backup, the snapshot of panic tikv is taken before merge, and the snapshot of other tikvs is taken after merge. So the target region leader sends CommitMerge raft log to panic tikv, but the source region leader doesn't send the following raft log (because it is merged), which causes the source region to panic when handling catch up log from target region.

 
y this is bc tikv keep restarting with same issue.
Because target region keeps sending CatchUpLogs to source region, and source region keeps panicking when handling CatchUpLogs.

### 2023-10-10T11:25:09.000+0800 [REDACTED_USER]

FYI, we have filed an issue for tracking this case. 
TiKV panic due to catch up logs during ebs restore · Issue #15739 · tikv/tikv (github.com)

### 2023-10-10T21:12:02.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 10/Oct/23 1:11 PM

Hi [REDACTED_USER],
The RC already identified, and you can find details in below issue, we will try to work out the solution for it ASAP and keep you updating, thanks.
https://github.com/tikv/tikv/issues/15739
 
Regards
Jiamin Li

### 2023-11-10T05:22:50.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/Nov/23 9:22 PM

Hi [REDACTED_USER], 
the issue has been tracked below link, can we close this ticket itself?

### 2023-11-14T01:07:12.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 13/Nov/23 5:07 PM

Hi [REDACTED_USER], 
will close this ticket by the end of Tuesday if no further response and if new issues occur, feel free to contact us on slack or open a new ticket.
