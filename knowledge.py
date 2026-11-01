"""
knowledge.py - Verified knowledge base for Ariya Career & Research AI Agent.
Contains ground-truth facts, metrics, credentials, and deep-link definitions.
"""

from typing import Dict, Any, List

PROFILE: Dict[str, Any] = {
    "name": "Ryleen Ariyakutty",
    "handle": "ariya-boop",
    "title": "Software Engineer | Adversarial ML Researcher | Defensive Security Developer",
    "bio": (
        "Software Engineer with an MS in AI Engineering (in progress) and a BS in Software Engineering. "
        "Specializes in building secure, robust software: from client-side zero-knowledge encryption "
        "and hardened backend APIs to adversarial machine learning defense and automated SOC log analysis."
    ),
    "education": [
        {
            "degree": "MS, Artificial Intelligence Engineering",
            "institution": "Western Governors University",
            "period": "Expected 2027",
            "focus": "Adversarial Machine Learning, Robust Deep Learning, AI Security"
        },
        {
            "degree": "BS, Software Engineering",
            "institution": "Western Governors University",
            "period": "2026",
            "focus": "Full-Stack Engineering, Software Architecture, Distributed Systems"
        },
        {
            "degree": "Certificate in Cybersecurity Architecture & Operations",
            "institution": "Toronto Metropolitan University",
            "period": "2026",
            "focus": "Threat Modeling, Network Defense, Enterprise Security Architecture"
        }
    ],
    "links": {
        "linkedin": "https://www.linkedin.com/in/ryleen-ariyakutty",
        "github": "https://github.com/ariya-boop",
        "portfolio": "https://ariya-boop.github.io",
        "email": "ariyakuttyryleen@gmail.com"
    },
    "skills": {
        "languages": ["Python", "Java", "TypeScript", "JavaScript (ES6+)", "SQL", "Bash", "HTML5/CSS3"],
        "ai_ml": ["PyTorch", "scikit-learn", "torchvision", "NLP (TF-IDF)", "Adversarial ML (FGSM/PGD)", "Model Evaluation"],
        "backend": ["Flask", "REST APIs", "PostgreSQL", "SQLite", "Docker (non-root)", "Git", "pytest"],
        "security": ["STRIDE Threat Modeling", "IDOR Mitigation", "MITRE ATT&CK (T1110, T1078)", "Bandit SAST", "Pip-Audit SCA", "Audit Logging"],
        "app_and_game": ["Web Crypto API (AES-256-GCM, PBKDF2)", "HTML5 Canvas 2D Engine", "Web Audio API Procedural Synthesis"]
    },
    "projects": {
        "adversarial-ml-lab": {
            "name": "Adversarial Machine Learning Lab",
            "category": "AI Security & Computer Vision",
            "repo": "https://github.com/ariya-boop/adversarial-ml-lab",
            "summary": "Evaluated CNN fragility under bounded L-infinity perturbations, contrasting single-step FGSM vs 7-step PGD with random restarts.",
            "metrics": [
                "Clean baseline test accuracy: 97.66% on MNIST",
                "Exposed Gradient Masking: FGSM defense (88.75% at eps=0.2) collapsed to 20.47% under PGD",
                "Quantified robustness tax: 1.25% clean-accuracy trade-off",
                "Mapped to MITRE ATLAS AML.T0015 (Evasion)"
            ],
            "tags": ["PyTorch", "Adversarial ML", "PGD", "FGSM", "ATLAS"]
        },
        "secure-notes-api": {
            "name": "Secure Notes REST API & DevSecOps CI",
            "category": "Backend Engineering & DevSecOps",
            "repo": "https://github.com/ariya-boop/secure-notes-api",
            "summary": "Multi-tenant REST API engineered with query-level IDOR ownership enforcement across full CRUD, salted scrypt password hashing, and anti-repudiation audit logging.",
            "metrics": [
                "IDOR defense: SQL row-level scoping (WHERE id = ? AND user_id = ?)",
                "Anti-repudiation audit logs structured under secure_notes.audit",
                "Automated CI: 9 pytest cases, Bandit SAST (0 flaws), Pip-Audit SCA (0 CVEs)",
                "Non-root Docker container execution (appuser, UID 10001)"
            ],
            "tags": ["Flask", "SQLite", "pytest", "Docker", "DevSecOps", "STRIDE"]
        },
        "secure-notes-client": {
            "name": "CipherVault Zero-Knowledge Client",
            "category": "App Development & Cryptography",
            "repo": "https://github.com/ariya-boop/secure-notes-client",
            "demo": "https://ariya-boop.github.io/secure-notes-client/",
            "summary": "Zero-knowledge client-side encrypted notes application built with native W3C Web Crypto API so unencrypted data never touches the network.",
            "metrics": [
                "Hardware-accelerated AES-256-GCM authenticated encryption",
                "Client-side PBKDF2 key derivation with 100,000 rounds and random salt",
                "Unique 12-byte cryptographically secure IV per record",
                "Seamless integration with Secure Notes REST API backend"
            ],
            "tags": ["JavaScript", "Web Crypto API", "AES-256-GCM", "Zero-Knowledge"]
        },
        "auth-log-analyzer": {
            "name": "Linux Auth Log Threat Analyzer & SOC Response",
            "category": "Defensive Security & SOC Operations",
            "repo": "https://github.com/ariya-boop/auth-log-analyzer",
            "summary": "O(1) sliding-window forensic monitor detecting SSH brute-force clusters, distributed password sprays, and account takeovers.",
            "metrics": [
                "Account Takeover heuristic: Flags rapid failures followed by Accepted password",
                "MITRE ATT&CK: Mapped to T1110 (Password Guessing) and T1078 (Valid Accounts)",
                "Sensitivity Matrix: Grid-search tested across 24h simulated traffic (0 false positives)",
                "Authored formal SOC Incident Report INC-2026-1031"
            ],
            "tags": ["Python", "Threat Hunting", "MITRE ATT&CK", "SOC"]
        },
        "phishing-detector": {
            "name": "Phishing Email Detector",
            "category": "Applied NLP & Machine Learning",
            "repo": "https://github.com/ariya-boop/phishing-detector",
            "summary": "Explainable dual-pipeline text classifier combining sublinear TF-IDF n-grams with custom URL feature extractor (IP hosts, subdomain depth, lookalike keywords).",
            "metrics": [
                "98.93% accuracy, 97.54% precision, 96.75% F1 on 2,995 SpamAssassin emails",
                "Sub-millisecond inference latency (< 0.2 ms on CPU)",
                "Extracted top 20 discriminative phishing vs ham tokens for model explainability",
                "Conducted forensic failure mode root-cause analysis on 3 edge cases"
            ],
            "tags": ["Python", "scikit-learn", "NLP", "Feature Engineering"]
        },
        "cyber-defense-game": {
            "name": "CyberDefend: Packet Wars",
            "category": "Game Development & Cyber Simulation",
            "repo": "https://github.com/ariya-boop/cyber-defense-game",
            "demo": "https://ariya-boop.github.io/cyber-defense-game/",
            "summary": "Interactive 2D network packet defense simulation game built in HTML5 Canvas with procedural Web Audio API sound synthesis.",
            "metrics": [
                "Custom physics loop with requestAnimationFrame and delta-time state machine",
                "Simulates 4 threat classes: Port Scanners, Brute-Force Botnets, Phishing Lures, and Adversarial Exploits",
                "100% procedurally synthesized audio with zero audio file dependencies",
                "Smooth 60 FPS in modern browsers"
            ],
            "tags": ["HTML5 Canvas", "JavaScript", "Web Audio API", "Game Dev"]
        }
    }
}
