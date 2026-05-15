# GTOC-7040: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7040
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-07-30T18:28:38.000+0800
- Updated: 2025-03-06T18:08:06.732+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: backup-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We’re seeing that during our nightly BR backup runs, the I/O of our TiKVs in our silver cluster [REDACTED_CLUSTER] up to 700-900 MiB/s for about \~5 minutes.

```
tiup "br:${version}" backup full \
    --pd "$pd" \
    --filter '.' --filter '!cra_.' \
    --ratelimit 128 \
    --storage "s3://[REDACTED_BUCKET]/${env}/${cluster}/$(date +%s)" \
    --ca "${certdir}/ca.crt" \
    --cert "${certdir}/client.crt" \
    --key "${certdir}/client.pem" \
    --log-file="" \
    -c=0
```

This is what our BR job looks like. According to the [docs](https://docs.pingcap.com/tidb/stable/br-snapshot-guide#back-up-cluster-snapshots), it seems `--ratelimit` should be setting the `the maximum speed per TiKV performing backup tasks. The unit is in MiB/s.`

Is `--ratelimit` how we should be limiting the I/O to TiKVs? If so, is it working incorrectly? Are there any other levers we can pull here to limit I/O impact on TiKVs?

For context, this burst in TiKV I/O is causing latency and some timeouts to be hit in some of our applications.

## Recent Comments Excerpt

### 2024-08-09T02:42:31.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Aug/24 6:42 PM

Hi [REDACTED_USER],
Tested in our internal reproduction environment, reducing checksum concurrency can definitely reduce the MBps, but it cannot completely eliminate it. So you can continuously reduce it to 1. 
And I need to check with our PM to see if there is any roadmap for addressing the high MBps issue during the checksum phase.
[REDACTED_MEDIA]

### 2024-08-09T03:14:35.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 08/Aug/24 7:14 PM

For us, the I/O spike between 4 and 2 is almost the same 😥 .
I’m hesitant to move it to 
1
 because of the time it will take to run the backup script.
At concurrency of 
4

### 2024-08-09T20:41:33.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/Aug/24 12:41 PM

Thank you Andrew for your feedback and consideration. We understand the importance of minimizing the time taken to run the backup script while ensuring its reliability. We are actively monitoring and addressing the high MBps issue during checksumming to enhance efficiency as we scale. We will keep you updated on any roadmap developments. Your valuable insights are greatly appreciated as we strive to optimize the process for all scenarios.

### 2024-08-10T02:52:05.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 09/Aug/24 6:51 PM

[REDACTED_INTERNAL_URL]

### 2024-08-10T10:23:50.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 10/Aug/24 2:23 AM

Hi [REDACTED_USER],
According to feedback from my other co-workers, we already have a checksum at the SST file level. Disabling the checksum will only stop the table-level checksum. Many users choose to disable the checksum while still ensuring the availability of the backup set. Additionally, table-level checksums are processed through coprocessor requests, so Resource Control (
https://docs.pingcap.com/tidb/stable/tidb-resource-control
 ) would be useful. It is recommended to use this feature until it becomes GA( Still needs to go through several versions).
