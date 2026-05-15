# Issue 67819: PITR failure

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/67819
- State: OPEN
- Author: [REDACTED_USER]
- Created: 2026-04-16T08:55:17Z
- Updated: 2026-04-16T08:56:31Z
- Closed: N/A
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: TiKV, BR, Storage
- Categories: pitr-log-restore, storage-access, sst-ingest-import, checksum-consistency, observability-diagnosis
- Labels: affects-9.0, component/br
- Affected versions: affects-9.0

## Quick Match

- Title/error signature: `PITR failure`
- Search terms: BR; PITR; Storage; TiKV; checksum-consistency; observability-diagnosis; pitr-log-restore; sst-ingest-import; storage-access

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

### Summary

[REDACTED_USER]

### Code [REDACTED_USER]

`br/pkg/stream/stream_metas.go`, `MergeMigrations()`:

```go
func MergeMigrations(m1 *pb.Migration, m2 *pb.Migration) *pb.Migration {
    out := NewMigration()
    out.EditMeta = mergeMetaEdits(m1.GetEditMeta(), m2.GetEditMeta())
    out.Compactions = append(out.Compactions, m1.GetCompactions()...)
    out.Compactions = append(out.Compactions, m2.GetCompactions()...)       // both m1 and m2
    out.TruncatedTo = max(m1.GetTruncatedTo(), m2.GetTruncatedTo())
    out.DestructPrefix = append(out.DestructPrefix, m1.GetDestructPrefix()...)
    out.DestructPrefix = append(out.DestructPrefix, m2.GetDestructPrefix()...) // both m1 and m2
    out.IngestedSstPaths = append(out.IngestedSstPaths, m1.GetIngestedSstPaths()...)
    // ^^^ only m1, m2's IngestedSstPaths are silently dropped
    return out
}
```

All other repeated fields (`Compactions`, `DestructPrefix`) merge both `m1` and `m2`. `IngestedSstPaths` is the only field that drops `m2`.

### Impact

[REDACTED_USER]

**Currently masked by lock ordering**: In the current system, this does not cause correctness issues because restore holds a read lock that blocks truncate until PiTR has consumed the `IngestedSstPaths` directly from the layer files (via `Load()`). By the time truncate runs and merges the layers, PiTR has already used the SSTs.

**Becomes a correctness issue with lease-based lock expiration**: If lock leases are introduced (allowing expired locks to be reclaimed), truncate could run before PiTR consumes the layer's `IngestedSstPaths`, causing data loss for PiTR.

### Expected [REDACTED_USER]

`MergeMigrations` should preserve `m2`'s `IngestedSstPaths`, consistent with how it handles `Compactions` and `DestructPrefix`:

```go
out.IngestedSstPaths = append(out.IngestedSstPaths, m1.GetIngestedSstPaths()...)
out.IngestedSstPaths = append(out.IngestedSstPaths, m2.GetIngestedSstPaths()...)
```

This way, `processExtFullBackup()` can see all `IngestedSstPaths` and properly decide whether to keep or delete each `ext_backups` directory based on `Finished` status and `TruncatedTo`.

### Related

[REDACTED_USER]
