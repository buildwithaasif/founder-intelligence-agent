import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def extract_pain_points(search_results: list) -> dict:
    if not search_results:
        return {"pain_points": [], "problems": [], "market_gaps": []}

    context = ""
    for result in search_results:
        context += f"""
Title: {result['title']}
URL: {result['url']}
Snippet: {result['body']}
"""

    prompt = f"""
Analyze ONLY the provided search results.

Rules:
1. Use only information present in the search results.
2. Do not use your own knowledge.
3. Do not make assumptions.
4. If evidence is insufficient, return empty arrays.

Identify:
- Customer pain points (frustrations, complaints, unmet needs)
- Problems with existing solutions (what's broken about current options)
- Market gaps (opportunities where no good solution exists)

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "pain_points": ["pain point 1", "pain point 2"],
  "problems": ["problem 1", "problem 2"],
  "market_gaps": ["gap 1", "gap 2"]
}}

Search Results:
{context}
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
            return {
                "pain_points": result.get("pain_points", []),
                "problems": result.get("problems", []),
                "market_gaps": result.get("market_gaps", []),
            }
        except Exception:
            if attempt == MAX_RETRIES:
                return {"pain_points": [], "problems": [], "market_gaps": []}
    return {"pain_points": [], "problems": [], "market_gaps": []}
