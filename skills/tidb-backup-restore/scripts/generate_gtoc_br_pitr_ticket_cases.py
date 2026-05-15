#!/usr/bin/env python3
"""Generate anonymized GTOC BR/PITR Jira ticket precedent cases.

Requires the Atlassian MCP configured via mcp-remote and an existing OAuth
session. The generated files are meant for symptom matching, not for storing
raw customer data.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from rewrite_case_titles import rewrite_case_titles
from sanitize_case_corpus import sanitize_files


ATLASSIAN_MCP_URL = "https://mcp.atlassian.com/v1/mcp/authv2"
DEFAULT_CLOUD_ID = "tidb.atlassian.net"
DEFAULT_PROJECT = "GTOC"
MAX_TEXT_CHARS = 9000


CATEGORY_RULES: list[tuple[str, list[str]]] = [
    ("pitr-log-backup-lag", ["pitr", "log backup", "checkpoint", "resolved-ts", "resolved ts", "lag"]),
    ("backup-failure", ["backup failed", "backup failing", "br backup", "backup full", "full backup"]),
    ("restore-failure", ["restore failed", "restore failing", "br restore", "point restore", "restore point"]),
    ("storage-credential", ["s3", "gcs", "aws", "irsa", "webidentity", "web identity", "credential", "sts", "endpoint", "minio", "bucket"]),
    ("tikv-data-path", ["tikv", "sst", "ingest", "raft", "region", "resolved-ts", "resolved ts"]),
    ("operator-cr", ["operator", "backup cr", "restore cr", "log backup cr", "volumebackup", "k8s", "kubernetes", "pod"]),
    ("performance-resource", ["slow", "oom", "memory", "cpu", "timeout", "stuck", "hang", "too many", "large number"]),
    ("compatibility-upgrade", ["upgrade", "downgrade", "version", "8.5", "7.5", "compatib"]),
    ("observability-error-message", ["error message", "not accurate", "summary", "log", "diagnos", "prompt"]),
]


def run_node_mcp_script(script: str, timeout: int = 180) -> str:
    tmpdir = Path(tempfile.mkdtemp(prefix="gtoc-jira-mcp."))
    try:
        subprocess.run(["npm", "init", "-y"], cwd=tmpdir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(
            ["npm", "install", "@modelcontextprotocol/sdk"],
            cwd=tmpdir,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        result = subprocess.run(
            ["node", "--input-type=module"],
            cwd=tmpdir,
            input=script,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr or result.stdout)
        return result.stdout
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def fetch_jira_issues(cloud_id: str, jql: str, max_pages: int) -> list[dict[str, Any]]:
    script = f"""
import {{ Client }} from '@modelcontextprotocol/sdk/client/index.js';
import {{ StdioClientTransport }} from '@modelcontextprotocol/sdk/client/stdio.js';

const transport = new StdioClientTransport({{
  command: 'npx',
  args: ['-y', 'mcp-remote', {json.dumps(ATLASSIAN_MCP_URL)}],
}});
const client = new Client({{ name: 'gtoc-br-pitr-crawler', version: '0.0.1' }});
await client.connect(transport);

async function call(name, args) {{
  const response = await client.callTool({{ name, arguments: args }});
  if (response.isError) throw new Error(JSON.stringify(response));
  const text = response.content?.find((item) => item.type === 'text')?.text ?? '{{}}';
  return JSON.parse(text);
}}

