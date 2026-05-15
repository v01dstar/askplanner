# GTOC-8126: PITR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-8126
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2026-01-02T09:56:55.307+0800
- Updated: 2026-01-13T20:47:42.821+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, observability-error-message
- Labels: Escalate-to-L3

## Symptom / Description Excerpt

We’d like the `br` tool to fail fast if the computed approximate disk space requirement exceeds what is currently available (or comes within a small percentage of what is available, whatever you think is better).

## Recent Comments Excerpt

### 2026-01-02T09:56:59.844+0800 [REDACTED_USER]

fail to find L2 assignee: please escalate to L3

### 2026-01-02T09:57:02.602+0800 [REDACTED_USER]

assign to 余峻岑([REDACTED_EMAIL])

### 2026-01-02T09:57:03.509+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b5a461023cca0c4eb96a27b343e6) by lark

### 2026-01-02T09:58:27.196+0800 [REDACTED_USER]

Background
This request is a follow-up to 
GTOC-8008 (PITR doesn’t clean up disk space)
, based on a real PITR failure.
In the reported case:
Cluster had 
12 TiKV nodes
, each with ~75–125 GB free space before PITR.
