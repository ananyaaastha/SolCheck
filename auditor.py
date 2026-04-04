import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """You are an expert smart contract security auditor with deep knowledge of Solidity and EVM vulnerabilities.

When given a Solidity smart contract, analyse it thoroughly and return ONLY a valid JSON object (no markdown, no explanation outside the JSON) with this exact structure:

{
  "contract_name": "string - name of the contract",
  "overall_risk": "CRITICAL | HIGH | MEDIUM | LOW | SAFE",
  "summary": "string - 2-3 sentence executive summary of the contract and its security posture",
  "vulnerabilities": [
    {
      "id": "V-001",
      "title": "string - short vulnerability name",
      "severity": "CRITICAL | HIGH | MEDIUM | LOW | INFO",
      "category": "string - e.g. Reentrancy, Access Control, Integer Overflow, etc.",
      "description": "string - clear explanation of the vulnerability",
      "affected_lines": "string - e.g. 'Lines 34-41' or 'Line 22'",
      "impact": "string - what an attacker could do",
      "recommendation": "string - how to fix it",
      "code_snippet": "string - the vulnerable code snippet (max 5 lines)"
    }
  ],
  "gas_optimisations": [
    {
      "title": "string",
      "description": "string",
      "affected_lines": "string"
    }
  ],
  "positive_findings": ["string - list of good security practices found"],
  "audit_score": integer between 0 and 100
}

Vulnerability categories to check:
- Reentrancy (SWC-107)
- Integer Overflow/Underflow (SWC-101)
- Access Control issues (SWC-105, SWC-106)
- Unchecked external calls (SWC-104)
- tx.origin usage (SWC-115)
- Timestamp dependence (SWC-116)
- Unprotected selfdestruct (SWC-106)
- Denial of Service vectors
- Front-running vulnerabilities
- Uninitialised storage pointers (SWC-109)
- Floating pragma (SWC-103)
- Hardcoded addresses
- Missing events for critical state changes
- Improper use of block.number / block.timestamp

Be thorough but accurate. Only report genuine vulnerabilities. If the contract is safe, say so with an empty vulnerabilities array.
Return ONLY the JSON. No preamble, no markdown fences."""


def audit_contract(solidity_code: str) -> dict:
    """Send a Solidity contract to Groq and return structured audit results."""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY', '')}"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Audit this Solidity smart contract:\n\n{solidity_code}"}
        ],
        "temperature": 0.1,
        "max_tokens": 4096
    }

    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    raw_text = data["choices"][0]["message"]["content"].strip()

    # Strip markdown fences if model adds them
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
        raw_text = raw_text.strip()

    return json.loads(raw_text)