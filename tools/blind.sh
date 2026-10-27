#!/bin/bash
# Keep a repeat attempt blind to the attempts before it (docs/protocol.md, "Repeat attempts").
#
#   tools/blind.sh hide    FOLDER ROLE STASH   before an author's run: move the earlier attempts out of the checkout
#   tools/blind.sh restore FOLDER ROLE STASH   after it, before its changes are collected: put them back
#   tools/blind.sh audit   FOLDER              print the lines of this attempt's author transcripts that point at
#                                              an earlier attempt or the registry's published record
#
# Run from the repository root. `hide` does nothing on a dataset's first attempt. What it moves to STASH:
# the earlier attempt records; for the author role, the earlier entry (the author writes a new one in its
# place) and the questions an earlier author asked, whose text holds that author's results; the earlier
# attempts' transcripts and pilot notes; the pages that summarise attempts (docs/pilot-notes.md,
# docs/conversion-tracker.md, left as a stub); and .git, so that the history holds no earlier attempt either.
#
# `restore` puts everything back except, for the author role, the questions (they belong to the attempt that
# asked them, and stay in the history) and the earlier entry when the author wrote a new one. Nothing stops
# an agent that goes looking on the web; `audit` is how the reconcile step checks that it did not.
set -euo pipefail
cmd=$1; d=$2

if [ "$cmd" = audit ]; then
  # The earlier attempts' ids: every record but the newest, which is this attempt's.
  earlier=$(ls attempts/"$d"-*.yaml 2>/dev/null | sort | sed '$d' | xargs -n 1 basename 2>/dev/null | sed 's/\.yaml$//' | paste -sd '|' -)
  grep -nE "encorescience\.org|catalystneuro\.github\.io|reproduction-registry|catalystneuro/encore|attempt-[0-9]{2}/|git (log|show)${earlier:+|$earlier}" \
    transcripts/"$d"/author*.md 2>/dev/null || true
  exit 0
fi

role=$3; stash=$4
records=$(ls attempts/"$d"-*.yaml 2>/dev/null | sort || true)
# The author's run starts a new attempt, so every record is an earlier one; for the runs after it, the newest
# record is this attempt's own.
[ "$role" = author ] || records=$(echo "$records" | sed '$d')

if [ "$cmd" = hide ]; then
  [ -n "$records" ] || { echo "first attempt on $d: nothing to hide"; exit 0; }
  mkdir -p "$stash"
  : > "$stash/moved.txt"
  move(){ [ -e "$1" ] || return 0; mkdir -p "$stash/$(dirname "$1")"; mv "$1" "$stash/$1"; echo "$1" >> "$stash/moved.txt"; }
  # The earlier entry, read before its record is moved.
  entry=$(sed -nE 's/^entry: *"?([^" ]+)"? *$/\1/p' "$(echo "$records" | tail -n 1)")
  for r in $records; do move "$r"; done
  if [ "$role" = author ]; then
    echo "$entry" > "$stash/entry.txt"
    move "entries/$entry"
    move "questions/$d.yaml"
    # The earlier attempt's transcripts are still at the top of the dataset's folder; a claims run of this
    # attempt has already moved them aside, and its own (claims*, from the paper alone) stay.
    for f in transcripts/"$d"/*.md; do
      [ -e "$f" ] || continue
      case "$(basename "$f")" in claims*) ;; *) move "$f";; esac
    done
  fi
  for f in transcripts/"$d"/attempt-* docs/pilot-notes/"$d"-*.md; do move "$f"; done
  for f in docs/pilot-notes.md docs/conversion-tracker.md; do
    move "$f" && [ -e "$stash/$f" ] && echo "Left out of a blind attempt: this page describes other attempts." > "$f"
  done
  move .git
  echo "hid $(wc -l < "$stash/moved.txt") paths from the attempt on $d:"; cat "$stash/moved.txt"
  exit 0
fi

if [ "$cmd" = restore ]; then
  [ -s "$stash/moved.txt" ] || exit 0
  entry=$(cat "$stash/entry.txt" 2>/dev/null || true)
  while read -r p; do
    if [ "$role" = author ] && [ "$p" = "questions/$d.yaml" ]; then continue; fi
    if [ "$role" = author ] && [ -n "$entry" ] && [ "$p" = "entries/$entry" ] && [ -e "$p" ]; then continue; fi
    rm -rf "$p"; mkdir -p "$(dirname "$p")"; mv "$stash/$p" "$p"
  done < "$stash/moved.txt"
  rm -f "$stash/moved.txt"
  echo "restored the earlier attempts on $d"
  exit 0
fi
echo "usage: tools/blind.sh hide|restore FOLDER ROLE STASH, or tools/blind.sh audit FOLDER" >&2; exit 2
