# GTOC-7657: Restore storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7657
- Status: PENDING FOR SUPPORT
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2025-06-06T02:19:48.797+0800
- Updated: 2025-06-11T10:51:18.123+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Wenqi and I had a meeting with Customer [REDACTED_CUSTOMER]is configuration and this is very first they are trying to use it.

## Recent Comments Excerpt

### 2025-06-06T02:28:43.648+0800 [REDACTED_USER]

Description
The current implementation of backup/restore sets the option force-path-style to true, which breaks on S3 with FIPS regions as the endpoints must use virtual-host-style. Additionally, the older path style is also being deprecated and should not be the default for AWS.
see: 
https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#virtual-hosted-style-access
We need the br and related tooling that interacts with S3 to use virtual-host-style requests and use the fips endpoints (its ok to manually specify the endpoint)
ideally the system just respected the 
AWS_USE_FIPS_ENDPOINT
 env variable, but we found that not to be the case.

### 2025-06-06T08:50:56.859+0800 [REDACTED_USER]

Additional details shared by Customer : 
[REDACTED_CUSTOMER]/limitations, one that we hardcode the force-path-style to true by default, or at least for aws provider. And there is an issue once you try to workaround that by setting the endpoints etc.
 
After a bit of debugging with the tidb br client, I think that in the s3.go file that when you set the s3.endpoint it will set the endpoint for all aws sdk calls, this includes the STS endpoint which is not correct. It is trying to make an IAM STS call to the s3 endpoint which is why the format cannot be understood and I assumed it was related to the s3 call which was incorrect.
https://github.com/pingcap/tidb/blob/master/br/pkg/storage/s3.go#L355
The qs.Endpoint should instead be set just for the s3 client as per
https://github.com/pingcap/tidb/blob/master/br/pkg/storage/s3.go#L394

### 2025-06-06T10:17:49.849+0800 [REDACTED_USER]

This ticket wasn’t included all recent questions, so I’m copying it here for clarity:
Q1: The ticket has also been updated with some information on the endpoint handling which is not correct, as if specified, it also updates the STS endpoint—which makes no sense.
Yes, that’s the issue. When using a global AWS config to set the endpoint, it overrides all endpoints—including STS. If you are using assumeRole to grant permission, it will not work. This is as same as  
aws/aws-sdk-go#3972
.
We encountered this early on and have a draft PR to address it: 
pingcap/tidb#60319
.

### 2025-06-07T02:27:16.065+0800 [REDACTED_USER]

Update from Customer : 
[REDACTED_CUSTOMER]g in s3 options in the backupschedule spec did not make it to the br cli call, has there been any investigation into the bugs on the tidb-operator side?

### 2025-06-11T10:51:18.123+0800 [REDACTED_USER]

Does customer [REDACTED_CUSTOMER]configuration in both operator and br kernal can solve this case?
