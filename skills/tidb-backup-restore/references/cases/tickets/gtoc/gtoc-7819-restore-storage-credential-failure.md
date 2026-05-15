# GTOC-7819: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7819
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P1
- Issue type: Incident
- Created: 2025-07-31T09:32:40.807+0800
- Updated: 2026-02-21T04:01:57.479+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Backup and restore doesn’t seem to work in Azure Mooncake regions.  
The Azure endpoint seems to be hardcoded here - <custom data-type="smartlink" data-id="id-0">https://github.com/pingcap/tidb/blob/master/br/pkg/storage/azblob.go</custom> , and backup/log-backups fail because the request is sent to the the azure public URL instead.  
An example error - 

```
error="Get \"https://tibkprodcnn2.blob.core.windows.net/backup-data?restype=container\": dial tcp: lookup tibkprodcnn2.blob.core.windows.net on ****: no such host"
```

The request should have been sent to the Azure China cloud blob storage endpoint instead.  
The TiDB Operator also doesn’t seem to support the endpoint field in the Backup/Restore CR’s - <custom data-type="smartlink" data-id="id-1">https://github.com/pingcap/tidb-operator/blob/master/pkg/apis/pingcap/v1alpha1/types.go#L2066</custom> 

Is there any way to configure the Backup/Restore CR’s to override the endpoint for azure china cloud regions?  
If not is it possible to hotfix this?

## Recent Comments Excerpt

### 2025-07-31T11:00:52.913+0800 [REDACTED_USER]

@[REDACTED_USER]
 can you please ask databricks if they can try fixing it themselves and contribute the pr?  it’s quite tedious for us to test and valid the solution and go through the hotfix process.

### 2025-11-25T05:25:01.791+0800 [REDACTED_USER]

From customer: [REDACTED_CUSTOMER], and found one issue with the tikv side patch. 
https://github.com/tikv/tikv/pull/18801/files
The code
            let cred = Arc::new(ClientSecretCredential::new(
                new_http_client(),
                credential_info.tenant_id.clone(),
                credential_info.client_id.to_string(),
                credential_info.client_secret.secret().clone(),

### 2025-11-25T11:49:47.147+0800 [REDACTED_USER]

cc 
@[REDACTED_USER]
 about 
https://github.com/tikv/tikv/pull/18801
   ↑

### 2026-02-21T04:00:06.592+0800 [REDACTED_USER]

Databricks add some changes to the PR and made it work. The customer [REDACTED_CUSTOMER]
Fix Azure endpoint upstream pr.
tidb-operator: 
https://github.com/pingcap/tidb-operator/pull/6735
tikv: 
https://github.com/tikv/tikv/pull/19383
Please review. Thanks.

### 2026-02-21T04:01:57.479+0800 [REDACTED_USER]

See detail discussion for the draft PR provided by 
@[REDACTED_USER]
  
https://docs.google.com/document/d/1qlWTAsr3LnDx3ux-AuhsbjEI-p5C_UXBKQJGaP3Qd7I/edit?tab=t.0#heading=h.wvgvvcwpl9ij
