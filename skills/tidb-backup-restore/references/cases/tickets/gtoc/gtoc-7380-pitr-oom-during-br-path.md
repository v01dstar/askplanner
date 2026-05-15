# GTOC-7380: PITR OOM during BR path

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7380
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-02-04T06:15:58.722+0800
- Updated: 2025-03-06T17:38:13.473+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

This is internal testing on Atlassian Special Release. This release is based on 8.5.0 added feature to allow restore while log backup is running. 

I have a 1M table testcase that was working without log backup. Now with log backup. It fails with OOM even on a 64GB pod.

## Recent Comments Excerpt

### 2025-02-04T22:53:58.779+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2025-02-14T09:58:23.983+0800 [REDACTED_USER]

Is it possible to get a heap dump before OOM? it might need to run again and when it’s at the copying phase to take a manual heap dump. 
We are also having a feature to do heap dump automatically before OOM, we can also wait for that tool to be in master

### 2025-02-17T04:43:35.159+0800 [REDACTED_USER]

I took profile every 5 second till BR crashed. Here are all the profiles.
[REDACTED_MEDIA]

### 2025-02-19T00:21:14.946+0800 [REDACTED_USER]

thanks so much for the detailed heap dumps, we do see huge memory usage by the putSST method, I believe it’s reasonable to add a rate limit mechanism to it
[REDACTED_MEDIA]

### 2025-03-05T01:39:08.657+0800 [REDACTED_USER]

fix by juncen 
https://github.com/pingcap/tidb/pull/59696
 
verifying if it works
