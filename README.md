# SolCheck — AI-Powered Smart Contract Vulnerability Auditor

> An LLM-powered security analysis tool that audits Solidity smart contracts for vulnerabilities, gas inefficiencies, and security anti-patterns.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.1-lightgrey?style=flat-square)
![Claude API](https://img.shields.io/badge/Claude-Sonnet_4-orange?style=flat-square)
![Solidity](https://img.shields.io/badge/Solidity-0.6--0.8-purple?style=flat-square)

---

## Overview

SolCheck uses Claude (Anthropic's LLM) with a security-specialised system prompt to perform deep static analysis of Solidity smart contracts. It returns a structured JSON vulnerability report rendered in a clean web UI — covering 13+ vulnerability classes, gas optimisations, and an overall security score.

This project sits at the intersection of **AI**, **blockchain**, and **cybersecurity** — combining LLM reasoning with smart contract security domain knowledge.

---

## Features

- **13+ Vulnerability Classes Detected**
  - Reentrancy (SWC-107)
  - Integer Overflow/Underflow (SWC-101)
  - Access Control issues (SWC-105, SWC-106)
  - `tx.origin` authentication abuse (SWC-115)
  - Timestamp dependence (SWC-116)
  - Unchecked external calls (SWC-104)
  - Unprotected `selfdestruct`
  - Floating pragma (SWC-103)
  - Front-running vulnerabilities
  - And more...

- **Structured JSON Output** — each vulnerability includes ID, severity, affected lines, impact, code snippet, and fix recommendation

- **Audit Score (0–100)** — at-a-glance security health metric

- **Gas Optimisation Suggestions** — beyond security, flags inefficient patterns

- **Clean Web UI** — paste contract, get report instantly

---

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python 3.10+, Flask |
| AI Engine | Claude Sonnet (Anthropic API) |
| Frontend | Vanilla HTML/CSS/JS |
| Smart Contracts | Solidity 0.6–0.8 |

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ananyaaastha/SolCheck.git
cd SolCheck
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Anthropic API key

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### 4. Run the app

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Benchmark Results

Tested against known vulnerable contracts from [Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/) and [SWC Registry](https://swcregistry.io/):

| Contract | Known Vulnerabilities | Detected | Miss Rate |
|---|---|---|---|
| VulnerableBank | 4 | 4 | 0% |
| SimpleDAO (Reentrancy) | 1 | 1 | 0% |
| TimeLock (Overflow) | 1 | 1 | 0% |
| Phishing (tx.origin) | 1 | 1 | 0% |
| Crowdsale (Floating Pragma) | 1 | 1 | 0% |

---

## Sample Audit Output

```json
{
  "contract_name": "VulnerableBank",
  "overall_risk": "CRITICAL",
  "audit_score": 18,
  "summary": "VulnerableBank contains four critical vulnerabilities...",
  "vulnerabilities": [
    {
      "id": "V-001",
      "title": "Reentrancy in withdraw()",
      "severity": "CRITICAL",
      "category": "Reentrancy",
      "affected_lines": "Lines 18-22",
      "impact": "Attacker can drain contract ETH balance",
      "recommendation": "Apply Checks-Effects-Interactions pattern..."
    }
  ]
}
```

---

## Project Structure

```
SolCheck/
├── app.py              # Flask web server
├── auditor.py          # Claude API integration & audit logic
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt
└── README.md
```

---

## Why This Exists

Smart contract audits by professional firms cost $10,000–$50,000+. This tool makes basic security analysis accessible to developers during development — catching common vulnerabilities before deployment.

---

## Author

**Ananya Aastha** — [github.com/ananyaaastha](https://github.com/ananyaaastha)  
BIT (Computer Science), Queensland University of Technology
