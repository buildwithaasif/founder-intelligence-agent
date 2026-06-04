import ollama
from config import MODEL_NAME


def calculate_opportunity_score(
    startup_idea: str,
    competitors: str,
    pain_points: str,
    founder_profile: str,
):
    prompt = f"""
You are a YC partner and startup investor.

Startup Idea:
{startup_idea}

Founder Profile:
{founder_profile}

Competitors:
{competitors}

Pain Analysis:
{pain_points}

Score the startup from 0-100 on:

1. Market Opportunity
2. Founder Fit
3. Competition
4. Timing

Rules:
- Give each score from 0-100
- Explain each score briefly
- Calculate Overall Score

Finally return one verdict:

BUILD
MAYBE
AVOID

Format:

Market Opportunity: X/100
Reason: ...

Founder Fit: X/100
Reason: ...

Competition: X/100
Reason: ...

Timing: X/100
Reason: ...

Overall Score: X/100

Verdict: BUILD/MAYBE/AVOID
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

    return response["message"]["content"]
