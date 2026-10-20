#!/bin/bash
# Merge a dataset's checked claims file into main ahead of its attempt: the checkpoint after the claims
# check (docs/pipeline.md). Run from a clone of the repository:
#
#   tools/runner/merge_claims.sh FOLDER
#
# Takes claims/<folder>/ from the branch attempt/<folder>, opens a pull request from claims/<folder> with
# that alone, waits for its checks and merges it. Works in a temporary worktree, so the clone's checkout is
# left alone. When the attempt itself is merged later, its rebase on main drops the change main already
# has. Prints the pull request, or says there was nothing to merge.
set -euo pipefail
d=$1
tmp=$(mktemp -d)
trap 'git worktree remove --force "$tmp" >/dev/null 2>&1 || true; rm -rf "$tmp"' EXIT
git fetch -q origin main "attempt/$d"
git worktree add -q -f -B "claims/$d" "$tmp" origin/main
git -C "$tmp" checkout -q "origin/attempt/$d" -- "claims/$d"
if git -C "$tmp" diff --cached --quiet; then echo "$d: main already has these claims"; exit 0; fi
label=$(python3 "$(dirname "$0")/describe.py" label "$d" 2>/dev/null || echo "$d")
git -C "$tmp" -c user.name='github-actions[bot]' -c user.email='github-actions[bot]@users.noreply.github.com' \
  commit -q -m "Claims for $label, checked" -m "From attempt/$d, after its claims check said the file is ready (docs/pipeline.md)."
git -C "$tmp" push -q --force origin "claims/$d"
pr=$(gh pr list --head "claims/$d" --state open --json url --jq '.[0].url // empty')
[ -n "$pr" ] || pr=$(gh pr create --base main --head "claims/$d" --title "Claims for $label, checked" \
  --body "The claims file for $label, read from the paper and checked by a second reader, merged ahead of the attempt, which goes on in \`attempt/$d\` (docs/pipeline.md).

🤖 Generated with [Claude Code](https://claude.com/claude-code)")
echo "$d: $pr"
while true; do
  s=$(gh pr checks "$pr" --json bucket 2>/dev/null) || { sleep 30; continue; }
  echo "$s" | jq -e 'length>0 and all(.bucket!="pending")' >/dev/null && break
  sleep 30
done
if echo "$s" | jq -e 'all(.bucket=="pass" or .bucket=="skipping")' >/dev/null; then
  if gh pr merge "$pr" --merge >/dev/null; then
    git push -q origin --delete "claims/$d" 2>/dev/null || true
    echo "$d: claims merged"; exit 0
  fi
fi
echo "$d: the claims pull request did not pass its checks: $pr"; exit 1
