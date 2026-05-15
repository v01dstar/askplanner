# GTOC-6998: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6998
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-07-01T12:08:05.000+0800
- Updated: 2025-03-07T10:55:26.192+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

p999 read jumped from 20ms to 15 secon. Lots of failed queries as well.

The error rate and latency seems unexpected. Can you share what happens during checksum phase. And what could be causing the perf regression. 

Attached

* tikv logs. 
* metric screenshots of tidb, tikv grpc, tikv backup. 
* snapshot CR

## Recent Comments Excerpt

### 2024-07-26T17:08:50.000+0800 [REDACTED_USER]

please also confirm if the ebs type is gps with 8000iops/800mbps.

### 2024-07-26T17:33:29.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Jul/24 9:33 AM

Hi [REDACTED_USER],
Here are some new updates:
When we were backing up, scanning data from disk is pretty slow.
[REDACTED_MEDIA]
This suggests that the reading was probably throttled when backing up.
Then, when we are checksumming, the `coprocessor` RPC (which tries to run a compiled SQL-like query in TiKV) latency increases greatly, but the real processing time of `select` wasn't increased. (The metric below is in fact P999, I temporarily changed the promQL)

### 2024-08-02T03:56:26.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/Aug/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-08-03T03:44:11.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/Aug/24 7:43 PM

We have weekly call. Airbnb is still testing.

### 2024-08-10T03:56:49.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/Aug/24 7:56 PM

The status of this ticket was "Waiting For Customer" status with no update for 7 days. Please take a look.
