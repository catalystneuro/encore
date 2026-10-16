#!/bin/bash
# One attempt on one dandiset, start to finish, run from a clone of the repository:
#
#   tools/runner/chain.sh DANDISET [VERSION]
#
# Runs the roles of the attempt (author, two verification rounds and their revisions, a third round
# when the last revision proposed changes) in GitHub Actions, one after another, then records and
# merges it. Picks up where an earlier chain stopped: roles already committed to the branch
# attempt/<dandiset> are skipped, and a run of the next role that is still going is waited for. A
# branch already merged into main belongs to an earlier attempt and is deleted first, so a repeat
# attempt starts from main. A run that fails on the subscription's session limit is retried after
# 30 minutes from where it started; any other failure stops the chain.
#
# Finishing takes a lock ($RUNNER_STATE/finalize.lock), so that one attempt at a time is rebased on
# main, recorded (the recorder role adds the README row and the pilot notes) and merged once its
# checks pass; each lands on a main that has the ones before it.
#
# The last line printed is "<dandiset> MERGED <pr>", "<dandiset> STOPPED ...", or
# "<dandiset> CHECKS FAILED <pr>", which leaves the pull request open.
set -uo pipefail
d=$1; VERSION=${2:-}
STATE=${RUNNER_STATE:-/tmp}
here=$(cd "$(dirname "$0")" && pwd)
export REGISTRY_ROOT=$PWD
log(){ echo "$(date -u +%Y-%m-%dT%H:%MZ) $d $*"; }

remote_branch(){ git ls-remote --heads origin "attempt/$d" | cut -f1; }
fetch(){ git fetch -q origin main 2>/dev/null || true; git fetch -q origin "attempt/$d" 2>/dev/null || true; }
# Roles committed on the branch since it left main, most recent last.
done_roles(){ git log --reverse --format=%s origin/main..origin/attempt/"$d" 2>/dev/null \
  | sed -nE "s/^Agent run on $d: ([a-z0-9-]+) \(success\)$/\1/p"; }
is_done(){ done_roles | grep -qx "$1"; }
run_of(){ gh run list --workflow attempt.yml --limit 100 --json databaseId,displayTitle,status \
  | python "$here/describe.py" run "$d" "$1"; }
wait_run(){ local st; while true; do
  st=$(gh run view "$1" --json status,conclusion --jq '"\(.status) \(.conclusion)"' 2>/dev/null) || { sleep 60; continue; }
  case "$st" in completed*) echo "${st#completed }"; return;; esac; sleep 60; done; }

run_role(){ local role=$1 tries=0 start before id st
  while true; do
    fetch; start=$(remote_branch)
    read -r id st <<<"$(run_of "$role")"
    if [ -n "${id:-}" ] && [ "$st" != completed ]; then
      log "$role: waiting for run $id, already going"
    else
      before=${id:-}
      if [ "$role" = author ] && [ -n "$VERSION" ]; then
        gh workflow run attempt.yml -f dandiset="$d" -f role="$role" -f version="$VERSION" || { sleep 60; continue; }
      else
        gh workflow run attempt.yml -f dandiset="$d" -f role="$role" || { sleep 60; continue; }
      fi
      id=""
      for _ in $(seq 1 60); do read -r id st <<<"$(run_of "$role")"; [ -n "${id:-}" ] && [ "$id" != "$before" ] && break; id=""; sleep 5; done
      [ -n "$id" ] || { log "STOPPED: the run of $role was not found"; return 1; }
      log "$role started: run $id"
    fi
    st=$(wait_run "$id"); log "$role $st (run $id)"
    [ "$st" = success ] && return 0
    if gh run view "$id" --log 2>/dev/null | grep -q "session limit" && [ $tries -lt 100 ]; then
      tries=$((tries+1))
      # Put the branch back where the run started, and check that it took.
      if [ -n "$start" ]; then git push -q --force origin "$start:refs/heads/attempt/$d"
      else git push -q origin --delete "attempt/$d" 2>/dev/null || true; fi
      [ "$(remote_branch)" = "$start" ] || { log "STOPPED: could not reset attempt/$d after the session limit"; return 1; }
      log "$role hit the session limit; branch reset, retry $tries in 30 minutes"
      sleep 1800; continue
    fi
    log "STOPPED at $role (run $id)"; return 1
  done; }

fetch
if [ -n "$(remote_branch)" ] && git merge-base --is-ancestor origin/attempt/"$d" origin/main; then
  git push -q origin --delete "attempt/$d" && log "deleted attempt/$d, merged with an earlier attempt"
  fetch
fi
for role in author verifier-1 author-revise-1 verifier-2 author-revise-2; do
  is_done "$role" && continue
  run_role "$role" || { echo "$d STOPPED at $role"; exit 1; }
done
fetch
latest=$(git ls-tree -r --name-only origin/attempt/"$d" attempts | grep "^attempts/$d-" | sort | tail -n 1)
if git show "origin/attempt/$d:$latest" | python -c "import yaml,sys; sys.exit(0 if any(o.get('proposed') for o in yaml.safe_load(sys.stdin)['outcomes']) else 1)"; then
  log "has proposed changes: third round"
  for role in verifier-3 author-revise-3; do
    is_done "$role" && continue
    run_role "$role" || { echo "$d STOPPED at $role"; exit 1; }
  done
fi

# Finish, one dandiset at a time.
until mkdir "$STATE/finalize.lock" 2>/dev/null; do sleep 60; done
trap 'rmdir "$STATE/finalize.lock" 2>/dev/null' EXIT
log "finishing"
fetch
git checkout -q -B "attempt/$d" origin/attempt/"$d"
if ! git rebase -q origin/main; then
  git rebase --abort; echo "$d STOPPED: the branch does not rebase on main"; exit 1
fi
git push -q --force-with-lease origin "attempt/$d"
is_done recorder || run_role recorder || { echo "$d STOPPED at recorder"; exit 1; }
fetch; git checkout -q -B "attempt/$d" origin/attempt/"$d"
title=$(python "$here/describe.py" title "$d")
pr=$(gh pr list --head "attempt/$d" --state open --json url --jq '.[0].url // empty')
if [ -z "$pr" ]; then
  pr=$(gh pr create --base main --head "attempt/$d" --title "$title" \
    --body "$(python "$here/describe.py" body "$d")") || { echo "$d STOPPED: could not open a pull request"; exit 1; }
fi
log "pull request $pr"
while true; do
  s=$(gh pr checks "$pr" --json bucket 2>/dev/null) || { sleep 60; continue; }
  echo "$s" | jq -e 'length>0 and all(.bucket!="pending")' >/dev/null && break
  sleep 60
done
if echo "$s" | jq -e 'all(.bucket=="pass" or .bucket=="skipping")' >/dev/null; then
  gh pr merge "$pr" --merge >/dev/null && { echo "$d MERGED $pr"; exit 0; }
  echo "$d STOPPED: merging $pr failed"; exit 1
fi
echo "$d CHECKS FAILED $pr"; exit 1
