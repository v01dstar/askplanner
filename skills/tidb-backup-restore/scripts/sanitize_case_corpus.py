#!/usr/bin/env python3
"""Sanitize ticket and issue case files.

The goal is to preserve technical debugging value while removing customer,
cluster, person, and environment identifiers from case corpora.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_TARGETS = [
    "skills/tidb-backup-restore/references/cases/tickets",
    "skills/tidb-backup-restore/references/cases/issues",
    "skills/tidb-backup-restore/references/playbooks/gtoc-br-pitr-ticket-summary.md",
]


TECHNICAL_URL_ALLOWLIST = [
    "https://github.com/pingcap/tidb/issues/",
    "https://github.com/pingcap/tidb/pull/",
    "https://github.com/tikv/",
    "https://github.com/aws/",
    "https://tidb.atlassian.net/browse/GTOC-",
]

SENSITIVE_NAME_WORDS = [
    # Historical customer/environment tokens observed in legacy ticket titles.
    # Keep this list narrow; broader cluster/resource regexes handle future cases.
    "affin",
    "bulbasaur",
    "delhilver",
    "mussel",
    "pikachu",
    "shared3",
    "wetech",
]


def _protect_allowed_urls(text: str) -> tuple[str, dict[str, str]]:
    placeholders: dict[str, str] = {}

    def repl(match: re.Match[str]) -> str:
        url = match.group(0)
        if any(url.startswith(prefix) for prefix in TECHNICAL_URL_ALLOWLIST):
            token = f"__ALLOWED_URL_{len(placeholders)}__"
            placeholders[token] = url
            return token
        return url

    text = re.sub(r"https://[^\s)>\"]+", repl, text)
    return text, placeholders


def _protect_local_markdown_links(text: str) -> tuple[str, dict[str, str]]:
    placeholders: dict[str, str] = {}

    def repl(match: re.Match[str]) -> str:
        link = match.group(0)
        token = f"__LOCAL_MD_LINK_{len(placeholders)}__"
        placeholders[token] = link
        return token

    text = re.sub(r"(?<=\]\()[^)]+\.md(?=\))", repl, text)
    return text, placeholders


def _restore_allowed_urls(text: str, placeholders: dict[str, str]) -> str:
    for token, url in placeholders.items():
        text = text.replace(token, url)
    return text


def _restore_placeholders(text: str, placeholders: dict[str, str]) -> str:
    for token, value in placeholders.items():
        text = text.replace(token, value)
    return text


def sanitize_text(text: str) -> str:
    text, allowed_urls = _protect_allowed_urls(text)
    text, local_links = _protect_local_markdown_links(text)

    # Source-control and ticket metadata that is not useful for diagnosis.
    text = re.sub(r"(?m)^- Author: .*$", "- Author: [REDACTED_USER]", text)
    text = re.sub(r"(?m)^- Reporter: .*$", "- Reporter: [REDACTED_USER]", text)
    text = re.sub(r"(?m)^- Assignee: .*$", "- Assignee: [REDACTED_USER]", text)
    text = re.sub(r"(?m)^(###\s+\S+\s+)@?[^\n]+$", r"\1[REDACTED_USER]", text)

    # Support, observability, meeting, media, and customer-console links.
    text = re.sub(r"https://tidb\.support\.pingcap\.com/[^\s)>\"]+", "[REDACTED_SUPPORT_URL]", text)
    text = re.sub(r"https://internal\.pingcap\.net/[^\s)>\"]+", "[REDACTED_INTERNAL_URL]", text)
    text = re.sub(r"https://clinic\.pingcap\.com/[^\s)>\"]+", "[REDACTED_CLINIC_URL]", text)
    text = re.sub(r"https://teams\.microsoft\.com/[^\s)>\"]+", "[REDACTED_MEETING_URL]", text)
    text = re.sub(r"https://app\.podium-prod\.fkcloud\.in/[^\s)>\"]+", "[REDACTED_CUSTOMER_CONSOLE_URL]", text)
    text = re.sub(r"https://github\.com/user-attachments/[^\s)>\"]+", "[REDACTED_ATTACHMENT_URL]", text)
    text = re.sub(r"https://github\.com/pingcap/tidb/assets/[^\s)>\"]+", "[REDACTED_ATTACHMENT_URL]", text)
    text = re.sub(r"blob:https://[^\s)]+", "[REDACTED_MEDIA_BLOB]", text)
    text = re.sub(r"!\[\]\(\[REDACTED_MEDIA_BLOB\]\)", "[REDACTED_MEDIA]", text)
    text = re.sub(r"!\[[^\]]*\]\(\[REDACTED_ATTACHMENT_URL\]\)", "[REDACTED_ATTACHMENT]", text)
    text = re.sub(r"<img[^>]+src=\"\[REDACTED_ATTACHMENT_URL\]\"[^>]*>", "[REDACTED_ATTACHMENT]", text)
    text = re.sub(r"<custom[^>]*>\[REDACTED_[A-Z_]+URL\]</custom>", "[REDACTED_LINK]", text)

    # Users, mentions, emails, and ticket IDs from support systems.
    text = re.sub(r"@[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,3}", "@[REDACTED_USER]", text)
    text = re.sub(r"\b(?!root@)[a-z][a-z0-9._-]{2,}@(?=\[REDACTED_ENV_NAME\])", "[REDACTED_USER]@", text)
    text = re.sub(r'"text":\s*"@[^"]+"', '"text": "@[REDACTED_USER]"', text)
    text = re.sub(r'"id":\s*"[0-9a-fA-F:]{8,}"', '"id": "[REDACTED_ID]"', text)
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[REDACTED_EMAIL]", text)
    text = re.sub(r"\b(?:NAID|ONCALL|INC)-\d+\b", "[REDACTED_TICKET_ID]", text)

    # Credentials, tokens, buckets, storage object paths, and cloud request IDs.
    text = re.sub(r"AKIA[0-9A-Z]{16}", "[REDACTED_AWS_ACCESS_KEY]", text)
    text = re.sub(r"\[(REDACTED_[A-Z_]+)\]\]+", r"[\1]", text)
    text = re.sub(r"(?i)(secret|token|password|passwd|api[_-]?key|private_key|private_key_id)\s*[:=]\s*(?!\[REDACTED_SECRET\])[^,\]\s}]+", r"\1=[REDACTED_SECRET]", text)
    text = re.sub(r"s3://([^/\s]+)/", "s3://[REDACTED_BUCKET]/", text)
    text = re.sub(r'(?i)(bucket[":\s=]+)[A-Za-z0-9._-]{8,}', r"\1[REDACTED_BUCKET]", text)
    text = re.sub(r'(?i)("?aws_request_id"?\s*[:=]\s*"?)[A-Z0-9+/=]{8,}', r"\1[REDACTED_AWS_REQUEST_ID]", text)
    text = re.sub(r'(?i)("?s3_extended_request_id"?\s*[:=]\s*"?)[A-Za-z0-9+/=]{16,}', r"\1[REDACTED_AWS_EXTENDED_REQUEST_ID]", text)
    text = re.sub(r"(?i)(request id:?\s*)[a-z0-9+/=-]{8,}", r"\1[REDACTED_REQUEST_ID]", text)
    text = re.sub(r"(?i)(host id:?\s*)[a-z0-9+/=-]{16,}", r"\1[REDACTED_HOST_ID]", text)
    text = re.sub(r"s3://\[REDACTED_BUCKET\]/\[REDACTED_OBJECT_PATH\]\]+", "s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]", text)
    text = re.sub(r"s3://\[REDACTED_BUCKET\]/(?!\[REDACTED_OBJECT_PATH\])[\w./=+%:@?&-]+", "s3://[REDACTED_BUCKET]/[REDACTED_OBJECT_PATH]", text)
    text = re.sub(r"(?i)(aws\s+s3api\s+get-object\b[^\n]*?--key\s+)(?!\[REDACTED_OBJECT_PATH\])\S+", r"\1[REDACTED_OBJECT_PATH]", text)

    # UUIDs, long numeric IDs, timestamps-as-IDs, and IP addresses.
    text = re.sub(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b", "[REDACTED_UUID]", text)
    text = re.sub(r"\b[0-9]{12,}\b", "[REDACTED_LONG_ID]", text)
    text = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "[REDACTED_IP]", text)

    # Kubernetes and TiDB Cloud resource names. Preserve the resource kind and component role.
    text = re.sub(r"(?i)(namespace[:=/\s]+)[a-z0-9][a-z0-9._-]{4,}", r"\1[REDACTED_NAMESPACE]", text)
    text = re.sub(r"(?i)(cluster(?:Namespace)?[:=/\s]+)[a-z0-9][a-z0-9._-]{4,}", r"\1[REDACTED_CLUSTER]", text)
    text = re.sub(r"(?i)(name[:=/\s]+)(integrated-backup-schedule-s3|[a-z0-9][a-z0-9._-]{12,})", r"\1[REDACTED_RESOURCE_NAME]", text)
    text = re.sub(r"\b[a-z][a-z0-9]{2,}(?:-[a-z0-9]+){0,4}-(?:prod|production|stg|staging|stage|dev|test|eks|ml|dr|v[0-9]+)(?:-[a-z0-9]+)*\b", "[REDACTED_ENV_NAME]", text, flags=re.IGNORECASE)
    text = re.sub(r"\b[a-z0-9][a-z0-9-]{3,}-(?:tidb|tikv|pd|ticdc|monitor|backup|restore)-[a-z0-9-]*\b", "[REDACTED_RESOURCE_NAME]", text)
    text = re.sub(r"\b(?:prod|production|stg|staging|dev|test)[a-z0-9._-]*-(?:tidb|tikv|pd|br|backup|restore)[a-z0-9._-]*\b", "[REDACTED_RESOURCE_NAME]", text, flags=re.IGNORECASE)
    text = re.sub(r"\b(?:[a-z0-9]+-){2,}(?:prod|stg|stage|dev|test|hyd|dr|qos|saas|ads|assets|payment|coin|shop)[a-z0-9-]*\b", "[REDACTED_ENV_NAME]", text, flags=re.IGNORECASE)
    for word in SENSITIVE_NAME_WORDS:
        text = re.sub(rf"\b{re.escape(word)}(?:[-\s]+(?:prod|production|stg|staging|stage|dev|test|eks|ml|dr|cluster|clusters))?\b", "[REDACTED_ENV_NAME]", text, flags=re.IGNORECASE)

    # Customer names in common title/context positions. Avoid rewriting generic technical prose.
    text = re.sub(r"(?i)(Customer(?: is)?(?: reporting| has| says| asked| uploaded)?[:\s]+)[A-Z][A-Za-z0-9_. -]{2,40}", r"\1[REDACTED_CUSTOMER]", text)
    text = re.sub(r"(?m)^(- \[[A-Z]+-\d+: )(\[REDACTED_[A-Z_]+]\s*-\s*)", r"\1", text)
    text = re.sub(r"(?m)^(#\s+GTOC-\d+:\s+)(?:\[[A-Z_]+]\s*-\s+)(.+)$", r"\1\2", text)
    text = re.sub(r"(?m)^(#\s+GTOC-\d+:\s+)(?:\[[A-Z_]+]:\s+)(.+)$", r"\1\2", text)
    text = re.sub(r"(?m)^(#\s+(?:GTOC-\d+|Issue \d+):\s+)([^\n]*?)(?:\bon[ \t]+|\bfor[ \t]+|\bdue to[ \t]+)?\[REDACTED_ENV_NAME\][ \t]+(?:cluster|clusters)?[ \t]*([^\n]*)$", r"\1\2[REDACTED_CLUSTER] \3", text)
    text = re.sub(r"(?m)^(#\s+(?:GTOC-\d+|Issue \d+):[^\n]*?)\s+<!-- generated by scripts/[^>]+ -->$", r"\1", text)
    text = re.sub(r"(?i)commented by [A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,3}", "commented by [REDACTED_USER]", text)
    text = re.sub(r"(?i)\bHi [A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,3},", "Hi [REDACTED_USER],", text)
    text = re.sub(r"\[REDACTED_CUSTOMER\](?:\[REDACTED_CUSTOMER\])+", "[REDACTED_CUSTOMER]", text)

    text = _restore_placeholders(text, local_links)
    text = _restore_allowed_urls(text, allowed_urls)
    return text


def slugify(value: str, limit: int = 90) -> str:
    value = value.lower()
    value = value.replace("[redacted_customer]", "redacted-customer")
    value = value.replace("[redacted_resource_name]", "redacted-resource")
    value = value.replace("[redacted_env_name]", "redacted-env")
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value[:limit].rstrip("-") or "case")


def sanitized_case_filename(file: Path, text: str) -> str | None:
    match = re.search(r"(?m)^#\s+(GTOC-\d+):\s+(.+)$", text)
    if match:
        return f"{match.group(1).lower()}-{slugify(match.group(2))}.md"
    match = re.search(r"(?m)^#\s+Issue\s+(\d+):\s+(.+)$", text)
    if match:
        return f"issue-{match.group(1)}-{slugify(match.group(2))}.md"
    return None


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(set(files))


def sanitize_files(paths: list[Path], dry_run: bool = False) -> tuple[int, int]:
    changed = 0
    total = 0
    files = iter_markdown_files(paths)
    rename_map: dict[str, str] = {}
    for file in files:
        total += 1
        old = file.read_text(encoding="utf-8")
        new = sanitize_text(old)
        if new != old:
            changed += 1
            if not dry_run:
                file.write_text(new, encoding="utf-8")
        new_name = sanitized_case_filename(file, new)
        if new_name and new_name != file.name:
            target = file.with_name(new_name)
            if not target.exists() or target == file:
                rename_map[file.name] = new_name
                if not dry_run:
                    file.rename(target)

    if rename_map:
        if not dry_run:
            for file in iter_markdown_files(paths):
                old = file.read_text(encoding="utf-8")
                new = old
                for old_name, new_name in rename_map.items():
                    new = new.replace(old_name, new_name)
                if new != old:
                    file.write_text(new, encoding="utf-8")
        changed += len(rename_map)
    return total, changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", default=DEFAULT_TARGETS)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    total, changed = sanitize_files([Path(path) for path in args.paths], dry_run=args.dry_run)
    mode = "Would sanitize" if args.dry_run else "Sanitized"
    print(f"{mode} {changed}/{total} markdown files")


if __name__ == "__main__":
    main()
