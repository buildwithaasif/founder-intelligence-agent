import ollama
from config import MODEL_NAME
import json


def customer_discovery(
    startup_idea: str,
    recommendation: str,
):
    prompt = f"""
You are an expert startup GTM strategist.

Startup Idea:
{startup_idea}

Recommendation:
{recommendation}

Extract customer intelligence.

Return ONLY valid JSON. No markdown, no explanation.

Format exactly:

{{
  "icp": "Ideal Customer Profile in 1-2 lines",
  "buyer_persona": "short description",
  "biggest_pain": "main pain point",
  "trigger_event": "what makes them buy",
  "where_they_hang_out": ["platforms/communities"],
  "first_100_customers": ["steps to acquire"],
  "pricing_expectation": "low/medium/high or range",
  "competitive_advantage": "why users choose this"
}}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "icp": "",
            "buyer_persona": "",
            "biggest_pain": "",
            "trigger_event": "",
            "where_they_hang_out": [],
            "first_100_customers": [],
            "pricing_expectation": "unknown",
            "competitive_advantage": "",
            "raw": content
        }