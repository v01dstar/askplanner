# Issue 57066: Backup gets stuck

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/57066
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-11-01T07:17:19Z
- Updated: 2024-11-05T03:12:27Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, BR, PD
- Categories: backup-failure, observability-diagnosis
- Labels: affects-8.5, component/br, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, severity/major, type/bug
- Affected versions: affects-8.5, may-affects-5.4, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1

## Quick Match

- Title/error signature: `Backup gets stuck`
- Search terms: BR; Backup; PD; TiDB; backup-failure; observability-diagnosis

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br backup
2、injection pd leader io delay 

### 2. [REDACTED_USER]
br backup succeed

### 3. [REDACTED_USER]
br backup failed
[br.log.2024-10-31T04.27.51Z.zip]([REDACTED_ATTACHMENT_URL])

Detail BR log in /tmp/br.log.2024-10-31T04.27.51Z 
{level:warn,ts:2024-10-31T04:28:54.823024Z,logger:etcd-client,caller:v3@v3.5.12/retry_interceptor.go:62,msg:retrying of unary invoker failed,target:etcd-endpoints://0xc0022a08c0/tc-pd.[REDACTED_RESOURCE_NAME]:2379,attempt:0,error:rpc error: code = Unavailable desc = etcdserver: leader changed}
{level:warn,ts:2024-10-31T04:28:54.966914Z,logger:etcd-client,caller:v3@v3.5.12/retry_interceptor.go:62,msg:retrying of unary invoker failed,target:etcd-endpoints://0xc0022a08c0/tc-pd.[REDACTED_RESOURCE_NAME]:237"

### 4. [REDACTED_USER]
./br -V
 Release Version: v8.5.0-alpha-19-g49c3eba4b0
Git Commit Hash: 49c3eba4b061a3098e0095dfd7803b955948ce94
Git Branch: HEAD
Go Version: go1.23.2
UTC Build Time: 2024-10-30 15:51:01
Race Enabled: false
