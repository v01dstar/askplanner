# Backup Restore References

This directory stores backup/restore knowledge that is too long or too case-specific for `SKILL.md`.

Organize content by axis first, then link related cases from multiple axes when needed. Backup/restore incidents often cross product architecture, component ownership, and operation workflow.

## Layout

- `architectures/` - TiDBX and Classic architecture-specific guidance.
- `components/` - TiDB, TiKV, Operator, BR, Lightning, and storage responsibility boundaries.
- `workflows/` - operation-specific workflows for backup, restore, PITR, and import.
- `playbooks/` - curated reusable workflows and diagnosis notes.
- `cases/tickets/` - support ticket-derived field cases.
- `cases/issues/` - GitHub issue-derived cases and fix lineage.

## Naming

- Ticket cases: `ticket-<id>-short-symptom.md`
- GitHub issues: `issue-<number>-short-symptom.md`
- Playbooks: `<topic>.md`
- Architecture notes: `<topic>.md`
- Component notes: `<component-topic>.md`
- Workflow notes: `<operation-topic>.md`

Keep names lowercase and hyphen-separated.

## Case Template

```markdown
# <Short Symptom>

## Source

- Ticket:
- GitHub issue:
- Related PRs:

## Symptom

## Classification

- Architecture: TiDBX | Classic
- Operation: Backup | Restore | PITR | Import
- Components: TiDB | TiKV | Operator | BR | Lightning | Storage | Multi-component

## Environment

- TiDB:
- TiKV:
- PD:
- BR/Lightning:
- Deployment:
- Storage:

## Evidence

## Root Cause

## Workaround

## Fixed Version

## Follow-ups
```
