#!/bin/bash
# Put a dataset's checked claims file on main ahead of its attempt: the checkpoint after the claims check
# (docs/pipeline.md). Run from a clone of the repository:
#
#   tools/runner/merge_claims.sh FOLDER
#
# Takes claims/<folder>/ from the branch attempt/<folder>, validates each file against
# schemas/claims.schema.json, and commits it straight to main, with no pull request; when main has
# moved on in the meantime, it starts again from the new main. Works in a temporary worktree, so the
# clone's checkout is left alone. When the attempt itself is merged later, its rebase on main drops the
# change main already has.
set -euo pipefail
d=$1
here=$(cd "$(dirname "$0")" && pwd)
label=$(python3 "$here/describe.py" label "$d" 2>/dev/null || echo "$d")
tmp=$(mktemp -d)
trap 'git worktree remove --force "$tmp" >/dev/null 2>&1 || true; rm -rf "$tmp"' EXIT
for try in 1 2 3 4 5; do
  git fetch -q origin main "attempt/$d"
  git worktree remove --force "$tmp" >/dev/null 2>&1 || true; rm -rf "$tmp"
  git worktree add -q --detach "$tmp" origin/main
  git -C "$tmp" checkout -q "origin/attempt/$d" -- "claims/$d"
  if git -C "$tmp" diff --cached --quiet; then echo "$d: main already has these claims"; exit 0; fi
  (cd "$tmp" && python - "claims/$d" <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, "tools")
import yaml
from entry import _plain, schema
bad = 0
for path in sorted(Path(sys.argv[1]).glob("*.yaml")):
    for err in schema("claims").iter_errors(_plain(yaml.safe_load(path.read_text()))):
        print(f"{path}: {'/'.join(map(str, err.path)) or '(top level)'}: {err.message}")
        bad += 1
sys.exit(1 if bad else 0)
PY
  ) || { echo "$d: the claims file does not validate; not merged"; exit 1; }
  git -C "$tmp" -c user.name='github-actions[bot]' -c user.email='github-actions[bot]@users.noreply.github.com' \
    commit -q -m "Claims for $label, checked" \
    -m "From attempt/$d, after its claims check said the file is ready (docs/pipeline.md)."
  if git -C "$tmp" push -q origin HEAD:main 2>/dev/null; then echo "$d: claims merged into main"; exit 0; fi
  sleep $((try * 5))
done
echo "$d: could not push the claims to main"; exit 1
