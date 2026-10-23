#!/usr/bin/env python3
"""Log literature-search queries at run time and render them for the search record.

Used by `literature-search` (see ../references/modes-literature.md, step 4). Each
query is appended to a JSONL log as soon as it runs, so the search record can
report real hit counts instead of reconstructing them later.

Subcommands:
  add     append one query row (source, query, filters, returned count, retained IDs)
  render  print the log as a Markdown table for the search record

A count that was not captured is stored as null and rendered as `not logged`.

Usage:
  log_search.py add --log docs/literature/search_log_2026-10-23.jsonl \
      --source PubMed --query "ethnic AND heart failure" --filters "from 2015" \
      --count 143 --retained N001,N004
  log_search.py render --log docs/literature/search_log_2026-10-23.jsonl
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path


def add(args: argparse.Namespace) -> int:
    row = {
        "logged_at": dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds"),
        "source": args.source,
        "query": args.query,
        "filters": args.filters or "",
        "count": args.count,
        "retained": [x for x in (args.retained or "").split(",") if x],
        "note": args.note or "",
    }
    log = Path(args.log)
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return 0


def render(args: argparse.Namespace) -> int:
    log = Path(args.log)
    if not log.exists():
        print(f"no log at {log}", file=sys.stderr)
        return 2
    rows = [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines() if line.strip()]

    def cell(text: str) -> str:
        # Display-only escaping; the JSONL log keeps the original text.
        # Line breaks become " ↵ " so a row stays one table line (also inside code spans).
        flat = str(text).replace("\r\n", "\n").replace("\r", "\n").replace("\n", " ↵ ")
        return flat.replace("|", "\\|")

    print("| # | Logged at | Source | Query | Filters | Returned | Retained |")
    print("| --- | --- | --- | --- | --- | ---: | --- |")
    for i, r in enumerate(rows, 1):
        count = "not logged" if r.get("count") is None else r["count"]
        print(
            f"| {i} | {r['logged_at']} | {cell(r['source'])} | `{cell(r['query'])}` | "
            f"{cell(r.get('filters', ''))} | {count} | {', '.join(r.get('retained', []))} |"
        )
    logged = [r["count"] for r in rows if r.get("count") is not None]
    print(f"\n{len(rows)} queries; {len(logged)} with counts; {sum(logged)} records returned before de-duplication.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("--log", required=True)
    a.add_argument("--source", required=True)
    a.add_argument("--query", required=True)
    a.add_argument("--filters")
    a.add_argument("--count", type=int)
    a.add_argument("--retained", help="comma-separated source IDs kept from this query")
    a.add_argument("--note")
    r = sub.add_parser("render")
    r.add_argument("--log", required=True)
    args = p.parse_args()
    return add(args) if args.cmd == "add" else render(args)


if __name__ == "__main__":
    sys.exit(main())
