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

STEP 4: WHAT YC WOULD TELL YOU

Write 4-6 direct, honest pieces of advice in the style of Y Combinator partners (like Paul Graham or Sam Altman).
Write as if you're talking directly to the founder. Be blunt but helpful.

Rules:
- Each piece of advice should be 1-2 sentences
- Reference specific data from the analysis (competitor count, founder gaps, red flags)
- Include at least one piece of advice that is counterintuitive or surprising
- Include at least one reference to a YC principle ("make something people want", "do things that don't scale", "talk to users", "launch fast")
- If the idea has red flags, address them directly
- If the founder has skill gaps, call them out honestly
- End with one encouraging but realistic note

Example style:
"Your competitor count isn't the problem — it's proof this market has money in it. But you need to be 10x better, not 10% better. Right now your differentiation is weak."
"You're a technical founder building a sales-heavy business. This almost never works solo. Find a co-founder who sells before you write another line of code."

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
  "next_30_days": ["step1", "step2", "step3"],
  "yc_advice": ["advice point 1", "advice point 2", "advice point 3", "advice point 4", "advice point 5", "advice point 6"]
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
                    "yc_advice": ["Talk to at least 20 potential customers before building anything."],
                }
    return {}