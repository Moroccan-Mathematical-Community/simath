#!/bin/bash
# GaussPivot simulation launcher for Linux

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR/../../.."

cd "$REPO_ROOT" || exit 1

python3 algorithms/GaussPivot/GaussPivot.py "$@"
