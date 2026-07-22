#!/usr/bin/env bash
# Serve the dashboard locally, auto-pulling the latest committed build.
# Usage: ./serve_dashboard.sh [port]   (default 8787)
# Open http://localhost:8787/dashboard.html — the page refreshes itself every
# 15 minutes; this script pulls the repo every 10 so the file it serves is fresh.
set -euo pipefail
cd "$(dirname "$0")"
PORT="${1:-8787}"

( while true; do git pull --quiet || true; sleep 600; done ) &
PULLER=$!
trap 'kill $PULLER 2>/dev/null' EXIT

echo "Dashboard at: http://localhost:${PORT}/dashboard.html (Ctrl-C to stop)"
python3 -m http.server "$PORT" --bind 127.0.0.1
