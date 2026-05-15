# GTOC-7161: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7161
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-09-26T01:46:05.000+0800
- Updated: 2025-03-06T18:01:11.306+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

[REDACTED_USER]@[REDACTED_ENV_NAME]:/var/log/tidb$ sudo docker exec -it tidb-pd br log status  --pd=[REDACTED_ENV_NAME].ec2.pin220.com:2379  --ca /var/lib/normandie/fuse/ca/root --cert /var/lib/normandie/fuse/chain/generic --key /var/lib/normandie/fuse/key/generic   Detail BR log in /tmp/br.log.2024-09-24T18.11.02Z  ● Total 1 Tasks. > #1 <                             name: pitr_3                           status: ○ ERROR                            start: 2024-08-31 17:51:51.903 +0000                              end: 2090-11-18 14:07:45.624 +0000                          storage: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]                      speed(est.): 0.00 ops/s               checkpoint\[global\]: 2024-09-22 14:29:13.253 +0000; gap=51h41m51s           error\[store=154115209\]: KV:LogBackup:Io error-happen-at\[store=154115209\]: 2024-09-22 14:31:35.732 +0000; gap=51h39m29s   error-message\[store=154115209\]: I/O Error: No such file or directory (os error 2)

## Recent Comments Excerpt

### 2024-09-26T01:46:20.000+0800 [REDACTED_USER]

notified (陈书宁([REDACTED_EMAIL]), ) by lark
