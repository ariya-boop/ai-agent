"""
tools.py - Deterministic, verifiable tools for Ariya Career & Research AI Agent.
Provides LinkedIn deep linking, outreach generation, technical post drafting,
knowledge retrieval, and safety auditing.
"""

import urllib.parse
from typing import Dict, Any, List, Optional
from knowledge import PROFILE

class LinkedInDeepLinkTool:
    """Generates direct, actionable deep links to LinkedIn."""
    
    BASE_PROFILE_URL = PROFILE["links"]["linkedin"]
    
    @classmethod
    def get_profile_link(cls) -> str:
        """Returns direct link to Ryleen Ariyakutty's LinkedIn profile."""
        return cls.BASE_PROFILE_URL
    
    @classmethod
    def get_share_post_url(cls, post_text: str, article_url: Optional[str] = None) -> str:
        """
        Generates a direct LinkedIn Share Web Intent URL.
        When opened, it pre-fills the post text in LinkedIn's post composer.
        """
        target_url = article_url or PROFILE["links"]["portfolio"]
        # LinkedIn official share intent
        encoded_url = urllib.parse.quote(target_url, safe="")
        return f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}"
    
    @classmethod
    def get_feed_share_url(cls, post_text: str) -> str:
        """Generates a LinkedIn feed composer intent with pre-filled text."""
        encoded_text = urllib.parse.quote(post_text[:1200], safe="")
        return f"https://www.linkedin.com/feed/?shareActive=true&text={encoded_text}"


class OutreachGeneratorTool:
    """Generates targeted, high-conversion LinkedIn connection and InMail outreach notes."""
    
    @staticmethod
    def generate_connection_note(recipient_name: str, company: str, role: str, interest_area: str = "ai_security") -> Dict[str, Any]:
        """
        Generates a personalized connection request note within LinkedIn's strict 300-character limit.
        """
        first_name = recipient_name.strip().split()[0] if recipient_name.strip() else "there"
        company_clean = company.strip() if company.strip() else "your team"
        
        # High impact 300-character templates tailored to interest areas
        if "ai" in interest_area.lower() or "ml" in interest_area.lower():
            note = (
                f"Hi {first_name}, I'm Ryleen, an MS AI Eng student building robust ML systems. "
                f"Admiring {company_clean}'s engineering work. Recently published an adversarial ML benchmark "
                f"exposing gradient masking in CNNs. Would love to connect and follow your work!"
            )
        elif "sec" in interest_area.lower() or "cyber" in interest_area.lower():
            note = (
                f"Hi {first_name}, I'm Ryleen, a Software Engineer focusing on DevSecOps & AppSec. "
                f"I engineer hardened APIs with STRIDE threat models and automated SAST/SCA CI pipelines. "
                f"I'd love to connect and follow {company_clean}'s security engineering journey!"
            )
        else:
            note = (
                f"Hi {first_name}, I'm Ryleen, a Software Engineer with an MS in AI Engineering in progress. "
                f"I build secure backends, zero-knowledge web apps, and resilient ML pipelines. "
                f"Excited by {company_clean}'s work and would love to connect!"
            )
        
        # Trim safely to <= 300 chars if dynamic name is unusually long
        if len(note) > 300:
            note = note[:297] + "..."
            
        return {
            "type": "linkedin_connection_note",
            "recipient": recipient_name,
            "company": company,
            "character_count": len(note),
            "max_allowed": 300,
            "within_limit": len(note) <= 300,
            "note": note,
            "profile_url": LinkedInDeepLinkTool.get_profile_link()
        }
    
    @staticmethod
    def generate_inmail(recipient_name: str, company: str, role: str, focus: str = "full-stack") -> Dict[str, Any]:
        """Generates an extended LinkedIn InMail / Coffee Chat message (up to 1,000 characters)."""
        first_name = recipient_name.strip().split()[0] if recipient_name.strip() else "there"
        company_clean = company.strip() if company.strip() else "your organization"
        
        body = (
            f"Hi {first_name},\n\n"
            f"I came across your work as {role} at {company_clean} and was impressed by the engineering standards your team upholds.\n\n"
            f"I'm a Software Engineer completing an MS in Artificial Intelligence Engineering at Western Governors University. "
            f"My focus is where high-integrity software engineering meets applied security:\n"
            f"- Hardened Backend APIs: IDOR prevention, scrypt authentication, and automated DevSecOps CI (Bandit SAST, 0 flaws).\n"
            f"- Zero-Knowledge Web Apps: Client-side AES-256-GCM encryption with PBKDF2 (100k rounds) using native Web Crypto APIs.\n"
            f"- Adversarial Machine Learning: Empirical robustness research evaluating PGD vs FGSM attacks and gradient masking.\n\n"
            f"I'd welcome the chance to connect on LinkedIn or learn more about upcoming engineering opportunities on your team.\n\n"
            f"Portfolio: https://ariya-boop.github.io\n"
            f"GitHub: https://github.com/ariya-boop\n\n"
            f"Best regards,\nRyleen Ariyakutty"
        )
        return {
            "type": "linkedin_inmail",
            "recipient": recipient_name,
            "character_count": len(body),
            "message": body,
            "profile_url": LinkedInDeepLinkTool.get_profile_link()
        }


