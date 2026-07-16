#!/usr/bin/env python3
"""Verify the evidence-extraction cache against its source full-text markdown.

Project-agnostic checker for the `gap-synthesis` large-corpus map-reduce
(see ../references/evidence-extraction-contract.md). It enforces the trust
mechanism of the cache:

  * every `quote` anchor must appear verbatim (whitespace/case/markdown-normalized)
    in the paper's source markdown  -> HARD FAIL if missing;
  * every quantitative finding must be anchored: a row with no anchor, or
    `anchor_kind: none` on a `verification_status: fulltext_verified` record,
    is a HARD FAIL (the no-unanchored-number rule);
  * `section`/`table` anchors are soft-checked (WARN if not found);
  * each record's `source_sha256` must match the markdown-cache manifest
    (HARD FAIL on mismatch; WARN if the manifest is unavailable).

Exit status: 0 = clean (warnings allowed), 1 = one or more hard failures,
2 = usage/IO error.

Usage:
  verify_extract_anchors.py --extracts docs/literature/extracts \
      --fulltext docs/literature/fulltext \
      --manifest docs/literature/fulltext/manifest.csv
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "error: PyYAML is required (pip install pyyaml)\n"
    )
    sys.exit(2)

VALID_ANCHOR_KINDS = {"quote", "section", "table", "none"}
QUOTE_MAX_WORDS = 25

_WS = re.compile(r"\s+")
_EMPH = re.compile(r"[*_`]+")


def normalize(text: str) -> str:
    """Lowercase, fold unicode, strip markdown emphasis, collapse whitespace."""
    text = unicodedata.normalize("NFKC", text)
    # unify common scientific/punctuation glyphs so quotes still match
    for a, b in (("≥", ">="), ("≤", "<="), ("–", "-"),
                 ("—", "-"), ("−", "-"), ("’", "'"),
                 ("“", '"'), ("”", '"')):
        text = text.replace(a, b)
    text = _EMPH.sub("", text)
    text = _WS.sub(" ", text)
    return text.strip().lower()


def load_frontmatter(path: Path):
    """Return the parsed YAML front-matter dict, or None if absent/invalid."""
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return None
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:  # pragma: no cover
        raise ValueError(f"invalid YAML front-matter: {exc}") from exc
    return data if isinstance(data, dict) else None


def load_manifest_sha(manifest: Path) -> dict[str, str]:
    """Map citation_key (md/pdf filename stem) -> source_sha256 from the manifest."""
    out: dict[str, str] = {}
    with manifest.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        cols = reader.fieldnames or []
        sha_col = next((c for c in cols if "sha" in c.lower()), None)
        key_col = next((c for c in cols if c.lower() in ("md_file", "md")), None)
        if key_col is None:
            key_col = next((c for c in cols if "pdf" in c.lower()), None)
        if sha_col is None or key_col is None:
            return out
        for row in reader:
            stem = Path(str(row[key_col]).strip()).stem
            out[stem] = str(row[sha_col]).strip().lower()
    return out


def check_record(path: Path, fulltext_dir: Path, manifest_sha: dict[str, str]):
    """Return (hard_failures, warnings) lists of message strings for one record."""
    hard: list[str] = []
    warn: list[str] = []

    try:
        fm = load_frontmatter(path)
    except ValueError as exc:
        return [str(exc)], warn
    if fm is None:
        return ["missing or malformed YAML front-matter"], warn

    key = str(fm.get("citation_key", path.stem)).strip()
    vstatus = str(fm.get("verification_status", "")).strip()

    # required identity fields
    for field in ("citation_key", "md_file", "source_sha256", "schema_version"):
        if not fm.get(field):
            hard.append(f"missing required field '{field}'")

    # SHA reconciliation with the markdown-cache manifest
    rec_sha = str(fm.get("source_sha256", "")).strip().lower()
    if manifest_sha:
        exp = manifest_sha.get(key)
        if exp is None:
            warn.append(f"citation_key '{key}' not found in manifest")
        elif rec_sha and rec_sha != exp:
            hard.append(f"source_sha256 mismatch (record {rec_sha[:12]}.. vs manifest {exp[:12]}..)")

    # source markdown for quote checking
    md_path = fulltext_dir / f"{key}.md"
    source_norm = normalize(md_path.read_text(encoding="utf-8")) if md_path.exists() else None
    if source_norm is None:
        warn.append(f"source markdown not found: {md_path}")

    findings = fm.get("findings") or []
    if not isinstance(findings, list):
        hard.append("'findings' must be a list")
        findings = []

    for i, f in enumerate(findings):
        if not isinstance(f, dict):
            hard.append(f"finding[{i}] is not a mapping")
            continue
        label = f.get("claim", f"finding[{i}]")
        kind = str(f.get("anchor_kind", "")).strip().lower()
        anchor = str(f.get("anchor", "")).strip()

        if not kind:
            hard.append(f"{label}: unanchored number (no anchor_kind)")
            continue
        if kind not in VALID_ANCHOR_KINDS:
            hard.append(f"{label}: invalid anchor_kind '{kind}'")
            continue
        if kind == "none":
            if vstatus != "needs_pdf":
                hard.append(f"{label}: anchor_kind 'none' requires verification_status: needs_pdf")
            continue
        if not anchor:
            hard.append(f"{label}: anchor_kind '{kind}' but empty anchor")
            continue

        if kind == "quote":
            if len(anchor.split()) > QUOTE_MAX_WORDS:
                hard.append(f"{label}: quote anchor exceeds {QUOTE_MAX_WORDS} words")
            if source_norm is not None and normalize(anchor) not in source_norm:
                hard.append(f"{label}: quote anchor not found in source markdown")
        else:  # section / table -> soft check
            if source_norm is not None and normalize(anchor) not in source_norm:
                warn.append(f"{label}: {kind} anchor '{anchor}' not located in source (soft)")

    return hard, warn


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extracts", required=True, type=Path, help="extraction-cache directory")
    ap.add_argument("--fulltext", required=True, type=Path, help="source full-text markdown directory")
    ap.add_argument("--manifest", type=Path, help="markdown-cache manifest CSV (for SHA reconciliation)")
    args = ap.parse_args()

    if not args.extracts.is_dir():
        sys.stderr.write(f"error: extracts dir not found: {args.extracts}\n")
        return 2
    if not args.fulltext.is_dir():
        sys.stderr.write(f"error: fulltext dir not found: {args.fulltext}\n")
        return 2

    manifest_sha: dict[str, str] = {}
    if args.manifest:
        if args.manifest.exists():
            manifest_sha = load_manifest_sha(args.manifest)
        else:
            sys.stderr.write(f"warning: manifest not found: {args.manifest}; skipping SHA check\n")

    records = sorted(p for p in args.extracts.glob("*.md") if p.name.lower() != "readme.md")
    if not records:
        sys.stderr.write(f"error: no extract records (*.md) in {args.extracts}\n")
        return 2

    total_hard = 0
    total_warn = 0
    failed_files = 0
    for path in records:
        hard, warn = check_record(path, args.fulltext, manifest_sha)
        if hard or warn:
            print(f"\n{path.name}:")
            for m in hard:
                print(f"  FAIL  {m}")
            for m in warn:
                print(f"  warn  {m}")
        if hard:
            failed_files += 1
        total_hard += len(hard)
        total_warn += len(warn)

    print(
        f"\nchecked {len(records)} records | "
        f"{total_hard} hard failure(s) across {failed_files} file(s) | "
        f"{total_warn} warning(s)"
    )
    return 1 if total_hard else 0


if __name__ == "__main__":
    sys.exit(main())
