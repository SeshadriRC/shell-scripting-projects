#!/usr/bin/env bash
# ==============================================================================
# Topic 1 Exercise: Create your Server Configuration Script
# Task: Edit the variables below and run the script!
#
# Run with:
#   ./exercise.sh
# or with arguments:
#   ./exercise.sh server-01 22
# ==============================================================================

# TODO: Define a default SERVER_NAME using $1 with fallback "k8s-master-node"
SERVER_NAME="${1:-k8s-master-node}"

# TODO: Define a default PORT using $2 with fallback "22"
SSH_PORT="${2:-22}"

# TODO: Define a static variable for ENVIRONMENT
ENVIRONMENT="staging"

echo "--------------------------------------------------"
echo "Configuring Server:"
echo "Hostname:    ${SERVER_NAME}"
echo "Port:        ${SSH_PORT}"
echo "Environment: ${ENVIRONMENT}"
echo "--------------------------------------------------"

# Exit successfully
exit 0
