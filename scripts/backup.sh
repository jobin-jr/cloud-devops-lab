#!/bin/bash
# ==============================================================================
# InPrac Cloud Lab - Automated Backup & Disaster Recovery Script
# ==============================================================================

set -euo pipefail

BACKUP_DIR="./backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="cloud_lab_backup_${TIMESTAMP}.tar.gz"

echo "=== Starting Automated Backup: ${TIMESTAMP} ==="

# Ensure backup directory exists
mkdir -p "${BACKUP_DIR}"

# Export Redis data snapshot if container is running
if docker ps --format '{{.Names}}' | grep -q "inprac_cache"; then
    echo "[1/3] Triggering Redis background save..."
    docker exec inprac_cache redis-cli bgsave || true
    sleep 2
fi

# Archive configurations, application code, and data volumes
echo "[2/3] Compressing application configurations and data..."
tar -czf "${BACKUP_DIR}/${ARCHIVE_NAME}" \
    --exclude="backups" \
    --exclude=".git" \
    --exclude="__pycache__" \
    compose.yaml \
    nginx/ \
    app/

# Generate SHA256 integrity checksum
echo "[3/3] Generating checksum for verification..."
sha256sum "${BACKUP_DIR}/${ARCHIVE_NAME}" > "${BACKUP_DIR}/${ARCHIVE_NAME}.sha256"

# Rotate backups: Retain only the last 7 daily archives
echo "Cleaning up archives older than 7 days..."
find "${BACKUP_DIR}" -type f -name "cloud_lab_backup_*.tar.gz" -mtime +7 -delete
find "${BACKUP_DIR}" -type f -name "cloud_lab_backup_*.sha256" -mtime +7 -delete

echo "=== Backup Completed Successfully: ${BACKUP_DIR}/${ARCHIVE_NAME} ==="
