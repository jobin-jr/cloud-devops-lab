#!/bin/bash
# ==============================================================================
# InPrac Cloud Lab - Production Deployment & Health Verification
# ==============================================================================

set -euo pipefail

echo "=== Deploying Cloud Edge Infrastructure ==="

# Step 1: Pull and build latest container images
echo "[1/4] Building container images..."
docker compose build --pull

# Step 2: Launch containers in background
echo "[2/4] Starting containerized services..."
docker compose up -d --remove-orphans

# Step 3: Healthcheck verification loop (Wait up to 30s)
echo "[3/4] Verifying healthcheck endpoints..."
MAX_ATTEMPTS=6
ATTEMPT=1
SUCCESS=0

until [ $ATTEMPT -gt $MAX_ATTEMPTS ]; do
    if curl -s -f http://localhost/health > /dev/null; then
        echo "Healthcheck passed on attempt ${ATTEMPT}!"
        SUCCESS=1
        break
    else
        echo "Waiting for services to become healthy... (Attempt ${ATTEMPT}/${MAX_ATTEMPTS})"
        sleep 5
        ATTEMPT=$((ATTEMPT + 1))
    fi
done

# Step 4: Outcome check & automatic rollback trigger
if [ $SUCCESS -eq 1 ]; then
    echo "=== [SUCCESS] Deployment is healthy and accepting traffic on port 80 ==="
    docker compose ps
    if [ -n "${ALERT_WEBHOOK_URL:-}" ]; then
        curl -s -X POST -H "Content-Type: application/json" \
             -d '{"content":"✅ **InPrac Edge Gateway**: Production deployment healthy on lab.euprac.xyz"}' \
             "${ALERT_WEBHOOK_URL}" > /dev/null || true
    fi
else
    echo "=== [FAILURE] Healthcheck failed. Rolling back services... ==="
    docker compose down
    if [ -n "${ALERT_WEBHOOK_URL:-}" ]; then
        curl -s -X POST -H "Content-Type: application/json" \
             -d '{"content":"🚨 **InPrac Edge Gateway Alert**: Healthcheck failed! Automated rollback executed."}' \
             "${ALERT_WEBHOOK_URL}" > /dev/null || true
    fi
    exit 1
fi

