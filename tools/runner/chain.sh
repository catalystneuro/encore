#!/bin/bash
# One attempt on one paper, start to finish, run from a clone of the repository:
#
#   tools/runner/chain.sh PAPER|DATASET [VERSION]      (tingley-2021; or 000147, DANDI:000147, <archive>:<id>)
#
# Records are by paper (docs/paper-first.md). Given a dataset, the chain makes its paper match first, which lists
# the dataset for its paper (merge_match.sh), and goes on under the paper's key; given a paper, it starts from
# the claims. From the claims on, the paper's name is the chain's: its branch attempt/<paper>, its runs, its
# files, $RUNNER_STATE/attempt-<paper>. The attempt uses every dataset papers/datasets/<paper>.yaml lists.
#
# Runs the roles of the attempt in GitHub Actions, one after another: the paper match, when main has none
# for the dataset (papers.yml; docs/pipeline.md step 1), the reader's claims and their
# check (papers.yml, the only runs that write the claims file), the author, the reader's answers to the
# author's questions and the author's run on them when there are questions (only a suspected misreading
# of the claims file is a question; the author takes method details from the paper), two verification rounds
# and their revisions, a third round when the last revision proposed changes, and for a repeat attempt the
# reconcile step, which compares it with the attempt before it. Then it records and merges the attempt. A
# claims file whose check says it is not ready stops the chain, for a
# person to look at. A repeat attempt on a new version of the dataset (VERSION given) keeps the
# claims file, unless the earlier attempt is deprecated. Picks up where an earlier chain stopped: roles
# committed since the attempt began ($RUNNER_STATE/attempt-<dataset>), on its branch or already on main,
# are skipped, and a run of the next role that is still going is waited for. When a new attempt starts, a
# branch already merged into main belongs to an earlier attempt and is deleted first, so the attempt
# starts from main; a branch merged while its attempt is going is kept. A run that fails on the subscription's session or weekly limit is retried after
# 30 minutes from where it started; one that fails on the network or the machine (a dropped connection, a runner
# shut down, no log) is retried twice after 5 minutes; one that fails because GitHub itself is failing (its git
# refusing the paper store's deploy key, or answering 5xx, as in the incident of 2026-11-04) is retried every 15
# minutes for up to 6 hours (OUTAGE_TRIES); any other failure stops the chain.
#
# Each role runs first on the unverified account (RUNNER_ACCOUNT=verified skips it). A run that
# account's safety checks flag (FLAGGED), or that has no token for it (UNVERIFIED-UNAVAILABLE), is
# not committed; the branch is put back and the role runs again on the verified account, as do the
# rest of the dataset's roles: a paper that was flagged once will be again. With RUNNER_FALLBACK=none
# the chain stops there instead, leaving $RUNNER_STATE/flagged-<dataset>, and the lane goes on to the
# next dataset: for when the verified account has no budget left.
#
# Finishing has main merged in, the attempt recorded (the recorder role adds the pilot notes) and its pull
# request merged once its checks pass. Chains finish side by side, each in a worktree of its own (see Finish).
#
# The paper match goes straight to main (merge_match.sh). When it leaves the dataset no usable paper the chain
# stops: for a person to confirm or correct the verdicts (held), or for good (no_match, confirmed). A claims
# file whose claims, links aside, are mostly on data elsewhere stops the chain too, before its checkpoint: the
# paper is likely not the dataset's. With MATCH_ONLY=1 the chain stops after the paper match, deletes the
# branch, and prints "<dataset> MATCH <status>".
#
# A new attempt skips the claims and their check when main already has a claims file whose check
# passed (put there by a claims-only chain, say). With CLAIMS_ONLY=1 the chain stops after the
# checkpoint instead: the checked claims and their runs' transcripts go into main, the branch is
# deleted, and the attempt is left for a later chain, which then starts from those claims.
#
# A dataset with no published version is skipped. The last line printed is "<dataset> MERGED <pr>",
# "<dataset> CLAIMS MERGED", "<dataset> SKIPPED ...", "<dataset> STOPPED ...", "<dataset> CHECKS
# FAILED <pr>", which leaves the pull request open, or "<dataset> RESTART: ..." (exit 75), when gh can no
# longer verify TLS from this process and the chain is to be resumed from a fresh one.
set -uo pipefail
VERSION=${2:-}
STATE=${RUNNER_STATE:-/tmp}
here=$(cd "$(dirname "$0")" && pwd)
export REGISTRY_ROOT=$PWD
# A paper's key, or a dataset's folder name (000147 for DANDI, <archive>-<id> otherwise), names the chain's files
# and branch; a dataset's name is replaced by its paper's once the paper match lists it for one.
# A paper is one main lists (papers/datasets/<key>.yaml); the dataset parser would take "holdgraf-2016" for archive
# "holdgraf", so it cannot tell them apart.
git fetch -q origin main 2>/dev/null || true
if git cat-file -e "origin/main:papers/datasets/$1.yaml" 2>/dev/null; then
  d=$1; is_paper=1
