#!/usr/bin/env bash
# Copy a dataset's papers from the private paper store into a directory.
#
#   PAPERS_DEPLOY_KEY=... tools/get_papers.sh FOLDER[,FOLDER...] DEST [DOI]     (000147, or <archive>-<id>)
#
# With DOI, only that paper's files (its text, PDF and supplements, named by the DOI) and the datasets' data
# descriptors: a dataset's folder also holds the papers of the others tested on it, which this run is not about
# (a paper that reuses a dataset shares the folder with the paper the data were published with).
#
# Several folders, for a paper on several datasets: the store files papers under the datasets they came with.
#
# Used by the workflows that run in the `papers` environment (docs/pipeline.md). The key and the
# store's checkout are deleted before it returns. Fails when the store has no full text for the
# dataset: the paper must be supplied first.
set -euo pipefail
dandiset=$1; dest=$2; doi=${3:-}
tmp=$(mktemp -d); key="$tmp/key"; store="$tmp/store"
trap 'rm -rf "$tmp"' EXIT
printf '%s\n' "$PAPERS_DEPLOY_KEY" > "$key"; chmod 600 "$key"
export GIT_SSH_COMMAND="ssh -i $key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
export GIT_LFS_SKIP_SMUDGE=1
git clone -q --depth 1 --filter=blob:none --sparse git@github.com:catalystneuro/registry-papers.git "$store"
IFS=, read -r -a folders <<<"$dandiset"
git -C "$store" sparse-checkout set "${folders[@]}"
git -C "$store" lfs pull --include "$(printf '%s/*,' "${folders[@]}" | sed 's/,$//')" || true
rm -f "$key"
# A data descriptor (<id>.data-description.txt, the dataset's own documentation) is not the paper's text.
# The store names a paper's files by its DOI with / as -, lower case (tools/store.py, slug).
prefix=$(printf '%s' "$doi" | tr 'A-Z/' 'a-z-')
mine(){ case "$(basename "$1")" in *.data-description.txt) return 0;; esac
        [ -z "$prefix" ] || case "$(basename "$1")" in "$prefix".*) return 0;; *) return 1;; esac; }
texts=$(for f in "${folders[@]}"; do for t in "$store/$f"/*.txt; do [ -e "$t" ] && mine "$t" && echo "$t"; done; done \
  | grep -v '\.data-description\.txt$' || true)
if [ -z "$texts" ]; then
  echo "::error::No full text for ${doi:-$dandiset} in the paper store under $dandiset: supply the paper (docs/pipeline.md)"; exit 1
fi
mkdir -p "$dest"
for f in "${folders[@]}"; do for x in "$store/$f"/*; do [ -f "$x" ] && mine "$x" && cp "$x" "$dest/"; done; done; true
ls -la "$dest"
head -n 6 "$dest"/*.txt
