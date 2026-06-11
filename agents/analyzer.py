import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def extract_competitors(search_results: list) -> dict:
    """
    Analyzes search results and returns categorized competitors.
    
    Returns:
        dict with keys: direct, indirect, adjacent, potential
    """
    if not search_results:
        return {
            "direct": [],
            "indirect": [],
            "adjacent": [],
            "potential": []
        }

    context = ""
    for result in search_results:
        context += f"""
Title: {result['title']}
URL: {result['url']}
Snippet: {result['body']}
"""

    prompt = f"""
You are a startup competitive intelligence analyst using Y Combinator's framework.

Below are search results about a startup idea.

Your task:
1. Identify competitor companies from the search results.
2. Categorize each one into exactly one of these groups:

- DIRECT COMPETITORS: Companies solving the SAME problem for the SAME customers with a SIMILAR approach
- INDIRECT COMPETITORS: Alternative solutions customers currently use to solve the same problem (could be manual processes, spreadsheets, or different product categories)
- ADJACENT THREATS: Companies that don't currently compete but COULD easily expand into this market with their existing capabilities
- POTENTIAL ENTRANTS: Well-funded startups or large companies that might enter this market soon

3. Remove duplicates, advertisements, and blog posts.
4. If you can't find any companies for a category, return an empty list.

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "direct": ["Company A", "Company B"],
  "indirect": ["Manual spreadsheets", "Company C"],
  "adjacent": ["BigCo Inc"],
  "potential": ["WellFunded Startup X"]
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
            
            # Handle markdown code blocks
            if content.startswith("```"):
                content = content.split("\n", 1)[1]
                if content.endswith("```"):
                    content = content[:-3]
            
            result = json.loads(content)
            
            # Validate structure
            return {
                "direct": result.get("direct", []),
                "indirect": result.get("indirect", []),
                "adjacent": result.get("adjacent", []),
                "potential": result.get("potential", []),
            }
            
        except Exception:
            if attempt == MAX_RETRIES:
                # Fallback: extract any company names as direct
                lines = [line.strip().lstrip("-•* ") for line in response["message"]["content"].split("\n") if line.strip()]
                return {
                    "direct": lines[:10],
                    "indirect": [],
                    "adjacent": [],
                    "potential": []
                }
    
    return {
        "direct": [],
        "indirect": [],
        "adjacent": [],
        "potential": []
    }


def get_competitors_flat(competitors_dict: dict) -> list[str]:
    """
    Flattens categorized competitors into a single list.
    Useful for functions that just need a count or simple list.
    """
    all_competitors = []
    for category in ["direct", "indirect", "adjacent", "potential"]:
        all_competitors.extend(competitors_dict.get(category, []))
    return all_competitors