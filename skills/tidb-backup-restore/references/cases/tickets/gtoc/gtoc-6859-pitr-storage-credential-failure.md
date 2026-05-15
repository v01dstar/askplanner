# GTOC-6859: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6859
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-04-19T15:30:50.000+0800
- Updated: 2025-03-06T18:13:55.661+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

【问题描述】

br full back to aws s3 遇到报错：

```
Error: error happen in store 5 at [REDACTED_IP]:20160: Io(Custom { kind: Other, error: "failed to put object rusoto error Couldn't find AWS credentials in sources (Couldn't find AWS credentials in environment, credentials file, or IAM role;No (or empty) AWS_ACCESS_KEY_ID in environment;Couldn't stat credentials file: [ \"/home/tidb/.aws/credentials\" ]. Non existant, or no permission.;Could not get request from environment: Neither environment variable 'AWS_CONTAINER_CREDENTIALS_FULL_URI' nor 'AWS_CONTAINER_CREDENTIALS_RELATIVE_URI' is set;EOF while parsing a value at line 1 column 0)." }): [BR:KV:ErrKVStorage]tikv storage occur I/O error
```

s3 bucket 权限

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::[REDACTED_RESOURCE_NAME]",
                "arn:aws:s3:::[REDACTED_RESOURCE_NAME]/*"
            ]
        }
    ]
}
```

## Recent Comments Excerpt

### 2024-04-22T14:16:44.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 22/Apr/24 6:16 AM
其他 tikv 节点是否有备份数据生成？
这个 log 看不出其他节点是否完成了备份，如何查看其他节点是否存在备份文件。
btw我只能看到有的 region range 备份是成功的，有的是失败的
[2024/04/17 10:05:34.808 +00:00] [INFO] [client.go:904] ["backup range completed"] [range-sn=2] [startKey=74800000000000000C5F720000000000000000] [endKey=74800000000000000C5F72FFFFFFFFFFFFFFFF00] [take=2.184821ms]

### 2024-04-23T11:14:48.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 23/Apr/24 3:14 AM

s3 中没有 sst file 说明不止一个 tikv 有问题
[REDACTED_MEDIA]
排除使用了不同 linux user 去测试 aws cli
[REDACTED_MEDIA]
resource * 客户拒绝测试
{{{ "Version": "2012-10-17", "Statement": [ { "Sid": "VisualEditor0", "Effect": "Allow", "Action": "s3:

### 2024-04-24T16:30:17.000+0800 [REDACTED_USER]

root cause:
当前 tikv 使用的 s3 sdk（rusoto) 不支持 IMDSv2，而用户的环境强制开启了 IMDSv2，因此获取不到对应的 IAM role 信息。
https://github.com/rusoto/rusoto/issues/1818#issuecomment-689731018

### 2024-04-25T17:13:03.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 25/Apr/24 9:12 AM

rootcause
tikv 的 rust 库不支持 IAM 的 IMDSv2 访问（br 等 golang 工具是支持）
workaround
1、把 IMDSv2 限制改成 option
2、后续 rust 版本支持、开发

### 2024-04-26T14:59:01.000+0800 [REDACTED_USER]

可以关单
 
尝试说明下 IMDSv2 设置位置。
[REDACTED_MEDIA]
