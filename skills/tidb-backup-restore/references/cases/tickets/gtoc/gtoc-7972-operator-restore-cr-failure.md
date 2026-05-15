# GTOC-7972: Operator restore CR failure

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7972
- Status: Resolved
- Resolution: Done
- Priority: P2
- Issue type: Incident
- Created: 2025-10-17T09:33:37.364+0800
- Updated: 2025-10-27T17:39:12.239+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: Restore
- Components: BR
- Categories: operator-cr, compatibility-upgrade
- Labels: N/A

## Symptom / Description Excerpt

We’re getting a vulnerability report on

`package [golang.org/x/crypto v0.18.0]: Upgrade to one of the following versions: v0.31.0`

```
Discovered at Image Layer Index: 8
Image Layer Command: COPY /backup-tools/tidb-lightning-ctl /tidb-lightning-ctl # buildkit
Vulnerable Package: golang.org/x/crypto v0.18.0
```

But we can’t even find the image in any of our clusters. So we’re wondering if this is an ephemeral pod spawned by some operator process or something. Where can we find it?

## Recent Comments Excerpt

### 2025-10-17T09:33:44.570+0800 [REDACTED_USER]

assign to 陈青璟([REDACTED_EMAIL])

### 2025-10-17T10:53:58.544+0800 [REDACTED_USER]

notified (郭虎([REDACTED_EMAIL]), om_x100b402eb298f5300f1b045cab2e323) by lark

### 2025-10-17T10:54:05.224+0800 [REDACTED_USER]

notified (陈青璟([REDACTED_EMAIL]), om_x100b402eb20cc5f80f231a3d9d642d2) by lark

### 2025-10-17T17:44:47.624+0800 [REDACTED_USER]

The vulnerabilities involving 
golang.org/x/crypto
 beyond v0.18 are:
CVE-2024-45337
: [9.1/10] Improper authorization when using this library as an 
SSH server
, fixed in v0.31
CVE-2025-22869

### 2025-10-25T20:34:47.655+0800 [REDACTED_USER]

feel free to close this ticket. Thanks.
