# GTOC-6422: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6422
- Status: Canceled
- Resolution: Cancel
- Priority: P2
- Issue type: Incident
- Created: 2023-09-09T05:59:49.000+0800
- Updated: 2024-07-02T11:58:52.000+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

## Description

 

We are testing EBS BR. And just saw that some volumes don’t have the necessary tags. The expected tags were requested in doc - \[!https://developers.google.com/drive/images/drive_icon.png!https://docs.google.com/document/d/1QCPdpYkgg9kkQwpr2RNECLNX5Ki0_0H8DYaTvpmtddg/edit\] - Connect your Google account . Also listed below:

* [ebs.csi.aws.com/cluster=true](http://ebs.csi.aws.com/cluster=true)

* CSIVolumeName=<pvc_name> ex: pvc-daff-ddfasdfs-dafdsaf-dafsdf-asdfa

* [kubernetes.io/created-for/pvc/name=](http://kubernetes.io/created-for/pvc/name=)<tikv_pod_name> Ex: [REDACTED_ENV_NAME]

Example volume - vol-09ae4cc4057556d64. Screenshot attached.

## Recent Comments Excerpt

### 2023-09-09T10:24:09.000+0800 [REDACTED_USER]

@[REDACTED_USER]
 What do you want, create the tags for TiKV EBS ?
 
p.s. There is no screenshot attached.

### 2023-09-09T14:23:59.000+0800 [REDACTED_USER]

This issue is escalated ticket from AirBnB for the EBS snapshot BR feature. 
@[REDACTED_USER]
  It seems some tags missing is caused by failure of the restore.  Can you please ask customer [REDACTED_CUSTOMER]

1. status of the volume restore
2. log of the operator and restore pods
