# GTOC-6534: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-6534
- Status: CAN'T REPRODUCE
- Resolution: Cannot Reproduce
- Priority: P2
- Issue type: Incident
- Created: 2023-11-29T03:54:58.000+0800
- Updated: 2025-05-29T11:01:01.019+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: operator-cr
- Labels: N/A

## Symptom / Description Excerpt

Seems like even in async mode, restore blocks on warmup to complete. [Code](https://github.com/pingcap/tidb-operator/blob/master/pkg/fedvolumebackup/restore/restore_manager.go#L159-L162). Can you clarify the motivation behind 

[VolumeRestoreCR](https://gist.github.com/nkg-/a146d00efbb8e2b8c4d0474a80fd97c7). [RestoreCR](https://gist.github.com/nkg-/ea22642cd7600f947fe7fad2471b4ab6). In this case, DataRestore finished a full 2hrs before warmup finished, so Restore could have finished 2hrs earlier as well. 

If no solid reason, we would request removing that wai.t

## Recent Comments Excerpt

### 2023-11-29T03:54:59.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 26/Nov/23 9:45 PM

Hi [REDACTED_USER], thanks for contacting PingCAP support, we are checking with BR team on this, and will provide update later.

### 2023-12-14T10:21:08.000+0800 [REDACTED_USER]

commented by [REDACTED_USER] - 14/Dec/23 2:21 AM

Closing. Not an issue.
