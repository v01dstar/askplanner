# GTOC-6971: Log backup checkpoint lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6971
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-06-19T00:10:13.000+0800
- Updated: 2025-03-06T18:10:26.161+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

All incrementa backups are failing for few clusters   
[https://br.noah.fkcloud.in/k8s/configs/[REDACTED_ENV_NAME]/rpos/](https://br.noah.fkcloud.in/k8s/configs/[REDACTED_ENV_NAME]/rpos/)  
[https://br.noah.fkcloud.in/k8s/configs/[REDACTED_ENV_NAME]/rpos/](https://br.noah.fkcloud.in/k8s/configs/[REDACTED_ENV_NAME]/rpos/)

## Recent Comments Excerpt

### 2024-06-26T15:25:10.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Jun/24 7:25 AM

Hi @[REDACTED_USER] ,
Has this cluster ever upgraded its resources? Is the problem solved?
https://github.com/pingcap/tidb/pull/54100
  

This PR optimises this issue. This PR will be included in future releases. Maybe v7.5.3

### 2024-06-27T19:27:54.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 27/Jun/24 11:27 AM

Hi Yilong ,

We have upgraded the cluster from v6.5.3 to v7.5.1 , since then it is failing.

### 2024-06-27T19:43:29.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 27/Jun/24 11:43 AM

When is v7.5.3 expected to release ?

### 2024-07-01T09:09:35.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 01/Jul/24 1:09 AM

Hi@[REDACTED_USER] ,
You can try to increase the bandwidth of the BR machine.(The upgrade means bandwidth)
There is no confirmed release date for v7.5.3 now. I will notify you as soon as I have a confirmed time.

### 2024-07-16T13:13:37.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 16/Jul/24 5:13 AM

Hi @[REDACTED_USER] 

1. Did you get chance to increase bandwidth of the BR machine and test it out.

2. As of now we tentatively we plan to release v7.5.3 on 31st July.
