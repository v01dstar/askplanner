#!/usr/bin/env python3
"""Generate TiDB BR issue precedent cases from GitHub.

The output is intentionally searchable markdown. It is not a final playbook;
it is a local precedent corpus for deciding whether a new backup/restore
symptom has appeared before.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from rewrite_case_titles import rewrite_case_titles
from sanitize_case_corpus import sanitize_files


DEFAULT_QUERY_LABEL = "component/br"
MAX_BODY_CHARS = 20000


CATEGORY_RULES: list[tuple[str, list[str]]] = [
    ("pitr-log-restore", ["pitr", "point restore", "restore point", "log backup", "log restore", "resolved-ts", "resolved ts"]),
    ("restore-failure", ["restore failed", "restore fail", "restoring", "restore hang", "restore stuck", "restore panic"]),
    ("backup-failure", ["backup failed", "backup fail", "backup hang", "backup stuck", "backup panic", "backup sql"]),
    ("storage-access", ["s3", "gcs", "azure", "blob", "hdfs", "nfs", "storage", "credential", "credentials", "iam", "access denied", "permission", "tls", "io error", "i/o error"]),
    ("schema-metadata", ["schema", "metadata", "ddl", "system table", "mysql.", "column mismatch", "table filter", "placement", "temporary table"]),
    ("region-split-scatter", ["region", "split", "scatter", "pre-split", "presplit", "split key", "store count"]),
    ("sst-ingest-import", ["sst", "ingest", "import", "download", "rewrite", "merge migration", "migration"]),
    ("checkpoint-retry", ["checkpoint", "retry", "backoff", "resume", "pause", "progress", "checkpoint file"]),
    ("performance-resource", ["slow", "performance", "oom", "memory", "cpu", "throughput", "concurrency", "limiter", "quota", "stuck"]),
    ("checksum-consistency", ["checksum", "consistency", "data loss", "corrupt", "inconsistent", "wrong result"]),
    ("gc-safepoint", ["gc", "safe point", "safepoint", "service safe point"]),
    ("compatibility-upgrade", ["compatib", "upgrade", "downgrade", "new backup", "old br", "version mismatch", "column mismatch"]),
    ("observability-diagnosis", ["error message", "summary", "log", "diagnose", "diagnostic", "metrics"]),
]

COMPONENT_RULES: list[tuple[str, list[str]]] = [
    ("TiDB", ["tidb", "sql", "schema", "ddl", "mysql.", "system table", "gc", "safepoint", "checksum"]),
    ("TiKV", ["tikv", "sst", "ingest", "raft", "region", "split", "scatter", "compaction", "resolved-ts", "resolved ts"]),
    ("Operator", ["operator", "backup cr", "restore cr", "kubernetes", "k8s", "pod", "secret", "service account", "pvc"]),
    ("BR", ["br", "backup", "restore", "checkpoint", "pitr", "log backup"]),
    ("Lightning", ["lightning", "import", "local sort"]),
    ("Storage", ["s3", "gcs", "azure", "blob", "hdfs", "nfs", "storage", "credential", "iam", "tls", "endpoint"]),
    ("PD", [" pd ", "pd-", "pd.", "placement", "scheduler", "tso"]),
]


def run_gh_issue_list(repo: str, label: str, limit: int) -> list[dict[str, Any]]:
    cmd = [
        "gh",
        "issue",
        "list",
        "--repo",
        repo,
        "--state",
        "all",
        "--label",
        label,
        "--limit",
        str(limit),
        "--json",
        "number,title,state,labels,createdAt,updatedAt,closedAt,url,author,body",
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def slugify(value: str, limit: int = 90) -> str:
    value = value.lower()
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    if len(value) > limit:
        value = value[:limit].rstrip("-")
    return value or "untitled"


def labels(issue: dict[str, Any]) -> list[str]:
    return sorted(label["name"] for label in issue.get("labels", []))


def text_for(issue: dict[str, Any]) -> str:
    return f"{issue.get('title', '')}\n{issue.get('body', '')}".lower()


def has_keyword(text: str, keyword: str) -> bool:
    keyword = keyword.lower()
    if re.fullmatch(r"[a-z0-9_+-]+", keyword):
        return re.search(rf"(?<![a-z0-9_+-]){re.escape(keyword)}(?![a-z0-9_+-])", text) is not None
    return keyword in text


def classify_categories(issue: dict[str, Any]) -> list[str]:
    text = text_for(issue)
    found = [name for name, words in CATEGORY_RULES if any(has_keyword(text, word) for word in words)]
    return found or ["uncategorized"]


def classify_components(issue: dict[str, Any]) -> list[str]:
    text = f" {text_for(issue)} "
    found = [name for name, words in COMPONENT_RULES if any(has_keyword(text, word) for word in words)]
    return found or ["BR"]


def classify_operation(issue: dict[str, Any]) -> str:
    text = text_for(issue)
    if any(word in text for word in ["pitr", "point restore", "restore point", "log backup", "log restore"]):
        return "PITR"
    if any(word in text for word in ["lightning", "import"]):
        return "Import"
    if "restore" in text:
        return "Restore"
    if "backup" in text:
        return "Backup"
    return "Backup/Restore"


def classify_architecture(issue: dict[str, Any]) -> str:
    text = text_for(issue)
    if any(word in text for word in ["tidb x", "tidbx", "byoc", "tidb cloud"]):
        return "TiDBX"
    if any(word in text for word in ["operator", "kubernetes", "k8s", "tiup", "self-hosted", "classic"]):
        return "Classic"
    return "Unknown"


def affected_versions(label_names: list[str]) -> list[str]:
    versions = []
    for label in label_names:
        if label.startswith("affects-") or label.startswith("may-affects-"):
            versions.append(label)
    return versions


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def is_bugfix_precedent(issue: dict[str, Any]) -> bool:
    label_names = set(labels(issue))
    if "type/feature-request" in label_names or "type/enhancement" in label_names:
        return False

    text = text_for(issue)
    title = (issue.get("title") or "").lower()
    bug_signals = [
        "failed",
        "failure",
        "error",
        "panic",
        "oom",
        "stuck",
        "hang",
        "timeout",
        "too slow",
        "inconsistent",
        "data loss",
        "wrong",
        "leak",
        "nil pointer",
        "invalid",
        "cannot",
        "can't",
        "does not",
        "not accurate",
        "mismatch",
        "too high",
        "too small",
        "silently",
        "exceeds",
        "lag",
    ]
    feature_signals = [
        "support ",
        "feature request",
        "enhancement",
        "refactor",
        "tracking issue",
        "deliver ",
        "add ",
        "implement ",
        "security issue",
    ]
    if any(signal in title for signal in feature_signals) and not any(signal in title for signal in bug_signals):
        return False
    if "type/bug" in label_names or "type/regression" in label_names:
        return any(signal in text for signal in bug_signals)
    return any(signal in text for signal in bug_signals) and not any(signal in text for signal in feature_signals)


def is_test_noise(issue: dict[str, Any]) -> bool:
    label_names = set(labels(issue))
    if "component/test" in label_names or "flaky-test" in label_names:
        return True
    title = (issue.get("title") or "").lower()
    test_signals = [
        "flaky",
        " unit test",
        "integration test",
        " test ",
        "ci fail",
        "ci failed",
        "test failure",
        "stabilize ",
        "run_group_br_tests",
    ]
    return any(signal in f" {title} " for signal in test_signals)


def filter_issues(
    issues: list[dict[str, Any]],
    since: datetime | None,
    bugfix_only: bool,
    exclude_tests: bool,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    stats = Counter()
    selected: list[dict[str, Any]] = []
    for issue in issues:
        stats["fetched"] += 1
        label_names = set(labels(issue))
        created_at = parse_time(issue.get("createdAt"))
        if since and created_at and created_at < since:
            stats["excluded_before_since"] += 1
            continue
        if exclude_tests and is_test_noise(issue):
            stats["excluded_test_noise"] += 1
            continue
        if bugfix_only and not is_bugfix_precedent(issue):
            stats["excluded_non_bugfix"] += 1
            continue
        selected.append(issue)
        stats["selected"] += 1
    return selected, dict(stats)


def linked_prs(issue: dict[str, Any]) -> list[str]:
    text = issue.get("body") or ""
    urls = set(re.findall(r"https://github\.com/pingcap/tidb/pull/\d+", text))
    refs = set(re.findall(r"(?<![\w/])#(\d{4,6})(?!\w)", text))
    for ref in refs:
        urls.add(f"https://github.com/pingcap/tidb/pull/{ref}")
    return sorted(urls)


def format_body(body: str) -> str:
    body = body.strip()
    if not body:
        return "_No issue body captured._"
    if len(body) <= MAX_BODY_CHARS:
        return body
    return body[:MAX_BODY_CHARS].rstrip() + "\n\n_Trimmed. See the GitHub issue for full context._"


def case_markdown(issue: dict[str, Any]) -> str:
    label_names = labels(issue)
    categories = classify_categories(issue)
    components = classify_components(issue)
    prs = linked_prs(issue)
    author = issue.get("author") or {}
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def val(name: str) -> str:
        return issue.get(name) or ""

    lines = [
        f"# Issue {issue['number']}: {issue['title']}",
        "",
        "<!-- generated by scripts/generate_tidb_br_issue_cases.py; do not hand-edit generated issue cases -->",
        "",
        "## Source",
        "",
        f"- GitHub issue: {issue['url']}",
        f"- State: {issue['state']}",
        f"- Author: {author.get('login', '')}",
        f"- Created: {val('createdAt')}",
        f"- Updated: {val('updatedAt')}",
        f"- Closed: {val('closedAt') or 'N/A'}",
        f"- Generated: {generated_at}",
        "",
        "## Classification",
        "",
        f"- Architecture: {classify_architecture(issue)}",
        f"- Operation: {classify_operation(issue)}",
        f"- Components: {', '.join(components)}",
        f"- Categories: {', '.join(categories)}",
        f"- Labels: {', '.join(label_names) if label_names else 'N/A'}",
        f"- Affected versions: {', '.join(affected_versions(label_names)) or 'N/A'}",
        "",
        "## Quick Match",
        "",
        f"- Title/error signature: `{issue['title']}`",
        f"- Search terms: {'; '.join(sorted(set(categories + components + [classify_operation(issue)])))}",
        "",
        "## Linked PRs Mentioned In Body",
        "",
    ]
    if prs:
        lines.extend(f"- {url}" for url in prs)
    else:
        lines.append("- N/A")
    lines.extend([
        "",
        "## Issue Body",
        "",
        format_body(issue.get("body") or ""),
        "",
    ])
    return "\n".join(lines)


def write_readme(
    out_dir: Path,
    issues: list[dict[str, Any]],
    files: dict[int, str],
    filter_stats: dict[str, int],
    since: datetime | None,
    bugfix_only: bool,
    exclude_tests: bool,
) -> None:
    state_counts = Counter(issue["state"] for issue in issues)
    category_counts: Counter[str] = Counter()
    component_counts: Counter[str] = Counter()
    operation_counts: Counter[str] = Counter()
    for issue in issues:
        category_counts.update(classify_categories(issue))
        component_counts.update(classify_components(issue))
        operation_counts.update([classify_operation(issue)])

    lines = [
        "# TiDB BR Issue Cases",
        "",
        "<!-- generated by scripts/generate_tidb_br_issue_cases.py; do not hand-edit generated issue index -->",
        "",
        f"Generated from `pingcap/tidb` issues with label `{DEFAULT_QUERY_LABEL}`.",
        "",
        "## Filters",
        "",
        f"- Since: {since.date().isoformat() if since else 'none'}",
        f"- Bugfix only: {str(bugfix_only).lower()}",
        f"- Exclude test noise: {str(exclude_tests).lower()}",
        f"- Fetched before filters: {filter_stats.get('fetched', len(issues))}",
        f"- Excluded before since: {filter_stats.get('excluded_before_since', 0)}",
        f"- Excluded non-bugfix: {filter_stats.get('excluded_non_bugfix', 0)}",
        f"- Excluded test noise: {filter_stats.get('excluded_test_noise', 0)}",
        "",
        "## Summary",
        "",
        f"- Total issues: {len(issues)}",
        f"- Open: {state_counts.get('OPEN', 0)}",
        f"- Closed: {state_counts.get('CLOSED', 0)}",
        "",
        "## Category Counts",
        "",
    ]
    lines.extend(f"- `{name}`: {count}" for name, count in category_counts.most_common())
    lines.extend(["", "## Component Counts", ""])
    lines.extend(f"- `{name}`: {count}" for name, count in component_counts.most_common())
    lines.extend(["", "## Operation Counts", ""])
    lines.extend(f"- `{name}`: {count}" for name, count in operation_counts.most_common())
    lines.extend(["", "## Cases", ""])
    for issue in sorted(issues, key=lambda item: item["number"], reverse=True):
        cats = ", ".join(classify_categories(issue))
        lines.append(f"- [{issue['number']}: {issue['title']}]({files[issue['number']]}) - {issue['state']}; {cats}")
    lines.append("")
    out_dir.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def write_precedent_index(
    path: Path,
    issues: list[dict[str, Any]],
    files: dict[int, str],
    since: datetime | None,
    bugfix_only: bool,
) -> None:
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for issue in issues:
        for category in classify_categories(issue):
            by_category[category].append(issue)

    lines = [
        "# BR Issue Precedent Index",
        "",
        "<!-- generated by scripts/generate_tidb_br_issue_cases.py; do not hand-edit generated precedent index -->",
        "",
        "Use this index when a backup/restore symptom appears and you need to check whether a similar TiDB BR issue has happened before.",
        "",
        f"Scope: `component/br`, {'bugfix-oriented' if bugfix_only else 'all issue types'}, created since `{since.date().isoformat() if since else 'no lower bound'}`.",
        "",
        "## How To Use",
        "",
        "1. Match the user symptom to one or more categories below.",
        "2. Open the linked case files and compare title, labels, affected versions, and issue body.",
        "3. If the issue is closed, inspect linked PRs or the GitHub issue timeline for fixed-version evidence.",
        "4. If no category matches, search the case directory directly with `rg '<error text>' references/cases/issues`.",
        "",
    ]
    for category in sorted(by_category):
        category_issues = sorted(by_category[category], key=lambda item: item["number"], reverse=True)
        lines.extend([f"## {category}", ""])
        for issue in category_issues[:80]:
            rel = Path("../cases/issues").joinpath(files[issue["number"]]).as_posix()
            affected = ", ".join(affected_versions(labels(issue))) or "affected version unknown"
            lines.append(f"- [{issue['number']}: {issue['title']}]({rel}) - {issue['state']}; {affected}; {issue['url']}")
        if len(category_issues) > 80:
            lines.append(f"- ... {len(category_issues) - 80} more in `references/cases/issues/README.md`")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="pingcap/tidb")
    parser.add_argument("--label", default=DEFAULT_QUERY_LABEL)
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument("--since", default=None, help="UTC lower bound for createdAt, YYYY-MM-DD. Defaults to two years ago.")
    parser.add_argument("--all-types", action="store_true", help="Include feature/enhancement issues instead of bugfix-oriented filtering.")
    parser.add_argument("--include-tests", action="store_true", help="Include component/test and flaky-test issues.")
    parser.add_argument("--out-dir", default="skills/tidb-backup-restore/references/cases/issues")
    parser.add_argument("--index", default="skills/tidb-backup-restore/references/playbooks/br-issue-precedent-index.md")
    args = parser.parse_args()

    if args.since:
        since = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)
    else:
        since = datetime.now(timezone.utc) - timedelta(days=730)

    fetched_issues = run_gh_issue_list(args.repo, args.label, args.limit)
    issues, filter_stats = filter_issues(
        fetched_issues,
        since=since,
        bugfix_only=not args.all_types,
        exclude_tests=not args.include_tests,
    )
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for old_case in out_dir.glob("issue-*.md"):
        old_case.unlink()

    files: dict[int, str] = {}
    for issue in issues:
        filename = f"issue-{issue['number']}-{slugify(issue['title'])}.md"
        files[issue["number"]] = filename
        out_dir.joinpath(filename).write_text(case_markdown(issue), encoding="utf-8")

    write_readme(out_dir, issues, files, filter_stats, since, not args.all_types, not args.include_tests)
    write_precedent_index(Path(args.index), issues, files, since, not args.all_types)
    sanitize_files([out_dir, Path(args.index)])
    rewrite_case_titles([out_dir, Path(args.index)])
    sanitize_files([out_dir, Path(args.index)])
    print(f"Fetched {filter_stats.get('fetched', len(fetched_issues))} issues")
    print(f"Selected {len(issues)} issue cases after filters")
    print(f"Generated issue cases in {out_dir}")
    print(f"Generated precedent index at {args.index}")


if __name__ == "__main__":
    main()
