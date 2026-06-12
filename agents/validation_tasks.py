import ollama
import json
from config import MODEL_NAME, MAX_RETRIES


def generate_validation_tasks(
    assumptions: dict,
    startup_idea: str,
    competitors: dict,
    pain_points: dict,
) -> dict:
    """
    Generates specific, actionable validation tasks for each assumption.
    Each task tells the founder exactly what to do, how to measure success,
    and how to know if the assumption is wrong.
    """
    # Format inputs
    assumptions_text = json.dumps(assumptions, indent=2)

    if isinstance(competitors, dict):
        comp_text = json.dumps(competitors, indent=2)
    else:
        comp_text = str(competitors)

    pain_text = json.dumps(pain_points, indent=2)

    prompt = f"""
You are a startup validation expert trained in Y Combinator's "do things that don't scale" methodology.

Startup Idea:
{startup_idea}

Founder's Assumptions:
{assumptions_text}

Competitive Landscape:
{comp_text}

Market Pain Points:
{pain_text}

---

Your job: For EACH assumption, create a specific, actionable validation task that the founder can actually DO.

Rules for each task:
1. Be extremely specific — not "talk to customers" but "post in r/SaaS asking founders how they currently do X, then DM 15 people who respond"
2. Include clear success criteria (what evidence would prove the assumption RIGHT)
3. Include clear failure criteria (what evidence would prove the assumption WRONG)
4. Assign a method: customer_interview, landing_page_test, competitor_analysis, survey, prototype_test, or secondary_research
5. Estimate time needed: hours, days, or weeks
6. Assign priority: high (core assumption that could kill the idea), medium (important but not fatal), or low (nice to validate)

Types of validation methods:
- customer_interview: Talk directly to potential customers
- landing_page_test: Create a simple landing page and measure signups
- competitor_analysis: Deep-dive into competitor offerings, pricing, reviews
- survey: Run a structured survey in target communities
- prototype_test: Build something minimal and get reactions
- secondary_research: Find existing data, reports, or studies

Return ONLY valid JSON. No markdown, no explanation.

Format:
{{
  "tasks": [
    {{
      "assumption": "The original assumption text",
      "task": "Specific action to take",
      "success_criteria": "What you'd see if the assumption is CORRECT",
      "failure_criteria": "What you'd see if the assumption is WRONG",
      "method": "customer_interview",
      "time_estimate": "1-2 weeks",
      "priority": "high"
    }}
  ],
  "summary": {{
    "total_tasks": 6,
    "high_priority_count": 2,
    "medium_priority_count": 3,
    "low_priority_count": 1,
    "estimated_total_time": "3-4 weeks",
    "recommended_first_task": "The ONE task the founder should do first and why"
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
                # Build basic fallback
                fallback_tasks = []
                for a in assumptions.get("assumptions", []):
                    fallback_tasks.append({
                        "assumption": a.get("assumption", ""),
                        "task": f"Interview 10 potential customers about: {a.get('assumption', '')}",
                        "success_criteria": "8+ customers confirm this is true",
                        "failure_criteria": "Fewer than 3 customers agree",
                        "method": "customer_interview",
                        "time_estimate": "1-2 weeks",
                        "priority": "high"
                    })
                return {
                    "tasks": fallback_tasks,
                    "summary": {
                        "total_tasks": len(fallback_tasks),
                        "high_priority_count": len(fallback_tasks),
                        "medium_priority_count": 0,
                        "low_priority_count": 0,
                        "estimated_total_time": f"{len(fallback_tasks)}-{len(fallback_tasks) * 2} weeks",
                        "recommended_first_task": "Start with the first assumption — it's usually the riskiest."
                    }
                }
    return {"tasks": [], "summary": {}}
