# Issue 59995: Restore fails with [BR:PD:ErrPDBatchScanRegion]

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/59995
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2025-03-11T01:28:13Z
- Updated: 2025-03-11T01:28:43Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB, TiKV, BR
- Categories: region-split-scatter
- Labels: component/br, may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5, severity/major, type/bug
- Affected versions: may-affects-6.1, may-affects-6.5, may-affects-7.1, may-affects-7.5, may-affects-8.1, may-affects-8.5

## Quick Match

- Title/error signature: `Restore fails with [BR:PD:ErrPDBatchScanRegion]`
- Search terms: BR; Restore; TiDB; TiKV; region-split-scatter

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]
use br restore data from v8.1.2 to master

<!-- a step by step guide for reproducing the bug. -->

### 2. [REDACTED_USER]
restore success 

### 3. [REDACTED_USER]

`[2025/03/10 11:57:02.732 +00:00] [WARN] [split.go:254] ["failed to scan region, retrying"] [error="region 15043270's endKey not equal to next region 19117209's startKey, endKey: 7480000000000000FFA75F728000000196FFB51F0A0000000000FA, startKey: 7480000000000000FFA75F728000000196FFB5383A0000000000FA, region epoch: conf_ver:101 version:24411  conf_ver:89 version:24411 : [BR:PD:ErrPDBatchScanRegion]batch scan region"] [regionLength=3101044]`

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
From

> Release Version: v8.1.2
> Edition: Community
> Git Commit Hash: a21402da4ab5b342d2bb4da5bff954eecc7a20e1
> Git Branch: heads/refs/tags/v8.1.2
> UTC Build Time: 2025-03-07 01:19:19
> GoVersion: go1.21.10
> Race Enabled: false
> Check Table Before Drop: false
> Store: tikv

TO

> Release Version: v9.0.0-alpha-381-g739a934
> Edition: Community
> Git Commit Hash: 739a934f631eb413ff3b150b0a7fc9db55eefcbd
> Git Branch: HEAD
> UTC Build Time: 2025-03-10 06:19:26
> GoVersion: go1.23.7
> Race Enabled: false
> Check Table Before Drop: false
> Store: tikv
