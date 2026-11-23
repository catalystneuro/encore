#!/usr/bin/env bash
# Lays the protocol over a checkout of the registry: encore-protocol's docs/, schemas/ and tools/, at the version
# the checkout's protocol.lock names. The registry holds only the records; its .gitignore keeps the protocol's
# files out of its commits (encore-protocol's README, "Relation to the registry").
#
#   tools/protocol.sh             # this checkout
#   tools/protocol.sh DIR         # another checkout or worktree of the registry, at its own protocol.lock
#   ENCORE_PROTOCOL=~/dev/encore-protocol tools/protocol.sh
#                                 # a local clone of encore-protocol as it is, uncommitted changes and all,
#                                 # to try a change to the protocol against the records
#
# Run it again after a pull that changes protocol.lock. The versions come from a cached bare clone,
# $ENCORE_CACHE/protocol.git (default ~/.cache/encore). Files a version laid before are removed first, so that a
# file the protocol drops does not linger.
set -euo pipefail

dest=$(cd "${1:-$(dirname "$0")/..}" && pwd)
folders=(docs schemas tools)
laid=$(git -C "$dest" rev-parse --path-format=absolute --git-path protocol-laid)

if [ ! -f "$dest/protocol.lock" ]; then
  # A checkout from before the protocol had a repository of its own (2026-11-23), such as an old attempt's branch,
  # holds the protocol itself.
  if [ -f "$dest/docs/protocol.md" ]; then echo "protocol: $dest has no protocol.lock and holds the protocol itself"; exit 0; fi
  echo "error: $dest has no protocol.lock" >&2; exit 1
fi
ref=$(tr -d '[:space:]' < "$dest/protocol.lock")

# The files the last laying left, if this checkout's own commits do not track them.
if [ -f "$laid" ]; then
  while IFS= read -r f; do
    [ -n "$f" ] && ! git -C "$dest" ls-files --error-unmatch -- "$f" >/dev/null 2>&1 && rm -f "$dest/$f"
  done < "$laid"
fi

if [ -n "${ENCORE_PROTOCOL:-}" ]; then
  src=$(cd "$ENCORE_PROTOCOL" && pwd)
  (cd "$src" && git ls-files -co --exclude-standard -- "${folders[@]}") > "$laid"
  (cd "$src" && tar -cf - -T "$laid") | tar -xf - -C "$dest"
  echo "protocol: the working tree of $src laid over $dest (protocol.lock names $ref)"
  exit 0
fi

cache=${ENCORE_CACHE:-$HOME/.cache/encore}/protocol.git
url=https://github.com/encorescience/encore-protocol.git
[ -d "$cache" ] || git clone -q --bare "$url" "$cache"
if ! git -C "$cache" cat-file -e "$ref^{commit}" 2>/dev/null; then
  git -C "$cache" fetch -q --tags "$url" '+refs/heads/*:refs/heads/*'
  git -C "$cache" cat-file -e "$ref^{commit}" 2>/dev/null || git -C "$cache" fetch -q "$url" "$ref"
fi
git -C "$cache" ls-tree -r --name-only "$ref" -- "${folders[@]}" > "$laid"
git -C "$cache" archive "$ref" -- "${folders[@]}" | tar -xf - -C "$dest"
echo "protocol: $ref ($(git -C "$cache" rev-parse --short "$ref^{commit}")) laid over $dest"
