# GTOC-7276: Restore fails with [BR:Common:ErrUnknown]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7276
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2024-11-27T10:37:10.000+0800
- Updated: 2025-03-06T17:46:04.001+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

v7.5.3 版本 br 备份时报错退出

客户反馈此备份运行了几个月，检查了存储桶权限正常。发生最后一个报错后 br 就退出了.

 

日志请见附件（日志不全，前10行如下）

```java
[2024/11/26 12:00:01.557 +08:00] [INFO] [info.go:49] ["Welcome to Backup & Restore (BR)"] [release-version=v7.5.2] [git-hash=3c02c2aa1339a078d7a4983409852b01eb23bf9b] [gi
t-branch=HEAD] [go-version=go1.21.10] [utc-build-time="2024-06-05 09:53:48"] [race-enabled=false]
[2024/11/26 12:00:01.558 +08:00] [INFO] [common.go:755] [arguments] [__command="br backup full"] [checksum-concurrency=1] [concurrency=8] [crypter.key=94c5f337b148372186d
9b0074d4d968694c5f337b148372186d9b0074d4d9686] [crypter.method=aes256-ctr] [log-file=/data/backup/logs/backupfull_20241126_12_00_01.log] [pd="[[REDACTED_IP]:2379]"] [s3.e
ndpoint=https://oss-ap-southeast-1-internal.aliyuncs.com] [s3.provider=alibaba] [s3.region=US] [send-credentials-to-tikv=true] [storage=s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]
sg-[REDACTED_RESOURCE_NAME]/tidb/20241126_12_00_01/]
[2024/11/26 12:00:01.559 +08:00] [INFO] [conn.go:153] ["new mgr"] [pdAddrs=[REDACTED_IP]:2379]
[2024/11/26 12:00:01.569 +08:00] [INFO] [pd_service_discovery.go:606] ["[pd] update member urls"] [old-urls="[http://[REDACTED_IP]:2379]"] [new-urls="[http://[REDACTED_IP]
3:2379,<http://[REDACTED_IP]:2379>,<http://[REDACTED_IP]:2379>]"]
[2024/11/26 12:00:01.569 +08:00] [INFO] [pd_service_discovery.go:631] ["[pd] switch leader"] [new-leader=http://[REDACTED_IP]:2379] [old-leader=]
[2024/11/26 12:00:01.570 +08:00] [INFO] [pd_service_discovery.go:197] ["[pd] init cluster id"] [cluster-id=[REDACTED_LONG_ID]
[2024/11/26 12:00:01.573 +08:00] [INFO] [client.go:600] ["[pd] changing service mode"] [old-mode=UNKNOWN_SVC_MODE] [new-mode=PD_SVC_MODE]
[2024/11/26 12:00:01.573 +08:00] [INFO] [tso_client.go:231] ["[tso] switch dc tso global allocator serving address"] [dc-location=global] [new-address=http://[REDACTED_IP]
5:2379]
[2024/11/26 12:00:01.575 +08:00] [INFO] [tso_dispatcher.go:323] ["[tso] tso dispatcher created"] [dc-location=global]
[2024/11/26 12:00:01.575 +08:00] [INFO] [client.go:648] ["[pd] service mode changed"] [old-mode=UNKNOWN_SVC_MODE] [new-mode=PD_SVC_MODE]
[2024/11/26 12:00:01.576 +08:00] [WARN] [version.go:232] ["BR version is outdated, please consider use version 7.5.4 of BR"]
[2024/11/26 12:00:01.576 +08:00] [WARN] [version.go:232] ["BR version is outdated, please consider use version 7.5.4 of BR"]
[2024/11/26 12:00:01.576 +08:00] [WARN] [version.go:232] ["BR version is outdated, please consider use version 7.5.4 of BR"]

## Recent Comments Excerpt

### 2024-11-27T10:37:20.000+0800 [REDACTED_USER]

notified (栾成 ([REDACTED_EMAIL]), ) by lark

### 2024-11-27T11:14:06.000+0800 [REDACTED_USER]

从日志看备份失败了
[2024/11/27 04:29:36.714 +08:00] [ERROR] [backup.go:54] ["failed to backup"] [error="at fine-grained backup, remained ranges = 0: backoff exceeds the max backoff time 1h0m0s: [BR:Common:ErrUnknown]internal error"] 

checkpoint 的权限检查是一个 warn，倒不是影响备份失败的关键因素。只是影响备份断点的写入。

### 2024-11-27T11:28:18.000+0800 [REDACTED_USER]

有一个奇怪的日志
2024-11-27 04:29:32.611673679 +0800 HKT m=+59371.080668975 write error: write length 504096808 exceeds maximum file size 314572800
 
是 OSS bucket 内部有什么限制只允许 300M 的文件大小吗？🤔