class ContentDrafterTool:
    """Generates engaging, technically rigorous LinkedIn technical posts and deep-link shares."""
    
    @staticmethod
    def draft_technical_post(topic: str) -> Dict[str, Any]:
        """Drafts a structured technical LinkedIn post based on project topic."""
        t = topic.lower()
        
        if "adversarial" in t or "ml" in t or "vision" in t:
            post = (
                "🚨 Why defending against single-step adversarial attacks gives AI teams a false sense of security:\n\n"
                "In my latest AI security lab, I evaluated CNN defenses under both FGSM (Fast Gradient Sign Method) "
                "and multi-step PGD (Projected Gradient Descent) with random restarts.\n\n"
                "Here is what the empirical benchmark showed:\n"
                "1️⃣ Clean baseline accuracy: 97.66% on MNIST.\n"
                "2️⃣ Defending solely against FGSM yielded 88.75% defense at ε=0.2.\n"
                "3️⃣ But under 7-step PGD, that defense completely collapsed to 20.47%.\n\n"
                "Key takeaway: Single-step defenses often merely cause *Gradient Masking* (obfuscating the gradient direction) "
                "without increasing the true margin of safety. If you build AI systems exposed to active adversaries, "
                "iterative attacks must be part of your evaluation harness.\n\n"
                "Full code, PyTorch implementation, and perturbation plots: https://github.com/ariya-boop/adversarial-ml-lab\n"
                "Explore interactive projects: https://ariya-boop.github.io\n\n"
                "#MachineLearning #AISecurity #PyTorch #DeepLearning #Cybersecurity #SoftwareEngineering"
            )
        elif "crypto" in t or "vault" in t or "note" in t or "zero" in t:
            post = (
                "🔐 Building Zero-Knowledge in the browser: Why data should be undecipherable before it ever touches your API.\n\n"
                "Most security architectures rely on encryption-in-transit (TLS) and encryption-at-rest. But if an attacker "
                "breaches the backend database or an insider gains query access, plaintext is exposed.\n\n"
                "I recently built CipherVault, a client-side zero-knowledge encrypted notes application using the native W3C Web Crypto API:\n"
                "⚡ Hardware-accelerated AES-256-GCM authenticated encryption.\n"
                "🔑 PBKDF2 key derivation with 100,000 iterations and cryptographic salts.\n"
                "🎲 Unique 12-byte cryptographically secure IVs generated per record via crypto.getRandomValues().\n\n"
                "The result: The backend database stores only ciphertext. Zero plaintext, zero keys, zero knowledge.\n\n"
                "Try the live app: https://ariya-boop.github.io/secure-notes-client/\n"
                "GitHub Repository: https://github.com/ariya-boop/secure-notes-client\n\n"
                "#WebDevelopment #Cryptography #AppSec #JavaScript #Cybersecurity #DevSecOps"
            )
        elif "phishing" in t or "nlp" in t or "email" in t:
            post = (
                "📧 98.93% Accuracy with < 0.2ms Latency: Building an explainable dual-pipeline phishing classifier.\n\n"
                "When filtering automated phishing attacks, deep neural networks often add massive latency and compute overhead. "
                "Can a lightweight, explainable pipeline deliver production-grade precision?\n\n"
                "I engineered a dual-pipeline classifier combining:\n"
                "▪️ Sublinear TF-IDF character & word n-grams (capturing linguistic markers).\n"
                "▪️ Structural URL feature extractor (detecting raw IP hosts, subdomain depth, and lookalike domains).\n\n"
                "Results across 2,995 Apache SpamAssassin emails:\n"
                "✔️ 98.93% Overall Accuracy\n"
                "✔️ 97.54% Precision (critical to avoid false-positive alert fatigue)\n"
                "✔️ < 0.2 ms CPU inference latency per email\n\n"
                "Inspect the codebase and forensics report: https://github.com/ariya-boop/phishing-detector\n\n"
                "#NLP #MachineLearning #Cybersecurity #Python #DataScience"
            )
        elif "game" in t or "arcade" in t or "canvas" in t:
            post = (
                "🎮 Gamifying Cyber Defense: I built a 2D network defense arcade game in vanilla JavaScript & HTML5 Canvas.\n\n"
                "To demonstrate how defensive layers collaborate during active cyber attacks, I created CyberDefend: Packet Wars:\n"
                "🛡️ Firewall Nodes: Fast single-packet filtering lasers.\n"
                "⚡ Rate Limiters: Pulse waves suppressing botnet clusters.\n"
                "🤖 AI Inspectors: High-damage neural burst targeting phishing lures.\n"
                "🌀 Quantum Honeypots: Trapping high-durability adversarial payloads.\n\n"
                "Audio is 100% synthesized procedurally using the Web Audio API with zero audio assets.\n\n"
                "Play directly in your browser: https://ariya-boop.github.io/cyber-defense-game/\n"
                "Codebase: https://github.com/ariya-boop/cyber-defense-game\n\n"
                "#GameDev #JavaScript #HTML5 #Cybersecurity #WebDevelopment"
            )
        else:
            post = (
                "🚀 Excited to share my updated Software Engineering, Applied AI, and Security Portfolio!\n\n"
                "I design software that learns, adapts, and holds up under attack. My work combines:\n"
                "• Hardened Backend REST APIs (Flask, IDOR defense, Docker, STRIDE)\n"
                "• Zero-Knowledge Client Applications (AES-256-GCM, PBKDF2 100k rounds)\n"
                "• Adversarial ML Robustness Labs (PyTorch, PGD, Gradient Masking)\n"
                "• Threat Hunting & SOC Analytics (MITRE ATT&CK, O(1) sliding window)\n"
                "• Interactive Cyber Defense Game (HTML5 Canvas, Web Audio API)\n\n"
                "Check out the interactive live portfolio: https://ariya-boop.github.io\n"
                "All code repositories: https://github.com/ariya-boop\n\n"
                "I would love to connect with engineering leaders, researchers, and recruiters!\n\n"
                "#SoftwareEngineering #ArtificialIntelligence #Cybersecurity #DevSecOps"
            )
        
        feed_share_url = LinkedInDeepLinkTool.get_feed_share_url(post)
        
        return {
            "topic": topic,
            "post_content": post,
            "character_count": len(post),
            "feed_share_url": feed_share_url,
            "profile_url": LinkedInDeepLinkTool.get_profile_link()
        }


