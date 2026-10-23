#!/usr/bin/env bash
# ==============================================================================
# Script: analyze-logs.sh
# Description: Demonstrates core shell scripting commands (awk, grep, sed, sort,
#              uniq, cut) on real application log files.
# Usage: ./analyze-logs.sh
# ==============================================================================

set -eu

LOG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "============================================================"
echo "           SHELL SCRIPTING LOG ANALYSIS DEMO                "
echo "============================================================"
echo ""

# -------------------------------------------------------------
# 1. Total lines and size per log file
# -------------------------------------------------------------
echo "--- [1] Log Files Summary ---"
wc -l "$LOG_DIR"/*.log | awk '{printf "%-10s %s\n", $1, $2}'
echo ""

# -------------------------------------------------------------
# 2. Top 5 Client IP Addresses from access.log
# -------------------------------------------------------------
echo "--- [2] Top 5 Client IP Addresses (access.log) ---"
awk '{print $1}' "$LOG_DIR/access.log" | sort | uniq -c | sort -nr | head -n 5 | awk '{printf "  %6d requests  <-  %s\n", $1, $2}'
echo ""

# -------------------------------------------------------------
# 3. HTTP Status Code Distribution
# -------------------------------------------------------------
echo "--- [3] HTTP Status Codes Count (access.log) ---"
awk '{print $9}' "$LOG_DIR/access.log" | sort | uniq -c | sort -nr | while read -r count code; do
    printf "  Status %s : %4d requests\n" "$code" "$count"
done
echo ""

# -------------------------------------------------------------
# 4. Top 404 (Not Found) Endpoints
# -------------------------------------------------------------
echo "--- [4] Top 5 Missing URLs / 404 Errors (access.log) ---"
awk '$9 == "404" {print $7}' "$LOG_DIR/access.log" | sort | uniq -c | sort -nr | head -n 5 | awk '{printf "  %4d hits : %s\n", $1, $2}'
echo ""

# -------------------------------------------------------------
# 5. Application Log Level Counts (app.log)
# -------------------------------------------------------------
echo "--- [5] Log Level Distribution (app.log) ---"
grep -oE '\b(INFO|DEBUG|WARN|ERROR)\b' "$LOG_DIR/app.log" | sort | uniq -c | sort -nr | awk '{printf "  %-7s : %4d\n", $2, $1}'
echo ""

# -------------------------------------------------------------
# 6. Extract Unique Java Exceptions (app.log)
# -------------------------------------------------------------
echo "--- [6] Unique Java Exceptions and Occurrences (app.log) ---"
grep -E '^[a-zA-Z0-9\._]+Exception:' "$LOG_DIR/app.log" | cut -d: -f1 | sort | uniq -c | sort -nr | awk '{printf "  %3d  %s\n", $1, $2}'
echo ""

# -------------------------------------------------------------
# 7. Potential SSH Brute Force Attackers (auth.log)
# -------------------------------------------------------------
echo "--- [7] Failed SSH Logins by IP (auth.log) ---"
grep "Failed password" "$LOG_DIR/auth.log" | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -nr | awk '{printf "  %4d failed attempts from IP: %s\n", $1, $2}'
echo ""

# -------------------------------------------------------------
# 8. Slow Database Queries exceeding 1000ms (database.log)
# -------------------------------------------------------------
echo "--- [8] Top Slow Queries (> 1000ms) (database.log) ---"
grep "duration: " "$LOG_DIR/database.log" | awk -F'duration: ' '{print $2}' | awk '$1 > 1000 {print $1, $2, $0}' | head -n 3 | while read -r dur unit rest; do
    printf "  Latency: %s %s | Query: %s\n" "$dur" "$unit" "$(echo "$rest" | cut -d' ' -f3-)"
done
echo ""

# -------------------------------------------------------------
# 9. JSON Log parsing using native AWK / GREP (api-service.json.log)
# -------------------------------------------------------------
echo "--- [9] JSON Log Analysis: Error status codes (api-service.json.log) ---"
grep '"status_code": 500' "$LOG_DIR/api-service.json.log" | head -n 3 | while read -r line; do
    svc=$(echo "$line" | sed -n 's/.*"service": "\([^"]*\)".*/\1/p')
    route=$(echo "$line" | sed -n 's/.*"route": "\([^"]*\)".*/\1/p')
    ts=$(echo "$line" | sed -n 's/.*"timestamp": "\([^"]*\)".*/\1/p')
    printf "  [%s] Service: %-18s Route: %s -> HTTP 500\n" "$ts" "$svc" "$route"
done
echo ""

echo "============================================================"
echo " Analysis complete! Check logs/README.md for more exercises."
echo "============================================================"
