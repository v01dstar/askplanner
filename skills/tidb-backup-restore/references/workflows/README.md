# Workflow Axis

Use this directory for operation-specific diagnosis flows.

- `backup/` - full backup, incremental backup, snapshot backup, metadata generation, throughput, and storage write path.
- `restore/` - full restore, table/database restore, snapshot restore, checksum, partial restore state, and retry safety.
- `pitr/` - log backup, checkpoint continuity, resolved-ts, GC safepoint, restore timestamp, and gap diagnosis.
- `import/` - TiDB Lightning logical or physical import, local sort, SST ingest, checksum, and post-import validation.
