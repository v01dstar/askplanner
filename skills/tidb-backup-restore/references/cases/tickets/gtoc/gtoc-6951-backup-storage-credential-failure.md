# GTOC-6951: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6951
- Status: Todo
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-06-06T09:39:26.000+0800
- Updated: 2025-03-07T10:55:28.121+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], backup-failure, storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

We are just started to test snapshot backup on our test cluster (Cluster [REDACTED_CLUSTER]: 9 tikvs. 3TB total data). The backup doesn’t seem to making much progress after 13hrs. 

```
[progress.go:160] [progress] [step="Full Backup"] [progress=0.00%] [count="0 / 177"] [speed="? p/s"] [elapsed=13h10m0s] [remaining=?]
```

Please find attached the screenshot of backup metrics, backup pod logs, cluster spec metrics.

## Recent Comments Excerpt

### 2024-06-06T09:39:34.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Jun/24 1:38 AM
Escalate to L3 Information 
[REDACTED_TICKET_ID]

This ticket is reported by 
PingCAP Employee
: Naman Gupta

### 2024-06-06T09:39:41.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 06/Jun/24 1:39 AM

directly open ticket for BR team access based on meeting with airbnb

### 2024-06-11T07:11:31.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 10/Jun/24 11:11 PM

Patched 
https://github.com/tikv/tikv/pull/17099/files
 . Still got an error: 
[2024/06/10 23:07:22.800 +00:00] [WARN] [util.rs:114] ["aws request meet error."] [uuid=[REDACTED_UUID] [context=upload_small_file] [retry?=true] [err="Error during dispatch: error trying to connect: dns error: failed to lookup address information: Name or service not known"] [thread_id=246] [2024/06/10 23:07:25.090 +00:00] [INFO] [util.rs:66] ["hyper connecting to uri"] [req=
https://s3.us-east-1.amazonaws.com/

### 2024-06-15T03:20:30.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 14/Jun/24 7:20 PM

Copy Slack Final Investigation Result:
failure to run curl:
sh-5.1$ curl https://s3.us-east-1.amazonaws.com/ 
curl: (6) Could not resolve host: s3.us-east-1.amazonaws.com
Pod resolve.conf:
sh-5.1$  cat /etc/resolv.conf

### 2024-06-18T04:56:44.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 17/Jun/24 8:56 PM

Yeah. We can close the ticket for now.
