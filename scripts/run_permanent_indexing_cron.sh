#!/bin/bash
# ==============================================================================
# Permanent Enterprise Indexing & SEO Cron Execution Script
# Domain: https://krisalahiranandanitownships.com/
# ==============================================================================

set -e

# Project root directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${PROJECT_DIR}"

# Create logs directory if missing
mkdir -p "${PROJECT_DIR}/logs"
LOG_FILE="${PROJECT_DIR}/logs/indexing_cron.log"

# Keep last 5,000 lines of log to prevent disk growth
if [ -f "${LOG_FILE}" ] && [ $(wc -l < "${LOG_FILE}") -gt 10000 ]; then
    tail -n 5000 "${LOG_FILE}" > "${LOG_FILE}.tmp" && mv "${LOG_FILE}.tmp" "${LOG_FILE}"
fi

echo "======================================================================" >> "${LOG_FILE}"
echo "[$(date -u +"%Y-%m-%d %H:%M:%S UTC")] PERMANENT INDEXING CRON TRIGGERED" >> "${LOG_FILE}"
echo "Working Directory: ${PROJECT_DIR}" >> "${LOG_FILE}"
echo "======================================================================" >> "${LOG_FILE}"

# Execute master daily SEO sweep
if /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 scripts/daily_seo_sweep.py >> "${LOG_FILE}" 2>&1; then
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S UTC")] CRON EXECUTION SUCCESSFUL" >> "${LOG_FILE}"
else
    echo "[$(date -u +"%Y-%m-%d %H:%M:%S UTC")] CRON EXECUTION FAILED - RETURN CODE $?" >> "${LOG_FILE}"
fi

echo "======================================================================" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
