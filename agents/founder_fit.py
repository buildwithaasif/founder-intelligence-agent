import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def analyze_founder_fit(
    startup_idea: str,
    competitors,  # Can be dict or list
    pain_points: dict,
    founder_profile: str,
) -> dict:
    # Handle both categorized dict and flat list
    if isinstance(competitors, dict):
        comp_text = json.dumps(competitors, indent=2)
    else:
        comp_text = str(competitors)

    prompt = f"""
You are a startup advisor using Y Combinator's founder evaluation framework.

Founder Profile:
{founder_profile}

Startup Idea:
{startup_idea}

Competitive Landscape:
{comp_text}

Market Pain Points:
{pain_points}

---

STEP 1: FOUNDER FIT SCORING

Score the founder on these dimensions (0-100):

- technical_fit: Can they BUILD this? Do they have the technical skills?
- domain_fit: Do they understand this INDUSTRY and its customers?
- execution_speed: Can they move FAST and ship quickly?
- market_understanding: Do they deeply GET the problem and market dynamics?

---

STEP 2: STRENGTHS AND WEAKNESSES

Identify:
- key_strengths: What unique advantages does this founder bring?
- key_weaknesses: What critical skills or knowledge are they missing?

---

STEP 3: FOUNDER GAP ANALYSIS (YC Framework)

Based on YC's co-founder matching methodology, identify:

- missing_skills: What skills are COMPLETELY absent that this startup needs? (e.g., "sales", "marketing", "finance", "AI/ML", "industry connections")
- co-founder_recommendation: What TYPE of co-founder would best complement this founder? Be specific. Examples: "Technical co-founder with AI/ML expertise", "Business co-founder with B2B SaaS sales experience", "Domain expert with 10+ years in healthcare"
- solo_viability: Can this founder build this ALONE in the early stages? ("yes", "maybe", or "no")
- solo_viability_reason: One sentence explaining the solo viability assessment

---

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "technical_fit": 0-100,
  "domain_fit": 0-100,
  "execution_speed": 0-100,
  "market_understanding": 0-100,
  "key_strengths": ["strength 1", "strength 2"],
  "key_weaknesses": ["weakness 1", "weakness 2"],
  "missing_skills": ["skill 1", "skill 2"],
  "co_founder_recommendation": "specific co-founder type suggestion",
  "solo_viability": "yes/maybe/no",
  "solo_viability_reason": "one sentence explanation",
  "summary": "short 2-3 line overall assessment"
}}
"""

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response["message"]["content"].strip()
            if content.startswith("```"):
                content = content.split("\n", 1)[1]
                if content.endswith("```"):
                    content = content[:-3]
            return json.loads(content)
        except Exception:
            if attempt == MAX_RETRIES:
                return {
                    "technical_fit": 50,
                    "domain_fit": 50,
                    "execution_speed": 50,
                    "market_understanding": 50,
                    "key_strengths": ["Unable to parse"],
                    "key_weaknesses": ["Unable to parse"],
                    "missing_skills": [],
                    "co_founder_recommendation": "Unable to determine",
                    "solo_viability": "maybe",
                    "solo_viability_reason": "Analysis failed",
                    "summary": "Failed to analyze founder fit",
                }
    return {}