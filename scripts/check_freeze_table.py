#!/usr/bin/env python3
"""Check Table 1 of paper/sections/03-chain.md against the repositories.

For every row (repository, tag, short commit, date) the tag must exist in
the local clone, peel to that commit and carry that tagger date. Usage:

    python scripts/check_freeze_table.py --repos-dir <dir with the clones>

Exit status 1 on any mismatch. Standard library and git only.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROW = re.compile(r"^\| ([\w.-]+) \| `([^`]+)` \| `([0-9a-f]{7})` \| (\d{4}-\d{2}-\d{2}) \|")


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True).stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-dir", type=Path, required=True)
    ap.add_argument("--table", type=Path, default=Path("paper/sections/03-chain.md"))
    a = ap.parse_args()
    rows = [m.groups() for m in map(ROW.match, a.table.read_text(encoding="utf-8").splitlines()) if m]
    bad = 0
    for repo, tag, commit, date in rows:
        r = a.repos_dir / repo
        got = git(r, "rev-parse", "--short=7", f"refs/tags/{tag}^{{commit}}")
        when = git(r, "for-each-ref", "--format=%(taggerdate:short)", f"refs/tags/{tag}")
        if got != commit or when != date:
            bad += 1
            print(f"MISMATCH {repo} {tag}: table {commit} {date}, git {got or 'missing'} {when or 'no tagger date'}")
    print(f"{len(rows)} rows checked, {bad} mismatch(es)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
