#!/bin/bash
# Before a repeat attempt's author run is committed, move the earlier attempt's transcripts from
# transcripts/<dandiset>/ to transcripts/<dandiset>/attempt-NN/, where NN is the number of the latest
# attempt record already in attempts/. Every attempt's runs write to the same paths, so without this
# a repeat attempt overwrites the transcripts of the one before it.
#
#   tools/archive_transcripts.sh DANDISET     (from the repository root, before the new record is added)
set -euo pipefail
d=$1
ls transcripts/"$d"/*.md >/dev/null 2>&1 || exit 0
latest=$(ls attempts/"$d"-*.yaml 2>/dev/null | sort | tail -n 1)
[ -n "$latest" ] || exit 0
n=$(basename "$latest" .yaml); n=${n##*-}
mkdir -p transcripts/"$d"/attempt-"$n"
git mv transcripts/"$d"/*.md transcripts/"$d"/attempt-"$n"/
echo "moved the transcripts of attempt $n to transcripts/$d/attempt-$n/"
