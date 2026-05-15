# Issue 63663: Log backup checkpoint lag

## Source

- GitHub issue: https://github.com/pingcap/tidb/issues/63663
- State: CLOSED
- Author: [REDACTED_USER]
- Created: 2025-09-22T09:04:21Z
- Updated: 2025-10-10T20:31:36Z
- Closed: 2025-09-23T01:53:23Z
- Generated: 2026-05-15T00:20:39Z

## Classification

- Architecture: Unknown
- Operation: Backup/Restore
- Components: BR
- Categories: uncategorized
- Labels: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5, component/br, severity/major, type/bug
- Affected versions: affects-6.5, affects-7.1, affects-7.5, affects-8.1, affects-8.5

## Quick Match

- Title/error signature: `Log backup checkpoint lag`
- Search terms: BR; Backup/Restore; uncategorized

## Linked PRs Mentioned In Body

- N/A

## Issue Body

```go
	for len(data) > 0 {
		switch data[0] {
		case flagShortValuePrefix:
			vlen := data[1]
			if len(data[2:]) < int(vlen) {
				return errors.Annotatef(berrors.ErrInvalidArgument,
					"the length of short value is invalid, vlen: %v", int(vlen))
			}
			v.shortValue = data[2 : vlen+2]
			data = data[vlen+2:]
```

`vlen` is a length flag, which only support 0-255.  If vlen itself is 255, then vlen+2 would overflow.
We should transform it to a larger form to prevent the risk.
