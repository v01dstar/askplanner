# Issue 66280: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/66280
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-02-14T07:54:39Z
- Updated: 2026-03-20T10:15:33Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup
- Components: TiDB, BR, PD
- Categories: gc-safepoint, observability-diagnosis
- Labels: component/br, needs-cherry-pick-release-6.5, severity/moderate, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Backup; PD; TiDB; gc-safepoint; observability-diagnosis

## Linked PRs Mentioned In Body

- https://github.com/pingcap/tidb/pull/66279

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

```bash
# Using datetime format with a future timestamp
br backup full --pd "[REDACTED_IP]:2379" --storage "local:///tmp/backup" --backupts "2099-12-31 23:59:59+0800"

# Or using a very large TSO-like number representing future time
br backup full --pd "[REDACTED_IP]:2379" --storage "local:///tmp/backup" --backupts "[REDACTED_LONG_ID]"
```

### 2. [REDACTED_USER]

BR should reject the backup request with a clear error message:
```
Error: invalid backup timestamp: timestamp cannot be in the future (specified: 2099-12-31 23:59:59, current: 2026-02-14 15:30:00)
```

### 3. [REDACTED_USER]

BR accepts the future timestamp without validation. The backup operation proceeds without error, which is incorrect behavior because:
- Point-in-time backup should only work for past timestamps
- Future timestamps are semantically invalid for backup operations
- Users receive no feedback that they have provided an invalid parameter

### 4. [REDACTED_USER]

**Affected versions:**
- TiDB v6.5.3
- Current master branch (commit: d7ce2f2faa)

### Root [REDACTED_USER]

The validation logic has two gaps:

**1. In ParseTSString() function** (\`br/pkg/task/backup.go\` lines 789-814):
- Parses timestamp strings (both TSO and datetime formats)
- Converts to uint64 timestamp
- **Missing:** No check against current time

**2. In GetTS() function** (\`br/pkg/backup/client.go\` lines 458-497):
- Validates timestamp is not before GC safepoint (line 493)
- **Missing:** No check that timestamp is not in the future

### Code [REDACTED_USER]

**Current validation (only checks GC safepoint):**
```go
// br/pkg/backup/client.go:492-496
// check backup time do not exceed GCSafePoint
err = gc.CheckGCSafePoint(ctx, bc.mgr.GetGCManager(), backupTS)
if err != nil {
    return 0, errors.Trace(err)
}
```

**Flag definition:**
```go
// br/pkg/task/backup.go:119-120
flags.String(flagBackupTS, "", "the backup ts support TSO or datetime,"+
    " e.g. '[REDACTED_LONG_ID]', '2018-05-11 01:42:23'")
```

### Proposed [REDACTED_USER]

Add future timestamp validation in GetTS() function after the user-provided timestamp is set but before GC safepoint check:

**Location:** \`br/pkg/backup/client.go\` around line 470

```go
if ts > 0 {
    backupTS = ts

    // Validate timestamp is not in the future
    p, l, err := bc.mgr.GetPDClient().GetTS(ctx)
    if err != nil {
        return 0, errors.Trace(err)
    }
    currentTS := oracle.ComposeTS(p, l)
    if backupTS > currentTS {
        return 0, errors.Annotatef(berrors.ErrInvalidArgument,
            "backup timestamp cannot be in the future")
    }
} else {
    // ... existing code for getting current timestamp
}
```

### Related [REDACTED_USER]

Part of tracking issue: #66279
