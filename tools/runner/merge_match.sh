#!/bin/bash
# Put a dataset's paper match on main, whatever it says (docs/pipeline.md, step 1). Run from a clone of the
# repository:
#
#   tools/runner/merge_match.sh FOLDER
#
# Takes papers/match/<folder>.yaml and the paper-match run's transcript and report
# (transcripts/<folder>/paper-match*.md, when an agent ran) from the branch attempt/<folder>, validates the
# match file against schemas/paper-match.schema.json, and commits them straight to main, with no pull
# request; when main has moved on in the meantime, it starts again from the new main. On main, the match
# decides which paper an attempt uses, and holds a dataset with no usable paper out of the queue
# (tools/runner/describe.py). Works in a temporary worktree, so the clone's checkout is left alone.
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
  git -C "$tmp" checkout -q "origin/attempt/$d" -- "papers/match/$d.yaml"
  git -C "$tmp" ls-tree --name-only "origin/attempt/$d" "transcripts/$d/" | { grep '/paper-match[^/]*\.md$' || true; } \
    | xargs -r git -C "$tmp" checkout -q "origin/attempt/$d" --
  if git -C "$tmp" diff --cached --quiet; then echo "$d: main already has this paper match"; exit 0; fi
  (cd "$tmp" && python3 tools/paper_match.py validate "papers/match/$d.yaml") \
    || { echo "$d: the paper match does not validate; not merged"; exit 1; }
  status=$(cd "$tmp" && python3 tools/paper_match.py status "$d")
  git -C "$tmp" -c user.name='github-actions[bot]' -c user.email='github-actions[bot]@users.noreply.github.com' \
    commit -q -m "Paper match for $label: $status" \
    -m "From attempt/$d (docs/pipeline.md, step 1)."
  if git -C "$tmp" push -q origin HEAD:main 2>/dev/null; then echo "$d: paper match merged into main ($status)"; exit 0; fi
  sleep $((try * 5))
done
echo "$d: could not push the paper match to main"; exit 1
