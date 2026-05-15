# GTOC-7366: Backup/Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7366
- Status: Canceled
- Resolution: Cancel
- Priority: P3
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2025-01-23T16:42:37.616+0800
- Updated: 2025-05-15T16:07:29.184+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: BR
- Categories: storage-credential, compatibility-upgrade
- Labels: N/A

## Symptom / Description Excerpt

`我们有没有支持 BR 对 aliyun OSS SEE 服务端加密的计划？`

1. `FRM 中没找到对应记录`
2. `看 AWS 和 Azure 我们是支持的 `[静态加密 | TiDB 文档中心](https://docs.pingcap.com/zh/tidb/v7.5/encryption-at-rest#br-s3-%E6%9C%8D%E5%8A%A1%E7%AB%AF%E5%8A%A0%E5%AF%86)

`有付费客户要用，所以来咨询下 `[oss服务器端加密（SSE）-阿里云开发者社区](https://developer.aliyun.com/article/1467877)

`谢谢`

## Recent Comments Excerpt

### 2025-01-23T16:42:51.247+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark

### 2025-01-23T16:49:53.121+0800 [REDACTED_USER]

看了下 OSS 加密的介绍，似乎不需要客户端做什么事情，只要给存储空间开启加密即可。建议测试下看看。
[REDACTED_MEDIA]

### 2025-05-15T16:07:08.767+0800 [REDACTED_USER]

我们确实不需要做什么，感谢支持
