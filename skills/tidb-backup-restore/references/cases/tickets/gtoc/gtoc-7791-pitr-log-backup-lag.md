# GTOC-7791: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7791
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-07-24T02:07:17.077+0800
- Updated: 2025-08-27T00:17:33.369+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hi [REDACTED_USER],

We’re working on restore correctness validation, and porting <custom data-type="smartlink" data-id="id-0">https://github.com/pingcap/tidb-operator/pull/6267</custom>  to the Airbnb infrastructure. I have several questions regarding the issue:

1. Can you explain, on a high level, the scenario under which dataloss event during restore would be triggered? I understand that unexpected TiKV restart would change the GC configuration, but why this might be a problem?
2. What is the easiest way for us to reproduce the dataloss? We need to a repro in order to confirm that Airbnb fix is robust / working as expected.
3. At Airbnb, we’re running TiDB clusters across three independent K8s clusters. At the same time, logical restore CR is created in one zone only. My understanding of the #6267 is that we need ensure that config maps of _all_ TiKV nodes in the cluster are updated during backup, is that correct?
4. Is there direct or indirect way to identify if dataloss event has occurred during the restore process?

We’re using 8.5.2 (version is not avaiable in the menu of versions below)

## Recent Comments Excerpt

### 2025-07-24T02:07:33.385+0800 [REDACTED_USER]

notified (钟瀚震([REDACTED_EMAIL]), om_x100b4726008e38980f1eca467185ce0) by lark

### 2025-07-25T11:44:32.242+0800 [REDACTED_USER]

Essentially restarting TiKV rolled the configuration 
gc.ratio-threshold
 back so making GC was enabled during PiTR, but PiTR requires GC was fully disabled. 

Say we have a bakcup of a key 
K
 with 3 versions: 
[K@t1 ⇒ "foo", K@t2 ⇒ "bar", K@t3 ⇒ <deleted>]

### 2025-07-25T12:17:27.939+0800 [REDACTED_USER]

Unfortunately, there is currently no straightforward way to directly detect whether a data loss event occurred during the restore process.

However, one 
indirect signal
 could be the 
overlap between TiKV restart times and the restore window
. If TiKV was restarted during the restore—and 
the required configuration was not explicitly set manullay(cross k8s)

### 2025-07-26T05:10:57.448+0800 [REDACTED_USER]

From Airbnb:  Thank you for the update, we better understand the issue now. I have two follow-up questions:
My understanding is that repro scenario #2 is non-deterministic. At least, I was not able to easily repro a similar pattern (write + delete + write). Is there a way for us to deterministically reproduce the issue? Perhaps, by setting some special GC configuration ?
Would --checksum=true BR flag reliably detect the dataloss event if one occurs?
