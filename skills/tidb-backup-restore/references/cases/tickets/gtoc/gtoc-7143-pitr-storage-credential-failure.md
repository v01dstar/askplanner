# GTOC-7143: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7143
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-09-19T02:03:04.000+0800
- Updated: 2025-03-06T18:01:43.995+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, TiDB Operator
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER],

 

When backup, customer [REDACTED_CUSTOMER], please help to check:  
{{I0917 21:22:22.694198       9 backup.go:306\] \[2024/09/17 21:22:22.693 +00:00\] \[INFO\] \[collector.go:264\] \["Full Backup success summary"\] \[total-ranges=185\] \[ranges-succeed=185\] \[ranges-failed=0\] \[backup-checksum=6.683138ms\] \[backup-total-ranges=8\] \[backup-total-regions=145\] \[total-take=11.538275092s\] \[BackupTS=[REDACTED_LONG_ID]\] \[total-kv=64047469\] \[total-kv-size=10.68GB\] \[average-speed=925.9MB/s\] \[backup-data-size(after-compressed)=3.76GB\] \[Size=3759864831\]I0917 21:22:22.700862       9 backup.go:306\]  
I0917 21:22:22.700950       9 backup.go:326\] Run br commond \[backup full --pd=[REDACTED_ENV_NAME].tidb-cluster:2379 --log-level=info --send-credentials-to-tikv=true --storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] --s3.region=us-east-1 --s3.provider=aws --filter content_manager_prod.\* --concurrency=20 --checksum=false\] for cluster [REDACTED_CLUSTER]/[REDACTED_ENV_NAME] successfully  
I0917 21:22:22.700995       9 manager.go:389\] backup cluster [REDACTED_CLUSTER]/[REDACTED_ENV_NAME] data to s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] success  
2024/09/17 21:22:22 Ignoring, HTTP credential provider invalid endpoint host, "[REDACTED_IP]", only loopback hosts are allowed. <nil>  
E0917 21:22:53.707295       9 manager.go:408\] Get backup metadata for backup files in s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH] of cluster [REDACTED_CLUSTER]/[REDACTED_ENV_NAME] failed, err: read backup meta from bucket [REDACTED_BUCKET] and prefix prod/backups/data/pitr/[REDACTED_ENV_NAME]/[REDACTED_ENV_NAME].tidb-cluster-2379-2024-09-17t21-22-00: blob (key "backupmeta") (code=Unknown): NoCredentialProviders: no valid providers in chain. Deprecated.  
For verbose messaging see aws.Config.CredentialsChainVerboseErrors  
I0917 21:22:53.717027       9 backup_status_updater.go:128\] Backup: \[tidb-cluster/[REDACTED_CLUSTER]\] updated successfully  
error: read backup meta from bucket [REDACTED_BUCKET] and prefix prod/backups/data/pitr/[REDACTED_ENV_NAME]/[REDACTED_ENV_NAME].tidb-cluster-2379-2024-09-17t21-22-00: blob (key "backupmeta") (code=Unknown): NoCredentialProviders: no valid providers in chain. Deprecated.  
For verbose messaging see aws.Config.CredentialsChainVerboseErrors}}  
   
1\. They use IAM role for identify, with sendCredToTikv: true, I let then try false but still not working.  
2\. They checked IAM role permission, they have all permission ListBucket, GetObject, DeleteObject, PutObject  
root@[REDACTED_ENV_NAME]:/opt/tidb# /usr/local/aws-cli/v2/current/bin/aws s3api get-object --bucket [REDACTED_BUCKET] --key [REDACTED_OBJECT_PATH] ./bmt { "AcceptRanges": "bytes", "Expiration": "expiry-date=\\"Sat, 28 Sep 2024 00:00:00 GMT\\", rule-id=\\"prod/backups/ EF-2532\\"", "LastModified": "2024-09-17T23:15:34+00:00", "ContentLength": 373, "ETag": "\\"27c9c17c87a94788832af1b3aa06bca7\\"", "VersionId": "null", "ContentType": "binary/octet-stream", "ServerSideEncryption": "AES256", "Metadata": {} }  
   
3\. Their config:  
apiVersion: pingcap.com/v1alpha1  
kind: BackupSchedule  
metadata:  
  name: [REDACTED_RESOURCE_NAME]  
  namespace: [REDACTED_NAMESPACE]  
  annotations:  
    iam.amazonaws.com/role: arn:aws:iam::[REDACTED_LONG_ID]:role/EKSTiDBProd001MainUse1BaseIrsa  
spec:

## Recent Comments Excerpt

### 2024-09-19T10:34:31.000+0800 [REDACTED_USER]

Please review on customer [REDACTED_CUSTOMER], and let me when you plan on solve the issue.

### 2024-09-19T15:16:41.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark

### 2024-09-19T16:24:48.000+0800 [REDACTED_USER]

It seems 
@[REDACTED_USER]
 has locate the root cause and provide solution(upgrade to v1.6.0 tidb operator). what can I do right now?

### 2024-09-20T01:01:20.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 double check, and give an action plan on fix it in our branch.

### 2024-09-29T11:19:49.000+0800 [REDACTED_USER]

After several tests, tikv cannot works well, in my eks test env.
[REDACTED_MEDIA]
tikv cannot support pod identity, some times it works because of set --send-credientals-to-tikv=true, with this setting, tikv will use br pod credential to connect to S3, but with expiration the token is no longer avaiable. so log backup would fail eventually as test.
 

I file an issue about this 
https://github.com/tikv/tikv/issues/17600.
