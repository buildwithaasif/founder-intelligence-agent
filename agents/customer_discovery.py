import ollama
from config import MODEL_NAME


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

Identify:

1. Ideal Customer Profile (ICP)
2. Buyer Persona
3. Biggest Pain
4. Trigger Event that makes them buy
5. Where they hang out online
6. How to reach first 100 customers
7. Pricing expectations
8. Why they would choose this over competitors

Return concise markdown.

Format:

# ICP

# Buyer Persona

# Pain

# Trigger Event

# Acquisition Channels

# First 100 Customers

# Pricing

# Competitive Advantage
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