else
  d=$(python "$here/describe.py" folder "$1") || { echo "$1 STOPPED: neither a paper nor a dataset"; exit 1; }
  is_paper=""
fi
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
  | sort -n -u | sed -nE "s/^[0-9]+ Agent run on ($(names)): ([a-z0-9-]+) \(success\)$/\2/p"; }
# The names the chain's runs were committed under: its own, and for a paper, its datasets' folder names, under which
# an attempt that began before the cutover to paper-first records committed its runs.
names(){ { echo "$d"; [ -z "$is_paper" ] || git show "origin/main:papers/datasets/$d.yaml" 2>/dev/null \
  | python -c "import sys,yaml; sys.path.insert(0,'$REGISTRY_ROOT/tools'); import datasets; [print(datasets.folder(datasets.key_of(x['archive'], str(x['id'])))) for x in (yaml.safe_load(sys.stdin) or {}).get('datasets') or []]" 2>/dev/null; } \
  | paste -sd '|' -; }
is_done(){ done_roles | grep -qx "$1"; }
workflow_of(){ case "$1" in paper-match|claims|claims-check|answer) echo papers.yml;; *) echo attempt.yml;; esac; }
run_of(){ gh run list --workflow "$(workflow_of "$1")" --limit 100 --json databaseId,displayTitle,status \
  | python "$here/describe.py" run "$d" "$1"; }
# After macOS updates its trust store (trustd restarts), every gh call from a process that started before then can
# fail TLS ("x509: OSStatus -26276") while gh from a fresh shell works: on 2026-10-29 for 15 hours, on 2026-11-02
# for 7. The chain cannot recover from inside, so after STALE_TRIES such failures in a row it hands the dataset
# back: it prints "<dataset> RESTART: ..." and exits 75, and the lane (pool_lane.sh) puts the dataset back in
# its queue and stops, for the pacer to start a fresh lane, which resumes it. A run going on GitHub keeps going
# and is waited for by the resumed chain.
STALE_TLS="OSStatus -26276"; STALE_TRIES=${STALE_TRIES:-10}; tls_fails=0
stale(){ last=""; log "gh failed TLS ($STALE_TLS) $STALE_TRIES times in a row; this process needs restarting" >&2
  echo "$d RESTART: gh cannot verify TLS from this process (x509 $STALE_TLS); resume the chain from a fresh one"
  exit 75; }
# Counts a failed gh call's output towards the stale-TLS limit, and stops the chain at the limit.
gh_failed(){ if grep -q "$STALE_TLS" <<<"$1"; then tls_fails=$((tls_fails + 1)); [ $tls_fails -lt "$STALE_TRIES" ] || stale
             else tls_fails=0; fi; }
