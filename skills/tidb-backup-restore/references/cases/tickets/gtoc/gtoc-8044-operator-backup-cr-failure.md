# GTOC-8044: Operator backup CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8044
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-11-19T05:58:08.758+0800
- Updated: 2025-11-19T11:46:12.801+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB Lightning
- Categories: operator-cr, compatibility-upgrade
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

**Mitigation Recommendation**

* For package \[<custom data-type="smartlink" data-id="id-0">http://golang.org/x/crypto</custom>  v0.28.0\]: Upgrade to one of the following versions: v0.35.0
* For package \[<custom data-type="smartlink" data-id="id-1">http://golang.org/x/oauth2</custom>  v0.23.0\]: Upgrade to one of the following versions: v0.27.0

**Vulnerability Description**  
The CrowdStrike scanner has found a vulnerability on a container you own. Please review the mitigation recommendation(s) above to resolve it before the due date.

Discovered at Image Layer Index: 7  
Image Layer Command: COPY /tidb-lightning-ctl /tidb-lightning-ctl # buildkit  
Vulnerable Package: <custom data-type="smartlink" data-id="id-2">http://golang.org/x/crypto</custom>  v0.28.0

Vulnerable Package: <custom data-type="smartlink" data-id="id-3">http://golang.org/x/oauth2</custom>  v0.23.0

## Recent Comments Excerpt

### 2025-11-19T05:58:13.682+0800 [REDACTED_USER]

fail to find L2 assignee: please escalate to L3

### 2025-11-19T05:58:16.322+0800 [REDACTED_USER]

assign to 居佳佳([REDACTED_EMAIL])

### 2025-11-19T05:58:18.523+0800 [REDACTED_USER]

notified (居佳佳([REDACTED_EMAIL]), om_x100b5efaf15ad0a80f121aefcb029c4) by lark

### 2025-11-19T06:03:14.902+0800 [REDACTED_USER]

内部小结：oauth2 升级需求
客户通过 CrowdStrike 报告指出 TiDB 及 TiDB Operator 中使用的 
golang.org/x/oauth2
 存在安全漏洞，要求升级到 
v0.27.0
。
根据当前 TiDB 仓库（链接见下）：
https://github.com/pingcap/tidb/blob/58fc49e5bb33f94216fa3edf74df7603468a0b26/go.mod#L135

### 2025-11-19T11:46:12.644+0800 [REDACTED_USER]

will be fixed in 8.5, see 
https://github.com/pingcap/tidb/pull/64552
