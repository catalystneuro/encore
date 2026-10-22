#!/bin/bash
# One attempt on one dataset, start to finish, run from a clone of the repository:
#
#   tools/runner/chain.sh DATASET [VERSION]      (000147, DANDI:000147 or <archive>:<id>)
#
# Runs the roles of the attempt in GitHub Actions, one after another: the reader's claims and their
# check (papers.yml, the only runs that write the claims file), the author, the reader's answers to the
# author's questions and the author's run on them when there are questions, two verification rounds
# and their revisions, and a third round when the last revision proposed changes. Then it records
# and merges the attempt. A claims file whose check says it is not ready stops the chain, for a
# person to look at. A repeat attempt on a new version of the dataset (VERSION given) keeps the
# claims file, unless the earlier attempt is deprecated. Picks up where an earlier chain stopped: roles
# committed since the attempt began ($RUNNER_STATE/attempt-<dataset>), on its branch or already on main,
# are skipped, and a run of the next role that is still going is waited for. When a new attempt starts, a
# branch already merged into main belongs to an earlier attempt and is deleted first, so the attempt
# starts from main; a branch merged while its attempt is going is kept. A run that fails on the subscription's session or weekly limit is retried after
# 30 minutes from where it started; one that fails on the network or the machine (a dropped connection, a runner
# shut down, no log) is retried twice after 5 minutes; any other failure stops the chain.
#
# Each role runs first on the unverified account (RUNNER_ACCOUNT=verified skips it). A run that
# account's safety checks flag (FLAGGED), or that has no token for it (UNVERIFIED-UNAVAILABLE), is
# not committed; the branch is put back and the role runs again on the verified account, as do the
# rest of the dataset's roles: a paper that was flagged once will be again. With RUNNER_FALLBACK=none
# the chain stops there instead, leaving $RUNNER_STATE/flagged-<dataset>, and the lane goes on to the
# next dataset: for when the verified account has no budget left.
#
# Finishing takes a lock ($RUNNER_STATE/finalize.lock), so that one attempt at a time has main
# merged in, recorded (the recorder role adds the README row and the pilot notes) and merged once its
# checks pass; each lands on a main that has the ones before it.
#
# A new attempt skips the claims and their check when main already has a claims file whose check
# passed (put there by a claims-only chain, say). With CLAIMS_ONLY=1 the chain stops after the
# checkpoint instead: the checked claims and their runs' transcripts go into main, the branch is
# deleted, and the attempt is left for a later chain, which then starts from those claims.
#
# A dataset with no published version is skipped. The last line printed is "<dataset> MERGED <pr>",
# "<dataset> CLAIMS MERGED", "<dataset> SKIPPED ...", "<dataset> STOPPED ...", or "<dataset> CHECKS
# FAILED <pr>", which leaves the pull request open.
set -uo pipefail
VERSION=${2:-}
STATE=${RUNNER_STATE:-/tmp}
here=$(cd "$(dirname "$0")" && pwd)
export REGISTRY_ROOT=$PWD
# The dataset's folder name (000147 for DANDI, <archive>-<id> otherwise) names its files and branch.
d=$(python "$here/describe.py" folder "$1") || { echo "$1 STOPPED: not a dataset"; exit 1; }
# The account the next run uses; verified for the rest of the dataset once a run is flagged.
account=${RUNNER_ACCOUNT:-unverified}
[ -e "$STATE/verified-$d" ] && account=verified
log(){ echo "$(date -u +%Y-%m-%dT%H:%MZ) $d $*"; }
# The chain's last line, the reason a role stopped and its run, for notify(): a chain that stops for a
# person opens or updates the dataset's issue (notify.yml), and one that merges closes it.
last=""; last_why=""; last_run=""
end(){ last="$*"; echo "$*"; }
notify(){
  [ -n "$last" ] && [ "${RUNNER_NOTIFY:-}" != none ] || return 0
  gh workflow run notify.yml -f dataset="$d" -f status="$last" -f detail="$last_why" -f run="$last_run" \
    >/dev/null 2>&1 || log "could not dispatch notify.yml"
}
trap notify EXIT

