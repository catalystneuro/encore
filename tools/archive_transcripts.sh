#!/bin/bash
# Before a repeat attempt's author run is committed, move the earlier attempt's transcripts from
# transcripts/<paper>/ to transcripts/<paper>/attempt-NN/, where NN is the number of the latest
# attempt record already in attempts/. Every attempt's runs write to the same paths, so without this
# a repeat attempt overwrites the transcripts of the one before it. The paper match's transcript
# is the dataset's, not the paper's, and is kept apart in transcripts/match/<folder>/.
#
#   tools/archive_transcripts.sh PAPER     (the paper's key; from the repository root, before the new record is added)
set -euo pipefail
d=$1
files=$(ls transcripts/"$d"/*.md 2>/dev/null | grep -v '/paper-match[^/]*\.md$' || true)
[ -n "$files" ] || exit 0
# No attempt record yet (a claims run repeated before any attempt): nothing to archive; the new
# transcripts replace the earlier run's. `|| true`, since ls fails on no match under pipefail.
latest=$(ls attempts/ 2>/dev/null | grep -E "^${d}-[0-9]{2}\.yaml$" | sort | tail -n 1 || true)
[ -n "$latest" ] || exit 0
n=$(basename "$latest" .yaml); n=${n##*-}
mkdir -p transcripts/"$d"/attempt-"$n"
# shellcheck disable=SC2086
git mv $files transcripts/"$d"/attempt-"$n"/
echo "moved the transcripts of attempt $n to transcripts/$d/attempt-$n/"
