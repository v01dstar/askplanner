# GTOC-7538: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7538
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P3
- Issue type: Incident
- Created: 2025-04-22T05:16:41.785+0800
- Updated: 2025-05-12T18:55:51.151+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi,

We had a few instances today where the Log Backup was automatically paused on three different clusters. We had a Node Pool Rotation in progress, which was restarting “tidb” pods one by one. The log backup pauses seem to align with a tidb pod restart.

In case it matters, this was happening in AWS in the “us-east-1” region.

Could you please help us investigate this further? I will attach some logs, graphs to this ticket. Please let us know if you need any more information.

Thank you

## Recent Comments Excerpt

### 2025-04-22T05:16:59.016+0800 [REDACTED_USER]

notified (张博康([REDACTED_EMAIL]), om_x100b4f5f1268d9380f26294abe53f05) by lark

### 2025-04-22T05:17:54.737+0800 [REDACTED_USER]

看起来像是遇到了 
https://github.com/pingcap/tidb/issues/58031
[REDACTED_MEDIA]
但是从客户已经提供的 logs 来看，搜不到 checkpoint lag is too large
而且，tidb，tikv 日志 里 log backup 也没有任何的 ERROR 和 WARN

### 2025-04-22T11:26:51.314+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), om_x100b4f448965e8600f11a960926f726) by lark

### 2025-04-22T12:27:44.050+0800 [REDACTED_USER]

I think #58031 is still suspected… Because:
There isn’t a fatal error happen in TiKV side accroding to the metrics.
[REDACTED_MEDIA]
tidb-3
 became owner at 
[REDACTED_RESOURCE_NAME],2025/04/18 16:17:32.627
, the log entry is “begin running daemon”.
It was restarted around
