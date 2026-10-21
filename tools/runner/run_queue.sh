#!/bin/bash
# Keep LANES attempts going, each through chain.sh, until the queue is empty, the file
# $RUNNER_STATE/STOP exists, or STOP_AT (UTC, e.g. 2026-10-19T12:00) has passed; an attempt already
# started is always finished. Run it from a clone of the repository:
#
#   RUNNER_STATE=~/registry-runner tools/runner/run_queue.sh [LANES] [STOP_AT]
#
# LANES defaults to 1: two lanes reach the subscription's usage limits about twice as fast.
#
# With CLAIMS_ONLY=1 each chain stops once the dataset's checked claims are on main (chain.sh), and
# an empty queue is filled from the targets whose papers are all stored and that have no claims yet.
# Give such a runner its own RUNNER_STATE.
#
# Each lane takes the next item from $RUNNER_STATE/queue.txt (lines "DATASET [VERSION]", consumed
# from the top), and when that is empty the next target that describe.py chooses. The scripts are
# copied to $RUNNER_STATE/bin first: chain.sh checks out branches in the clone, and bash reads a
# script while it runs it. Progress goes to $RUNNER_STATE/runner.log, and each dataset's chain to
# $RUNNER_STATE/logs/<dataset>.log.
set -uo pipefail
STATE=${RUNNER_STATE:?set RUNNER_STATE}; LANES=${1:-1}; STOP_AT=${2:-}
export RUNNER_STATE=$STATE REGISTRY_ROOT=$PWD
mkdir -p "$STATE/logs" "$STATE/bin"; touch "$STATE/queue.txt" "$STATE/started.txt"
cp tools/runner/chain.sh tools/runner/describe.py tools/runner/merge_claims.sh "$STATE/bin/"
rmdir "$STATE/finalize.lock" "$STATE/pick.lock" 2>/dev/null
log(){ echo "$(date -u +%Y-%m-%dT%H:%MZ) $*" >> "$STATE/runner.log"; }

stopping(){
  [ -e "$STATE/STOP" ] && return 0
  [ -n "$STOP_AT" ] && [ "$(date -u +%s)" -ge "$(date -j -u -f %Y-%m-%dT%H:%M "$STOP_AT" +%s)" ]
}
pick(){ local item
  until mkdir "$STATE/pick.lock" 2>/dev/null; do sleep 2; done
  item=$(head -n 1 "$STATE/queue.txt")
  if [ -n "$item" ]; then
    tail -n +2 "$STATE/queue.txt" > "$STATE/queue.tmp" && mv "$STATE/queue.tmp" "$STATE/queue.txt"
  else
    git fetch -q origin 2>/dev/null || true
    # shellcheck disable=SC2046
    item=$(python "$STATE/bin/describe.py" "$([ "${CLAIMS_ONLY:-}" = 1 ] && echo next-claims || echo next)" \
      $(cut -d' ' -f1 "$STATE/started.txt")) || item=""
  fi
  [ -z "$item" ] || echo "$item" >> "$STATE/started.txt"
  rmdir "$STATE/pick.lock"
  echo "$item"
}
lane(){ local item d
  while ! stopping; do
    item=$(pick)
    [ -n "$item" ] || { log "lane $1: the queue is empty"; return; }
    d=${item%% *}
    log "lane $1: $item started"
    # shellcheck disable=SC2086
    "$STATE/bin/chain.sh" $item >> "$STATE/logs/$d.log" 2>&1
    log "lane $1: $(tail -n 1 "$STATE/logs/$d.log")"
  done
  log "lane $1: stopping"
}

log "runner started: $LANES lanes${CLAIMS_ONLY:+, claims only}${STOP_AT:+, no new attempts after $STOP_AT UTC}"
for i in $(seq 1 "$LANES"); do lane "$i" & sleep 120; done
wait
log "runner done"
