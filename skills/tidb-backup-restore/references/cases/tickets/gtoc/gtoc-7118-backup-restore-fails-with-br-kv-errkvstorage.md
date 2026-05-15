# GTOC-7118: Backup/Restore fails with [BR:KV:ErrKVStorage\]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7118
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2024-09-08T10:52:36.000+0800
- Updated: 2025-03-06T18:02:26.796+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, compatibility-upgrade
- Labels: N/A

## Symptom / Description Excerpt

[https://pingcap-ticket.atlassian.net/browse/APID-10866](https://pingcap-ticket.atlassian.net/browse/APID-10866)

 

br v6.5.5 版本

客户反馈备份过程报错 

Error: error happen in store 16 at [REDACTED_IP]:20160: Io(Custom { kind: Other, error: "failed to put object rusoto error Request ID: None Body: <?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\\n<Error><Code>InvalidAccessKeyId</Code><Message>The AWS Access Key Id you provided does not exist in our records.</Message><AWSAccessKeyId>ASIASYPQWAPQYUXMBQTL</AWSAccessKeyId><RequestId>W5P22T2634TQ42D1</RequestId><HostId>Eunk2hrBjAXQdRSkD7iCGUyL0NXPHAyjywVgu4eizMfM1s2Yxztb16D49Bt3x0xAsU7AjY62S8A=</HostId></Error>" }): \[BR:KV:ErrKVStorage\]tikv storage occur I/O error

 

客户反馈可以将数据写入 S3，之前使用 dumpling 备份到相同 S3 目录可以成功，确认 accesskey 没问题。

且 br 备份时可以在 S3 创建文件，是在备份中途才报错退出

[REDACTED_MEDIA]
日志：

[REDACTED_MEDIA]看起来现象类似 [[REDACTED_INTERNAL_URL])  ，不确定高版本是否解决这个问题

麻烦 oncall 老师帮忙看下

## Recent Comments Excerpt

### 2024-09-08T10:52:49.000+0800 [REDACTED_USER]

notified (徐锐([REDACTED_EMAIL]), ) by lark

### 2024-09-13T09:52:06.000+0800 [REDACTED_USER]

日志显示 TiKV store 1 没有设置好权限。

 

可能是因为客户的集群开启了 imdsv2，但是 6.5 版本的 tikv 还不支持通过 imdsv2 获取 IAM role。

IMDSv2 · Issue #1818 · rusoto/rusoto

### 2024-10-08T17:25:51.000+0800 [REDACTED_USER]

friendly ping 
@[REDACTED_USER]
 , any update from the customer [REDACTED_CUSTOMER]?
