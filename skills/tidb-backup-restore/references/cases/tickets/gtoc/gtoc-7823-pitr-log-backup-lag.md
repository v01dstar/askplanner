# GTOC-7823: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7823
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-08-03T23:02:38.168+0800
- Updated: 2025-08-04T11:22:27.065+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

tikv log backup lag spike with one single tikv 100% cpu

## Recent Comments Excerpt

### 2025-08-03T23:02:53.090+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b47c3ef7944b00f1ff795831f455) by lark

### 2025-08-03T23:03:56.535+0800 [REDACTED_USER]

This is a S1 request. 
@[REDACTED_USER]
 and I joined the bridge and collected CPU profiling, tikv logs and metrics. The issue was recovered by itself in about 30 minutes. Open On-call to root cause the problem.

### 2025-08-03T23:05:19.248+0800 [REDACTED_USER]

tikv cpu profiling at Aug 3 7:48AM PST
