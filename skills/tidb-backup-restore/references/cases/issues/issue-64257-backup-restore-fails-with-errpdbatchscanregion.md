# Issue 64257: Backup/Restore fails with ErrPDBatchScanRegion

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/64257
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-11-04T06:46:56Z
- Updated: 2025-11-10T04:24:54Z
- Closed: 2025-11-10T04:24:54Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: TiDB, TiKV, BR
- Categories: region-split-scatter, checkpoint-retry, observability-diagnosis
- Labels: component/br, severity/major, type/bug
- Affected versions: N/A

## Quick Match

- Title/error signature: `Backup/Restore fails with ErrPDBatchScanRegion`
- Search terms: BR; Backup/Restore; TiDB; TiKV; checkpoint-retry; observability-diagnosis; region-split-scatter

## Linked PRs Mentioned In Body

- N/A

## Issue Body

## Bug Report

Please answer these questions before submitting your issue. Thanks!

### 1. [REDACTED_USER]

<!-- a step by step guide for reproducing the bug. -->

```golang
	_ = utils.WithRetry(ctx, func() error {
		regions := make([]*RegionInfo, 0, 16)
		scanStartKey := startKey
		for {
			var batch []*RegionInfo
			if err != nil {
				batch, err = client.ScanRegions(ctx, scanStartKey, endKey, limit)
			} else {
				batch, err = client.ScanRegions(ctx, scanStartKey, endKey, limit, opt.WithAllowFollowerHandle())
			}

			if err != nil {
				err = errors.Annotatef(berrors.ErrPDBatchScanRegion.Wrap(err), "scan regions from start-key:%s, err: %s",
					redact.Key(scanStartKey), err.Error())
				return err
			}
			regions = append(regions, batch...)
			if len(batch) < limit {
				// No more region
				break
			}
			scanStartKey = batch[len(batch)-1].Region.GetEndKey()
			if len(scanStartKey) == 0 ||
				(len(endKey) > 0 && bytes.Compare(scanStartKey, endKey) >= 0) {
				// All key space have scanned
				break
			}
		}
		// if the number of regions changed, we can infer TiKV side really
		// made some progress so don't increase the retry times.
		if len(regions) != len(lastRegions) {
			backoffer.Stat.ReduceRetry()
		}
		lastRegions = regions

		if err = checkRegionConsistency(startKey, endKey, regions); err != nil {
			log.Warn("failed to scan region, retrying",
				logutil.ShortError(err),
				zap.Int("regionLength", len(regions)))
			return err
		}
		return nil
	}, backoffer)
```

When execute

```
if err != nil {
    batch, err = client.ScanRegions(ctx, scanStartKey, endKey, limit)
}
```

the err will be replace with a new error. So the next region scan will use follower-handle mode, which is unexpected.

### 2. [REDACTED_USER]

If encounter error, fallback to using follower handle mode.

### 3. [REDACTED_USER]

### 4. [REDACTED_USER]

<!-- Paste the output of SELECT tidb_version() -->