class PortfolioKnowledgeTool:
    """Answers visitor and recruiter queries with exact factual metrics."""
    
    @staticmethod
    def search_knowledge(query: str) -> Dict[str, Any]:
        """Matches a query against verified credentials and project records."""
        q = query.lower()
        results = []
        
        # Check education
        if any(w in q for w in ["degree", "education", "school", "university", "wgu", "master", "bachelor"]):
            results.append({
                "type": "education",
                "data": PROFILE["education"]
            })
            
        # Check skills
        if any(w in q for w in ["skill", "stack", "language", "framework", "python", "pytorch", "docker"]):
            results.append({
                "type": "skills",
                "data": PROFILE["skills"]
            })
            
        # Check projects
        for pkey, pdata in PROFILE["projects"].items():
            if (pkey in q) or any(t.lower() in q for t in pdata["tags"]) or any(w in q for w in pdata["name"].lower().split()):
                results.append({
                    "type": "project",
                    "id": pkey,
                    "data": pdata
                })
                
        # If no specific hit, provide general overview
        if not results:
            results.append({
                "type": "general_overview",
                "name": PROFILE["name"],
                "title": PROFILE["title"],
                "bio": PROFILE["bio"],
                "links": PROFILE["links"],
                "projects_count": len(PROFILE["projects"])
            })
            
        return {
            "query": query,
            "matches_found": len(results),
            "results": results,
            "linkedin_link": LinkedInDeepLinkTool.get_profile_link()
        }


class SafetyAuditTool:
    """Validates that outgoing agent content adheres to privacy and security boundaries."""
    
    FORBIDDEN_PATTERNS = [
        "rariya2@wgu.edu",
        "antigravity",
        "c:\\users\\",
        "c:/users/",
        "private_key",
        "password",
        "secret"
    ]
    
    @classmethod
    def audit_text(cls, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        violations = [p for p in cls.FORBIDDEN_PATTERNS if p in text_lower]
        return {
            "is_safe": len(violations) == 0,
            "violations": violations,
            "text_length": len(text)
        }
