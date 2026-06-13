import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def recommend_startup(
    startup_idea: str,
    founder_profile: str,
    competitors,  # Can be dict or list
    pain_points: dict,
    founder_fit: dict,
    opportunity_score: dict,
) -> dict:
    # Handle both categorized dict and flat list
    if isinstance(competitors, dict):
        comp_text = json.dumps(competitors, indent=2)
    else:
        comp_text = str(competitors)

    score_value = opportunity_score.get("overall_score", 50)

    prompt = f"""
You are an elite startup advisor using Y Combinator's proven evaluation methodology.

Founder Profile:
{founder_profile}

Startup Idea:
{startup_idea}

Competitors:
{comp_text}

Pain Analysis:
{pain_points}

Founder Fit:
{founder_fit}

Opportunity Score: {score_value}/100

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

CRITICAL RULES:
- Score below 50 → decision MUST be ABANDON (unless there is a VERY specific pivot that completely changes the market/approach)
- Score 50-74 → decision can be BUILD or PIVOT
- Score 75+ → decision should be BUILD
- If you say PIVOT when the score is below 50, the pivot must be dramatic — not the same market, not the same approach. A real pivot.
- If you say ABANDON, explain which red flags make this idea unfixable.

---

STEP 3: STRATEGY

If BUILD, provide detailed strategy for this specific idea.
If PIVOT, provide 2 different pivot suggestions:
  - Pivot A: Stay in the same market but different approach
  - Pivot B: Use founder skills in a completely different market
If ABANDON, explain why this idea cannot be saved and what type of idea the founder should pursue instead.

---

STEP 4: WHAT YC WOULD TELL YOU

Write 4-6 direct, honest pieces of advice in the style of Y Combinator partners (like Paul Graham or Sam Altman).
Write as if you're talking directly to the founder. Be blunt but helpful.

Rules:
- Each piece of advice should be 1-2 sentences
- Reference specific data from the analysis
- Include at least one counterintuitive insight
- Include at least one YC principle
- End with one encouraging but realistic note

---

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "red_flags": ["flag 1", "flag 2"],
  "red_flag_analysis": "1-2 sentence assessment",
  "decision": "BUILD or PIVOT or ABANDON",
  "decision_reasoning": "Why this decision makes sense given the score and red flags",
  "best_startup_angle": "primary direction or pivot suggestion",
  "pivot_option_a": "Same market, different approach (only if PIVOT)",
  "pivot_option_b": "Different market using founder skills (only if PIVOT)",
  "why_this_wins": ["reason1", "reason2"],
  "first_mvp": "simple MVP description",
  "ideal_customers": ["customer type 1"],
  "pricing_strategy": "pricing explanation",
  "biggest_risk": "main risk identified",
  "next_30_days": ["step1", "step2", "step3"],
  "yc_advice": ["advice 1", "advice 2", "advice 3", "advice 4", "advice 5", "advice 6"]
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
                    "red_flag_analysis": "Unable to complete analysis",
                    "decision": "PIVOT",
                    "decision_reasoning": "Insufficient data for clear decision",
                    "best_startup_angle": startup_idea,
                    "pivot_option_a": "",
                    "pivot_option_b": "",
                    "why_this_wins": ["Further analysis needed"],
                    "first_mvp": "Build a simple prototype",
                    "ideal_customers": ["Early adopters"],
                    "pricing_strategy": "Freemium",
                    "biggest_risk": "Unable to determine",
                    "next_30_days": ["Talk to 10 potential customers", "Build MVP"],
                    "yc_advice": ["Talk to at least 20 potential customers before building anything."],
                }
    return {}