const jql = {json.dumps(jql)};
const fields = ['summary','description','status','issuetype','priority','created','updated','resolution','labels','components','assignee','reporter','comment'];
let nextPageToken = undefined;
let all = [];
for (let page = 0; page < {max_pages}; page++) {{
  const args = {{ cloudId: {json.dumps(cloud_id)}, jql, maxResults: 100, fields, responseContentFormat: 'markdown' }};
  if (nextPageToken) args.nextPageToken = nextPageToken;
  const result = await call('searchJiraIssuesUsingJql', args);
  all.push(...(result.issues ?? []));
  nextPageToken = result.nextPageToken;
  if (!nextPageToken) break;
}}
await client.close();
console.log(JSON.stringify(all));
"""
    stdout = run_node_mcp_script(script)
    json_line = stdout.strip().splitlines()[-1]
    return json.loads(json_line)


def slugify(value: str, limit: int = 90) -> str:
    value = value.lower()
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return (value[:limit].rstrip("-") or "untitled")


def field(issue: dict[str, Any], name: str) -> Any:
    return issue.get("fields", {}).get(name)


def names(values: Any) -> list[str]:
    if not values:
        return []
    return [item.get("name", str(item)) if isinstance(item, dict) else str(item) for item in values]


def plain_name(value: Any) -> str:
    if isinstance(value, dict):
        return value.get("displayName") or value.get("name") or value.get("key") or ""
    return str(value or "")


def stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, list):
        return "\n".join(stringify(item) for item in value)
    if isinstance(value, dict):
        node_type = value.get("type")
        if node_type in {"media", "mediaInline"}:
            return "[REDACTED_MEDIA]"
        if node_type == "mention":
            return "@[REDACTED_USER]"
        if node_type == "inlineCard":
            return sanitize(value.get("attrs", {}).get("url", "[REDACTED_LINK]"))
        if "text" in value and isinstance(value["text"], str):
            return value["text"]
        if "content" in value:
            return stringify(value["content"])
        if "body" in value:
            return stringify(value["body"])
        return ""
    return str(value)


def text_for(issue: dict[str, Any]) -> str:
    parts = [stringify(field(issue, "summary")), stringify(field(issue, "description"))]
    comment = field(issue, "comment") or {}
    for c in comment.get("comments", []) if isinstance(comment, dict) else []:
        parts.append(stringify(c.get("body")))
    parts.extend(names(field(issue, "components")))
    return "\n".join(parts)


def sanitize(text: str) -> str:
    text = text or ""
    text = re.sub(r"https://tidb\.support\.pingcap\.com/[^\s)>\"]+", "[REDACTED_SUPPORT_URL]", text)
    text = re.sub(r"https://clinic\.pingcap\.com/[^\s)>\"]+", "[REDACTED_CLINIC_URL]", text)
    text = re.sub(r"https://teams\.microsoft\.com/[^\s)>\"]+", "[REDACTED_MEETING_URL]", text)
    text = re.sub(r"https://app\.podium-prod\.fkcloud\.in/[^\s)>\"]+", "[REDACTED_CUSTOMER_CONSOLE_URL]", text)
    text = re.sub(r"blob:https://[^\s)]+", "[REDACTED_MEDIA_BLOB]", text)
    text = re.sub(r"!\[\]\(\[REDACTED_MEDIA_BLOB\][^)]+\)", "[REDACTED_MEDIA]", text)
    text = re.sub(r"s3://([^/\s]+)/", "s3://[REDACTED_BUCKET]/", text)
    text = re.sub(r'(?i)(bucket[":\s=]+)[A-Za-z0-9._-]{8,}', r"\1[REDACTED_BUCKET]", text)
    text = re.sub(r'(?i)("?aws_request_id"?\s*[:=]\s*"?)[A-Z0-9+/=]{8,}', r"\1[REDACTED_AWS_REQUEST_ID]", text)
    text = re.sub(r'(?i)("?s3_extended_request_id"?\s*[:=]\s*"?)[A-Za-z0-9+/=]{16,}', r"\1[REDACTED_AWS_EXTENDED_REQUEST_ID]", text)
    text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[REDACTED_EMAIL]", text)
    text = re.sub(r"\b[0-9]{12,}\b", "[REDACTED_LONG_ID]", text)
    text = re.sub(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b", "[REDACTED_UUID]", text)
    text = re.sub(r"AKIA[0-9A-Z]{16}", "[REDACTED_AWS_ACCESS_KEY]", text)
    text = re.sub(r"(?i)(secret|token|password|passwd|api[_-]?key)\s*[:=]\s*\S+", r"\1=[REDACTED_SECRET]", text)
    return text.strip()


def is_relevant(issue: dict[str, Any]) -> bool:
    component_names = set(names(field(issue, "components")))
    if component_names.intersection({"BR", "PiTR", "TiKV BR"}):
        return True
    summary = (field(issue, "summary") or "").lower()
    description = stringify(field(issue, "description")).lower()
    summary_patterns = [
        r"\bbr\b",
        r"\bpitr\b",
        r"\bbackup\b",
        r"\brestore\b",
        r"\blog backup\b",
        r"\bsnapshot backup\b",
        r"\bsnapshot restore\b",
    ]
    if any(re.search(pattern, summary) for pattern in summary_patterns):
        return True
    description_patterns = [
        "log backup",
        "pitr",
        "br backup",
        "br restore",
        "backup cr",
        "restore cr",
    ]
    return any(pattern in description for pattern in description_patterns)


def classify(issue: dict[str, Any]) -> list[str]:
    text = text_for(issue).lower()
    found = [name for name, words in CATEGORY_RULES if any(word in text for word in words)]
    return found or ["uncategorized"]


def operation(issue: dict[str, Any]) -> str:
    text = text_for(issue).lower()
    if "pitr" in text or "point restore" in text or "restore point" in text or "log backup" in text:
        return "PITR"
    if "restore" in text:
        return "Restore"
    if "backup" in text:
        return "Backup"
    return "Backup/Restore"


def first_lines(text: str, max_lines: int = 18) -> str:
    clean = sanitize(text)
    clean = re.sub(r"\\n{3,}", "\n\n", clean)
    if len(clean) > MAX_TEXT_CHARS:
        clean = clean[:MAX_TEXT_CHARS].rstrip() + "\n\n_Trimmed; see Jira for full context._"
    lines = clean.splitlines()
    return "\n".join(lines[:max_lines]).strip() or "_No text captured._"


def comments_excerpt(issue: dict[str, Any]) -> str:
    comment = field(issue, "comment") or {}
    comments = comment.get("comments", []) if isinstance(comment, dict) else []
    if not comments:
        return "_No comments captured._"
    excerpts = []
    for c in comments[-5:]:
        author = plain_name(c.get("author"))
        created = c.get("created", "")
        body = first_lines(stringify(c.get("body")), max_lines=8)
        excerpts.append(f"### {created} {author}\n\n{body}")
    return "\n\n".join(excerpts)


def case_markdown(issue: dict[str, Any]) -> str:
    key = issue["key"]
    summary = field(issue, "summary") or ""
    status = field(issue, "status") or {}
    priority = field(issue, "priority") or {}
    resolution = field(issue, "resolution") or {}
    issue_type = field(issue, "issuetype") or {}
    components = names(field(issue, "components"))
    labels = field(issue, "labels") or []
    categories = classify(issue)

    return "\n".join([
        f"# {key}: {summary}",
        "",
        "<!-- generated by scripts/generate_gtoc_br_pitr_ticket_cases.py; do not hand-edit generated ticket cases -->",
        "",
        "## Source",
        "",
        f"- Jira: https://tidb.atlassian.net/browse/{key}",
        f"- Status: {status.get('name', '')}",
        f"- Resolution: {resolution.get('name', 'N/A') if resolution else 'N/A'}",
        f"- Priority: {priority.get('name', '')}",
        f"- Issue type: {issue_type.get('name', '')}",
        f"- Created: {field(issue, 'created')}",
        f"- Updated: {field(issue, 'updated')}",
        f"- Reporter: {plain_name(field(issue, 'reporter'))}",
        f"- Assignee: {plain_name(field(issue, 'assignee')) or 'Unassigned'}",
        "",
        "## Classification",
        "",
        "- Architecture: Unknown",
        f"- Operation: {operation(issue)}",
        f"- Components: {', '.join(components) or 'N/A'}",
        f"- Categories: {', '.join(categories)}",
        f"- Labels: {', '.join(labels) if labels else 'N/A'}",
        "",
        "## Symptom / Description Excerpt",
        "",
        first_lines(stringify(field(issue, "description")), max_lines=28),
        "",
        "## Recent Comments Excerpt",
        "",
        comments_excerpt(issue),
        "",
    ])


def write_outputs(out_dir: Path, summary_path: Path, issues: list[dict[str, Any]], jql: str, since: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("gtoc-*.md"):
        old.unlink()

    files: dict[str, str] = {}
    category_counts: Counter[str] = Counter()
    operation_counts: Counter[str] = Counter()
    component_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()

    for issue in issues:
        key = issue["key"]
        filename = f"{key.lower()}-{slugify(field(issue, 'summary') or '')}.md"
        files[key] = filename
        out_dir.joinpath(filename).write_text(case_markdown(issue), encoding="utf-8")
        category_counts.update(classify(issue))
        operation_counts.update([operation(issue)])
        component_counts.update(names(field(issue, "components")))
        status_counts.update([(field(issue, "status") or {}).get("name", "Unknown")])

    lines = [
        "# GTOC BR/PITR Ticket Summary",
        "",
        "<!-- generated by scripts/generate_gtoc_br_pitr_ticket_cases.py; do not hand-edit generated ticket summary -->",
        "",
        "This index summarizes recent GTOC Jira tickets related to BR, PITR, backup, restore, and log backup. It is intended for precedent matching when investigating a new backup/restore incident.",
        "",
        "## Query",
        "",
        f"- Since: `{since}`",
        f"- JQL: `{jql}`",
        f"- Total tickets: {len(issues)}",
        "",
        "## Status Counts",
        "",
    ]
    lines.extend(f"- `{k}`: {v}" for k, v in status_counts.most_common())
    lines.extend(["", "## Operation Counts", ""])
    lines.extend(f"- `{k}`: {v}" for k, v in operation_counts.most_common())
    lines.extend(["", "## Component Counts", ""])
    lines.extend(f"- `{k}`: {v}" for k, v in component_counts.most_common())
    lines.extend(["", "## Category Counts", ""])
    lines.extend(f"- `{k}`: {v}" for k, v in category_counts.most_common())
    lines.extend(["", "## High-Signal Recent Tickets", ""])
    for issue in issues[:40]:
        key = issue["key"]
        cats = ", ".join(classify(issue))
        status = (field(issue, "status") or {}).get("name", "Unknown")
        updated = field(issue, "updated")
        lines.append(f"- [{key}: {field(issue, 'summary')}]({Path('../cases/tickets/gtoc').joinpath(files[key]).as_posix()}) - {status}; updated {updated}; {cats}; https://tidb.atlassian.net/browse/{key}")
    if len(issues) > 40:
        lines.append(f"- ... {len(issues) - 40} more in `references/cases/tickets/gtoc/`")
    lines.append("")

    readme_lines = [
        "# GTOC BR/PITR Ticket Cases",
        "",
        "<!-- generated by scripts/generate_gtoc_br_pitr_ticket_cases.py; do not hand-edit generated ticket index -->",
        "",
        f"Generated from `{DEFAULT_PROJECT}` Jira tickets updated since `{since}`.",
        "",
        f"- Total tickets: {len(issues)}",
        "",
        "## Cases",
        "",
    ]
    for issue in issues:
        key = issue["key"]
        readme_lines.append(f"- [{key}: {field(issue, 'summary')}]({files[key]}) - {(field(issue, 'status') or {}).get('name', 'Unknown')}; {', '.join(classify(issue))}")
    readme_lines.append("")

    out_dir.joinpath("README.md").write_text("\n".join(readme_lines), encoding="utf-8")
    summary_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cloud-id", default=DEFAULT_CLOUD_ID)
    parser.add_argument("--project", default=DEFAULT_PROJECT)
    parser.add_argument("--since", default=None, help="Updated lower bound, YYYY-MM-DD. Defaults to two years ago.")
    parser.add_argument("--max-pages", type=int, default=10)
    parser.add_argument("--out-dir", default="skills/tidb-backup-restore/references/cases/tickets/gtoc")
    parser.add_argument("--summary", default="skills/tidb-backup-restore/references/playbooks/gtoc-br-pitr-ticket-summary.md")
    args = parser.parse_args()

    if args.since:
        since = args.since
    else:
        since = (datetime.now(timezone.utc) - timedelta(days=730)).date().isoformat()

    jql = (
        f'project = {args.project} AND updated >= "{since}" AND '
        '(component in (BR, PiTR, "TiKV BR") OR summary ~ "backup" OR summary ~ "restore" OR '
        'summary ~ "pitr" OR summary ~ "BR" OR description ~ "pitr" OR description ~ "log backup") '
        "ORDER BY updated DESC"
    )
    issues = [issue for issue in fetch_jira_issues(args.cloud_id, jql, args.max_pages) if is_relevant(issue)]
    out_dir = Path(args.out_dir)
    summary = Path(args.summary)
    write_outputs(out_dir, summary, issues, jql, since)
    sanitize_files([out_dir, summary])
    rewrite_case_titles([out_dir, summary])
    sanitize_files([out_dir, summary])
    print(f"Fetched {len(issues)} Jira tickets")
    print(f"Generated cases in {args.out_dir}")
    print(f"Generated summary at {args.summary}")


if __name__ == "__main__":
    main()
