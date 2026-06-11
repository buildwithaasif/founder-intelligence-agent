import ollama
import json
from config import MODEL_NAME, MAX_RETRIES
from agents.analyzer import get_competitors_flat


def calculate_opportunity_score(
    startup_idea: str,
    competitors,  # Can be dict (categorized) or list (flat)
    pain_points: dict,
    founder_profile: str,
) -> dict:
    # Handle both categorized dict and flat list
    if isinstance(competitors, dict):
        competitors_flat = get_competitors_flat(competitors)
        direct_count = len(competitors.get("direct", []))
        indirect_count = len(competitors.get("indirect", []))
        adjacent_count = len(competitors.get("adjacent", []))
        potential_count = len(competitors.get("potential", []))
    else:
        competitors_flat = competitors
        direct_count = len(competitors_flat)
        indirect_count = 0
        adjacent_count = 0
        potential_count = 0

    competitor_count = len(competitors_flat)
    pain_count = len(pain_points.get("pain_points", []))

    # Rule-based baseline
    # Direct competitors hurt more than indirect
    market_pain_score = min(100, pain_count * 15)
    competition_score = max(0, 100 - (direct_count * 12) - (indirect_count * 4) - (adjacent_count * 2))

    # Use LLM for founder-fit and timing
    prompt = f"""
You are a startup analyst. Score the founder-fit and market timing for this startup idea.

Founder Profile:
{founder_profile}

Startup Idea:
{startup_idea}

Competitive Landscape:
- Direct Competitors: {direct_count}
- Indirect Competitors: {indirect_count}
- Adjacent Threats: {adjacent_count}
- Potential Entrants: {potential_count}
- Pain Points Found: {pain_count}

Return ONLY valid JSON:
{{
  "founder_fit": 0-100,
  "timing": 0-100,
  "reasoning": "1-2 sentence explanation"
}}
"""

    founder_fit = 50
    timing = 50
    reasoning = ""

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
            result = json.loads(content)
            founder_fit = int(result.get("founder_fit", 50))
            timing = int(result.get("timing", 50))
            reasoning = result.get("reasoning", "")
            break
        except Exception:
            continue

    overall_score = int((market_pain_score + competition_score + founder_fit + timing) / 4)

    if overall_score >= 75:
        verdict = "BUILD"
    elif overall_score >= 50:
        verdict = "MAYBE"
    else:
        verdict = "AVOID"

    return {
        "market_pain_score": market_pain_score,
        "competition_score": competition_score,
        "founder_fit": founder_fit,
        "timing": timing,
        "overall_score": overall_score,
        "verdict": verdict,
        "reasoning": reasoning,
    }