# GTOC-7484: Dumpling export parameter issue

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7484
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-03-22T03:48:38.487+0800
- Updated: 2025-04-11T11:05:30.177+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: Dumpling
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We are trying to export a table from the TiDB database using dumpling which is failing. 

Here’s the table details:

```
CREATE TABLE `content_discovery` (

  `content_id` varchar(128) NOT NULL,

  `outlinks` json DEFAULT NULL,

  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (`content_id`) /*T![clustered_index] CLUSTERED */,

  KEY `update_at_idx` (`updated_at`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin /*T![ttl] TTL=`updated_at` + INTERVAL 2592000 SECOND */ /*T![ttl] TTL_ENABLE='ON' */ /*T![ttl] TTL_JOB_INTERVAL='24h' */
```

Table Size: 3 TB

Error:   
We have already tried with different values for **“-r”**  
1, 20, 10000, 10000, 200000

## Recent Comments Excerpt

### 2025-03-24T14:49:42.436+0800 [REDACTED_USER]

Let’s further reduce the concurrency to 2 (by -t), or reduce the mem-quota-query to 4294967296 (4G) (by tidb-mem-quota-query), since tidb_server_memory_limit is set to 19GiB

### 2025-03-25T02:10:36.016+0800 [REDACTED_USER]

The job failed again

The issue is that the job cannot split into multiple subtasks utilizing the PK. This make a single query to consume all the resources. 
[REDACTED_MEDIA]
[REDACTED_MEDIA]
 

tiup dumpling -u root -P 4000 -h [REDACTED_ENV_NAME] -r 200000 -t 2    -o "s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]"      --filetype csv     --sql "SELECT    * FROM web_content_prod.content_discovery WHERE updated_at > NOW() - INTERVAL 30 DAY;" -F 156MiB --output-filename-template 'web_content_dev.content_discovery.{{.Index}}'     --params tidb_replica_read=learner,max_execution_time=0,tidb_distsql_scan_concurrency=5 --tidb-mem-quota-query=4589934592 --loglevel "debug"

### 2025-03-25T12:24:04.874+0800 [REDACTED_USER]

I noticed that -t would not take effect if specifying --sql.
So to dump a large table, we indeed need to specify --where and -T, which can split chunks.

### 2025-04-05T02:57:18.597+0800 [REDACTED_USER]

@[REDACTED_USER]
 

This allows the query to create multiple subtasks with range on PK.  Since we are running all these queries on a SINGLE TiDB node which ultimately going to consume all the resources or with lesser number of threads it will take forever to create the dump.

### 2025-04-11T11:05:30.177+0800 [REDACTED_USER]

@[REDACTED_USER]
 Can you please check on the latest comment?
