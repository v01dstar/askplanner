# GTOC-7193: Restore failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7193
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Customer [REDACTED_CUSTOMER]
- Created: 2024-10-14T17:14:46.000+0800
- Updated: 2025-05-28T16:58:22.161+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: restore-failure
- Labels: N/A

## Symptom / Description Excerpt

详细内容参考：[https://pingcap.feishu.cn/wiki/Qv9zwHENdizw8tkqJs0cph12nVf](https://pingcap.feishu.cn/wiki/Qv9zwHENdizw8tkqJs0cph12nVf)

## Recent Comments Excerpt

### 2024-10-14T17:14:57.000+0800 [REDACTED_USER]

notified (梁杨可欣([REDACTED_EMAIL]), ) by lark

### 2024-10-14T17:17:53.000+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), ) by lark

### 2024-10-15T12:34:30.000+0800 [REDACTED_USER]

由於 show global bindings 是讀取內存而非直接 query `mysql.bind_info` 表，BR restore 了物理表後沒有刷新 tidb-server 的緩存，所以 show 返回的不是底層寫的值
可以試試在 BR restore 之後執行 
ADMIN RELOAD BINDINGS
 去更新緩存
