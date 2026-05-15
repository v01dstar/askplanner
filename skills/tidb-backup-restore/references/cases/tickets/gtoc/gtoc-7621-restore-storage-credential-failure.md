# GTOC-7621: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7621
- Status: Resolved
- Resolution: Done
- Priority: P1
- Issue type: Incident
- Created: 2025-05-28T06:30:56.988+0800
- Updated: 2025-06-09T08:55:57.185+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR, TiDB Lightning, TiDB Operator
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

I have worked with <custom data-type="mention" data-id="id-0">@[REDACTED_USER]</custom> on this issue. I followed <custom data-type="smartlink" data-id="id-1">https://docs.pingcap.com/tidb-in-kubernetes/stable/restore-from-s3/</custom>  to run a restore on eks

I used following config(recommended by step 4):

```
apiVersion: pingcap.com/v1alpha1
kind: Restore
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
  # annotations:
  #   iam.amazonaws.com/role: arn:aws:iam::[REDACTED_LONG_ID]:role/EKSTiDBProd002TidbUse1BaseIrsa
spec:
  # S3 source
  backupType: full
  serviceAccount: tidb-service
  s3:
    provider: aws
    region: us-east-1
    path: s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]

  # TiDB target
  to:
    host: [REDACTED_ENV_NAME].us-east-1.[REDACTED_LONG_ID].ec2.pin220.com
    port: 4000
    user: root
    secretName: [REDACTED_RESOURCE_NAME]

## Recent Comments Excerpt

### 2025-05-28T11:22:47.349+0800 [REDACTED_USER]

acked msg index: om_x100b4c533953acb40f22bcae5064120

### 2025-05-28T11:22:48.015+0800 [REDACTED_USER]

acked msg index: om_x100b4c53db24f2b40f18dc22c9a5ea9

### 2025-05-28T11:51:52.199+0800 [REDACTED_USER]

Discussed with 
@[REDACTED_USER]
 
@[REDACTED_USER]
 
@[REDACTED_USER]
 and 
@[REDACTED_USER]

### 2025-05-28T12:09:30.283+0800 [REDACTED_USER]

PR for English version of public doc - 
add dumpling-lightning-job by yiduoyunQ · Pull Request #2770 · pingcap/[REDACTED_RESOURCE_NAME]
Lark group: click 
https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=[REDACTED_SECRET]
 to join!

### 2025-06-09T08:55:56.641+0800 [REDACTED_USER]

用户使用方式有问题，已经给他们正确的文档了。
