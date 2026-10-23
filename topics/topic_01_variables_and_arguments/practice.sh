#!/usr/bin/env bash
# ==============================================================================
# Topic 1: Practice Script - Variables, Arguments & Exit Codes
# Usage:
#   ./practice.sh [SERVICE_NAME] [REPLICAS]
# ==============================================================================

# 1. Variables defined inside script
DEPLOYMENT_DATE=$(date "+%Y-%m-%d %H:%M:%S")
NAMESPACE="production"

# 2. Positional Arguments with Safe Defaults
# If $1 is empty, default to "frontend-ui"
# If $2 is empty, default to 2
SERVICE_NAME="${1:-frontend-ui}"
REPLICAS="${2:-2}"

# 3. Special Parameters
SCRIPT_NAME="$0"
TOTAL_ARGS="$#"

# 4. Displaying Deployment Metadata
echo "=================================================="
echo "         DEVOPS SERVICE DEPLOYMENT SUMMARY        "
echo "=================================================="
echo "Script Executed:  ${SCRIPT_NAME}"
echo "Arguments Passed: ${TOTAL_ARGS}"
echo "Deployment Time:  ${DEPLOYMENT_DATE}"
echo "Target Namespace: ${NAMESPACE}"
echo "Service Name:     ${SERVICE_NAME}"
echo "Desired Replicas: ${REPLICAS}"
echo "=================================================="

# 5. Exit code: 0 indicates successful completion
exit 0
