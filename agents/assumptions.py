import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def extract_assumptions(
    startup_idea: str,
    founder_profile: str,
) -> dict:
    """
    Extracts the hidden assumptions behind a startup idea.
    
    Returns a dict with a list of assumptions, each with:
    - assumption: the statement
    - category: problem, solution, market, customer, competition, or founder
    - confidence: high, medium, or low (how sure the founder probably is about this)
    """
    prompt = f"""
You are a startup analyst trained to identify hidden assumptions in startup ideas.

Founder Profile:
{founder_profile}

Startup Idea:
{startup_idea}

---

Every founder makes assumptions when they have an idea — beliefs they haven't validated yet.
Your job is to extract those assumptions so they can be tested.

Identify 5-7 key assumptions the founder is making. Cover these categories:

1. PROBLEM assumptions — beliefs about the pain point (it exists, it's urgent, people care)
2. SOLUTION assumptions — beliefs about the fix (it will work, it's better than alternatives)
3. MARKET assumptions — beliefs about the opportunity (market size, growth, timing)
4. CUSTOMER assumptions — beliefs about who will buy (who they are, willingness to pay)
5. COMPETITION assumptions — beliefs about alternatives (none exist, ours is better)
6. FOUNDER assumptions — beliefs about themselves (I can build this, I understand this market)

For each assumption:
- Write it as a clear, testable statement (not a question)
- Assign a category
- Assign a confidence level (how certain the founder probably feels about this):
  - HIGH = "obviously true, I'd bet on it"
  - MEDIUM = "I think so but not certain"
  - LOW = "I hope this is true but could be wrong"

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "assumptions": [
    {{
      "assumption": "Founders spend significant time on manual market research and would use an automated tool",
      "category": "problem",
      "confidence": "high"
    }},
    {{
      "assumption": "No existing tool effectively solves this problem",
      "category": "competition",
      "confidence": "medium"
    }}
  ]
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
            result = json.loads(content)
            return result
        except Exception:
            if attempt == MAX_RETRIES:
                return {
                    "assumptions": [
                        {
                            "assumption": "The problem exists and people want a solution",
                            "category": "problem",
                            "confidence": "medium"
                        },
                        {
                            "assumption": "People will pay for this solution",
                            "category": "customer",
                            "confidence": "medium"
                        },
                        {
                            "assumption": "No strong competitors exist in this space",
                            "category": "competition",
                            "confidence": "low"
                        }
                    ]
                }
    return {"assumptions": []}
