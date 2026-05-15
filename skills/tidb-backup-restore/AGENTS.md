# TiDB Backup Restore Agent Notes

Use this skill directory for backup/restore field knowledge across four axes:

- product architecture: `references/architectures/`
- component boundary: `references/components/`
- operation workflow: `references/workflows/`
- field precedents: `references/cases/`

## Default workflow

1. Start from `SKILL.md` to classify product architecture, operation, component boundary, and symptom.
2. Search `references/architectures/tidbx/` or `references/architectures/classic/` for deployment-specific behavior.
3. Search `references/components/` to understand likely ownership and evidence needs.
4. Search `references/workflows/` for operation-specific diagnosis.
5. Search `references/cases/tickets/` for customer-facing symptoms, evidence, and workarounds.
6. Search `references/cases/issues/` when fix PRs, affected versions, or open product gaps matter.
7. Promote repeated patterns into `references/playbooks/` or the relevant axis-specific reference instead of leaving them only in raw case files.

## GitHub BR issue corpus

Use `scripts/generate_tidb_br_issue_cases.py` to refresh the local corpus of `pingcap/tidb` issues labeled `component/br`.

The generated corpus includes both open and closed issues because the primary use case is precedent matching: deciding whether a new backup/restore symptom has happened before and finding the prior workaround, fix PR, or affected-version signal.

By default, the script keeps only issues created in the last two years, filters toward bugfix/regression/failure precedents, and excludes feature/enhancement work plus test-only noise. This keeps the skill focused on operational diagnosis rather than BR roadmap tracking.

Default output:

- `references/cases/issues/` - one generated markdown file per issue.
- `references/cases/issues/README.md` - generated issue index.
- `references/playbooks/br-issue-precedent-index.md` - generated category-based quick lookup.

Use:

```bash
python3 skills/tidb-backup-restore/scripts/generate_tidb_br_issue_cases.py
```

The generator runs `scripts/sanitize_case_corpus.py`, `scripts/rewrite_case_titles.py`, then `scripts/sanitize_case_corpus.py` again before it exits.

Useful overrides:

```bash
python3 skills/tidb-backup-restore/scripts/generate_tidb_br_issue_cases.py --since 2024-01-01
python3 skills/tidb-backup-restore/scripts/generate_tidb_br_issue_cases.py --all-types --include-tests
```

## Case file guidance

Keep case files concise and searchable. Prefer one file per ticket or issue.

Use filenames like:

- `ticket-<id>-short-symptom.md`
- `issue-<number>-short-symptom.md`

For TiDB GitHub references, use full URLs instead of bare issue or PR numbers.

## What to preserve

- customer-facing symptom
- product architecture: TiDBX or Classic
- component boundary: TiDB, TiKV, Operator, BR, Lightning, storage, or multi-component
- affected versions and deployment type
- exact backup/restore mode
- storage backend and relevant configuration
- key log snippets or error signatures
- root cause, workaround, and fixed version if known
- linked issues, PRs, and merge or release status

## Safety

Anonymize customer names, person names, cluster IDs, hostnames, bucket names, object paths, credentials, support links, clinic links, attachments, business data, UUIDs, long IDs, emails, and IP addresses before committing any ticket-derived material.

Run the corpus sanitizer after adding or regenerating ticket and issue cases:

```bash
python3 skills/tidb-backup-restore/scripts/sanitize_case_corpus.py
python3 skills/tidb-backup-restore/scripts/rewrite_case_titles.py
python3 skills/tidb-backup-restore/scripts/sanitize_case_corpus.py
```

The sanitizer rewrites markdown content, renames generated case files when titles contain sensitive identifiers, and updates local markdown links. The title normalizer rewrites each ticket or issue title into the shortest useful technical symptom by preferring concrete error signatures, then operation/category summaries. Preserve technical information that is useful for diagnosis: error strings, versions, component names, commands after identifiers are redacted, public GitHub issue/PR links, and GTOC source links.

Good title shapes:

- `PITR fails with [BR:Common:ErrInvalidArgument]`
- `Backup fails with FileExistedInExternalStorage`
- `Restore checkpoint resume failure`
- `Log backup checkpoint lag`
- `Backup storage credential failure`

## Jira GTOC ticket corpus

Use `scripts/generate_gtoc_br_pitr_ticket_cases.py` to refresh recent GTOC Jira tickets related to BR, PITR, backup, restore, and log backup.

The script uses Atlassian MCP through `mcp-remote`, searches tickets updated in the last two years by default, and writes anonymized markdown. It redacts support/clinic URLs, media blobs, long numeric IDs, UUIDs, emails, and obvious secret-like values.

Default output:

- `references/cases/tickets/gtoc/` - one generated markdown file per Jira ticket.
- `references/cases/tickets/gtoc/README.md` - generated ticket index.
- `references/playbooks/gtoc-br-pitr-ticket-summary.md` - generated category-based summary for precedent matching.

Use:

```bash
python3 skills/tidb-backup-restore/scripts/generate_gtoc_br_pitr_ticket_cases.py
```

The generator runs `scripts/sanitize_case_corpus.py`, `scripts/rewrite_case_titles.py`, then `scripts/sanitize_case_corpus.py` again before it exits.
