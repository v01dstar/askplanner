# GTOC-7967: PITR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7967
- Status: CAN'T REPRODUCE
- Resolution: Cannot Reproduce
- Priority: P0
- Issue type: Incident
- Created: 2025-10-15T01:24:16.754+0800
- Updated: 2025-10-15T01:37:04.175+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME]
- Labels: N/A

## Symptom / Description Excerpt

PITR restore is failing w/ weird error or passing and the db still doesn’t exist. It is also occasionally creating a restore lock issue that’s stopping snapshot restores.

## Recent Comments Excerpt

### 2025-10-15T01:24:21.134+0800 [REDACTED_USER]

fail to find L2 assignee: please escalate to L3

### 2025-10-15T01:26:23.184+0800 [REDACTED_USER]

this is duplicate of gtoc-7946. please close it.
