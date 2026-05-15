# GTOC-7442: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7442
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-03-04T10:29:37.457+0800
- Updated: 2025-03-29T00:15:54.793+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We have just run a PITR test on a new internal 8.5.1 build and are seeing a regression in snapshot backup performance. Previously we could restore a full snapshot of the cluster, consisting of \~60TB of S3 data, in 1-1.5hrs. When running the PITR test, the snapshot restore phase took \~9hrs.

Backup was taken after 8.5.1 upgrade w/ the following config:

```
--concurrency=256
--checksum=false
```

Restore was performed w/ 8.5.1 br and the following config:

```
--concurrency=256
--[REDACTED_RESOURCE_NAME]=64
```

It doesn’t appear that the snapshot restore process itself is affected, as we only observe download import RPC requests and TiKV import work being done for the first 1hr of the restore, in line w/ previous observations.

However, after those requests complete, we observe an \~8hr period where tikvs don’t appear to be doing any import work. From restore logs I see logs like:

```
...
I0303 05:44:08.807414       9 restore.go:176] [2025/03/03 05:44:08.807 +00:00] [INFO] [client.go:1067] ["success in validating checksum"] [db=oyster_production] [table=HippoProductDataV3]
...
```

These logs start after the download and import period and continue throughout the subsequent 8hrs, and are not previously present in our restore tests on 8.1.1.

## Recent Comments Excerpt

### 2025-03-05T01:32:56.575+0800 [REDACTED_USER]

assigned to myself. As we discussed in the chat, the restore is expected to run checksum now, which was not running in previous version due to a bug. However, the 8 hour long running was not expected and need to dig into further. It would be helpful to get a clinic from Airbnb to further analyze the issue.

### 2025-03-05T04:14:16.855+0800 [REDACTED_USER]

restore log uploaded.
Clinic: 
[REDACTED_CLINIC_URL]
  
From customer: [REDACTED_CUSTOMER]/ the default checksum-concurrency (64)

### 2025-03-06T01:27:07.901+0800 [REDACTED_USER]

after looking into it we found that there is one large table that’s taking 7 hours alone, the table is 13TB but checksum is running one thread per table and it scans the entire table sequentially. We should divide the table into multiple smaller ranges and run in parallel since it’s not imperative to calculate the checksum sequentially.

### 2025-03-26T06:03:05.980+0800 [REDACTED_USER]

but checksum is running one thread per table and it scans the entire table sequentially. We should divide the table into multiple smaller ranges and run in parallel since it’s not imperative to calculate the checksum sequentially.
so increasing checksum num-threads would only increase how many tables we checksum in parallel, and not increase the speed of checksumming this single large table, correct?
We should divide the table into multiple smaller ranges and run in parallel since it’s not imperative to calculate the checksum sequentially.
is there a fix/improvement we can track for above?

### 2025-03-29T00:15:54.793+0800 [REDACTED_USER]

yes I don’t think we have a proper way to calculate a single large table in parallel right now.
I will open a fix to turn off the restore checksum by default.
