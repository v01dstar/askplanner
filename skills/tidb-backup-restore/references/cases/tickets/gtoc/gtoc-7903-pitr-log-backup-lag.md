# GTOC-7903: PITR log backup lag

## Source

- Jira: https://tidb.atlassian.net/browse/GTOC-7903
- Status: Resolved
- Resolution: Done
- Priority: P3
- Issue type: Incident
- Created: 2025-09-15T09:54:45.619+0800
- Updated: 2025-09-29T17:00:19.576+0800
- Reporter: [REDACTED_USER]
- Assignee: [REDACTED_USER]

## Classification

- Architecture: Unknown
- Operation: PITR
- Components: BR
- Categories: [REDACTED_RESOURCE_NAME], storage-credential, tikv-data-path, operator-cr, performance-resource, compatibility-upgrade, observability-error-message
- Labels: N/A

## Symptom / Description Excerpt

# Objective

Evaluate whether `--ratelimit` on BR PITR restore affects end-to-end restore time.

# Test design

* **Cluster/[REDACTED_CLUSTER]:** `basic` / `tidb-cluster`
* **One-by-one execution:** strictly serialized; next run starts only after the previous Restore CR reaches `Complete/Failed`.
* **Database names:** `rate_test0 … rate_test7` (unchanged in SQL/tableFilter).
* **K8s resource names:** underscores replaced with hyphens for RFC1123 compliance (e.g., `[REDACTED_RESOURCE_NAME]`).
* **Variable under test:** `--ratelimit` = `1, 2, 4, 8, 16, 32, 64, 128` (doubling each run).
* **Constants:** same BR image (`docker.io/pingcap/br:v8.5.0-20250730-6bbe4cc`), same S3 paths/region, same `pitrRestoredTs`, same table filter, same placement/requirements flags.
* **Workload size:** \~**500 MiB** restored per run.
* **Observability:** `kubectl logs -f` captured to per-run files; Grafana panels watched (screenshot attached below).

# Results

Restore durations were tightly clustered, showing **no meaningful dependence on** `--ratelimit`:

* 1 → **4m20s**
* 2 → **4m41s**
* 4 → **3m52s**
* 8 → **4m40s**
* 16 → **3m42s**
* 32 → **3m58s**
* 64 → **4m57s**
* 128 → **3m59s**

## Recent Comments Excerpt

### 2025-09-15T09:55:02.741+0800 [REDACTED_USER]

notified (刘金龙([REDACTED_EMAIL]), om_x100b434351adb8840f11435ea0978a1) by lark

### 2025-09-15T09:58:33.657+0800 [REDACTED_USER]

upload restore log files:
[REDACTED_MEDIA]
And here is the clinic: 
[REDACTED_CLINIC_URL]

### 2025-09-15T10:03:40.750+0800 [REDACTED_USER]

notified (廖坚钧([REDACTED_EMAIL]), om_x100b4343717b21e00ec3cbfe00eb181) by lark

### 2025-09-15T10:52:32.382+0800 [REDACTED_USER]

https://github.com/pingcap/tidb/issues/63505
