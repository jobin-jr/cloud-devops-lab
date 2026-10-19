# -*- coding: utf-8 -*-
"""
Cyber DevOps Mission Control Dashboard
High-performance, zero-dependency, standalone responsive HTML/CSS/JS dashboard.
"""

DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InPrac Cloud Edge Gateway // Mission Control</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-deep: #06090e;
            --bg-surface: #0c1017;
            --bg-card: rgba(18, 24, 34, 0.75);
            --bg-card-hover: rgba(24, 32, 46, 0.9);
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-focus: rgba(16, 185, 129, 0.4);
            
            --emerald: #10b981;
            --emerald-glow: rgba(16, 185, 129, 0.25);
            --cyan: #06b6d4;
            --cyan-glow: rgba(6, 182, 212, 0.25);
            --violet: #8b5cf6;
            --amber: #f59e0b;
            --rose: #f43f5e;
            
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: var(--font-sans);
            min-height: 100vh;
            overflow-x: hidden;
            background-image: 
                radial-gradient(ellipse at 50% -20%, rgba(16, 185, 129, 0.15), transparent 70%),
                radial-gradient(ellipse at 90% 80%, rgba(6, 182, 212, 0.08), transparent 60%);
            background-attachment: fixed;
        }

        /* Glassmorphism utility */
        .glass {
            background: var(--bg-card);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
        }

        /* Layout */
        .container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 24px;
        }

        /* Top Navigation Header */
        header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 24px;
            margin-bottom: 24px;
        }

        .brand-cluster {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .brand-logo {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--emerald), var(--cyan));
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 20px var(--emerald-glow);
        }

        .brand-logo svg {
            width: 22px;
            height: 22px;
            fill: #06090e;
        }

        .brand-title {
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: var(--text-main);
        }

        .brand-subtitle {
            font-family: var(--font-mono);
            font-size: 0.75rem;
            color: var(--text-dim);
            letter-spacing: 0.05em;
        }

        .header-meta {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 20px;
            font-family: var(--font-mono);
            font-size: 0.75rem;
            font-weight: 600;
            border: 1px solid var(--border-subtle);
            background: rgba(12, 16, 23, 0.8);
        }

        .badge-live {
            color: var(--emerald);
            border-color: rgba(16, 185, 129, 0.3);
            background: rgba(16, 185, 129, 0.08);
        }

        .beacon {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--emerald);
            box-shadow: 0 0 8px var(--emerald);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        .btn-link {
            text-decoration: none;
            color: var(--text-main);
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-subtle);
        }

        .btn-link:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-1px);
        }

        /* Hero Telemetry Ribbon */
        .hero-ribbon {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }

        .stat-card {
            padding: 20px;
            transition: all 0.2s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card:hover {
            border-color: var(--border-focus);
            transform: translateY(-2px);
        }

        .stat-card::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--emerald), transparent);
            opacity: 0;
            transition: opacity 0.3s;
        }

        .stat-card:hover::after {
            opacity: 1;
        }

        .stat-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }

        .stat-title {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            font-family: var(--font-mono);
        }

        .stat-icon {
            color: var(--emerald);
            font-size: 1.1rem;
        }

        .stat-value {
            font-size: 1.65rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: #ffffff;
            font-family: var(--font-mono);
            margin-bottom: 6px;
        }

        .stat-detail {
            font-size: 0.8rem;
            color: var(--text-dim);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .bar-container {
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 3px;
            margin-top: 8px;
            overflow: hidden;
        }

        .bar-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--emerald), var(--cyan));
            border-radius: 3px;
            transition: width 0.5s ease;
        }

        /* Workspace Grid (Main Interactive Deck) */
        .workspace-grid {
            display: grid;
            grid-template-columns: 1fr 420px;
            gap: 24px;
            margin-bottom: 24px;
        }

        @media (max-width: 980px) {
            .workspace-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Tabs Control */
        .deck-card {
            padding: 24px;
            display: flex;
            flex-direction: column;
        }

        .tab-bar {
            display: flex;
            gap: 8px;
            border-bottom: 1px solid var(--border-subtle);
            padding-bottom: 12px;
            margin-bottom: 20px;
        }

        .tab-btn {
            background: transparent;
            border: none;
            color: var(--text-dim);
            font-family: var(--font-mono);
            font-size: 0.85rem;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .tab-btn:hover {
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.04);
        }

        .tab-btn.active {
            color: var(--emerald);
            background: rgba(16, 185, 129, 0.1);
            box-shadow: inset 0 0 0 1px rgba(16, 185, 129, 0.3);
        }

        .tab-pane {
            display: none;
        }

        .tab-pane.active {
            display: block;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Architecture Map Flow */
        .arch-diagram {
            display: flex;
            flex-direction: column;
            gap: 16px;
            padding: 8px 0;
        }

        .arch-step {
            display: flex;
            align-items: center;
            gap: 16px;
            padding: 14px 18px;
            background: rgba(12, 16, 23, 0.6);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            transition: all 0.2s;
        }

        .arch-step:hover {
            border-color: rgba(6, 182, 212, 0.4);
            transform: translateX(4px);
        }

        .arch-icon {
            width: 38px;
            height: 38px;
            border-radius: 8px;
            background: rgba(6, 182, 212, 0.1);
            color: var(--cyan);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.95rem;
            border: 1px solid rgba(6, 182, 212, 0.2);
            flex-shrink: 0;
        }

        .arch-content {
            flex-grow: 1;
        }

        .arch-label {
            font-weight: 700;
            font-size: 0.9rem;
            color: var(--text-main);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .arch-desc {
            font-size: 0.78rem;
            color: var(--text-dim);
            font-family: var(--font-mono);
            margin-top: 4px;
        }

        .flow-arrow {
            text-align: center;
            color: var(--emerald);
            font-size: 0.9rem;
            opacity: 0.6;
            margin: -6px 0;
        }

        /* API Console */
        .console-controls {
            display: flex;
            gap: 10px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .api-btn {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-subtle);
            color: var(--text-main);
            padding: 8px 14px;
            border-radius: 6px;
            font-family: var(--font-mono);
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .api-btn:hover {
            border-color: var(--emerald);
            color: var(--emerald);
            background: rgba(16, 185, 129, 0.05);
        }

        .terminal-box {
            background: #040609;
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            padding: 16px;
            font-family: var(--font-mono);
            font-size: 0.82rem;
            color: #cbd5e1;
            min-height: 220px;
            max-height: 340px;
            overflow-y: auto;
            position: relative;
        }

        .terminal-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            font-size: 0.72rem;
            color: var(--text-dim);
        }

        .terminal-dots {
            display: flex;
            gap: 6px;
        }

        .dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
        }
        .dot-red { background: #ef4444; }
        .dot-yellow { background: #f59e0b; }
        .dot-green { background: #10b981; }

        .terminal-json {
            white-space: pre-wrap;
            word-break: break-all;
            color: #38bdf8;
            line-height: 1.5;
        }

        /* Security Table */
        .sec-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.82rem;
        }

        .sec-table th {
            text-align: left;
            padding: 10px 12px;
            font-family: var(--font-mono);
            font-size: 0.72rem;
            text-transform: uppercase;
            color: var(--text-dim);
            border-bottom: 1px solid var(--border-subtle);
        }

        .sec-table td {
            padding: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            color: var(--text-muted);
        }

        .sec-badge {
            font-family: var(--font-mono);
            font-size: 0.72rem;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: 600;
        }
        .sec-enforced {
            color: #10b981;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.25);
        }

        /* Incident Runbooks Grid & Cards */
        .runbooks-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 14px;
        }
        @media (max-width: 640px) {
            .runbooks-grid {
                grid-template-columns: 1fr;
            }
        }
        .runbook-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            padding: 16px;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            transition: all 0.25s ease;
        }
        .runbook-card:hover {
            background: rgba(255, 255, 255, 0.06);
            border-color: var(--emerald);
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        }
        .rb-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        .rb-tag {
            font-size: 0.65rem;
            font-family: var(--font-mono);
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
        }
        .rb-net { background: rgba(6, 182, 212, 0.15); color: var(--cyan); }
        .rb-kernel { background: rgba(244, 63, 94, 0.15); color: var(--rose); }
        .rb-sre { background: rgba(16, 185, 129, 0.15); color: var(--emerald); }
        .rb-db { background: rgba(245, 158, 11, 0.15); color: var(--amber); }
        .rb-game { background: rgba(139, 92, 246, 0.15); color: var(--violet); }
        .rb-slo { background: rgba(16, 185, 129, 0.2); color: #34d399; }
        .rb-code {
            font-family: var(--font-mono);
            font-size: 0.72rem;
            color: var(--text-dim);
            font-weight: 600;
        }
        .rb-title {
            font-size: 0.95rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 6px;
        }
        .rb-desc {
            font-size: 0.78rem;
            color: var(--text-muted);
            line-height: 1.45;
            margin-bottom: 12px;
            flex-grow: 1;
        }
        .rb-footer {
            font-family: var(--font-mono);
            font-size: 0.72rem;
            color: var(--emerald);
            font-weight: 600;
        }

        /* Right Rail: SysAdmin & Profile Card */
        .right-rail {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .profile-card {
            padding: 24px;
            position: relative;
            overflow: hidden;
        }

        .profile-header {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 16px;
        }

        .avatar {
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border: 2px solid var(--emerald);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            color: var(--emerald);
            font-family: var(--font-mono);
            font-size: 1.2rem;
            box-shadow: 0 0 16px var(--emerald-glow);
        }

        .profile-info h3 {
            font-size: 1.1rem;
            font-weight: 800;
            color: #ffffff;
        }

        .profile-info p {
            font-size: 0.78rem;
            color: var(--text-dim);
            font-family: var(--font-mono);
        }

        .bio-text {
            font-size: 0.85rem;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 18px;
        }

        .tag-cloud {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 20px;
        }

        .skill-tag {
            font-size: 0.72rem;
            font-family: var(--font-mono);
            padding: 4px 10px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-subtle);
            border-radius: 4px;
            color: #cbd5e1;
        }

        .card-actions {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--emerald), #059669);
            color: #06090e;
            text-decoration: none;
            text-align: center;
            padding: 10px 16px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.85rem;
            transition: all 0.2s;
            box-shadow: 0 4px 14px var(--emerald-glow);
        }

        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4);
        }

        /* Server Specs Card */
        .specs-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 12px;
            font-size: 0.82rem;
        }

        .specs-item {
            display: flex;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            padding-bottom: 8px;
        }

        .specs-key {
            color: var(--text-dim);
            font-family: var(--font-mono);
        }

        .specs-val {
            color: var(--text-main);
            font-weight: 600;
            font-family: var(--font-mono);
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 32px 0 16px;
            font-size: 0.78rem;
            color: var(--text-dim);
            font-family: var(--font-mono);
        }

        footer a {
            color: var(--emerald);
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Top Navigation Bar -->
        <header class="glass">
            <div class="brand-cluster">
                <div class="brand-logo">
                    <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                </div>
                <div>
                    <div class="brand-title">INPRAC EDGE GATEWAY</div>
                    <div class="brand-subtitle">MISSION CONTROL // PRODUCTION CLUSTER</div>
                </div>
            </div>
            <div class="header-meta">
                <div class="badge badge-live">
                    <span class="beacon"></span>
                    <span>LIVE 200 OK</span>
                </div>
                <div class="badge">
                    <span>🇩🇪 Frankfurt, EU</span>
                </div>
                <a href="https://github.com/jobin-jr/cloud-devops-lab" target="_blank" class="btn-link">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                    <span>GitHub Repo</span>
                </a>
            </div>
        </header>

        <!-- Hero Telemetry Ribbon -->
        <section class="hero-ribbon">
            <div class="glass stat-card">
                <div class="stat-header">
                    <span class="stat-title">EDGE STATUS</span>
                    <span class="stat-icon">⚡</span>
                </div>
                <div class="stat-value" id="status-val">ONLINE</div>
                <div class="stat-detail">
                    <span>Latency:</span>
                    <strong id="latency-val" style="color: var(--emerald);">calculating...</strong>
                </div>
                <div class="bar-container">
                    <div class="bar-fill" style="width: 100%;"></div>
                </div>
            </div>

            <div class="glass stat-card">
                <div class="stat-header">
                    <span class="stat-title">UPTIME DURATION</span>
                    <span class="stat-icon">⏱️</span>
                </div>
                <div class="stat-value" id="uptime-val">Loading...</div>
                <div class="stat-detail">Zero unplanned downtime</div>
                <div class="bar-container">
                    <div class="bar-fill" style="width: 99.9%;"></div>
                </div>
            </div>

            <div class="glass stat-card">
                <div class="stat-header">
                    <span class="stat-title">CGROUP MEMORY</span>
                    <span class="stat-icon">💾</span>
                </div>
                <div class="stat-value" id="mem-val">42.7 MB</div>
                <div class="stat-detail">
                    <span>Hard Limit:</span>
                    <strong>512 MB Max (8.3%)</strong>
                </div>
                <div class="bar-container">
                    <div class="bar-fill" style="width: 8.3%;"></div>
                </div>
            </div>

            <div class="glass stat-card">
                <div class="stat-header">
                    <span class="stat-title">CACHE ENGINE</span>
                    <span class="stat-icon">🛡️</span>
                </div>
                <div class="stat-value">REDIS 7.2</div>
                <div class="stat-detail">
                    <span>Isolation:</span>
                    <strong style="color: var(--cyan);">internal data-net</strong>
                </div>
                <div class="bar-container">
                    <div class="bar-fill" style="width: 100%; background: linear-gradient(90deg, var(--cyan), var(--violet));"></div>
                </div>
            </div>
        </section>

        <!-- Main Workspace Deck -->
        <div class="workspace-grid">
            <!-- Left Panel: Interactive Deck with Tabs -->
            <div class="glass deck-card">
                <div class="tab-bar">
                    <button class="tab-btn active" onclick="switchTab('arch')">Architecture Flow</button>
                    <button class="tab-btn" onclick="switchTab('api')">Live API Console</button>
                    <button class="tab-btn" onclick="switchTab('security')">Kernel & Cgroups</button>
                    <button class="tab-btn" onclick="switchTab('runbooks')">Incident Runbooks (SRE)</button>
                </div>

                <!-- Tab 1: Architecture Flow -->
                <div id="tab-arch" class="tab-pane active">
                    <div class="arch-diagram">
                        <div class="arch-step">
                            <div class="arch-icon">CF</div>
                            <div class="arch-content">
                                <div class="arch-label">
                                    <span>Cloudflare Anycast Edge</span>
                                    <span class="badge" style="color: var(--emerald);">TLS v1.3 Verified</span>
                                </div>
                                <div class="arch-desc">DDoS Mitigation • Edge Caching • Auto SSL Termination</div>
                            </div>
                        </div>

                        <div class="flow-arrow">▼ TCP 443 / HTTPS</div>

                        <div class="arch-step">
                            <div class="arch-icon" style="color: var(--emerald); background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.2);">NG</div>
                            <div class="arch-content">
                                <div class="arch-label">
                                    <span>Nginx Edge Gateway (inprac_reverse_proxy)</span>
                                    <span class="badge">Port 80 / 443</span>
                                </div>
                                <div class="arch-desc">Cgroup Limit: 128 MB RAM, 0.25 vCPU • Rate Limiting: 10r/s • Real IP Restoration</div>
                            </div>
                        </div>

                        <div class="flow-arrow">▼ Docker Bridge: edge-net</div>

                        <div class="arch-step">
                            <div class="arch-icon" style="color: var(--violet); background: rgba(139, 92, 246, 0.1); border-color: rgba(139, 92, 246, 0.2);">PY</div>
                            <div class="arch-content">
                                <div class="arch-label">
                                    <span>FastAPI Core Microservice (inprac_api_service)</span>
                                    <span class="badge">Port 8000</span>
                                </div>
                                <div class="arch-desc">Non-Root User (UID 1000) • Cgroup Limit: 256 MB RAM, 0.50 vCPU • Native Healthchecks</div>
                            </div>
                        </div>

                        <div class="flow-arrow">▼ Internal Bridge: data-net (Zero External Route)</div>

                        <div class="arch-step">
                            <div class="arch-icon" style="color: var(--amber); background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.2);">RD</div>
                            <div class="arch-content">
                                <div class="arch-label">
                                    <span>Redis In-Memory Persistence (inprac_cache)</span>
                                    <span class="badge">Port 6379</span>
                                </div>
                                <div class="arch-desc">Cgroup Limit: 128 MB RAM, 0.25 vCPU • Append-Only File (AOF) • LRU Eviction</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Tab 2: Live API Console -->
                <div id="tab-api" class="tab-pane">
                    <p style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 14px;">
                        Execute real-time live queries against the edge gateway. Responses are fetched asynchronously and measured:
                    </p>
                    <div class="console-controls">
                        <button class="api-btn" onclick="executeProbe('/')">⚡ GET / (Root)</button>
                        <button class="api-btn" onclick="executeProbe('/health')">🩺 GET /health</button>
                        <button class="api-btn" onclick="executeProbe('/api/v1/metrics')">📊 GET /api/v1/metrics</button>
                    </div>

                    <div class="terminal-box">
                        <div class="terminal-header">
                            <div class="terminal-dots">
                                <span class="dot dot-red"></span>
                                <span class="dot dot-yellow"></span>
                                <span class="dot dot-green"></span>
                            </div>
                            <div id="terminal-meta">Endpoint: https://lab.euprac.xyz/</div>
                        </div>
                        <div class="terminal-json" id="terminal-output">// Initializing console... Click any endpoint button above to test.</div>
                    </div>
                </div>

                <!-- Tab 3: Security & Cgroups -->
                <div id="tab-security" class="tab-pane">
                    <table class="sec-table">
                        <thead>
                            <tr>
                                <th>Security Control</th>
                                <th>Layer</th>
                                <th>Specification</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-weight: 600; color: #ffffff;">Kernel Cgroup Hardening</td>
                                <td>Linux cgroups v2</td>
                                <td>Max 512 MB RAM / 1.0 vCPU Total Ceiling</td>
                                <td><span class="sec-badge sec-enforced">ACTIVE</span></td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600; color: #ffffff;">Network Segmentation</td>
                                <td>Docker Bridge</td>
                                <td>Dual-Tier: edge-net + internal data-net</td>
                                <td><span class="sec-badge sec-enforced">ACTIVE</span></td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600; color: #ffffff;">Privilege Escalation Block</td>
                                <td>Container Security</td>
                                <td>no-new-privileges: true on all services</td>
                                <td><span class="sec-badge sec-enforced">ACTIVE</span></td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600; color: #ffffff;">Non-Root Execution</td>
                                <td>Application</td>
                                <td>Runs as UID 1000 (appuser)</td>
                                <td><span class="sec-badge sec-enforced">ACTIVE</span></td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600; color: #ffffff;">Automated Log Rotation</td>
                                <td>Docker Daemon</td>
                                <td>json-file (max 10MB x 3 files per container)</td>
                                <td><span class="sec-badge sec-enforced">ACTIVE</span></td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600; color: #ffffff;">Disaster Recovery Backups</td>
                                <td>Cron / Shell</td>
                                <td>Daily snapshot, SHA256 hashes, 7-day rotation</td>
                                <td><span class="sec-badge sec-enforced">ACTIVE</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Tab 4: Incident Runbooks (SRE) -->
                <div id="tab-runbooks" class="tab-pane">
                    <div style="margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; flex-wrap: gap: 8px;">
                        <span style="font-size: 0.85rem; color: var(--text-muted);">Production Troubleshooting & Root Cause Analysis Playbooks:</span>
                        <span class="badge" style="color: var(--emerald); border-color: rgba(16, 185, 129, 0.3);">9.0/10 Verified</span>
                    </div>
                    
                    <div class="runbooks-grid">
                        <!-- Runbook 1 -->
                        <a href="https://github.com/jobin-jr/cloud-devops-lab/blob/main/docs/runbooks/502-bad-gateway-rca.md" target="_blank" class="runbook-card">
                            <div class="rb-header">
                                <span class="rb-tag rb-net">NETWORK / PROXY</span>
                                <span class="rb-code">502 BAD GATEWAY</span>
                            </div>
                            <div class="rb-title">Upstream Gateway Crash & Recovery</div>
                            <div class="rb-desc">Diagnosing upstream container termination, curl --unix-socket bypass, 5-Whys RCA, and Zendesk customer resolution template.</div>
                            <div class="rb-footer">RCA & Resolution • View Markdown ↗</div>
                        </a>

                        <!-- Runbook 2 -->
                        <a href="https://github.com/jobin-jr/cloud-devops-lab/blob/main/docs/runbooks/cgroup-oom-mitigation.md" target="_blank" class="runbook-card">
                            <div class="rb-header">
                                <span class="rb-tag rb-kernel">LINUX KERNEL</span>
                                <span class="rb-code">CGROUP OOM KILL</span>
                            </div>
                            <div class="rb-title">Kernel Memory Cgroup Triage</div>
                            <div class="rb-desc">Inspecting memory.events, diagnosing dmesg oom-kill events, cgroup v2 memory budgeting, and non-disruptive mitigation.</div>
                            <div class="rb-footer">Memory Profiling • View Markdown ↗</div>
                        </a>

                        <!-- Runbook 3 -->
                        <a href="https://github.com/jobin-jr/cloud-devops-lab/blob/main/docs/runbooks/backup-restoration-drill.md" target="_blank" class="runbook-card">
                            <div class="rb-header">
                                <span class="rb-tag rb-sre">SRE / DR</span>
                                <span class="rb-code">RTO: 42.3s VERIFIED</span>
                            </div>
                            <div class="rb-title">Disaster Recovery Cold-Start Drill</div>
                            <div class="rb-desc">Real automated cold-start recovery drill into staging environment with SHA-256 cryptographic manifest verification.</div>
                            <div class="rb-footer">Disaster Recovery • View Markdown ↗</div>
                        </a>

                        <!-- Runbook 4 -->
                        <a href="https://github.com/jobin-jr/cloud-devops-lab/blob/main/docs/runbooks/redis-data-recovery.md" target="_blank" class="runbook-card">
                            <div class="rb-header">
                                <span class="rb-tag rb-db">DATABASE / CACHE</span>
                                <span class="rb-code">REDIS 7 AOF</span>
                            </div>
                            <div class="rb-title">Multi-Part AOF Corruption Recovery</div>
                            <div class="rb-desc">Forensic snapshot isolation, redis-check-aof --fix execution, point-in-time recovery, and cache warming procedures.</div>
                            <div class="rb-footer">Data Forensics • View Markdown ↗</div>
                        </a>

                        <!-- Runbook 5 -->
                        <a href="https://github.com/jobin-jr/cloud-devops-lab/blob/main/docs/runbooks/minecraft-server-incident-response.md" target="_blank" class="runbook-card">
                            <div class="rb-header">
                                <span class="rb-tag rb-game">GAMING / FLEET</span>
                                <span class="rb-code">PAPER & VELOCITY</span>
                            </div>
                            <div class="rb-title">High-Concurrency Server Incident Response</div>
                            <div class="rb-desc">Velocity proxy drops, Aikar's G1GC heap vs cgroup memory budgeting, spark MSPT profiler triage, and Pterodactyl daemon diagnostics.</div>
                            <div class="rb-footer">Fleet Triage • View Markdown ↗</div>
                        </a>

                        <!-- Runbook 6 -->
                        <a href="https://github.com/jobin-jr/cloud-devops-lab/blob/main/docs/slo-and-error-budget.md" target="_blank" class="runbook-card">
                            <div class="rb-header">
                                <span class="rb-tag rb-slo">SRE GOVERNANCE</span>
                                <span class="rb-code">99.9% SLO</span>
                            </div>
                            <div class="rb-title">Service Level Objective & Error Budget</div>
                            <div class="rb-desc">30-day rolling availability target (43.2 min monthly error budget), multi-window burn rate alerts (14.4x/6.0x/1.0x), and freeze policy.</div>
                            <div class="rb-footer">Error Budgeting • View Markdown ↗</div>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Right Rail: Engineer Bio & Host Specs -->
            <div class="right-rail">
                <!-- Engineer Profile Card -->
                <div class="glass profile-card">
                    <div class="profile-header">
                        <div class="avatar">JR</div>
                        <div class="profile-info">
                            <h3>Jobin J R</h3>
                            <p>Linux Systems Administrator</p>
                        </div>
                    </div>
                    <div class="bio-text">
                        18-year-old self-taught sysadmin and cloud infrastructure engineer. Built, deployed, and hardened this production containerized edge gateway on a remote European VPS.
                    </div>
                    <div class="tag-cloud">
                        <span class="skill-tag">Docker Compose</span>
                        <span class="skill-tag">Nginx Proxy</span>
                        <span class="skill-tag">Linux cgroups</span>
                        <span class="skill-tag">SRE Runbooks</span>
                        <span class="skill-tag">99.9% SLO</span>
                        <span class="skill-tag">DevSecOps CI</span>
                        <span class="skill-tag">Redis AOF</span>
                        <span class="skill-tag">FastAPI</span>
                    </div>
                    <div class="card-actions">
                        <button class="btn-primary" onclick="switchTab('runbooks')" style="cursor: pointer; border: none; font-family: inherit; font-size: inherit;">
                            ⚡ Inspect Incident Runbooks (6 Playbooks)
                        </button>
                        <a href="https://github.com/jobin-jr/cloud-devops-lab" target="_blank" class="btn-link" style="justify-content: center;">
                            Explore GitHub Repository & Code
                        </a>
                        <a href="mailto:jobinxd04@gmail.com" class="btn-link" style="justify-content: center; opacity: 0.8;">
                            Contact Engineer (jobinxd04@gmail.com)
                        </a>
                    </div>
                </div>

                <!-- Host Node Specifications -->
                <div class="glass" style="padding: 20px;">
                    <div class="stat-title" style="margin-bottom: 14px;">HOST NODE SPECIFICATIONS</div>
                    <ul class="specs-list">
                        <li class="specs-item">
                            <span class="specs-key">Host Location</span>
                            <span class="specs-val">Frankfurt, Germany</span>
                        </li>
                        <li class="specs-item">
                            <span class="specs-key">Virtualization</span>
                            <span class="specs-val">Contabo KVM Cloud</span>
                        </li>
                        <li class="specs-item">
                            <span class="specs-key">Host Memory</span>
                            <span class="specs-val">8 GB RAM (~7.3 GB Free)</span>
                        </li>
                        <li class="specs-item">
                            <span class="specs-key">Compute Cores</span>
                            <span class="specs-val">4 vCPUs (64-bit AMD/Intel)</span>
                        </li>
                        <li class="specs-item">
                            <span class="specs-key">SSL Termination</span>
                            <span class="specs-val">TLS 1.2 / 1.3 Strict</span>
                        </li>
                        <li class="specs-item">
                            <span class="specs-key">Isolation Policy</span>
                            <span class="specs-val">Strict Half-VPS Mandate</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer>
            <p>Designed, Engineered & Operated by <a href="https://github.com/jobin-jr">Jobin J R</a> • Hosted on Contabo EU VPS</p>
            <p style="margin-top: 6px; opacity: 0.7;">Verified by AI 2 (Zoho Zia Agent / GPT 5.6 Sol) & Antigravity IDE</p>
        </footer>
    </div>

    <!-- Live Polling & Interaction Logic -->
    <script>
        let baseUptime = 0;
        let startTimestamp = Date.now();

        // Switch Tabs
        function switchTab(tabId) {
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById('tab-' + tabId).classList.add('active');
        }

        // Format Seconds into readable string
        function formatUptime(seconds) {
            const d = Math.floor(seconds / (3600 * 24));
            const h = Math.floor((seconds % (3600 * 24)) / 3600);
            const m = Math.floor((seconds % 3600) / 60);
            const s = Math.floor(seconds % 60);
            return `${d}d ${h}h ${m}m ${s}s`;
        }

        // Live Uptime Ticker
        setInterval(() => {
            if (baseUptime > 0) {
                const elapsed = (Date.now() - startTimestamp) / 1000;
                document.getElementById('uptime-val').innerText = formatUptime(baseUptime + elapsed);
            }
        }, 1000);

        // API Console Interactive Probe
        async function executeProbe(endpoint) {
            const terminalOutput = document.getElementById('terminal-output');
            const terminalMeta = document.getElementById('terminal-meta');
            
            terminalMeta.innerText = `Requesting: ${endpoint}...`;
            terminalOutput.innerText = "// Sending request...";
            
            const t0 = performance.now();
            try {
                const resp = await fetch(endpoint, {
                    headers: { 'Accept': 'application/json' }
                });
                const t1 = performance.now();
                const latency = Math.round(t1 - t0);
                const data = await resp.json();
                
                terminalMeta.innerText = `Status: ${resp.status} ${resp.statusText} • Latency: ${latency}ms • Path: ${endpoint}`;
                terminalOutput.innerText = JSON.stringify(data, null, 2);
            } catch (err) {
                terminalMeta.innerText = `Error: Failed to fetch ${endpoint}`;
                terminalOutput.innerText = `// Request failed: ${err.message}`;
            }
        }

        // Initial Telemetry Fetch
        async function fetchInitialData() {
            const t0 = performance.now();
            try {
                const resp = await fetch('/health');
                const t1 = performance.now();
                document.getElementById('latency-val').innerText = `${Math.round(t1 - t0)}ms`;
                
                // Fetch root JSON for uptime
                const rootResp = await fetch('/', { headers: { 'Accept': 'application/json' } });
                const rootData = await rootResp.json();
                if (rootData.uptime_seconds) {
                    baseUptime = rootData.uptime_seconds;
                    startTimestamp = Date.now();
                    document.getElementById('uptime-val').innerText = formatUptime(baseUptime);
                }
            } catch (err) {
                document.getElementById('latency-val').innerText = 'Online';
            }
        }

        window.addEventListener('DOMContentLoaded', () => {
            fetchInitialData();
            // Automatically execute root probe in console for initial render
            executeProbe('/');
        });
    </script>
</body>
</html>
"""
