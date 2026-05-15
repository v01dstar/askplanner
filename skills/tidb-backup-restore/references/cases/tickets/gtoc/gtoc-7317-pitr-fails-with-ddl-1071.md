# GTOC-7317: PITR fails with [ddl:1071]

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7317
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2024-12-20T09:06:17.000+0800
- Updated: 2025-03-07T10:55:10.686+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

PITR error, error message is:

Error: failed to repair ingest index: \[ddl:1071\]Specified key was too long (8200 bytes); max key length is 3072 bytes

Check tidb config and max-index-length is correct set. Also customer [REDACTED_CUSTOMER]

[REDACTED_MEDIA]
Does this mean pitr does not take tidb config max-index-length?

## Recent Comments Excerpt

### 2024-12-20T09:06:38.000+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), ) by lark

### 2024-12-20T09:07:23.000+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2024-12-20T09:43:00.000+0800 [REDACTED_USER]

Error happened with this DDL:
ALTER TABLE `test_db_06`.`MetadataMigrationSummary` 
ADD INDEX `idx_metadatamigrationsummary_trackid_name_sourceobjectname`(`TrackingId`,`Name`,`SourceObjectName`) 
USING BTREE VISIBLE
Stack trace
[2024/12/18 22:33:14.925 +00:00] [WARN] [session.go:2150] ["run statement failed"] 
[schemaVersion=66203] 
[error="[ddl:1071]Specified key was too long (8200 bytes); max key length is 3072 bytes"]

### 2024-12-20T09:43:46.000+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), ) by lark

### 2024-12-25T15:23:19.000+0800 [REDACTED_USER]

This is a new bug: 
https://github.com/pingcap/tidb/issues/58430
Fixed by: 
https://github.com/pingcap/tidb/pull/58433
