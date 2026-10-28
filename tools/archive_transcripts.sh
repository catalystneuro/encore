#!/bin/bash
# Before a repeat attempt's author run is committed, move the earlier attempt's transcripts from
# transcripts/<dandiset>/ to transcripts/<dandiset>/attempt-NN/, where NN is the number of the latest
# attempt record already in attempts/. Every attempt's runs write to the same paths, so without this
# a repeat attempt overwrites the transcripts of the one before it. The paper match's transcript
# (paper-match*.md) is the dataset's, not an attempt's, and stays.
#
#   tools/archive_transcripts.sh DANDISET     (from the repository root, before the new record is added)
set -euo pipefail
d=$1
files=$(ls transcripts/"$d"/*.md 2>/dev/null | grep -v '/paper-match[^/]*\.md$' || true)
[ -n "$files" ] || exit 0
# No attempt record yet (a claims run repeated before any attempt): nothing to archive; the new
# transcripts replace the earlier run's. `|| true`, since ls fails on no match under pipefail.
latest=$(ls attempts/"$d"-*.yaml 2>/dev/null | sort | tail -n 1 || true)
[ -n "$latest" ] || exit 0
n=$(basename "$latest" .yaml); n=${n##*-}
mkdir -p transcripts/"$d"/attempt-"$n"
# shellcheck disable=SC2086
git mv $files transcripts/"$d"/attempt-"$n"/
echo "moved the transcripts of attempt $n to transcripts/$d/attempt-$n/"
