# GTOC-7475: Operator PITR CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7475
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-03-19T10:39:14.044+0800
- Updated: 2025-04-18T09:38:50.643+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

This is Atlassian’s 8M table project. The current test cluster has 100,000 schemas. Each schema has 80 tables. Each table only have a few rows. Total 8M tables.

Backup takes 2.5 hour. However restore takes 6h. Atlassian has an RTO of 4h.

## Recent Comments Excerpt

### 2025-03-19T10:39:28.051+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), om_8ebad9bb0d3b8fbf6e075adb761f6469) by lark

### 2025-03-19T10:46:10.377+0800 [REDACTED_USER]

[REDACTED_MEDIA]
This is time break down:
50mins for restore create all dbs (without tables)
2:30mins to create all tables in previously created dbs
“update metas” took 2:40mins
6 hours total ( log backup off , checksums off)

### 2025-03-19T13:45:47.120+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_2b62eae03a7f5a443b48d08a40f0a942) by lark

### 2025-03-19T23:09:09.234+0800 [REDACTED_USER]

UPDATE: 
The CREATE SCHEMA and CREATE TABLE ddls are already executed in batch and in parallel. According to the devs this seems not improvable.
The unconditional “update metas” was introduced by 
https://github.com/pingcap/tidb/pull/51535
, which essentially boils down to running 
REPLACE INTO mysql.stats_meta
 9 million times. As this is a DML-only operation, if it is possible to change it to SST ingestion (via DXF?) it should be much faster.
an alternative solution is add a switch to disable updating stats entirely.
