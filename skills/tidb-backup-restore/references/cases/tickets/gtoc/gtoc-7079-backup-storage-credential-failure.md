# GTOC-7079: Backup storage credential failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7079
- Status: UNDER INVESTIGATION
- Resolution: N/A
- Priority: P2
- Issue type: Incident
- Created: 2024-08-15T20:42:12.000+0800
- Updated: 2025-03-06T18:03:34.068+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, observability-error-message
- Labels: change-p2

## Symptom / Description Excerpt

Hello, we are having ebs backup failure for the past several days in production.

Impact: We saw continuous ebs backup failures since 5d ago. This caused no success backup in the past several days and SLA violation for the [REDACTED_ENV_NAME] cluster, which is the major tidb cluster with 360TB data.

Symptom: Volume backups failed due to backup member in one region, 1e, failed. [!https://gist.github.com/favicon.ico!gist:fc246ff3eddc211765d4b68db6fd5682](https://gist.github.com/olivia-chen-github/fc246ff3eddc211765d4b68db6fd5682)

Investigation: We found there are multiple createSnapshot requests for one single tikv/volume within very short period of time (1m) and the requests got throttled from aws side and caused the following volumebackup failures due to the rate limit. ([create snapshots events link](https://gist.github.com/olivia-chen-github/1fabd99dd0aa099ab6b619be47597856))

To better understand this issue, can you pls help us understand what triggered the snapshot creation against one tikv volume repeatedly within one backup process? and how should we avoid it? Thanks.

## Recent Comments Excerpt

### 2024-08-22T15:39:16.000+0800 [REDACTED_USER]

A patch that fixed this perhaps looks like:
diff --git a/br/pkg/aws/ebs.go b/br/pkg/aws/ebs.go
index fc4169e6fb..99e419b229 100644
--- a/br/pkg/aws/ebs.go
+++ b/br/pkg/aws/ebs.go
@@ -11,6 +11,8 @@ import (
 
 	"github.com/aws/aws-sdk-go/aws"

### 2024-08-22T16:02:26.000+0800 [REDACTED_USER]

Also, after checking the code, I'm afraid that in fact we are failed due to *
we have exceeded the retry times
* but not we have sent too many requests. That is, it seems API quota exceeded errors can also be retryed:
// aws-sdk-go/aws/client/default_retryer.go
// ShouldRetry returns true if the request should be retried.
func (d DefaultRetryer) ShouldRetry(r *request.Request) bool {

	// ShouldRetry returns false if number of max retries is 0.

### 2024-08-24T04:27:16.000+0800 [REDACTED_USER]

From Airbnb: Why do we need a parameter, though? My understanding is that 5 seconds is default for EBS per volume. So tidb-opertor default retry tuning should be the way it won’t exceeds the quota. What do I miss?  Also could we please log each retried error as well?

### 2024-08-26T18:18:28.000+0800 [REDACTED_USER]

Yes you are right, we don't need an extra argument. My point is that the failure wasn't caused by we have exceeded the quota but we have exceeded the max retry time. Reducing the retry time to make it won't exceed the quota makes sense but it may not be helpful in our scenario as the retry procedure fails faster.
So I think increase the retry back off time will be relatively helpful. Also I'm going to adding some logs when encountered error. (As the patch provided before) I will format a PR soon by that patch, but perhaps it will be tricky to test it (Aha, AWS services not always returns 5xx status code, also when we mocking go-sdk we will bypass the retry logic as it is in our client...).

### 2024-08-26T18:34:55.000+0800 [REDACTED_USER]

A draft pr here: 
https://github.com/pingcap/tidb/pull/55667/files
