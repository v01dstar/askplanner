# GTOC-7254: Restore failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7254
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2024-11-18T10:22:52.000+0800
- Updated: 2025-03-07T10:55:22.156+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: tikv-data-path
- Labels: N/A

## Symptom / Description Excerpt

This is not causing any issues currently. When I looked into the gold cluster [REDACTED_CLUSTER], there’s always a brief spike of tikv IO usage when checksumming starts. See the screenshot below. Notice how at \~03:05 PT, there’s a spike of IO up to almost 400 MBps.

Why is there this large, sudden spike of IO that quickly recedes and gradually tapers off? I know that we set `checksum_concurrency` to 2 because we’ve had issues with this field in other clusters, and it is set as such in the gold cluster as well.

I’m creating this ticket to ask preemptively (in case this spike in IO usage becomes a problem in the future) – is there a way to “smooth” out the IO usage such that there isn’t such a big spike in the beginning? It seems strange that it’d be so high in the beginning, but it’d be close to zero not long after the spike.

## Recent Comments Excerpt

### 2024-11-18T10:23:59.000+0800 [REDACTED_USER]

[REDACTED_MEDIA]

### 2024-11-18T11:47:08.000+0800 [REDACTED_USER]

notified (余峻岑([REDACTED_EMAIL]), ) by lark

### 2024-11-18T11:48:44.000+0800 [REDACTED_USER]

table level checksumming in backup/restore is not necessary. please see google doc 
https://docs.google.com/document/d/1oh5PIA02v1pA5KM7hNKKm3tODxpuTen_ejXSJnwMq3M/edit?tab=t.0.
ska customers like airbnb, paypay are turning off --checksum already.

### 2024-12-01T03:44:38.000+0800 [REDACTED_USER]

This ticket can be closed now. thanks.
