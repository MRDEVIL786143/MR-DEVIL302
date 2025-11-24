
                    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> DEVIL COOKIES ENGINE </title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Exo+2:wght@300;400;600;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --quantum-primary: #7e22ce;
            --quantum-accent: #06b6d4;
            --quantum-bg: #0f0f23;
            --quantum-surface: #1a1b4b;
            --quantum-text: #e0f2fe;
            --quantum-glow: #a855f7;
            --quantum-danger: #ef4444;
            --quantum-success: #10b981;
            --quantum-warning: #f59e0b;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Exo 2', sans-serif;
            background: 
                radial-gradient(circle at 10% 20%, rgba(126, 34, 206, 0.1) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 20%),
                linear-gradient(135deg, var(--quantum-bg) 0%, #1e1b4b 100%);
            color: var(--quantum-text);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        .quantum-container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        .quantum-header {
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
        }

        .quantum-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 4rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--quantum-primary), var(--quantum-accent));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 0 30px rgba(126, 34, 206, 0.5);
            margin-bottom: 1rem;
            position: relative;
            display: inline-block;
        }

        .quantum-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--quantum-accent), transparent);
        }

        .quantum-subtitle {
            font-size: 1.2rem;
            color: var(--quantum-accent);
            font-weight: 300;
            letter-spacing: 3px;
            text-transform: uppercase;
        }

        .hologram-panel {
            background: rgba(26, 27, 75, 0.7);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(126, 34, 206, 0.3);
            border-radius: 20px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 0 0 1px rgba(126, 34, 206, 0.1),
                0 10px 30px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }

        .hologram-panel::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(126, 34, 206, 0.1), transparent);
            transition: left 0.6s ease;
        }

        .hologram-panel:hover::before {
            left: 100%;
        }

        .panel-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--quantum-accent);
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .panel-title i {
            font-size: 1.5rem;
        }

        .quantum-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .quantum-input-group {
            margin-bottom: 1.5rem;
        }

        .input-label {
            display: block;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--quantum-accent);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .quantum-input {
            width: 100%;
            background: rgba(15, 15, 35, 0.8);
            border: 1px solid rgba(126, 34, 206, 0.3);
            border-radius: 12px;
            padding: 1rem 1.2rem;
            color: var(--quantum-text);
            font-family: 'Exo 2', sans-serif;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .quantum-input:focus {
            outline: none;
            border-color: var(--quantum-primary);
            box-shadow: 
                0 0 0 3px rgba(126, 34, 206, 0.2),
                inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .quantum-textarea {
            width: 100%;
            background: rgba(15, 15, 35, 0.8);
            border: 1px solid rgba(126, 34, 206, 0.3);
            border-radius: 12px;
            padding: 1rem 1.2rem;
            color: var(--quantum-text);
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
            resize: vertical;
            min-height: 120px;
        }

        .quantum-textarea:focus {
            outline: none;
            border-color: var(--quantum-primary);
            box-shadow: 
                0 0 0 3px rgba(126, 34, 206, 0.2),
                inset 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .quantum-btn {
            background: linear-gradient(135deg, var(--quantum-primary), var(--quantum-accent));
            color: white;
            border: none;
            border-radius: 12px;
            padding: 1.2rem 2rem;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 
                0 5px 15px rgba(126, 34, 206, 0.4),
                0 0 0 1px rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }

        .quantum-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s ease;
        }

        .quantum-btn:hover::before {
            left: 100%;
        }

        .quantum-btn:hover {
            transform: translateY(-3px);
            box-shadow: 
                0 8px 25px rgba(126, 34, 206, 0.6),
                0 0 0 1px rgba(255, 255, 255, 0.1);
        }

        .quantum-btn:active {
            transform: translateY(0);
        }

        .quantum-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .quantum-btn.secondary {
            background: linear-gradient(135deg, var(--quantum-surface), #2d3748);
        }

        .quantum-btn.danger {
            background: linear-gradient(135deg, var(--quantum-danger), #dc2626);
        }

        .session-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .session-card {
            background: rgba(15, 15, 35, 0.8);
            border: 1px solid rgba(126, 34, 206, 0.3);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .session-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(to bottom, var(--quantum-primary), var(--quantum-accent));
        }

        .session-card:hover {
            transform: translateY(-5px);
            border-color: var(--quantum-primary);
            box-shadow: 0 10px 25px rgba(126, 34, 206, 0.3);
        }

        .session-id {
            font-family: 'Courier New', monospace;
            background: rgba(0, 0, 0, 0.3);
            padding: 0.8rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            font-size: 0.9rem;
            word-break: break-all;
            border: 1px solid rgba(126, 34, 206, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .session-actions {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .session-actions .quantum-btn {
            padding: 0.7rem 1rem;
            font-size: 0.8rem;
        }

        .session-detail {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.8rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .detail-label {
            font-weight: 600;
            color: var(--quantum-accent);
        }

        .status-badge {
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
        }

        .status-running {
            background: rgba(16, 185, 129, 0.2);
            color: var(--quantum-success);
            border: 1px solid rgba(16, 185, 129, 0.3);
        }

        .status-stopped {
            background: rgba(239, 68, 68, 0.2);
            color: var(--quantum-danger);
            border: 1px solid rgba(239, 68, 68, 0.3);
        }

        .status-paused {
            background: rgba(245, 158, 11, 0.2);
            color: var(--quantum-warning);
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        .matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            opacity: 0.03;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            color: var(--quantum-accent);
            overflow: hidden;
        }

        .floating-elements {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .floating-element {
            position: absolute;
            width: 100px;
            height: 100px;
            background: radial-gradient(circle, rgba(126, 34, 206, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            filter: blur(20px);
            animation: float 15s infinite linear;
        }

        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(26, 27, 75, 0.9);
            border: 1px solid var(--quantum-primary);
            border-radius: 10px;
            padding: 1rem 1.5rem;
            color: var(--quantum-text);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            transform: translateX(400px);
            transition: transform 0.3s ease;
            z-index: 1000;
            max-width: 400px;
        }

        .notification.show {
            transform: translateX(0);
        }

        .notification.success {
            border-color: var(--quantum-success);
        }

        .notification.error {
            border-color: var(--quantum-danger);
        }

        .notification.warning {
            border-color: var(--quantum-warning);
        }

        .stats-panel {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .stat-card {
            background: rgba(15, 15, 35, 0.6);
            border: 1px solid rgba(126, 34, 206, 0.2);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--quantum-accent);
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 0.9rem;
            color: var(--quantum-text);
            opacity: 0.8;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255,255,255,.3);
            border-radius: 50%;
            border-top-color: var(--quantum-accent);
            animation: spin 1s ease-in-out infinite;
        }

        .error-message {
            color: var(--quantum-danger);
            font-size: 0.8rem;
            margin-top: 0.5rem;
            display: none;
        }

        .hidden {
            display: none !important;
        }

        @keyframes float {
            0% {
                transform: translate(0, 0) rotate(0deg);
            }
            33% {
                transform: translate(30px, 50px) rotate(120deg);
            }
            66% {
                transform: translate(-20px, 80px) rotate(240deg);
            }
            100% {
                transform: translate(0, 0) rotate(360deg);
            }
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }

        @media (max-width: 768px) {
            .quantum-title {
                font-size: 2.5rem;
            }
            
            .quantum-grid {
                grid-template-columns: 1fr;
            }
            
            .session-grid {
                grid-template-columns: 1fr;
            }
            
            .stats-panel {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="matrix-bg" id="matrixBg"></div>
    <div class="floating-elements">
        <div class="floating-element" style="top: 10%; left: 5%; animation-delay: 0s;"></div>
        <div class="floating-element" style="top: 60%; left: 80%; animation-delay: -5s;"></div>
        <div class="floating-element" style="top: 30%; left: 70%; animation-delay: -10s;"></div>
    </div>

    <div id="notification" class="notification"></div>

    <div class="quantum-container">
        <header class="quantum-header">
            <h1 class="quantum-title">
                <i class="fas fa-biohazard"></i>
                QUANTUM COOKIES ENGINE
                <i class="fas fa-atom"></i>
            </h1>
            <p class="quantum-subtitle">Advanced Session Management System</p>
        </header>

        <!-- Statistics Panel -->
        <div class="stats-panel">
            <div class="stat-card">
                <div class="stat-value" id="totalSessions">0</div>
                <div class="stat-label">Total Sessions</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="activeSessions">0</div>
                <div class="stat-label">Active Sessions</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="totalMessages">0</div>
                <div class="stat-label">Messages Sent</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="successRate">100%</div>
                <div class="stat-label">Success Rate</div>
            </div>
        </div>

        <!-- Start Server Panel -->
        <section class="hologram-panel">
            <h2 class="panel-title">
                <i class="fas fa-rocket"></i>
                INITIATE SESSION
            </h2>
            <form id="start-form" class="quantum-grid" enctype="multipart/form-data">
                <div class="quantum-input-group">
                    <label class="input-label">Authentication Key</label>
                    <input type="password" id="password" name="password" class="quantum-input" placeholder="Enter secure passkey" required>
                    <div class="error-message" id="password-error"></div>
                </div>
                <div class="quantum-input-group">
                    <label class="input-label">Target Thread ID</label>
                    <input type="text" id="targetID" name="targetID" class="quantum-input" placeholder="e.g., 9804642186231419" required>
                    <div class="error-message" id="targetID-error"></div>
                </div>
                <div class="quantum-input-group">
                    <label class="input-label">Opponent Identifier</label>
                    <input type="text" id="hatersname" name="hatersname" class="quantum-input" placeholder="Enter target name" required>
                    <div class="error-message" id="hatersname-error"></div>
                </div>
                <div class="quantum-input-group">
                    <label class="input-label">Time Interval (Seconds)</label>
                    <input type="number" id="timer" name="timer" class="quantum-input" placeholder="60" min="1" max="3600" required>
                    <div class="error-message" id="timer-error"></div>
                </div>
                <div class="quantum-input-group" style="grid-column: 1 / -1;">
                    <label class="input-label">Cookies Data</label>
                    <textarea id="cookies" name="cookies" class="quantum-textarea" placeholder="Paste your Facebook cookies here..." required></textarea>
                    <div class="error-message" id="cookies-error"></div>
                </div>
                <div class="quantum-input-group">
                    <label class="input-label">Message Payload File</label>
                    <input type="file" id="abusingfile" name="abusingfile" class="quantum-input" accept=".txt" required>
                    <div class="error-message" id="abusingfile-error"></div>
                </div>
                <div class="quantum-input-group" style="grid-column: 1 / -1;">
                    <button type="submit" class="quantum-btn" id="start-btn">
                        <i class="fas fa-play-circle"></i>
                        <span class="btn-text">ACTIVATE SESSION</span>
                        <span class="loading hidden"><div class="loading"></div> Starting...</span>
                    </button>
                </div>
            </form>
        </section>

        <!-- Stop Server Panel -->
        <section class="hologram-panel">
            <h2 class="panel-title">
                <i class="fas fa-stop-circle"></i>
                TERMINATE SESSION
            </h2>
            <form id="stop-form">
                <div class="quantum-input-group">
                    <label class="input-label">Session ID</label>
  