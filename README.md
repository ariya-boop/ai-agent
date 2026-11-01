# Ariya AI Agent | LinkedIn & Career Intelligence

An autonomous, tool-calling AI agent designed to bridge software engineering portfolios, technical research, and professional networking on **LinkedIn**.

Directly connected to [Ryleen Ariyakutty's LinkedIn Profile](https://www.linkedin.com/in/ryleen-ariyakutty).

---

## 1. Overview & Architecture

The **Ariya Career Agent** implements an autonomous **ReAct (Reason + Act)** loop that interprets visitor and recruiter intents, consults an empirical knowledge base of project metrics, drafts platform-compliant LinkedIn outreach messages, and constructs direct deep-linking URLs to LinkedIn.

```
                      +-----------------------------+
                      |     Recruiter / Visitor     |
                      |   (CLI, REST API, or Web)   |
                      +-----------------------------+
                                     |
                                     v
                       +---------------------------+
                       |    Ariya Career Agent     |
                       |    (ReAct Decision Loop)   |
                       +---------------------------+
                                     |
         +---------------------------+---------------------------+
         |                           |                           |
         v                           v                           v
+------------------+       +-------------------+       +--------------------+
|  LinkedIn Link   |       |  Outreach Drafter |       |   Content Drafter  |
|      Tool        |       |    (<=300 chars)  |       |  (Share Intents)   |
+------------------+       +-------------------+       +--------------------+
         |                           |                           |
         v                           v                           v
Direct Profile URLs        Personalized Notes          One-Click Posts
(linkedin.com/in/...)      for Connections & InMail     with Web Intents
         |                           |                           |
         +---------------------------+---------------------------+
                                     |
                                     v
                       +---------------------------+
                       |    Safety & PII Audit     |
                       |   (Zero Leakage Policy)   |
                       +---------------------------+
                                     |
                                     v
                       +---------------------------+
                       |   LinkedIn Platform API   |
                       |  & Pre-Filled Web Intents |
                       +---------------------------+
```

---

## 2. Key Capabilities & Tools

### 🔗 1. Direct LinkedIn Deep Linking
- Formulates direct profile navigation links to `https://www.linkedin.com/in/ryleen-ariyakutty`.
- Builds one-click LinkedIn post-sharing intents (`https://www.linkedin.com/feed/?shareActive=true&text=...`).

### 🤝 2. LinkedIn Connection & InMail Generator
- **Connection Notes ($\le$ 300 characters)**: Tailored notes for recruiters, engineering managers, and researchers that strictly respect LinkedIn's 300-character limitation.
- **Extended InMail Messages**: 1,000-character structured pitches highlighting relevant technical overlap (DevSecOps, Adversarial ML, or Full-Stack).

### 📝 3. Technical Thought Leadership Drafter
- Generates high-engagement technical LinkedIn posts summarizing empirical results from Ryleen's projects:
  - *Adversarial ML Lab*: Exposing gradient masking under iterative PGD attacks.
  - *CipherVault*: Zero-knowledge AES-256-GCM encryption in the browser.
  - *Phishing Detector*: Sub-millisecond NLP classification and URL heuristics.
  - *CyberDefend*: Procedural Web Audio API synthesis and canvas physics.

### 🤖 4. Verified Portfolio Knowledge Retrieval
- Cites exact measured numbers from production benchmarks (e.g. 98.93% accuracy on 2,995 SpamAssassin emails, 0 SAST flaws via Bandit, non-root Docker UID 10001).

### 🛡️ 5. Automated Privacy & Safety Guardrail
- Automatically scans all outgoing agent output for private identifiers, ensuring compliance with strict privacy standards.

---

## 3. Quick Start & CLI Usage

### Prerequisites
- Python 3.10+
- Install dependencies:
```bash
pip install -r requirements.txt
```

### 1. Interactive Terminal Chat
Chat interactively with the agent:
```bash
python agent.py chat
```

### 2. Generate LinkedIn Connection Note
```bash
python agent.py outreach --name "Sarah" --company "Google" --role "Engineering Lead" --focus "ai_security"
```
Output:
```text
=== LinkedIn Connection Note (278/300 chars) ===
Hi Sarah, I'm Ryleen, an MS AI Eng student building robust ML systems. Admiring Google's engineering work. Recently published an adversarial ML benchmark exposing gradient masking in CNNs. Would love to connect and follow your work!

Direct LinkedIn Profile: https://www.linkedin.com/in/ryleen-ariyakutty
```

### 3. Draft a Technical LinkedIn Post
```bash
python agent.py post --topic "adversarial-ml"
```
Returns a fully formatted LinkedIn post ready for publishing, with a one-click share link.

### 4. Launch Local Web UI & REST Server
```bash
python agent.py serve --port 5050
```
Open [http://localhost:5050](http://localhost:5050) in your browser to interact with the responsive web interface.

---

## 4. REST API Endpoints

| Endpoint | Method | Payload | Description |
|---|---|---|---|
| `/api/chat` | `POST` | `{"message": "string"}` | Sends a natural language query to the agent ReAct loop. |
| `/api/outreach` | `POST` | `{"name": "...", "company": "...", "role": "..."}` | Generates tailored 300-char connection and InMail notes. |
| `/api/post` | `POST` | `{"topic": "adversarial-ml"}` | Drafts a technical post and returns a LinkedIn share URL. |
| `/api/health` | `GET` | *None* | Health check and LinkedIn profile target verification. |

---

## 5. Automated Testing

Run the full pytest suite:
```bash
pytest test_agent.py -v
```
All 9 test cases validate:
- Direct LinkedIn deep-link URI formatting
- Strict $\le$ 300 character boundary enforcement
- ReAct tool selection
- REST API response status and payloads
- Safety policy audit enforcement

---

## 6. Links & Verification

- **LinkedIn Profile**: [https://www.linkedin.com/in/ryleen-ariyakutty](https://www.linkedin.com/in/ryleen-ariyakutty)
- **Live Portfolio**: [https://ariya-boop.github.io](https://ariya-boop.github.io)
- **GitHub Repositories**: [https://github.com/ariya-boop](https://github.com/ariya-boop)
