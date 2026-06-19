#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: scripts/install_slash_commands.sh /abs/path/to/project [cursor|claude|both]" >&2
  exit 1
fi

PROJECT_ROOT="$1"
PLATFORM="${2:-both}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

case "${PLATFORM}" in
  cursor)
    mkdir -p "${PROJECT_ROOT%/}/.cursor/commands"
    cp "${REPO_ROOT}/.cursor/commands/c2d.md" "${PROJECT_ROOT%/}/.cursor/commands/c2d.md"
    ;;
  claude)
    mkdir -p "${PROJECT_ROOT%/}/.claude/commands"
    cp "${REPO_ROOT}/.claude/commands/c2d.md" "${PROJECT_ROOT%/}/.claude/commands/c2d.md"
    ;;
  both)
    mkdir -p "${PROJECT_ROOT%/}/.cursor/commands" "${PROJECT_ROOT%/}/.claude/commands"
    cp "${REPO_ROOT}/.cursor/commands/c2d.md" "${PROJECT_ROOT%/}/.cursor/commands/c2d.md"
    cp "${REPO_ROOT}/.claude/commands/c2d.md" "${PROJECT_ROOT%/}/.claude/commands/c2d.md"
    ;;
  *)
    echo "Invalid platform: ${PLATFORM}. Use cursor, claude, or both." >&2
    exit 1
    ;;
esac

echo "Installed c2d slash command support to: ${PROJECT_ROOT}"
