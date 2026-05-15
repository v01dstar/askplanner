# GTOC-7403: PITR gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7403
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-02-14T12:39:43.945+0800
- Updated: 2025-03-26T08:50:28.830+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR, PD, TiKV
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

**From customer**

3 different tidb clusters in 3 different prod locations had log backup fail with the following errors during PD leader change (from pd pod restart):

```
Detail BR log in /tmp/br.log.2025-02-12T20.27.06Z
● Total 1 Tasks.
> #1 <
                          name: [REDACTED_RESOURCE_NAME]
                        status: ○ ERROR
                         start: 2024-09-22 06:21:57.367 +0000
                           end: 2090-11-18 14:07:45.624 +0000
                       storage: azure://backup-data/log-manager/log-2024-09-22t06-21-35
                   speed(est.): 0.00 ops/s
            checkpoint[global]: 2025-02-12 19:49:35.527 +0000; gap=37m33s
          error[store=1664032]: KV:LogBackup:Etcd
error-happen-at[store=1664032]: 2025-02-12 19:52:54.84 +0000; gap=34m13s
  error-message[store=1664032]: Etcd meet error grpc request error: status: Unavailable, message: "error trying to connect: tcp connect error: Connection refused (os error 111)", details: [], metadata: MetadataMap { headers: {} }
```

2 had above error, 1 had the following error:

```
 error-message[store=1379001]: Etcd meet error grpc request error: status: Unavailable, message: "error trying to connect: dns error: failed to lookup address information: Name or service not known", details: [], metadata: MetadataMap
```

We had a disk replace combined with a regular binary rollout here. It looks like the 3 spare replicas (upscale) as part of disk replace started getting turned up concurrently with pd restarts. When pd leader changed [REDACTED_RESOURCE_NAME] (store id = `1664032` ) just turned up at around the same time and resulted in this issue somehow.

## Recent Comments Excerpt

### 2025-02-20T11:51:58.554+0800 [REDACTED_USER]

The log backup process has a finite retry limit (14s) – this is just a hypothesis.

The relevant code is in LazyEtcdClientInner::connect:
async fn connect(&mut self) -> Result<&EtcdStore> {
    let store = retry(|| {
        // For now, the interface of the `etcd_client` doesn't allow us to control
        // how channels are created when connecting, hence we cannot update the TLS config
        // at runtime. Currently, we manually check the clients each time we retrieve them.

### 2025-02-27T14:00:36.042+0800 [REDACTED_USER]

Customer [REDACTED_CUSTOMER]
[REDACTED_MEDIA]
[REDACTED_MEDIA]
[REDACTED_MEDIA]

### 2025-03-04T09:57:14.916+0800 [REDACTED_USER]

Did customer [REDACTED_CUSTOMER]
https://github.com/pingcap/tidb/issues/58031
 ?

or can they upload tidb advancer owner around 
02/12 19:54:29.160

### 2025-03-04T22:38:48.500+0800 [REDACTED_USER]

@[REDACTED_USER]
 
No update from customer, pushed again
[REDACTED_MEDIA]

### 2025-03-26T08:50:28.787+0800 [REDACTED_USER]

customer [REDACTED_CUSTOMER]
