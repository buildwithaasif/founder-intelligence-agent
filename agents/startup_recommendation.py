import ollama
from config import MODEL_NAME


def recommend_startup(
    startup_idea: str,
    founder_profile: str,
    competitors: str,
    pain_points: str,
    founder_fit: str,
    opportunity_score: str,
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

Decide whether the founder should:

1. Build this startup
2. Pivot the startup
3. Abandon the idea

If building:

- Recommend the exact startup angle
- Explain why it is the best opportunity
- Describe the first MVP
- Describe ideal customers
- Describe pricing strategy

Return:

# Recommendation

## Decision

## Best Startup Angle

## Why This Wins

## First MVP

## Ideal Customers

## Pricing

## Biggest Risk

## Next 30 Days
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

    return response["message"]["content"]
