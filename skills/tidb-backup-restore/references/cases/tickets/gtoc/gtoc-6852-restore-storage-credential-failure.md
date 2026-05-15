# GTOC-6852: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6852
- Status: Canceled
- Resolution: Cancel
- Priority: P3
- Issue type: Incident
- Created: 2024-04-17T12:06:08.000+0800
- Updated: 2025-03-06T18:14:06.171+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: restore-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We’ve observed that when restoring large databases or tables (few terabyte scale), the `br restore` task will sometimes stop without a logged reason. 

For example, we started `br restore` at `2024/04/12 17:21:33.828 UTC` (1:21 EDT) and the last line in `/tmp/br.log.2024-04-12T17.21.33Z` was logged at `2024/04/12 18:07:44.074 UTC`.

```
nohup tiup br:v6.5.3 restore table \
--pd [REDACTED_RESOURCE_NAME].plaid-db.io:2379 \
--db ${DATABASE_NAME} \
--table ${TABLE_NAME} \
--storage "${SNAPSHOT_IDENTIFIER}" \
2>&1 | sudo tee nohup.out &
```

When checking the br log, the last line would simply be something like `[2024/04/12 18:07:44.074 +00:00] [INFO] [client.go:1167] ["import files done"] [files="{total=1,files=\"[154684940/156324449_15133_e947a9383aba44af5b03e0208fd20798f7eed584b31532d8ca5dc06705c110b1_1712752955880_write.sst]\",totalKVs=495878,totalBytes=82315748,totalSize=16377953}"] [take=4.760434028s]` which is quite similar to previously logged lines and doesn’t have any error information,

Checking the logs of our validation cluster, we did see some potentially alarming errors like `[sst_service.rs:826] ["send rpc response"] [err=RemoteStopped]` around the time that the job stopped. We will attach the logs shortly (need to redact first). Would you be able to look at these and advise?

## Recent Comments Excerpt

### 2024-04-18T05:50:07.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 9:49 PM

Would that be on the machine from which we initiate the restore job, or a specific node in the cluster we’re restoring to?

### 2024-04-18T05:58:11.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Apr/24 9:58 PM

Hi @[REDACTED_USER] be the machine that runs BR.

### 2024-04-27T01:01:33.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Apr/24 5:01 PM

Hi [REDACTED_USER], just want to follow up on this ticket, feel free to let us know if there is any more questions, thanks.

### 2024-04-30T01:02:56.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 29/Apr/24 5:02 PM

Hi [REDACTED_USER], just want to follow up again on this ticket. If there is no more question, we will close this ticket in next few days, thanks.

### 2024-05-03T01:03:11.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 02/May/24 5:02 PM

Hi [REDACTED_USER], it seems there is no follow up questions, will close this ticket, and feel free to reopen it if needed, thanks.
