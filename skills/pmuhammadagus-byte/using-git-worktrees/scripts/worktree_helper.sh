#!/usr/bin/env bash
# Helper to create and clean up git worktrees (using-git-worktrees).
# Safe by default: 'create' only; 'remove' requires an explicit flag + prompt.
# The branch is preserved unless you delete it separately.
#
# Usage:
#   bash scripts/worktree_helper.sh create <path> <branch-name> [start-point]
#   bash scripts/worktree_helper.sh remove <path>
#   bash scripts/worktree_helper.sh list
set -euo pipefail

cmd="${1:-}"
case "$cmd" in
  create)
    path="${2:-}"
    branch="${3:-}"
    start="${4:-}"
    if [ -z "$path" ] || [ -z "$branch" ]; then
      echo "Usage: worktree_helper.sh create <path> <branch-name> [start-point]" >&2
      exit 1
    fi
    if [ -e "$path" ]; then
      echo "Path $path already exists." >&2
      exit 1
    fi
    if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      echo "Not inside a git repo (run from the repo root)." >&2
      exit 1
    fi
    if [ -n "$start" ]; then
      git worktree add "$path" -b "$branch" "$start"
    else
      git worktree add "$path" -b "$branch"
    fi
    echo "Created worktree at $path on branch $branch"
    echo "Do your work there, then: worktree_helper.sh remove $path"
    ;;
  remove)
    path="${2:-}"
    if [ -z "$path" ]; then echo "Usage: worktree_helper.sh remove <path>" >&2; exit 1; fi
    printf "Remove worktree %s (branch stays unless deleted separately)? [y/N]: " "$path"
    read -r ans
    if [[ "$ans" == y || "$ans" == Y ]]; then
      git worktree remove "$path" --force 2>/dev/null || git worktree remove "$path"
      git worktree prune
      echo "Removed and pruned $path"
    else
      echo "Aborted."
    fi
    ;;
  list)
    git worktree list
    ;;
  *)
    echo "Usage: worktree_helper.sh {create|remove|list} ..." >&2
    exit 1
    ;;
esac
