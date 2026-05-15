# GTOC-8079: Restore fails with Job has failed, original reason BackoffLimitExceeded\

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8079
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-12-04T09:16:28.840+0800
- Updated: 2026-01-13T20:49:53.506+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We’re getting backup failures in some environments that are on a more recent version of tidb. The backups are reporting \`message: exceed retry times, max is 2, failed reason Job [REDACTED_RESOURCE_NAME] has failed, original reason BackoffLimitExceeded\` 

The affected version is 1.0.6 for the forked version of this repo: <custom data-type="smartlink" data-id="id-0">https://github.com/pingcap/tidb-operator/blob/release-1.x/CHANGELOG.md</custom>  on the 1.x branch this wasn’t an option in the affected version select box so I picked a random version. 

Logs of backup attached

## Recent Comments Excerpt

### 2025-12-09T18:21:20.330+0800 [REDACTED_USER]

@[REDACTED_USER]
 
OK, will check with customer [REDACTED_CUSTOMER]

### 2025-12-18T08:01:20.107+0800 [REDACTED_USER]

GTOC-8079 问题阶段性小结（BR backup BackoffLimitExceeded）
背景：

客户在使用 tidb-operator + [REDACTED_RESOURCE_NAME] 执行 snapshot full backup 时，持续遇到失败。operator 最终报错为 BackoffLimitExceeded，backup CR 达到 max retry 次数后进入 Failed。问题在客户的一个生成集群可稳定复现。
第一阶段观察（早期日志）
BR 日志中可以看到正常的启动流程：
启动 domain
加载 InfoSchema（V2）

### 2025-12-18T08:04:07.153+0800 [REDACTED_USER]

这是早期日志：
[REDACTED_MEDIA]
 
这是设了GOMEMLIMIT后的日志：
[REDACTED_MEDIA]

### 2025-12-18T08:05:07.395+0800 [REDACTED_USER]

k8s信息:
apiVersion: pingcap.com/v1alpha1
kind: Backup
metadata:
  name: [REDACTED_RESOURCE_NAME]
  namespace: [REDACTED_NAMESPACE]
spec:
  imagePullSecrets:

### 2025-12-18T08:05:45.478+0800 [REDACTED_USER]

最后一点：if I use a table filter and target a subset of data (I only targeted one small database), it does work.
