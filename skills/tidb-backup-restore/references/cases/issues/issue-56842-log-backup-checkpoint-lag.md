# Issue 56842: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/56842
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2024-10-25T09:50:28Z
- Updated: 2024-11-11T09:03:08Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR, PD
- Categories: checkpoint-retry, observability-diagnosis
- Labels: component/br, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; PD; Restore; TiDB; TiKV; checkpoint-retry; observability-diagnosis

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

1. run log pause

### 2. [REDACTED_USER]
1. the global checkpoint will not change until running log resume

### 3. [REDACTED_USER]
1. After br log pausing, the global checkpoint is still moving forward
![Xgf7GbUP9m](https://user-images.githubusercontent.com/81375082/169221991-[REDACTED_UUID].jpg)
![RX8BjPNDtO](https://user-images.githubusercontent.com/81375082/169222010-[REDACTED_UUID].jpg)

After br pausing, the status is sended to the PD, but the changed status on PD is not watched by Tikv. This issue is may be related to the etcd.


### 4. [REDACTED_USER]
v6.1.0-alpha
