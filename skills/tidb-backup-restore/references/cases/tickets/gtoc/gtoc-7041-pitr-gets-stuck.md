# GTOC-7041: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7041
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-07-30T23:31:05.000+0800
- Updated: 2025-03-06T18:08:05.007+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

log backup checkpoint metric stops updating around 7/18 \~10:40a PT and hasn’t recovered since then. additionally, don’t see any logs/data in s3 since that time. doesn’t appear to be correlated w/ deploy or other cluster [REDACTED_CLUSTER]

I’ve attached the log backup CR, clinic metrics from the period around when the log backup stopped <custom data-type="smartlink" data-id="id-0">[REDACTED_CLINIC_URL]> , and sample tikv logs (tikv-0-a).

beyond root-causing log issue and getting the log backup resumed, given that the log backup has been stuck for over 1 week, are the missing logs recoverable? when issues like this occur, how long can the log backup be paused before we are unable to recover the logs? is it determined by the cluster gc window similar to snapshot backup?

## Recent Comments Excerpt

### 2024-08-07T05:00:13.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Aug/24 8:59 PM

Questions on the br --gc-ttl option, the default is 24 hours. If I want to stop the current job, and create a new job with --commit-ts=previous checkpoint ts, does this 24 hours mean I can do so within 24 hours window? 
The current behavior is that I can only recreate a new job with commit-ts setting to within 10 minutes, which is the global gc ttl. 
So not sure if this is a bug or expected behavior.

### 2024-08-07T05:22:03.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Aug/24 9:21 PM

Hi @[REDACTED_USER] is because you can only specify --gc-ttl when you pause log backup(
https://docs.pingcap.com/tidb/stable/br-pitr-manual
 ), right now there is still no interface in operator. Refer 
https://github.com/pingcap/tidb-operator/issues/5699

### 2024-08-07T08:39:06.000+0800 [REDACTED_USER]

if you manually stop log backup task then only the global gc ttl(10mins) is effective.
If log backup is down by error, the default gc-ttl is 24h, which will prevent GC moving forward in 24h. which means you will have 24hours to handle this error.

### 2024-08-07T08:46:50.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 07/Aug/24 12:46 AM

@[REDACTED_USER] I need to make a correction. 
if you manually 
stop
 log backup task then only the global gc ttl(10mins) is effective. However you can 
pause

### 2024-08-10T01:01:29.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/Aug/24 5:01 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
