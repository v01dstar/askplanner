# GTOC-7834: PITR storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7834
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2025-08-08T09:54:11.517+0800
- Updated: 2025-09-15T01:25:26.129+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Airbnb runs correctness tests for the PiTR restore, with the goal to validate the restores are consistent with a source. We’re using sync-diff tool to compare the databases, but observe performance and stability issues with the tool. One alternative we consider is to use `ADMIN CHECKSUM TABLE` command instead and compare CRCs of the tables.

Our understanding is that PingCAP relies on checksuming in internal testing as well.

Few questions:

1. Are there scenarios which are not covered by CHECKSUM TABLE command, but are covered by sync-diff? The goal is just to validate the equality, not to find specific rows which are inconsistent.
2. Are there known limitations of the `ADMIN CHECKSUM TABLE` command? Specifically, limits on the table size?
3. Is there a performance benefit in running multiple `ADMIN CHECKSUM TABLE` commands in parallel, with the goal to better leverage CPU allocation on TiKV?
4. One additional question: at the Airbnb / PingCAP sync it was mentioned that PingCAP also uses a separate “not opensource” table checksuming mechanism. Can you sched more details on this? Is it addressing some limitations / issues of the `ADMIN CHECKSUM TABLE` command?

## Recent Comments Excerpt

### 2025-08-08T09:54:24.846+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b4661c3cff7740f270b85fd2e81b) by lark

### 2025-08-08T15:15:28.382+0800 [REDACTED_USER]

Are there scenarios which are not covered by CHECKSUM TABLE command, but are covered by sync-diff? The goal is just to validate the equality, not to find specific rows which are inconsistent.
It seems not. 
CHECKSUM TABLE
 should always be more strict than 
sync-diff
. 
CHECKSUM TABLE
 compares data equality bytewise, ignoring logical equality like collation or near floating numbers.

### 2025-09-11T15:58:58.474+0800 [REDACTED_USER]

The questions are answered and it seems there isn’t further questions from the customer. Close it due to inactive. Feel free to reopen it or create new tickets when you have any new questions about this topic.
