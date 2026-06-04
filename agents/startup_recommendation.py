import ollama
from config import MODEL_NAME
import json


def recommend_startup(
    startup_idea: str,
    founder_profile: str,
    competitors: list,
    pain_points: list,
    founder_fit: dict,
    opportunity_score: dict,
):
    prompt = f"""
You are an elite startup advisor.

Founder Profile:
{founder_profile}

Startup Idea:
{startup_idea}

Competitors:
{competitors}

Pain Analysis:
{pain_points}

Founder Fit:
{founder_fit}

Opportunity Score:
{opportunity_score}

Your task:

Decide one final outcome:
- BUILD
- PIVOT
- ABANDON

Return ONLY valid JSON (no markdown, no explanation).

Format exactly:

{{
  "decision": "BUILD/PIVOT/ABANDON",
  "best_startup_angle": "clear idea direction",
  "why_this_wins": ["reason1", "reason2"],
  "first_mvp": "simple MVP description",
  "ideal_customers": ["customer type 1", "customer type 2"],
  "pricing_strategy": "pricing explanation",
  "biggest_risk": "main risk",
  "next_30_days": ["step1", "step2", "step3"]
}}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "decision": "PIVOT",
            "best_startup_angle": "",
            "why_this_wins": [],
            "first_mvp": "",
            "ideal_customers": [],
            "pricing_strategy": "",
            "biggest_risk": "",
            "next_30_days": [],
            "raw": content,
        }
