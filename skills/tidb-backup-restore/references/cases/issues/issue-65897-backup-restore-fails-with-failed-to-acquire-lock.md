# Issue 65897: Backup/Restore fails with failed to acquire lock

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/65897
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2026-01-29T03:11:27Z
- Updated: 2026-01-29T20:05:21Z
- Closed: 2026-01-29T20:05:21Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Classic
- Operation: Backup/Restore
- Components: TiDB, Operator, BR, Storage, PD
- Categories: storage-access, observability-diagnosis
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Backup/Restore fails with failed to acquire lock`
- Search terms: BR; Backup/Restore; Operator; PD; Storage; TiDB; observability-diagnosis; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run cmd
 {"command": " /br  log \"truncate\" \"--storage\" \"s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]\" \"--pd\" \"http://tc-pd.xxx:2379\" \"--until\" \"[REDACTED_LONG_ID]\"", "timeout": "3h", "resource name": "br"}

### 2. [REDACTED_USER]
br  log truncate can succeed

### 3. [REDACTED_USER]
br  log truncate failed 
2026-01-27T12:41:39.309Z        INFO        8028647        host/host.go:51        Execute command        {"command": " /br  log \"truncate\" \"--storage\" \"s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]\" \"--pd\" \"http://tc-pd.xxx:2379\" \"--until\" \"[REDACTED_LONG_ID]\"", "timeout": "3h", "resource name": "br"}
2026-01-27T12:41:39.311Z        INFO        k8s/client.go:271        it should be noted that a long-running command will not be interrupted even the use case has ended. For more information, please refer to https://github.com/pingcap/test-infra/discussions/129
Detail BR log in /tmp/br.log.2026-01-27T12.41.39Z 
Error: failed to acquire lock on 'truncating.lock': failed to read existed lock file truncating.lock: failed to read s3 file, file info: input.bucket='tmp', input.key='ha-[REDACTED_ENV_NAME]/truncating.lock': operation error S3: GetObject, https response error StatusCode: 404, RequestID: 188E96F8E78C2D30, HostID: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, NoSuchKey: : during initial check: operation error S3: ListObjects, https response error StatusCode: 400, RequestID: , HostID: , api error XMinioInvalidResourceName: Resource name contains bad components such as ".." or ".".
2026-01-27T12:41:39.385Z        INFO        8028647        host/host.go:58        Execute command error        {"command": " /br  log \"truncate\" \"--storage\" \"s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]\" \"--pd\" \"http://tc-pd.xxx:2379\" \"--until\" \"[REDACTED_LONG_ID]\"", "exit code": 1, "stdout": "", "stderr": "Detail BR log in /tmp/br.log.2026-01-27T12.41.39Z \nError: failed to acquire lock on 'truncating.lock': failed to read existed lock file truncating.lock: failed to read s3 file, file info: input.bucket='tmp', input.key='ha-[REDACTED_ENV_NAME]/truncating.lock': operation error S3: GetObject, https response error StatusCode: 404, RequestID: 188E96F8E78C2D30, HostID: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855, NoSuchKey: : during initial check: operation error S3: ListObjects, https response error StatusCode: 400, RequestID: , HostID: , api error XMinioInvalidResourceName: Resource name contains bad components such as \"..\" or \".\".\n", "error": "command terminated with exit code 1"}
2026-01-27T12:41:39.385Z        INFO        8028647        host/host.go:62        Execute command finished        {"command": " /br  log \"truncate\" \"--storage\" \"s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]\" \"--pd\" \"http://tc-pd.xxx:2379\" \"--until\" \"[REDACTED_LONG_ID]\"", "execute duration": "76.386435ms"}
2026-01-27T12:41:39.385Z        ERROR        8028647        host/br.go:255        BR log failed

### 4. [REDACTED_USER]
./tidb-server -V
 Release Version: v9.0.0-beta.2.pre-1122-g5da5f2a
Edition: Community
Git Commit Hash: 5da5f2a4fd8e8a6235fc452b2c211b437cbec86a
Git Branch: HEAD
UTC Build Time: 2026-01-26 16:06:02
GoVersion: go1.25.6
Race Enabled: false
Check Table Before Drop: false
Store: unistore
Kernel Type: Classic
2026-01-27T18:13:44.870+0800	INFO	k8s/client.go:141	it should be noted that a long-running command will not be interrupted even the use case has ended. For more information, please refer to https://github.com/pingcap/test-infra/discussions/129
