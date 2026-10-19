from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import time
import os
import platform

from dashboard import DASHBOARD_HTML

app = FastAPI(title="InPrac Cloud Edge Gateway", version="1.2.1")

START_TIME = time.time()
REQUEST_COUNTER = 0

@app.get("/")
def read_root(request: Request):
    """
    Intelligent & Cache-Safe Edge Route:
    - Renders the Cyber DevOps Mission Control Dashboard for web browsers.
    - Honors explicit application/json requests even from browsers or test tools.
    - Emits Cache-Control: no-store and Vary: Accept to prevent proxy cache variant confusion.
    """
    global REQUEST_COUNTER
    REQUEST_COUNTER += 1

    accept = request.headers.get("accept", "").lower()
    sec_fetch_dest = request.headers.get("sec-fetch-dest", "").lower()
    user_agent = request.headers.get("user-agent", "").lower()

    # Rule 1: If client explicitly requests application/json, always return JSON
    if "application/json" in accept and "text/html" not in accept:
        return JSONResponse(
            content={
                "status": "online",
                "service": "InPrac Cloud Edge Gateway",
                "environment": os.getenv("APP_ENV", "production"),
                "uptime_seconds": round(time.time() - START_TIME, 2),
                "requests_served": REQUEST_COUNTER,
                "message": "Welcome to the containerized microservice stack."
            },
            headers={"Cache-Control": "no-store, must-revalidate", "Vary": "Accept"}
        )

    # Rule 2: If browser navigation document or text/html is requested, return Dashboard
    if "text/html" in accept or sec_fetch_dest == "document" or ("mozilla" in user_agent and "application/json" not in accept):
        return HTMLResponse(
            content=DASHBOARD_HTML,
            status_code=200,
            headers={"Cache-Control": "no-store, must-revalidate", "Vary": "Accept"}
        )

    # Rule 3: Default fallback for curl / scripts / automated scrapers
    return JSONResponse(
        content={
            "status": "online",
            "service": "InPrac Cloud Edge Gateway",
            "environment": os.getenv("APP_ENV", "production"),
            "uptime_seconds": round(time.time() - START_TIME, 2),
            "requests_served": REQUEST_COUNTER,
            "message": "Welcome to the containerized microservice stack."
        },
        headers={"Cache-Control": "no-store, must-revalidate", "Vary": "Accept"}
    )

@app.get("/api/v1/status")
def get_status():
    """Deterministic JSON status endpoint for monitoring and automation."""
    global REQUEST_COUNTER
    return {
        "status": "online",
        "service": "InPrac Cloud Edge Gateway",
        "environment": os.getenv("APP_ENV", "production"),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "requests_served": REQUEST_COUNTER
    }

@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard():
    """Deterministic HTML-only URL for the Mission Control Dashboard."""
    return HTMLResponse(
        content=DASHBOARD_HTML,
        status_code=200,
        headers={"Cache-Control": "no-cache"}
    )

@app.get("/health")
def health_check():
    """Standard healthcheck endpoint used by Docker, load balancers, and monitoring."""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "system": {
            "os": platform.system(),
            "release": platform.release(),
            "python_version": platform.python_version()
        }
    }

@app.get("/api/v1/metrics")
def get_metrics():
    """Production telemetry endpoint with transparent telemetry attribution."""
    global REQUEST_COUNTER
    return {
        "source": "simulated_cluster_telemetry",
        "active_connections": 42,
        "memory_status": "optimal",
        "database_health": "connected",
        "requests_processed": 1024 + REQUEST_COUNTER
    }
