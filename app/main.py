from fastapi import FastAPI
import time
import os
import platform

app = FastAPI(title="Cloud DevOps Telemetry Service", version="1.0.0")

START_TIME = time.time()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "InPrac Cloud Edge Gateway",
        "environment": os.getenv("APP_ENV", "production"),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "message": "Welcome to the containerized microservice stack."
    }

@app.get("/health")
def health_check():
    """Standard healthcheck endpoint used by Docker and load balancers."""
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
