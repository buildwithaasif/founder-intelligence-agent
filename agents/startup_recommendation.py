import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def recommend_startup(
    startup_idea: str,
    founder_profile: str,
    competitors: list[str],
    pain_points: dict,
    founder_fit: dict,
    opportunity_score: dict,
) -> dict:
    prompt = f"""
You are an elite startup advisor using Y Combinator's proven evaluation methodology.

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

---

STEP 1: RED FLAG SCAN

First, scan the idea against YC's known startup anti-patterns. Check if ANY of these apply:

- "Uber for X" — copying a marketplace model without understanding why the original succeeded
- Solution looking for a problem — starting with technology and hunting for a use case
- Requires behavior change without strong incentive — asking people to change habits with no clear reward
- Market graveyard — this market has many failed startups (indicates structural problem, not opportunity)
- No clear customer acquisition path — can't explain how to reach customers cost-effectively
- "Tarpit idea" — sounds profitable but has hidden structural problems (e.g., events, local services)
- Fake urgency — problem exists but nobody is actively trying to solve it or paying for solutions
- Commodity market — no way to differentiate; only competition is on price

---

STEP 2: DECISION

Based on the red flag scan and all data, decide: BUILD, PIVOT, or ABANDON.

If PIVOT, suggest a specific direction change.
If ABANDON, explain which red flags make this fatal.

---

STEP 3: STRATEGY

If BUILD, provide detailed strategy.
If PIVOT, provide new direction and first steps.

---

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "red_flags": ["flag 1 found", "flag 2 found"] or [] if none,
  "red_flag_analysis": "1-2 sentence assessment of the red flags found",
  "decision": "BUILD or PIVOT or ABANDON",
  "best_startup_angle": "clear idea direction or pivot suggestion",
  "why_this_wins": ["reason1", "reason2"],
  "first_mvp": "simple MVP description",
  "ideal_customers": ["customer type 1"],
  "pricing_strategy": "pricing explanation",
  "biggest_risk": "main risk identified",
  "next_30_days": ["step1", "step2", "step3"]
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
                    "red_flags": [],
                    "red_flag_analysis": "Unable to complete red flag scan",
                    "decision": "PIVOT",
                    "best_startup_angle": startup_idea,
                    "why_this_wins": ["Further analysis needed"],
                    "first_mvp": "Build a simple prototype",
                    "ideal_customers": ["Early adopters"],
                    "pricing_strategy": "Freemium",
                    "biggest_risk": "Unable to determine",
                    "next_30_days": ["Talk to 10 potential customers", "Build MVP"],
                }
    return {}