remote_branch(){ git ls-remote --heads origin "attempt/$d" | cut -f1; }
fetch(){ git fetch -q origin main 2>/dev/null || true; git fetch -q origin "attempt/$d" 2>/dev/null || true; }
# Roles committed on the branch since it left main, most recent last.
# The attempt in progress began at the time in $STATE/attempt-<folder>, written when it started and removed
# when it is merged. Its roles are the runs committed since then, on its branch or already on main (a
# branch merged early, or the claims checkpoint): an earlier attempt's runs are older and do not count.
mark="$STATE/attempt-$d"
done_roles(){ { git log --since="$(cat "$mark" 2>/dev/null || echo 2000-01-01)" --format='%ct %s' origin/main 2>/dev/null
                git log --since="$(cat "$mark" 2>/dev/null || echo 2000-01-01)" --format='%ct %s' origin/attempt/"$d" 2>/dev/null; } \
  | sort -n -u | sed -nE "s/^[0-9]+ Agent run on $d: ([a-z0-9-]+) \(success\)$/\1/p"; }
is_done(){ done_roles | grep -qx "$1"; }
workflow_of(){ case "$1" in claims|claims-check|answer) echo papers.yml;; *) echo attempt.yml;; esac; }
run_of(){ gh run list --workflow "$(workflow_of "$1")" --limit 100 --json databaseId,displayTitle,status \
  | python "$here/describe.py" run "$d" "$1"; }
wait_run(){ local st; while true; do
  st=$(gh run view "$1" --json status,conclusion --jq '"\(.status) \(.conclusion)"' 2>/dev/null) || { sleep 60; continue; }
  case "$st" in completed*) echo "${st#completed }"; return;; esac; sleep 60; done; }

# Put the branch back where a run started, and check that it took.
reset_branch(){ local start=$1
  if [ -n "$start" ]; then git push -q --force origin "$start:refs/heads/attempt/$d"
  else git push -q origin --delete "attempt/$d" 2>/dev/null || true; fi
  [ "$(remote_branch)" = "$start" ]; }

run_role(){ local role=$1 tries=0 flaky=0 start before id st runlog acct
  while true; do
    fetch; start=$(remote_branch)
    read -r id st <<<"$(run_of "$role")"
    if [ -n "${id:-}" ] && [ "$st" != completed ]; then
      log "$role: waiting for run $id, already going"
    else
      before=${id:-}
      # The recorder reads no paper, so it starts on the unverified account even for a dataset whose paper
      # was flagged; only a flag on the recorder's own run moves it to the verified one.
      acct=$account; [ "$role" = recorder ] && acct=${recorder_account:-${RUNNER_ACCOUNT:-unverified}}
      if [ "$role" = author ] && [ -n "$VERSION" ]; then
        gh workflow run attempt.yml -f dataset="$d" -f role="$role" -f version="$VERSION" -f account="$acct" || { sleep 60; continue; }
      else
        gh workflow run "$(workflow_of "$role")" -f dataset="$d" -f role="$role" -f account="$acct" || { sleep 60; continue; }
      fi
      id=""
      for _ in $(seq 1 60); do read -r id st <<<"$(run_of "$role")"; [ -n "${id:-}" ] && [ "$id" != "$before" ] && break; id=""; sleep 5; done
      [ -n "$id" ] || { last_why="the run of $role was not found"; log "STOPPED: $last_why"; return 1; }
      log "$role started: run $id"
    fi
    last_run=$id; st=$(wait_run "$id"); log "$role $st (run $id)"
    [ "$st" = success ] && return 0
    runlog=$(gh run view "$id" --log-failed 2>/dev/null || gh run view "$id" --log 2>/dev/null)
    if echo "$runlog" | grep -qE "FLAGGED on the unverified account|UNVERIFIED-UNAVAILABLE"; then
      # Put the branch back where the run started, and run the role, and the rest, on the verified account.
      reset_branch "$start" || { last_why="could not reset attempt/$d after the flag"; log "STOPPED: $last_why"; return 1; }
      why=$(echo "$runlog" | grep -oE "(FLAGGED on the unverified account|UNVERIFIED-UNAVAILABLE)[^\"]*" | head -n 1 | cut -c1-200)
      if [ "${RUNNER_FALLBACK:-verified}" = none ]; then
        # The verified account is not to be used (out of budget, say): leave the dataset for later.
        last_why="$why; no fallback to the verified account"
        touch "$STATE/flagged-$d"; log "STOPPED at $role: $last_why"; return 1
      fi
      log "$role: $why; on the verified account from here"
      account=verified; recorder_account=verified; touch "$STATE/verified-$d"
      continue
    fi
    if echo "$runlog" | grep -qE "session limit|weekly limit" && [ $tries -lt 100 ]; then
      tries=$((tries+1))
      reset_branch "$start" || { last_why="could not reset attempt/$d after the usage limit"; log "STOPPED: $last_why"; return 1; }
      log "$role hit a usage limit; branch reset, retry $tries in 30 minutes"
      sleep 1800; continue
    fi
    # A failure of the network or of the machine, not of the agent: a connection dropped or timed out, the runner
    # was shut down, or the run left no log. Tried twice more; an agent that ran out of time is not.
    if { [ -z "$runlog" ] || echo "$runlog" | grep -qE "ReadTimeout|ConnectionError|Connection (reset|aborted)|exit code 143|shutdown signal|lost communication"; } \
       && ! echo "$runlog" | grep -q "timed out after" && [ $flaky -lt 2 ]; then
      flaky=$((flaky+1))
      reset_branch "$start" || { last_why="could not reset attempt/$d after a failed run"; log "STOPPED: $last_why"; return 1; }
      log "$role failed on the network or the machine (run $id); branch reset, retry $flaky in 5 minutes"
      sleep 300; continue
    fi
    last_why="the run of $role failed"; log "STOPPED at $role (run $id)"; return 1
  done; }

