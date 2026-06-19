#!/usr/bin/env bash

set -euo pipefail

PLATFORM="${1:-all}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

install_skill() {
  local target_root="$1"
  local target_dir="${target_root%/}/c2d"
  mkdir -p "${target_dir}"
  rsync -a --delete --exclude ".git" "${REPO_ROOT}/" "${target_dir}/"
  echo "Installed c2d skill to: ${target_dir}"
}

case "${PLATFORM}" in
  codex)
    install_skill "${HOME}/.codex/skills"
    ;;
  cursor)
    install_skill "${HOME}/.cursor/skills"
    ;;
  claude)
    install_skill "${HOME}/.claude/skills"
    mkdir -p "${HOME}/.claude/commands"
    cp "${REPO_ROOT}/.claude/commands/c2d.md" "${HOME}/.claude/commands/c2d.md"
    echo "Installed c2d Claude command to: ${HOME}/.claude/commands/c2d.md"
    ;;
  all)
    install_skill "${HOME}/.codex/skills"
    install_skill "${HOME}/.cursor/skills"
    install_skill "${HOME}/.claude/skills"
    mkdir -p "${HOME}/.claude/commands"
    cp "${REPO_ROOT}/.claude/commands/c2d.md" "${HOME}/.claude/commands/c2d.md"
    echo "Installed c2d Claude command to: ${HOME}/.claude/commands/c2d.md"
    ;;
  *)
    echo "Usage: scripts/install_c2d.sh [codex|cursor|claude|all]" >&2
    exit 1
    ;;
esac
