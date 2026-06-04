import ollama
from config import MODEL_NAME


def generate_startup_ideas(founder_profile):
    prompt = f"""
You are a world-class startup strategist.

Founder Profile:
{founder_profile}

Generate 10 startup ideas.

Requirements:
- Match the founder's skills
- Focus on large markets
- Focus on AI opportunities
- Focus on problems people will pay for

For each idea provide:

1. Startup Name
2. One-line description
3. Why it fits the founder

Keep concise.
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
