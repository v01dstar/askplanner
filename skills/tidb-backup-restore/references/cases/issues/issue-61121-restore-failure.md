# Issue 61121: Restore failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/61121
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-05-15T04:47:58Z
- Updated: 2025-05-24T04:21:15Z
- Closed: 2025-05-24T04:21:15Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, BR, Storage, PD
- Categories: restore-failure, storage-access
- Labels: affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-8.5

## Quick Match

- Title/error signature: `Restore failure`
- Search terms: BR; PD; Restore; Storage; TiDB; restore-failure; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
1、run br restore with keyspace and tls

### 2. [REDACTED_USER]
br restore can succeed

### 3. [REDACTED_USER]
br restore failed with keyspace and tls

`[2025/05/15 03:13:50.032 +00:00] [WARN] [pd_service_discovery.go:843] ["[pd] failed to get cluster id"] [url=http://db-a576e8f4-pd.tidbe1490e6244bbafa2619534f1a8c5969a-0-0:2379] [error="[PD:client:ErrClientGetMember]error:rpc error: code = Unavailable desc = connection error: desc = \"error reading server preface: read tcp [REDACTED_IP]:37178->[REDACTED_IP]:2379: read: connection reset by peer\" target:db-a576e8f4-pd.tidbe1490e6244bbafa2619534f1a8c5969a-0-0:2379 status:TRANSIENT_FAILURE: error:rpc error: code = Unavailable desc = connection error: desc = \"error reading server preface: read tcp [REDACTED_IP]:37178->[REDACTED_IP]:2379: read: connection reset by peer\" target:db-a576e8f4-pd.tidbe1490e6244bbafa2619534f1a8c5969a-0-0:2379 status:TRANSIENT_FAILURE"]`

### 4. [REDACTED_USER]
sh-5.1# ./br -V
Release Version: v8.5.1
Git Commit Hash: fea86c8e35ad4a86a5e1160701f99493c2ee547c
Git Branch: HEAD
Go Version: go1.23.4
UTC Build Time: 2025-01-16 07:41:21
Race Enabled: false