# Only published datasets: a DANDI draft can change under an attempt, and the record could not name
# the version it tested.
if [ "$(python "$here/describe.py" published "$d")" != true ]; then
  echo "$d SKIPPED: no published version"; exit 1
fi
fetch
if [ ! -e "$mark" ]; then
  # A new attempt. A branch already merged into main belongs to an earlier one; start from main.
  if [ -n "$(remote_branch)" ] && git merge-base --is-ancestor origin/attempt/"$d" origin/main; then
    git push -q origin --delete "attempt/$d" && log "deleted attempt/$d, merged with an earlier attempt"
    fetch
  fi
  date -u +%Y-%m-%dT%H:%M:%SZ > "$mark"
fi
step(){ is_done "$1" || run_role "$1" || { end "$d STOPPED at $1"; exit 1; }; }
# On the branch: python reads a file of the attempt's branch from stdin.
on_branch(){ git show "origin/attempt/$d:$1" 2>/dev/null; }
claims_file(){ git ls-tree -r --name-only origin/attempt/"$d" "claims/$d" | grep '\.yaml$' | head -n 1; }

deprecated=$(python "$here/describe.py" deprecated "$d")
on_main=$(python "$here/describe.py" claims-ready "$d")
if [ "$on_main" = true ] && [ "$deprecated" != true ] && ! is_done claims; then
  log "main has checked claims; skipping the claims and their check"
  [ "${CLAIMS_ONLY:-}" = 1 ] && { rm -f "$mark"; end "$d CLAIMS MERGED (already on main)"; exit 0; }
