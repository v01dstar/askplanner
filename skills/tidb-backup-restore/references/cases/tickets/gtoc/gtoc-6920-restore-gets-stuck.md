# GTOC-6920: Restore gets stuck

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6920
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-05-14T12:57:46.000+0800
- Updated: 2025-03-06T18:11:51.025+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

Hello, we are testing 7.5.1 image and found one volumerestore stuck due to pd crashing in one data plane. The other 2 data planes works well and have tikv started. but the problematic data plane’s restore is invalid due to one local pd crash.

problematic pd log: <custom data-type="smartlink" data-id="id-0">https://gist.github.com/olivia-chen-github/002a8e5a0c04713895f0994a98f18ff4</custom>  in the log we saw the pd dns resolved and pd address valid. but it complained cant find the pd 

volumerestore cr: <custom data-type="smartlink" data-id="id-1">https://gist.github.com/olivia-chen-github/bd6881725c5db14a22d568ea1de4e0f5</custom> 

problematic restore cr: <custom data-type="smartlink" data-id="id-2">https://gist.github.com/olivia-chen-github/8e88608b59753f86813ad8807b22b298</custom> 

Could you pls help us understand this issue? thanks

## Recent Comments Excerpt

### 2024-05-21T00:58:05.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 20/May/24 4:57 PM

Please find the logs for the initial PD startup
[REDACTED_MEDIA]

### 2024-05-21T10:01:15.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 21/May/24 2:01 AM

Hi [REDACTED_USER], Olivia & Naman,
Hope you are well. I think the possible reason and workaround already specified in the loop on the 15th, May, could you please try, and let us know the result, thanks. 
Regards
Jiamin Li

### 2024-05-30T16:12:47.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/May/24 8:12 AM

The status of this ticket has been set to "Waiting For Customer" status with no update for 7 days. Please take a look.

### 2024-05-31T04:31:23.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 30/May/24 8:31 PM

Left a follow up message to Olivia, asking her to try the workaround, switch the status back to Waiting for Customer

### 2024-05-31T08:12:28.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 31/May/24 12:12 AM

@[REDACTED_USER], as discussed on Slack, since you have already tried the walkaround and able to resolve the pd restart issue, I will close this ticket and feel free to contact us if there is anything else needed, thanks.
