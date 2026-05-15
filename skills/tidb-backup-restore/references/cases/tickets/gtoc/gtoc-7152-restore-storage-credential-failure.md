# GTOC-7152: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7152
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-09-22T01:25:59.000+0800
- Updated: 2025-03-06T18:01:27.198+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, performance-resource, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

The customer [REDACTED_CUSTOMER]e database, consistently failing at 37%. The log indicated a possible network or permission issue; however, the customer [REDACTED_CUSTOMER] not the underlying problem.

Error: Cannot read s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]

More details on:  [APID-10890](https://pingcap-ticket.atlassian.net/browse/APID-10890)

## Recent Comments Excerpt

### 2024-09-23T11:58:25.000+0800 [REDACTED_USER]

there're some background I didn't provided, that're something below:

1. the network is OK, and 
"BR did always dided at 37%".
[REDACTED_MEDIA]
 
2. Permission is OK. Customer [REDACTED_CUSTOMER](though, I didn't tell customer [REDACTED_CUSTOMER]
[REDACTED_MEDIA]

### 2024-09-23T12:03:34.000+0800 [REDACTED_USER]

I don't if someone familiar with S3 about this ERROR "
Request entity too large: limit is
 
3145728
{*}{*}".
IMO, this one could be the key to resolve this one.

### 2024-09-23T12:21:01.000+0800 [REDACTED_USER]

Agreed. Let's request the customer [REDACTED_CUSTOMER]'s origin and confirm whether they've made any recent configuration changes.

### 2024-09-23T15:58:44.000+0800 [REDACTED_USER]

Key log info in TiKV side:
tikv log[2024/09/23 11:59:26.002 +07:00] [WARN] [util.rs:90] ["aws request meet error."] [uuid=[REDACTED_UUID] [context=get_cred_on_premise] [retry?=true] [err="Couldn't find AWS credentials in environment, credentials file, or IAM role;No (or empty) AWS_ACCESS_KEY_ID in environment;Couldn't stat credentials file: [ \"/root/.aws/credentials\" ]. Non existant, or no permission.;Could not get request from environment: Neither environment variable 'AWS_CONTAINER_CREDENTIALS_FULL_URI' nor 'AWS_CONTAINER_CREDENTIALS_RELATIVE_URI' is set;EOF while parsing a value at line 1 column 0"]
Root Cause:
br can’t support AWS IMDSv2 in v6.5.

### 2024-09-23T16:07:17.000+0800 [REDACTED_USER]

let customer [REDACTED_CUSTOMER]
[REDACTED_MEDIA]
