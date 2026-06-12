import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def map_evidence(
    assumptions: dict,
    competitors: dict,
    pain_points: dict,
    search_results: list = None,
) -> dict:
    """
    Maps research findings to each assumption and rates whether evidence
    supports, rejects, or is unclear for each assumption.
    
    Returns a dict with evidence-mapped assumptions and an overall summary.
    """
    # Format competitors
    if isinstance(competitors, dict):
        comp_text = json.dumps(competitors, indent=2)
    else:
        comp_text = str(competitors)

    # Format pain points
    pain_text = json.dumps(pain_points, indent=2)

    # Format search results (limit to avoid huge prompts)
    search_context = ""
    if search_results:
        for result in search_results[:10]:  # Limit to 10 results
            search_context += f"""
Title: {result.get('title', '')}
Snippet: {result.get('body', '')}
"""

    # Format assumptions
    assumptions_text = json.dumps(assumptions, indent=2)

    prompt = f"""
You are an evidence analyst. Your job is to match research findings against the founder's assumptions and determine what's actually true.

FOUNDER'S ASSUMPTIONS:
{assumptions_text}

RESEARCH FINDINGS:

COMPETITORS FOUND:
{comp_text}

PAIN POINTS & MARKET GAPS:
{pain_text}

WEB SEARCH RESULTS (sample):
{search_context if search_context else "No search results available"}

---

For EACH assumption, analyze the evidence and return:

- assumption: the original assumption statement
- verdict: one of:
  - "SUPPORTED" — evidence clearly confirms this
  - "REJECTED" — evidence clearly contradicts this
  - "PARTIALLY SUPPORTED" — some evidence supports, some doesn't
  - "UNCLEAR" — not enough evidence either way
- evidence_summary: 1-2 sentences explaining what evidence led to this verdict. Reference specific competitors, pain points, or search results.
- confidence_change: did the confidence go "UP", "DOWN", or "UNCHANGED" based on evidence?

Then provide an overall summary with:
- total_assumptions: total number analyzed
- supported_count: how many were SUPPORTED
- rejected_count: how many were REJECTED
- partial_count: how many were PARTIALLY SUPPORTED
- unclear_count: how many were UNCLEAR
- biggest_blind_spot: the most important assumption that was WRONG (REJECTED)
- most_validated: the assumption with the STRONGEST support
- revised_direction: 1-2 sentences on how the evidence changes the startup approach

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "assumptions": [
    {{
      "assumption": "original assumption text",
      "verdict": "SUPPORTED",
      "evidence_summary": "Evidence from X and Y supports this...",
      "confidence_change": "UP"
    }}
  ],
  "overall": {{
    "total_assumptions": 7,
    "supported_count": 3,
    "rejected_count": 1,
    "partial_count": 2,
    "unclear_count": 1,
    "biggest_blind_spot": "Founders will pay for this — rejected by evidence showing...",
    "most_validated": "The problem exists — supported by multiple Reddit threads...",
    "revised_direction": "The core problem is real but the monetization approach needs rethinking..."
  }}
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
                # Build a basic fallback
                fallback_assumptions = []
                for a in assumptions.get("assumptions", []):
                    fallback_assumptions.append({
                        "assumption": a.get("assumption", ""),
                        "verdict": "UNCLEAR",
                        "evidence_summary": "Unable to analyze evidence for this assumption.",
                        "confidence_change": "UNCHANGED"
                    })
                return {
                    "assumptions": fallback_assumptions,
                    "overall": {
                        "total_assumptions": len(fallback_assumptions),
                        "supported_count": 0,
                        "rejected_count": 0,
                        "partial_count": 0,
                        "unclear_count": len(fallback_assumptions),
                        "biggest_blind_spot": "Unable to determine — evidence mapping failed",
                        "most_validated": "Unable to determine — evidence mapping failed",
                        "revised_direction": "Run the analysis again with more search results."
                    }
                }
    return {"assumptions": [], "overall": {}}
