import ollama
from config import MODEL_NAME


def analyze_founder_fit(
    startup_idea: str,
    competitors: str,
    pain_points: str,
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

Pain Analysis:
{pain_points}

Evaluate:

1. Is this market crowded?
2. Is there still opportunity?
3. What founder advantages does THIS founder have?
4. What skills is THIS founder missing?
5. What would make THIS founder stand out?

Return concise bullet points.
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
