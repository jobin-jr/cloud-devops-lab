# Operational Engineering & Incident Response Runbooks

Welcome to the production operations and disaster recovery documentation for the **InPrac Cloud Edge Gateway**.

This directory contains standardized, evidence-backed operational runbooks designed to guide systems administrators, infrastructure engineers, and technical support staff through triage, diagnosis, remediation, and root-cause analysis (RCA) during system anomalies.

---

## 📋 Runbook Directory Index

| Runbook File | Scenario & Scope | Operational Category | Target RTO / SLA |
| :--- | :--- | :--- | :--- |
| **[`502-bad-gateway-rca.md`](502-bad-gateway-rca.md)** | Upstream reverse proxy communication breakdown, socket drops, and worker starvation. | 🔴 High Severity (Production Applicable) | RTO: < 5 Minutes |
| **[`cgroup-oom-mitigation.md`](cgroup-oom-mitigation.md)** | Linux kernel cgroup memory exhaustion (`OOMKilled: true`), container thrashing, and memory leak triage. | 🟠 Medium/High Severity (Production Applicable) | RTO: < 8 Minutes |
| **[`backup-restoration-drill.md`](backup-restoration-drill.md)** | Cold-start disaster recovery restoration drill into isolated staging with SHA256 cryptographic verification. | 🟢 Maintenance & Drill (Controlled Verification) | RTO: < 60 Seconds (Measured: 42s) |
| **[`redis-data-recovery.md`](redis-data-recovery.md)** | Cache corruption, append-only file (AOF) recovery, and cache warming procedures. | 🟡 Low/Medium Severity (Controlled Lab Drill) | RTO: < 10 Minutes |
| **[`minecraft-server-incident-response.md`](minecraft-server-incident-response.md)** | Minecraft (Paper 1.20+) & Velocity proxy routing drops, JVM heap vs cgroup OOM, low TPS/MSPT profiling, and Pterodactyl triage. | 🎮 Game Hosting & Infrastructure | RTO: < 8 Minutes |

---

## 🏛️ Operational Philosophy

1. **Least-Invasive Remediation First:** Always prefer surgical, reversible fixes over broad restarts. Blindly restarting services destroys ephemeral logs and process crash state required for true Root Cause Analysis.
2. **Preserve Forensic Evidence:** Copy logs, inspect socket tables (`ss -tulpn`), and snapshot memory state before making destructive changes.
3. **Transparent Communication:** Customers and stakeholders must receive prompt, empathetic, and technically accurate updates without speculation or false promises.
4. **Mandatory Post-Incident RCA:** Every major anomaly requires a documented 5-Whys Root Cause Analysis and permanent preventative action items.

---

## 🛠️ Global Diagnostic Quick-Reference

```bash
# Check status of all stack containers
docker compose ps

# Inspect real-time container resource utilization vs cgroup caps
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}"

# Inspect host memory and swap allocation
free -m

# Inspect all listening TCP/UDP sockets
ss -tulpn

# Inspect recent Nginx reverse proxy error logs
docker logs --tail 100 inprac_reverse_proxy

# Inspect recent core API service logs
docker logs --tail 100 inprac_api_service
```