# A failed check is retried, but logged after 5 in a row and then hourly, so that a chain that cannot reach
# GitHub shows in its log. Prints stale-tls after STALE_TRIES TLS failures in a row.
wait_run(){ local st fails=0 tls=0; while true; do
  if ! st=$(gh run view "$1" --json status,conclusion --jq '"\(.status) \(.conclusion)"' 2>&1); then
    fails=$((fails + 1))
    [ $((fails % 60)) = 5 ] && log "cannot check run $1 ($fails tries): $(echo "$st" | head -n 1)" >&2
    if grep -q "$STALE_TLS" <<<"$st"; then tls=$((tls + 1)); [ $tls -lt "$STALE_TRIES" ] || { echo stale-tls; return; }
    else tls=0; fi
    sleep 60; continue
  fi
  fails=0; tls=0
  case "$st" in completed*) echo "${st#completed }"; return;; esac; sleep 60; done; }

# Put the branch back where a run started, and check that it took.
reset_branch(){ local start=$1
  if [ -n "$start" ]; then git push -q --force origin "$start:refs/heads/attempt/$d"
  else git push -q origin --delete "attempt/$d" 2>/dev/null || true; fi
  [ "$(remote_branch)" = "$start" ]; }

GITHUB_DOWN='git@github\.com: Permission denied \(publickey\)|remote: fatal error in commit_refs|remote rejected.*\((Internal Server Error|failure)\)|github\.com.*(returned error: 50[0-4]|HTTP 50[0-4]|Internal Server Error|Service Unavailable|Bad Gateway)'
run_role(){ local role=$1 tries=0 flaky=0 outage=0 start before id st runlog acct out
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
      # The paper match is on a dataset; every other role on the paper.
      target="paper=$d"; [ "$role" = paper-match ] && target="dataset=$d"
      if [ "$role" = author ] && [ -n "$VERSION" ]; then
        out=$(gh workflow run attempt.yml -f "$target" -f role="$role" -f version="$VERSION" -f account="$acct" 2>&1) \
          || { gh_failed "$out"; sleep 60; continue; }
      else
        out=$(gh workflow run "$(workflow_of "$role")" -f "$target" -f role="$role" -f account="$acct" 2>&1) \
          || { gh_failed "$out"; sleep 60; continue; }
      fi
      tls_fails=0
      id=""
      for _ in $(seq 1 60); do read -r id st <<<"$(run_of "$role")"; [ -n "${id:-}" ] && [ "$id" != "$before" ] && break; id=""; sleep 5; done
      [ -n "$id" ] || { last_why="the run of $role was not found"; log "STOPPED: $last_why"; return 1; }
      log "$role started: run $id"
    fi
    last_run=$id; st=$(wait_run "$id"); [ "$st" = stale-tls ] && stale; log "$role $st (run $id)"
    [ "$st" = success ] && return 0
    runlog=$(gh run view "$id" --log-failed 2>/dev/null || gh run view "$id" --log 2>/dev/null)
    if echo "$runlog" | grep -qE "FLAGGED on the [a-z]+ account|[A-Z]+-UNAVAILABLE"; then
      # Put the branch back where the run started, and run the role, and the rest, on the verified account.
      reset_branch "$start" || { last_why="could not reset attempt/$d after the flag"; log "STOPPED: $last_why"; return 1; }
      why=$(echo "$runlog" | grep -oE "(FLAGGED on the [a-z]+ account|[A-Z]+-UNAVAILABLE)[^\"]*" | head -n 1 | cut -c1-200)
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
    # GitHub failing, not the run: on 2026-11-04 its git refused the paper store's deploy key, unchanged, and
    # answered pushes with 500s for hours. Every run then fails in its first minutes, before the agent starts.
    # When only the commit job failed, the agent's work is in the run's artifact: that job is run again, and the
    # chain waits for the same run, rather than running the agent again.
    # Only GitHub's own errors count, never an error the agent met on another service, so that a failed agent is
    # not run again for hours.
    if echo "$runlog" | grep -qE "$GITHUB_DOWN" \
       && [ $outage -lt "${OUTAGE_TRIES:-24}" ]; then
      outage=$((outage+1))
      if ! echo "$runlog" | cut -f1 | grep -qvx commit; then
        log "$role: its commit failed because GitHub is failing (run $id); its commit job again in 15 minutes, retry $outage"
        sleep 900
        until gh run rerun "$id" --failed >/dev/null 2>&1; do
          outage=$((outage+1))
          [ $outage -lt "${OUTAGE_TRIES:-24}" ] || { last_why="could not run the commit job of run $id again"; log "STOPPED: $last_why"; return 1; }
          sleep 900
        done
        sleep 20; continue   # the same run, queued again: waited for at the top of the loop
      fi
      reset_branch "$start" || { last_why="could not reset attempt/$d after GitHub failed"; log "STOPPED: $last_why"; return 1; }
      log "$role failed because GitHub is failing (run $id); branch reset, retry $outage in 15 minutes"
      sleep 900; continue
    fi
    # A failure of the network or of the machine, not of the agent: a connection dropped or timed out, the runner
    # was shut down, or the run left no log. Tried twice more; an agent that ran out of time is not.
    if { [ -z "$runlog" ] || echo "$runlog" | grep -qE "ReadTimeout|ConnectionError|Connection (reset|aborted)|exit code 143|shutdown signal|lost communication|Temporary failure resolving|Could not resolve host|Unable to fetch some archives"; } \
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
claims_file(){ git ls-tree --name-only origin/attempt/"$d" "claims/$d.yaml" | head -n 1; }
# The paper's attempt records on its branch: attempts/<paper>-NN.yaml, not another paper's whose key begins with it.
records_on_branch(){ git ls-tree -r --name-only origin/attempt/"$d" attempts | grep -E "^attempts/$d-[0-9]{2}\.yaml$" | sort; }

# The paper match: the claims are read only from a paper whose data the dataset holds. A chain given a paper
# starts after it.
match=matched
[ -n "$is_paper" ] || match=$(python "$here/describe.py" match "$d")
if [ "$match" = unchecked ]; then
  step paper-match
  out=$("$here/merge_match.sh" "$d" 2>&1); st=$?
  echo "$out" | while read -r line; do log "$line"; done
  [ $st = 0 ] || { end "$d STOPPED: the paper match did not go into main"; exit 1; }
  fetch
  match=$(python "$here/describe.py" match "$d")
fi
if [ "${MATCH_ONLY:-}" = 1 ]; then
  # Only the paper match was asked for; it and its transcript are on main.
  git push -q origin --delete "attempt/$d" 2>/dev/null || true
  rm -f "$mark"; end "$d MATCH $match"; exit 0
fi
case "$match" in
  matched)
    if [ -z "$is_paper" ]; then
      # From here the chain is the paper's: the dataset's branch held only its paper match, now on main.
      fetch
      # A dataset matched before papers were listed by paper match (or by hand) is listed now.
      if ! p=$(python "$here/describe.py" paper "$d"); then
        "$here/merge_match.sh" "$d" --adopt 2>&1 | while read -r line; do log "$line"; done
        fetch
        p=$(python "$here/describe.py" paper "$d") || { end "$d STOPPED: the paper match is on main, but the dataset could not be listed for its paper (papers/datasets/)"; exit 1; }
      fi
      log "the paper match lists the dataset for paper $p; going on as $p"
      git push -q origin --delete "attempt/$d" 2>/dev/null || true
      [ -e "$STATE/attempt-$p" ] || mv "$mark" "$STATE/attempt-$p" 2>/dev/null || true
      rm -f "$mark"
      [ -e "$STATE/verified-$d" ] && { mv "$STATE/verified-$d" "$STATE/verified-$p"; account=verified; }
      d=$p; is_paper=1; mark="$STATE/attempt-$d"
      [ -e "$STATE/verified-$d" ] && account=verified
      if [ "$(python "$here/describe.py" published "$d")" != true ]; then
        end "$d SKIPPED: a dataset of the paper has no published version"; exit 1
      fi
      fetch
      if [ ! -e "$mark" ] || { [ -n "$(remote_branch)" ] && git merge-base --is-ancestor origin/attempt/"$d" origin/main; }; then
        # A new attempt on the paper. A branch already merged into main belongs to an earlier one; start from main.
        if [ -n "$(remote_branch)" ] && git merge-base --is-ancestor origin/attempt/"$d" origin/main; then
          git push -q origin --delete "attempt/$d" && log "deleted attempt/$d, merged with an earlier attempt"
          fetch
        fi
        [ -e "$mark" ] || date -u +%Y-%m-%dT%H:%M:%SZ > "$mark"
      fi
    fi;;
  held) last_why="the paper match leaves no usable paper; confirm the verdicts in papers/match/$d.yaml (confirmed: true) or correct them"
        end "$d STOPPED: no paper matches the dataset; see papers/match/$d.yaml"; exit 1;;
  no_match) rm -f "$mark"; end "$d SKIPPED: no paper matches the dataset (papers/match/$d.yaml)"; exit 1;;
  *) end "$d STOPPED: the paper match left a paper without a verdict; see papers/match/$d.yaml"; exit 1;;
