from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import time
import os
import platform

from dashboard import DASHBOARD_HTML

app = FastAPI(title="InPrac Cloud Edge Gateway", version="1.2.0")

START_TIME = time.time()

@app.get("/")
def read_root(request: Request):
    """
    Intelligent Edge Route:
    - Renders the Cyber DevOps Mission Control Dashboard for web browsers.
    - Returns structured JSON for automated APIs, curl, and microservices.
    """
    accept_header = request.headers.get("accept", "").lower()
    user_agent = request.headers.get("user-agent", "").lower()

    # If accessed by a web browser or specifically requesting HTML
    if "text/html" in accept_header or "mozilla" in user_agent:
        return HTMLResponse(content=DASHBOARD_HTML, status_code=200)

    # Standard JSON telemetry payload
    return JSONResponse(
        content={
            "status": "online",
            "service": "InPrac Cloud Edge Gateway",
            "environment": os.getenv("APP_ENV", "production"),
            "uptime_seconds": round(time.time() - START_TIME, 2),
            "message": "Welcome to the containerized microservice stack."
        },
        status_code=200
    )

@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard():
    """Dedicated direct URL for the Cyber DevOps Mission Control Dashboard."""
    return HTMLResponse(content=DASHBOARD_HTML, status_code=200)

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
    """Simulated production telemetry endpoint."""
    return {
        "active_connections": 42,
        "memory_status": "optimal",
        "database_health": "connected",
        "requests_processed": 1024
    }
