# GTOC-7157: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7157
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P4
- Issue type: Incident
- Created: 2024-09-24T13:05:59.000+0800
- Updated: 2025-03-06T18:01:18.292+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: TiDB Operator
- Categories: operator-cr, performance-resource
- Labels: N/A

## Symptom / Description Excerpt

Atlassian has a requirement to use internal docker images. I need to replace the pingcap/br:v8.2.0 image used by Backup/BackupSchedule jobs (with a copy that we maintain). I browsed the tidb operator code but couldn't figure out where this was configured. Could you please help me figure out how to override this image?  
   
should we change the below code to setup Backup and Restore resources? \* [https://github.com/pingcap/tidb-operator/blob/master/examples/advanced/backup.yaml#L207](https://github.com/pingcap/tidb-operator/blob/master/examples/advanced/backup.yaml#L207)

* [https://github.com/pingcap/tidb-operator/blob/master/examples/advanced/restore.yaml#L206](https://github.com/pingcap/tidb-operator/blob/master/examples/advanced/restore.yaml#L206)

## Recent Comments Excerpt

### 2024-09-24T13:06:09.000+0800 [REDACTED_USER]

notified (张学程([REDACTED_EMAIL]), ) by lark

### 2024-09-24T13:20:20.000+0800 [REDACTED_USER]

just set the `toolImage` of Backup/Restore CR to your internal docker image