elif [ -z "$VERSION" ] || [ "$deprecated" = true ]; then
  step claims
  fetch
  # The reader writes no claims file when the paper's text is not enough to read them from (a missing
  # supplement, say); its report says what to supply.
  [ -n "$(claims_file)" ] || { end "$d STOPPED: the reader wrote no claims file; see transcripts/$d/claims-report.md"; exit 1; }
  step claims-check
  fetch
  ready=$(on_branch "$(claims_file)" | python -c "import yaml,sys; c=(yaml.safe_load(sys.stdin) or {}).get('checks') or [{}]; print(str(c[-1].get('ready', False)).lower())")
  [ "$ready" = true ] || { end "$d STOPPED: the claims check says the claims file is not ready"; exit 1; }
  # The checkpoint: the checked claims go into main now, ahead of the attempt. A failure here does not stop it.
  if [ "${CLAIMS_ONLY:-}" = 1 ]; then
    out=$("$here/merge_claims.sh" "$d" --with-transcripts 2>&1); st=$?
    echo "$out" | while read -r line; do log "$line"; done
    [ $st = 0 ] || { end "$d STOPPED: the claims did not go into main"; exit 1; }
    # The claims and their runs' transcripts are on main; the next chain on this dataset starts from main.
    git push -q origin --delete "attempt/$d" 2>/dev/null || true
    rm -f "$mark"; end "$d CLAIMS MERGED"; exit 0
  fi
  "$here/merge_claims.sh" "$d" 2>&1 | while read -r line; do log "$line"; done || true
fi
step author
fetch
open_questions=$(on_branch "questions/$d.yaml" | python -c "import yaml,sys; q=yaml.safe_load(sys.stdin) or []; q=q.get('questions', []) if isinstance(q, dict) else q; print(sum(1 for x in q if not x.get('answered')))" 2>/dev/null || echo 0)
if [ "${open_questions:-0}" != 0 ] || is_done answer; then
  log "$open_questions open questions"
  step answer
  step author-answers
fi
for role in verifier-1 author-revise-1 verifier-2 author-revise-2; do step "$role"; done
fetch
latest=$(git ls-tree -r --name-only origin/attempt/"$d" attempts | grep "^attempts/$d-" | sort | tail -n 1)
if git show "origin/attempt/$d:$latest" | python -c "import yaml,sys; sys.exit(0 if any(o.get('proposed') for o in yaml.safe_load(sys.stdin)['outcomes']) else 1)"; then
  log "has proposed changes: third round"
  for role in verifier-3 author-revise-3; do step "$role"; done
fi

# Finish, one dataset at a time.
until mkdir "$STATE/finalize.lock" 2>/dev/null; do sleep 60; done
trap 'rmdir "$STATE/finalize.lock" 2>/dev/null; notify' EXIT
log "finishing"
fetch
git checkout -q -B "attempt/$d" origin/attempt/"$d"
# Merge main in, not rebase: main already has the checked claims (the checkpoint), so a rebase replays
# the branch's claims, claims-check and answer commits onto them and stops on an add/add conflict. The
# branch's claims file is the same or later (the reader's answers), so it is kept; any other conflict
# stops the chain.
if ! git merge -q --no-edit -m "Merge main into attempt/$d" origin/main >/dev/null; then
  git checkout -q HEAD -- "claims/$d" 2>/dev/null
  if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
    git merge --abort; end "$d STOPPED: the branch does not merge with main"; exit 1
  fi
  git commit -q --no-edit
fi
git push -q origin "attempt/$d"
is_done recorder || run_role recorder || { end "$d STOPPED at recorder"; exit 1; }
fetch; git checkout -q -B "attempt/$d" origin/attempt/"$d"
title=$(python "$here/describe.py" title "$d")
pr=$(gh pr list --head "attempt/$d" --state open --json url --jq '.[0].url // empty')
if [ -z "$pr" ]; then
  pr=$(gh pr create --base main --head "attempt/$d" --title "$title" \
    --body "$(python "$here/describe.py" body "$d")") || { end "$d STOPPED: could not open a pull request"; exit 1; }
fi
log "pull request $pr"
while true; do
  s=$(gh pr checks "$pr" --json bucket 2>/dev/null) || { sleep 60; continue; }
  echo "$s" | jq -e 'length>0 and all(.bucket!="pending")' >/dev/null && break
  sleep 60
done
if echo "$s" | jq -e 'all(.bucket=="pass" or .bucket=="skipping")' >/dev/null; then
  gh pr merge "$pr" --merge >/dev/null && { rm -f "$mark"; end "$d MERGED $pr"; exit 0; }
  end "$d STOPPED: merging $pr failed"; exit 1
fi
end "$d CHECKS FAILED $pr"; exit 1
