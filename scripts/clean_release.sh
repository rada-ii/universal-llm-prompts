#!/usr/bin/env bash
set -euo pipefail

NAME="universal-llm-prompts"
DATE="$(date +%Y%m%d)"
DIST_DIR="dist"
ARCHIVE="$DIST_DIR/${NAME}-${DATE}.zip"

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

if [ -d ".git" ] && command -v git >/dev/null 2>&1; then
  echo "INFO: Using git ls-files to build archive"
  git ls-files | zip -@ "$ARCHIVE"
else
  echo "INFO: Using zip -r with excludes"
  zip -r "$ARCHIVE" . -x "*.git/*" "*__MACOSX/*" "*.DS_Store" "*.zip" "dist/*"
fi

# Strip macOS cruft if any slipped through
zip -d "$ARCHIVE" "__MACOSX/*" "*.DS_Store" >/dev/null || true

echo "SUCCESS: Created $ARCHIVE"