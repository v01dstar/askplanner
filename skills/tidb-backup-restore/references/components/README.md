# Component Axis

Use this directory to separate backup/restore responsibility boundaries.

- `tidb/` - SQL metadata, schema, DDL, GC safepoint, checksum, and cluster-level settings.
- `tikv/` - SST ingest, raftstore, regions, compaction, disk IO, memory, resolved-ts, and log backup data path.
- `operator/` - Backup/Restore CRs, reconciliation, Kubernetes scheduling, secrets, service accounts, PVCs, and pod lifecycle.
- `br/` - BR task orchestration, metadata, checkpoint, retry, concurrency, and restore execution.
- `lightning/` - import mode, checkpoint, local sort, ingest, checksum, and post-import behavior.
- `storage/` - S3/GCS/Azure/NFS/object-store endpoint, credentials, IAM, TLS, listing, throttling, and consistency behavior.

Prefer component notes for evidence collection and ownership analysis. Put end-to-end procedures under `references/workflows/` or `references/playbooks/`.