esac

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
  # Claims mostly on data elsewhere mean the paper is likely not this dataset's: stop before the checkpoint. Not for
  # a paper that only reuses its datasets, whose own new data are elsewhere by nature.
  reuses=$(git show "origin/main:papers/datasets/$d.yaml" 2>/dev/null | python -c "import yaml,sys; d=(yaml.safe_load(sys.stdin) or {}).get('datasets') or []; print(str(bool(d) and all(x.get('relation') == 'reuses' for x in d)).lower())" 2>/dev/null || echo false)
  elsewhere=false
  [ "$reuses" = true ] || elsewhere=$(on_branch "$(claims_file)" | python -c "import yaml,sys; c=[x for x in (yaml.safe_load(sys.stdin) or {}).get('claims') or [] if x.get('kind') != 'link']; print(str(bool(c) and 2 * sum(x.get('data') == 'elsewhere' for x in c) > len(c)).lower())")
  if [ "$elsewhere" = true ]; then
    last_why="most of the claims are on data elsewhere, so the paper is likely not its datasets'; check papers/datasets/$d.yaml and their papers/match/ files"
    end "$d STOPPED: most claims are on data elsewhere"; exit 1
  fi
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
latest=$(records_on_branch | tail -n 1)
if git show "origin/attempt/$d:$latest" | python -c "import yaml,sys; sys.exit(0 if any(o.get('proposed') for o in yaml.safe_load(sys.stdin)['outcomes']) else 1)"; then
  log "has proposed changes: third round"
  for role in verifier-3 author-revise-3; do step "$role"; done
