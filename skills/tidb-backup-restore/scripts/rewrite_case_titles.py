#!/usr/bin/env python3
"""Rewrite case titles into concise searchable symptoms."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_TARGETS = [
    "skills/tidb-backup-restore/references/cases/tickets",
    "skills/tidb-backup-restore/references/cases/issues",
    "skills/tidb-backup-restore/references/playbooks/gtoc-br-pitr-ticket-summary.md",
    "skills/tidb-backup-restore/references/playbooks/br-issue-precedent-index.md",
]

NOISE_PREFIXES = [
    "[critical]",
    "[ebs br]",
    "[br]",
    "br:",
    "tidb br",
    "tidb backup",
    "customer",
    "[redacted_customer]:",
    "[redacted_env_name]:",
    "[redacted_cluster]",
]

ERROR_PATTERNS = [
    r"\[BR:[^\]\n]+]",
    r"\[[A-Za-z]+:\d+]",
    r"\bErr(?:Backup|Common|KVEpoch|PD|Restore|Storage|Stream|Unknown)[A-Za-z0-9_]*\b",
    r"\bFileExistedInExternalStorage\b",
    r"\bNoCredentialProviders\b",
    r"\bAccessDenied\b",
    r"\bInvalidAccessKeyId\b",
    r"\bEntityTooLarge\b",
    r"\bTransaction is too large\b",
    r"\bresolve lock timeout\b",
    r"\bno base id map found\b",
    r"\bfailed to acquire lock\b",
    r"\bslice bounds out of range\b",
    r"\bnil pointer\b",
    r"\binvalid memory address\b",
    r"\binvalid argument\b",
    r"\bErrKVEpochNotMatch\b",
    r"\bPD update failed\b",
    r"\bErrPDUpdateFailed\b",
    r"\bNo such file or directory\b",
    r"\bcheckpoint gap\b",
    r"\bcolumn mismatch\b",
    r"\bsplit key exceeds limit\b",
]


def slugify(value: str, limit: int = 90) -> str:
    value = value.lower()
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value[:limit].rstrip("-") or "case")


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(set(files))


def current_heading(text: str) -> tuple[str, str] | None:
    match = re.search(r"(?m)^#\s+((?:GTOC-\d+|Issue \d+)):\s+(.+)$", text)
    if not match:
        return None
    return match.group(1), match.group(2).strip()


def bullet_value(text: str, name: str) -> str:
    match = re.search(rf"(?m)^- {re.escape(name)}:\s*(.+)$", text)
    return match.group(1).strip() if match else ""


def clean_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title).strip(" -:_")
    title = title.strip("`")
    title = title.replace("**", "")
    title = title.replace("“", '"').replace("”", '"')
    title = re.sub(r"(?i)^error[:=]\s*", "", title)
    title = re.sub(r"\[[A-Z_]+]", "", title)
    title = re.sub(r"\b(?:prod|production|stg|staging|dev|test)\b", "", title, flags=re.IGNORECASE)
    for prefix in NOISE_PREFIXES:
        if title.lower().startswith(prefix):
            title = title[len(prefix) :].strip(" -:_")
    title = title.replace("TiKV", "TiKV").replace("Tikv", "TiKV").replace("Pitr", "PITR")
    title = title.replace("pitr", "PITR").replace("tidb", "TiDB").replace("tikv", "TiKV")
    title = title.replace("br ", "BR ").replace(" br", " BR")
    title = title.strip(" -:_")
    return title


def first_error_signature(text: str) -> str:
    for pattern in ERROR_PATTERNS:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            signature = clean_title(match.group(0))
            if signature.lower() not in {"error", "errors", "failed", "failure"}:
                return signature

    line_patterns = [
        r"(?im)^\s*error(?: message)?[:=]\s*(.+)$",
        r"(?im)\berror[=:]\s*\"?([^\"\n]{8,140})",
        r"(?im)\breason is\s+([^,\n]{8,120})",
        r"(?im)\bfailed,?\s+(?:err|error|reason)[:= ]+([^\"\n]{8,140})",
    ]
    for pattern in line_patterns:
        match = re.search(pattern, text)
        if match:
            value = re.sub(r"\[[A-Z_]+][^\s,\]]*", "[REDACTED]", match.group(1))
            signature = clean_title(value[:120])
            if signature.lower() not in {"error", "errors", "failed", "failure", "is"}:
                return signature
    return ""


def title_from_categories(operation: str, components: str, categories: str, body: str) -> str:
    text = body.lower()
    if "resolved-ts" in text or "rpo" in text or "lag" in text:
        if operation == "PITR":
            return "PITR log backup lag"
        return "Log backup checkpoint lag"
    if "oom" in text or "out of memory" in text:
        return f"{operation} OOM during {primary_component(components)} path"
    if "credential" in categories or "accessdenied" in text or "nocredentialproviders" in text:
        return f"{operation} storage credential failure"
    if "rate limit" in text or "throttl" in text or "slowdown" in text:
        return f"{operation} object storage throttling"
    if "checkpoint" in categories and "restore" in operation.lower():
        return "Restore checkpoint resume failure"
    if "schema" in categories or "system table" in text or "column mismatch" in text:
        return f"{operation} schema metadata mismatch"
    if "split" in text or "scatter" in text:
        return f"{operation} region split failure"
    if "panic" in text or "segmentation violation" in text or "sigsegv" in text:
        return f"{primary_component(components)} panic during {operation.lower()}"
    if "operator-cr" in categories:
        return f"Operator {operation.lower()} CR failure"
    return f"{operation} failure"


def primary_component(components: str) -> str:
    for candidate in ["TiKV", "Operator", "BR", "Storage", "PD", "TiDB", "Lightning"]:
        if candidate.lower() in components.lower():
            return candidate
    return "BR"


def normalize_title(text: str) -> str:
    heading = current_heading(text)
    if not heading:
        return ""
    original = clean_title(heading[1])
    operation = bullet_value(text, "Operation") or "Backup/Restore"
    components = bullet_value(text, "Components")
    categories = bullet_value(text, "Categories")
    compressed_existing = compressed_signature_title(operation, original, text)
    if compressed_existing and compressed_existing != original:
        return compressed_existing
    if is_normalized_title(original):
        return original
    signature = first_error_signature(text)
    compressed = compressed_signature_title(operation, signature, text)
    if compressed:
        return compressed

    if signature and len(signature) <= 80:
        title = f"{operation} fails with {signature}"
    else:
        title = title_from_categories(operation, components, categories, text)

    if original:
        original_lower = original.lower()
        if any(word in original_lower for word in ["lag", "rpo", "checkpoint"]) and "lag" not in title.lower():
            title = "Log backup checkpoint lag"
        elif any(word in original_lower for word in ["stuck", "hang", "paused"]) and not any(word in title.lower() for word in ["stuck", "paused", "lag"]):
            title = f"{operation} gets stuck"
        elif any(word in original_lower for word in ["corrupt", "incomplete", "data loss", "broken index"]):
            title = f"{operation} data consistency issue"
        elif "rate limit" in original_lower:
            title = f"{operation} object storage throttling"

    title = clean_title(title)
    title = re.sub(r"\s+", " ", title).strip()
    if len(title) > 96:
        title = title[:96].rsplit(" ", 1)[0].strip()
    return title or original


def compressed_signature_title(operation: str, signature: str, text: str) -> str:
    combined = f"{signature}\n{text}".lower()
    if "411" in combined and "length required" in combined:
        return f"{operation} fails with HTTP 411 Length Required"
    if "couldn't find aws credentials" in combined or "nocredentialproviders" in combined:
        return f"{operation} storage credential failure"
    if "event_loader.rs" in combined or "capturechan" in combined:
        return "PITR log backup event loader failure"
    if "huge amount of get region requests" in combined:
        return "Backup overloads PD region scan"
    if "different values for" in combined and "dumpling" in combined:
        return "Dumpling export parameter issue"
    if re.search(r"\[\d{4}/\d{2}/\d{2} ", signature):
        return title_from_categories(operation, bullet_value(text, "Components"), bullet_value(text, "Categories"), text)
    return ""


def is_normalized_title(title: str) -> bool:
    lowered = title.lower()
    stable_phrases = [
        " fails with ",
        " storage credential failure",
        " log backup lag",
        " object storage throttling",
        " gets stuck",
        " data consistency issue",
        " schema metadata mismatch",
        " region split failure",
        " oom during ",
        " panic during ",
        " cr failure",
        " checkpoint resume failure",
    ]
    return any(phrase in lowered for phrase in stable_phrases) or lowered.endswith(" failure")


def rewrite_text(text: str) -> tuple[str, str, str] | None:
    heading = current_heading(text)
    if not heading:
        return None
    case_id, old_title = heading
    new_title = normalize_title(text)
    if not new_title or new_title == old_title:
        return text, old_title, new_title
    new = re.sub(
        r"(?m)^#\s+((?:GTOC-\d+|Issue \d+)):\s+.+$",
        lambda match: f"# {match.group(1)}: {new_title}",
        text,
        count=1,
    )
    new = re.sub(r"(?m)^- Title/error signature:\s+`.*`$", f"- Title/error signature: `{new_title}`", new)
    return new, old_title, new_title


def target_filename(file: Path, text: str) -> str | None:
    heading = current_heading(text)
    if not heading:
        return None
    case_id, title = heading
    if case_id.startswith("GTOC-"):
        return f"{case_id.lower()}-{slugify(title)}.md"
    number = case_id.split()[1]
    return f"issue-{number}-{slugify(title)}.md"


def rewrite_case_titles(paths: list[Path], dry_run: bool = False) -> tuple[int, int]:
    total = 0
    changed = 0
    rename_map: dict[str, str] = {}
    title_map: dict[str, str] = {}

    for file in iter_markdown_files(paths):
        if not re.match(r"(gtoc-\d+|issue-\d+)-", file.name):
            continue
        total += 1
        old = file.read_text(encoding="utf-8")
        result = rewrite_text(old)
        if not result:
            continue
        new, _, new_title = result
        heading = current_heading(new)
        if heading:
            title_map[heading[0]] = new_title
        new_name = target_filename(file, new)
        if new != old:
            changed += 1
            if not dry_run:
                file.write_text(new, encoding="utf-8")
        if new_name and new_name != file.name:
            target = file.with_name(new_name)
            if not target.exists() or target == file:
                rename_map[file.name] = new_name
                if not dry_run:
                    file.rename(target)

    if rename_map:
        changed += len(rename_map)
        if not dry_run:
            for file in iter_markdown_files(paths):
                old = file.read_text(encoding="utf-8")
                new = old
                for old_name, new_name in rename_map.items():
                    new = new.replace(old_name, new_name)
                new = rewrite_index_titles(new, title_map)
                if new != old:
                    file.write_text(new, encoding="utf-8")
    elif title_map and not dry_run:
        for file in iter_markdown_files(paths):
            if re.match(r"(gtoc-\d+|issue-\d+)-", file.name):
                continue
            old = file.read_text(encoding="utf-8")
            new = rewrite_index_titles(old, title_map)
            if new != old:
                file.write_text(new, encoding="utf-8")
    return total, changed


def rewrite_index_titles(text: str, title_map: dict[str, str]) -> str:
    lines = text.splitlines()
    for case_id, title in title_map.items():
        if case_id.startswith("GTOC-"):
            prefix = f"- [{case_id}: "
            for index, line in enumerate(lines):
                if line.startswith(prefix) and "](" in line:
                    suffix = line.rsplit("](", 1)[1]
                    lines[index] = f"- [{case_id}: {title}]({suffix}"
        else:
            number = case_id.split()[1]
            prefix = f"- [{number}: "
            for index, line in enumerate(lines):
                if line.startswith(prefix) and "](" in line:
                    suffix = line.rsplit("](", 1)[1]
                    lines[index] = f"- [{number}: {title}]({suffix}"
    trailing = "\n" if text.endswith("\n") else ""
    return "\n".join(lines) + trailing


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", default=DEFAULT_TARGETS)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    total, changed = rewrite_case_titles([Path(path) for path in args.paths], dry_run=args.dry_run)
    mode = "Would rewrite" if args.dry_run else "Rewrote"
    print(f"{mode} {changed}/{total} case titles")


if __name__ == "__main__":
    main()
