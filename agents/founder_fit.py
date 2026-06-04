import ollama
from config import MODEL_NAME
import json


def analyze_founder_fit(
    startup_idea: str,
    competitors: list,
    pain_points: list,
    founder_profile: str,
):
    prompt = f"""
You are a startup advisor.

Founder Profile:
{founder_profile}

Startup Idea:
{startup_idea}

Competitors:
{competitors}

Pain Points:
{pain_points}

Analyze the founder fit.

Return ONLY valid JSON (no explanation, no markdown).

Format exactly like this:

{{
  "technical_fit": 0-100,
  "domain_fit": 0-100,
  "execution_speed": 0-100,
  "market_understanding": 0-100,
  "key_strengths": ["..."],
  "key_weaknesses": ["..."],
  "summary": "short 2-3 line summary"
}}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "technical_fit": 0,
            "domain_fit": 0,
            "execution_speed": 0,
            "market_understanding": 0,
            "key_strengths": [],
            "key_weaknesses": [],
            "summary": "Failed to parse model output",
            "raw": content
        }