fi
# A repeat attempt, made blind, is compared with the one before it once it is verified.
if [ "$(records_on_branch | grep -c .)" -gt 1 ]; then
  step reconcile
fi

# Finish. Each chain finishes in a worktree of its own, with no lock: until 2026-11-11 one chain at a time finished,
# holding $RUNNER_STATE/finalize.lock from the merge of main to the merge of its pull request, through the
# pull request's checks (which run the entry's notebooks again, up to 80 minutes). With ten lanes the chains
# queued for hours behind one another (kim-2022 for more than two and a half), and a lock left by a chain that
# died stopped them all (2026-11-10). The lock was there for the clone's one checkout and so that each attempt
# landed on a main that had the ones before it. The worktree does the first. For the second: an attempt adds its
# own files, GitHub refuses a merge that conflicts, and the chain then merges main in again and waits for the
# checks again (twice at most).
work=$(mktemp -d "${TMPDIR:-/tmp}/finish-$d.XXXXXX")
drop_work(){ git worktree remove --force "$work" >/dev/null 2>&1 || true; rm -rf "$work"; }
trap 'drop_work; notify' EXIT
# The attempt's branch in the worktree, with main merged in, pushed. Merge, not rebase: main already has the
# checked claims (the checkpoint), so a rebase replays the branch's claims, claims-check and answer commits onto
# them and stops on an add/add conflict. The branch's claims file is the same or later (the reader's answers),
# so it is kept; any other conflict stops the chain. Returns 1 when it does not merge, 2 or 3 when git fails.
merge_main(){
  fetch
  drop_work
  git worktree add -q --detach "$work" "origin/attempt/$d" >/dev/null 2>&1 || return 2
  if ! git -C "$work" merge -q --no-edit -m "Merge main into attempt/$d" origin/main >/dev/null 2>&1; then
    git -C "$work" checkout -q HEAD -- "claims/$d.yaml" 2>/dev/null
    if [ -n "$(git -C "$work" diff --name-only --diff-filter=U)" ]; then
      git -C "$work" merge --abort; return 1
    fi
    git -C "$work" commit -q --no-edit || return 2
  fi
  git -C "$work" push -q origin "HEAD:refs/heads/attempt/$d" || return 3
}
log "finishing"
round=0
while true; do
  round=$((round+1))
  merge_main; case $? in
    0) ;;
    1) end "$d STOPPED: the branch does not merge with main"; exit 1;;
    2) end "$d STOPPED: could not check out attempt/$d in a worktree"; exit 1;;
    *) end "$d STOPPED: could not push attempt/$d after merging main"; exit 1;;
  esac
  is_done recorder || run_role recorder || { end "$d STOPPED at recorder"; exit 1; }
  # The branch as the recorder left it, for the pull request's title and body (describe.py reads the tree).
  fetch; git -C "$work" checkout -q --detach "origin/attempt/$d" \
    || { end "$d STOPPED: could not check out attempt/$d after the recorder"; exit 1; }
  title=$(REGISTRY_ROOT="$work" python "$here/describe.py" title "$d")
  pr=$(gh pr list --head "attempt/$d" --state open --json url --jq '.[0].url // empty')
  if [ -z "$pr" ]; then
    pr=$(gh pr create --base main --head "attempt/$d" --title "$title" \
      --body "$(REGISTRY_ROOT="$work" python "$here/describe.py" body "$d")") || { end "$d STOPPED: could not open a pull request"; exit 1; }
  fi
  log "pull request $pr"
  # The checks waited for are those of the commit just pushed, asked for by that commit. GitHub can take minutes to
  # start them when its runners are busy; until then the pull request still shows the checks of the commit before,
  # finished. On 2026-11-10 wakhloo-2026 was stopped that way, at once, on the failure its push had been made to
  # fix. The entry check (check.yml, job "check") must be among them: the dashboard's preview alone, which can
  # start first, is not the checks.
  head=$(git -C "$work" rev-parse HEAD)
  again=""
  while true; do
    # GitHub runs no checks on a pull request that conflicts with main, so waiting for them would never end. Another
    # attempt merged since this one merged main in can conflict with it: main is merged in again.
    if [ "$(gh pr view "$pr" --json mergeable --jq .mergeable 2>/dev/null)" = CONFLICTING ]; then
      [ $round -lt 3 ] && { log "the pull request conflicts with main as it is now; merging main in again"; again=1; break; }
      last_why="$pr conflicts with main; merge main into attempt/$d, resolve the conflict, and start the chain again"
      end "$d STOPPED: the pull request conflicts with main ($pr)"; exit 1
    fi
    s=$(gh api "repos/{owner}/{repo}/commits/$head/check-runs?per_page=100" \
          --jq '[.check_runs[] | {name, status, conclusion}]' 2>/dev/null) || { sleep 60; continue; }
    echo "$s" | jq -e 'any(.name=="check") and all(.status=="completed")' >/dev/null && break
    sleep 60
  done
  [ -z "$again" ] || continue
  if echo "$s" | jq -e 'all(.conclusion=="success" or .conclusion=="skipped" or .conclusion=="neutral")' >/dev/null; then
    gh pr merge "$pr" --merge >/dev/null && { rm -f "$mark"; end "$d MERGED $pr"; exit 0; }
    # Main moved under it between the checks and the merge.
    if [ $round -lt 3 ] && [ "$(gh pr view "$pr" --json mergeable --jq .mergeable 2>/dev/null)" = CONFLICTING ]; then
      log "merging $pr failed on a conflict with main as it is now; merging main in again"; continue
    fi
    end "$d STOPPED: merging $pr failed"; exit 1
  fi
  end "$d CHECKS FAILED $pr"; exit 1
done
