#!/usr/bin/env bash
# ==============================================================================
# Script: generate-logs.sh
# Description: Generates or continuously appends sample log entries for shell scripting practice.
# Usage:
#   ./generate-logs.sh          -> Generates fresh sample log files
#   ./generate-logs.sh --stream  -> Continuously appends new lines to app.log & access.log
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "${1:-}" == "--stream" ]]; then
    echo "============================================================"
    echo " Streaming live logs to app.log & access.log (Ctrl+C to stop)"
    echo " Open another terminal and run:"
    echo "   tail -f logs/app.log"
    echo "   tail -f logs/access.log"
    echo "============================================================"

    HTTP_STATUSES=(200 200 200 200 201 400 401 403 404 500 502)
    METHODS=("GET" "GET" "POST" "GET" "PUT" "DELETE")
    ROUTES=("/api/v1/products" "/api/v1/cart" "/api/v1/orders" "/health" "/login" "/metrics")
    IPS=("192.168.1.45" "192.168.1.102" "203.0.113.195" "198.51.100.88" "10.0.2.15")

    while true; do
        sleep_sec=$((1 + RANDOM % 3))
        sleep "$sleep_sec"

        NOW_TS="$(date '+%Y-%m-%d %H:%M:%S.000')"
        ACCESS_TS="$(date '+%d/%b/%Y:%H:%M:%S +0000')"
        RAND_IP="${IPS[$RANDOM % ${#IPS[@]}]}"
        RAND_METHOD="${METHODS[$RANDOM % ${#METHODS[@]}]}"
        RAND_ROUTE="${ROUTES[$RANDOM % ${#ROUTES[@]}]}"
        RAND_STATUS="${HTTP_STATUSES[$RANDOM % ${#HTTP_STATUSES[@]}]}"
        RAND_BYTES=$((RANDOM % 5000 + 100))

        # Append to access.log
        echo "$RAND_IP - - [$ACCESS_TS] \"$RAND_METHOD $RAND_ROUTE HTTP/1.1\" $RAND_STATUS $RAND_BYTES \"-\" \"curl/8.5.0\"" >> "$SCRIPT_DIR/access.log"

        # Append to app.log
        if [[ "$RAND_STATUS" == "500" ]]; then
            echo "$NOW_TS [http-nio-8080-exec-1] ERROR c.e.controller.GlobalExceptionHandler - [trace_id=trace_$RANDOM] InternalServerError: Database query timed out" >> "$SCRIPT_DIR/app.log"
        elif [[ "$RAND_STATUS" == "404" ]]; then
            echo "$NOW_TS [http-nio-8080-exec-2] WARN  c.e.service.MetricsWatcher - [trace_id=trace_$RANDOM] Resource not found: $RAND_ROUTE" >> "$SCRIPT_DIR/app.log"
        else
            echo "$NOW_TS [http-nio-8080-exec-3] INFO  c.e.service.CoreApplication - [trace_id=trace_$RANDOM] Successfully served request to $RAND_ROUTE" >> "$SCRIPT_DIR/app.log"
        fi

        echo "[$(date '+%H:%M:%S')] Appended 1 entry to access.log and app.log"
    done
else
    echo "Generating fresh sample log files using python3..."
    python3 "$SCRIPT_DIR/generate_logs.py"
    echo ""
    echo "Done! Available log files in $SCRIPT_DIR:"
    ls -lh "$SCRIPT_DIR"/*.log
fi
