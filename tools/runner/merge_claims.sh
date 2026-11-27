#!/bin/bash
# Put a paper's checked claims file on main ahead of its attempt: the checkpoint after the claims check
# (docs/pipeline.md). Run from a clone of the repository:
#
#   tools/runner/merge_claims.sh PAPER [--with-transcripts]
#
# Takes claims/<paper>.yaml from the branch attempt/<paper> (and, with --with-transcripts, the claims
# runs' transcripts and reports, transcripts/<paper>/claims*.md, for a branch that is deleted
# afterwards), validates each claims file against schemas/claims.schema.json, and commits it straight
# to main, with no pull request; when main has moved on in the meantime, it starts again from the new
# main. Works in a temporary worktree, so the clone's checkout is left alone. When the attempt itself
# is merged later, the merge keeps the branch's claims file, the same or later.
set -euo pipefail
d=$1; with_transcripts=${2:-}
here=$(cd "$(dirname "$0")" && pwd)
label=$d
tmp=$(mktemp -d)
trap 'git worktree remove --force "$tmp" >/dev/null 2>&1 || true; rm -rf "$tmp"' EXIT
for try in 1 2 3 4 5; do
  git fetch -q origin main "attempt/$d"
  git worktree remove --force "$tmp" >/dev/null 2>&1 || true; rm -rf "$tmp"
  git worktree add -q --detach "$tmp" origin/main
  bash "$tmp/tools/protocol.sh" "$tmp" >/dev/null   # the protocol main names (schemas/claims.schema.json)
  git -C "$tmp" checkout -q "origin/attempt/$d" -- "claims/$d.yaml"
  if [ "$with_transcripts" = --with-transcripts ]; then
    git -C "$tmp" ls-tree --name-only "origin/attempt/$d" "transcripts/$d/" | { grep '/claims[^/]*\.md$' || true; } \
      | xargs -r git -C "$tmp" checkout -q "origin/attempt/$d" --
  fi
  if git -C "$tmp" diff --cached --quiet; then echo "$d: main already has these claims"; exit 0; fi
  # Not ahead of the attempt when it would break main: the latest attempt on main is checked against main's claims
  # file (tools/entry.py), so a new reading that drops or renames a claim that attempt recorded waits for the new
  # attempt's merge, which brings its claims file and a later record with it. On 2026-11-16 the checkpoint of
  # tingley-2018 renamed one claim, and every attempt's pull request failed its check until it was put back.
  dropped=$(cd "$tmp" && python - "$d" <<'PY'
import re, sys
from pathlib import Path
import yaml
d = sys.argv[1]
records = sorted(p for p in Path("attempts").glob(f"{d}-*.yaml") if re.fullmatch(rf"{re.escape(d)}-\d\d\.yaml", p.name))
if records:
    used = {o.get("claim") for o in (yaml.safe_load(records[-1].read_text()) or {}).get("outcomes") or []}
    have = {c.get("id") for c in (yaml.safe_load(Path(f"claims/{d}.yaml").read_text()) or {}).get("claims") or []}
    print(" ".join(sorted(x for x in used - have if x)))
PY
)
  if [ -n "$dropped" ]; then
    echo "$d: the new claims file has no claim $dropped, which the attempt on main records; left for the attempt's merge"
    exit 0
  fi
  (cd "$tmp" && python - "claims/$d.yaml" <<'PY'
import json, sys
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator
def plain(v):   # YAML dates as strings, so the schema's formats apply
    return ({k: plain(x) for k, x in v.items()} if isinstance(v, dict) else [plain(x) for x in v]
            if isinstance(v, list) else v.isoformat() if hasattr(v, "isoformat") else v)
schema = Draft202012Validator(json.loads(Path("schemas/claims.schema.json").read_text()))
bad = 0
for path in [Path(sys.argv[1])]:
    for err in schema.iter_errors(plain(yaml.safe_load(path.read_text()))):
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
