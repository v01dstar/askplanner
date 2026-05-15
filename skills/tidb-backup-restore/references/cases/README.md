# Field Cases

Use this directory for raw or lightly curated field precedents.

- `tickets/` - anonymized support ticket-derived cases.
- `issues/` - GitHub issue-derived cases and fix lineage.

Each case should include classification metadata for architecture, operation, and component boundary so it can be found from multiple axes.

Before committing ticket or issue cases, run:

```bash
python3 skills/tidb-backup-restore/scripts/sanitize_case_corpus.py
python3 skills/tidb-backup-restore/scripts/rewrite_case_titles.py
python3 skills/tidb-backup-restore/scripts/sanitize_case_corpus.py
```

The filter removes non-technical identifiers such as customer names, people, cluster and namespace names, bucket/object paths, internal/support/clinic/media links, secrets, UUIDs, long IDs, emails, and IP addresses. The title rewrite step makes titles concise and searchable by keeping the operation plus the strongest symptom or error signature. Keep technical signals intact: error strings, versions, component boundaries, public GitHub issue/PR links, and GTOC source links.
