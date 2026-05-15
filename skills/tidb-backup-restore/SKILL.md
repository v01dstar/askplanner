---
name: tidb-backup-restore
description: Diagnose TiDB backup and restore issues across TiDBX and Classic architectures, including BR, PITR, log backup, TiDB Lightning import, TiDB/TiKV/Operator interactions, cloud storage failures, checksum mismatches, and restore performance regressions. Use when handling backup/restore tickets, GitHub issues, or customer incidents.
---

# TiDB Backup Restore

Use this skill to triage backup and restore failures or performance issues across product architecture, component ownership, operation workflow, and field-case precedent.

## Workflow

1. Identify the product architecture:
   - TiDBX: managed control plane, platform automation, cloud-provider integration, and internal service ownership matter.
   - Classic: self-hosted, TiUP, Kubernetes/TiDB Operator, or customer-managed deployment details matter.
2. Identify the operation:
   - Backup: full backup, incremental backup, log backup, PITR, snapshot backup.
   - Restore: full restore, point-in-time restore, snapshot restore, table/database restore.
   - Import: TiDB Lightning physical or logical import.
3. Identify the likely component boundary:
   - TiDB: SQL metadata, DDL/schema, placement, GC safepoint, checksum, session/config behavior.
   - TiKV: SST ingest, raftstore, region, compaction, disk IO, memory, resolved-ts, log backup data path.
   - Operator: Backup/Restore CRs, scheduling, secrets, service accounts, PVCs, pod lifecycle, Kubernetes events.
   - BR/Lightning: task orchestration, metadata, checkpoint, retry, concurrency, restore/import execution.
   - Storage: S3/GCS/Azure/NFS endpoint, credential, IAM, TLS, list/read/write behavior, throttling.
4. Capture the environment:
   - TiDB, TiKV, PD, BR, and Lightning versions.
   - Deployment type: self-hosted, TiDB Cloud, Kubernetes/TiDB Operator, or TiUP.
   - Storage backend: S3, GCS, Azure Blob, NFS, local, or other S3-compatible storage.
   - Cluster scale: data size, table count, region count, TiKV count, and concurrency settings.
5. Collect evidence:
   - BR or Lightning command line, task ID, and full logs.
   - TiKV and PD logs around the failure window.
   - TiDB logs for DDL, GC, checksum, and metadata errors.
   - Operator CR YAML, events, pod logs, secrets/service account references, and reconciliation status when Kubernetes is involved.
   - Storage errors, credentials or IAM policy symptoms, and object path layout.
   - Metrics for IO, network, region scheduling, ingest, compaction, CPU, and memory.
6. Classify the symptom:
   - Storage access, credential, throttling, or object consistency issue.
   - Backup metadata, schema, DDL, or version compatibility issue.
   - Region, SST ingest, checksum, or data consistency issue.
   - Restore speed, import speed, compaction pressure, or resource saturation issue.
   - PITR/log backup checkpoint, resolved-ts, or gap issue.
7. Search local precedents by axis:
   - Product architecture: `references/architectures/tidbx/` or `references/architectures/classic/`.
   - Component boundary: `references/components/`.
   - Operation workflow: `references/workflows/`.
   - Field cases: `references/cases/tickets/` and `references/cases/issues/`.
   - Mature reusable playbooks: `references/playbooks/`.
8. Decide the next action:
   - Provide an operational workaround when the symptom is understood.
   - Recommend a safer retry plan when data consistency or partial restore state is involved.
   - Escalate with a minimal reproducer, logs, versions, and linked precedent when it looks like a product bug.

## High-signal rules

- Treat restore correctness as higher priority than speed. Do not suggest cleanup, retry, or overwrite steps until the current restore state is understood.
- Preserve the original BR or Lightning logs and backup metadata before changing the environment.
- Classify by TiDBX vs Classic before comparing cases. Similar BR symptoms can have different ownership, automation, and mitigation paths.
- Classify by component boundary before assigning root cause. Backup/restore incidents often cross TiDB metadata, TiKV ingest, Operator reconciliation, and object storage.
- For cloud storage failures, verify endpoint, region, path style, IAM permissions, TLS, and object listing behavior before assuming a BR bug.
- For PITR issues, check log backup task status, checkpoint continuity, GC safepoint, and the target restore timestamp.
- For performance issues, compare problem and baseline windows, then correlate throughput with TiKV ingest, compaction, disk IO, network, and object-store latency.
- Link full GitHub URLs when referencing TiDB issues or PRs.
- Before using or committing ticket/issue-derived cases, run `scripts/sanitize_case_corpus.py` and `scripts/rewrite_case_titles.py`. Remove customer, person, cluster, bucket, object-path, internal-link, attachment, secret, UUID, long-ID, email, and IP identifiers while preserving technical errors and public source links. Rewrite every case title into a concise searchable symptom, such as `PITR fails with [BR:Common:ErrInvalidArgument]`, `Backup fails with FileExistedInExternalStorage`, or `Log backup checkpoint lag`.

## References

- `references/README.md` - corpus layout and naming rules.
- `references/architectures/` - TiDBX vs Classic architecture-specific guidance.
- `references/components/` - TiDB, TiKV, Operator, BR, Lightning, and storage responsibility boundaries.
- `references/workflows/` - operation-specific workflows for backup, restore, PITR, and import.
- `references/playbooks/` - curated backup/restore workflows and diagnosis notes.
- `references/playbooks/br-issue-precedent-index.md` - generated quick lookup for historical `component/br` GitHub issues.
- `references/playbooks/gtoc-br-pitr-ticket-summary.md` - generated quick lookup for recent GTOC Jira BR/PITR tickets.
- `references/cases/tickets/` - ticket-derived field cases.
- `references/cases/issues/` - GitHub issue-derived cases with PR and version lineage.
