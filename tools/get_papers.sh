#!/usr/bin/env bash
# Copy a dataset's papers from the private paper store into a directory.
#
#   PAPERS_DEPLOY_KEY=... tools/get_papers.sh FOLDER DEST     (000147, or <archive>-<id>)
#
# Used by the workflows that run in the `papers` environment (docs/pipeline.md). The key and the
# store's checkout are deleted before it returns. Fails when the store has no full text for the
# dataset: the paper must be supplied first.
set -euo pipefail
dandiset=$1; dest=$2
tmp=$(mktemp -d); key="$tmp/key"; store="$tmp/store"
trap 'rm -rf "$tmp"' EXIT
printf '%s\n' "$PAPERS_DEPLOY_KEY" > "$key"; chmod 600 "$key"
export GIT_SSH_COMMAND="ssh -i $key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
export GIT_LFS_SKIP_SMUDGE=1
git clone -q --depth 1 --filter=blob:none --sparse git@github.com:catalystneuro/registry-papers.git "$store"
git -C "$store" sparse-checkout set "$dandiset"
git -C "$store" lfs pull --include "$dandiset/*" || true
rm -f "$key"
# A data descriptor (<id>.data-description.txt, the dataset's own documentation) is not the paper's text.
if ! ls "$store/$dandiset"/*.txt 2>/dev/null | grep -qv '\.data-description\.txt$'; then
  echo "::error::No full text for $dandiset in the paper store: supply the paper (docs/pipeline.md)"; exit 1
fi
mkdir -p "$dest" && cp "$store/$dandiset"/* "$dest/"
ls -la "$dest"
head -n 6 "$dest"/*.txt
