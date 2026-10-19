# Service Level Objectives (SLOs) & Error Budget Policy

**System Target:** InPrac Cloud Edge Gateway (`lab.euprac.xyz`)  
**Architecture:** Cloudflare Edge TLS 1.3 → Nginx Reverse Proxy → FastAPI → Redis  
**Framework:** Google SRE Reliability Model & CNCF Production Standards  
**Evaluation Window:** 30-Day Rolling Window  

---

## 1. Executive Summary

This document defines the formal **Service Level Indicators (SLIs)**, **Service Level Objectives (SLOs)**, and **Error Budget Governance Policies** for the InPrac Cloud Edge Gateway. 

Rather than pursuing an impossible and economically wasteful "100% uptime" target, this framework balances rapid operational iteration with deterministic user reliability.

---

## 2. Service Level Indicators (SLIs)

### SLI 1: Availability (Success Rate)
The proportion of valid HTTP requests that return successful responses (non-5xx status codes):

$$\text{Availability SLI} = \frac{\text{Total HTTP Requests} - (\text{HTTP } 500 + 502 + 503 + 504)}{\text{Total Valid HTTP Requests}} \times 100$$

*Note: HTTP 4xx responses (e.g., 400 Bad Request, 404 Not Found, 429 Rate Limited) reflect client-side behavior and are excluded from the unreliability metric.*

### SLI 2: Ingress Latency
The proportion of successful requests completed within the user-acceptable latency boundary:

$$\text{Latency SLI} = \frac{\text{Requests completed with round-trip latency } \le 350\text{ ms}}{\text{Total Successful Requests}} \times 100$$

---

## 3. Service Level Objectives (SLOs)

| Metric | Target SLO | Rolling Window | Monthly Error Budget | Unreliability Budget Allowance |
| :--- | :---: | :---: | :---: | :---: |
| **Availability** | **99.9%** | 30 Days | **0.1%** | **43.2 Minutes of Allowed Downtime / Month** |
| **Ingress Latency** | **95.0%** | 30 Days | **5.0%** | $\le 350\text{ ms}$ for 95% of all traffic |

---

## 4. Error Budget Burn-Rate Alerting Policy

We enforce multi-window burn-rate alerting to distinguish between short transient network blips and catastrophic service failure:

| Alert Tier | Burn Rate Factor | Window Consumed | Detection Time | Actionable Notification |
| :--- | :---: | :---: | :---: | :--- |
| 🔴 **P1 Emergency (Page)** | **14.4x** | 2% of budget | **1 Hour** | Immediate on-call escalation; freeze all deployments; execute `502-bad-gateway-rca.md`. |
| 🟠 **P2 Urgent (Ticket)** | **6.0x** | 5% of budget | **6 Hours** | Dedicated incident investigation ticket created; review upstream queue saturation. |
| 🟡 **P3 Warning (Log)** | **1.0x** | 10% of budget | **3 Days** | Review error logs during scheduled operational maintenance. |

---

## 5. Error Budget Exhaustion Governance

When the rolling 30-day error budget is **100% exhausted** (more than 43.2 minutes of total downtime or severe 5xx spikes observed):
1. **Feature Deployment Freeze:** All routine application feature updates are suspended immediately.
2. **Mandatory SRE Focus:** 100% of engineering bandwidth is redirected toward infrastructure hardening, memory leak remediation, and runbook updates.
3. **Deployment Resumption Criteria:** Deployments resume only after the rolling 30-day availability recovers above 99.9% and a documented 5-Whys RCA is completed.

---

## 6. Architecture Failure Domain Disclosure (Residual Risk)

In accordance with transparent engineering principles, the residual risks of this single-node deployment are formally documented:

1. **Single Node Host Failure Domain:** The stack runs on an isolated Contabo KVM VPS (`167.86.110.106`). A physical datacenter power loss or host hypervisor crash represents an unavoidable Single Point of Failure (SPOF).
2. **Disaster Recovery Mitigation:** To mitigate single-node loss, cold-start backup archives with cryptographic SHA-256 manifests are generated nightly (`scripts/backup.sh`), with an audited Recovery Time Objective (RTO) of **42.3 seconds** into clean environments (`docs/runbooks/backup-restoration-drill.md`).
3. **High-Availability Roadmap:** Transitioning to 99.99% (Tier-4 HA) requires deploying a secondary active-passive replica in an independent geographic availability zone with Anycast DNS health check failover.
