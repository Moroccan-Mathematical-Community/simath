#!/usr/bin/env bash
# Launcher for Dijkstra simulation on Linux
set -euo pipefail
PYTHON=${PYTHON:-python3}
DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../algorithms/Dijkstra" && pwd)
"$PYTHON" "$DIR/Dijkstra.py"
