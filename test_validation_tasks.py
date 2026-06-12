import sys
sys.path.insert(0, '.')

from agents.validation_tasks import generate_validation_tasks

print("Testing validation_tasks.py...\n")

# Fake assumptions
assumptions = {
    "assumptions": [
        {
            "assumption": "Founders spend significant time on manual market research and would use an automated tool",
            "category": "problem",
            "confidence": "high"
        },
        {
            "assumption": "No existing tool effectively solves this problem for pre-seed founders",
            "category": "competition",
            "confidence": "medium"
        },
        {
            "assumption": "Founders will pay a monthly subscription for market research automation",
            "category": "customer",
            "confidence": "medium"
        },
        {
            "assumption": "An AI agent can generate trustworthy, source-cited market research",
            "category": "solution",
            "confidence": "medium"
        },
        {
            "assumption": "The founder's security background is a trust signal for customers",
            "category": "founder",
            "confidence": "low"
        }
    ]
}

# Fake competitors
competitors = {
    "direct": ["CB Insights", "Crunchbase", "Gartner"],
    "indirect": ["Manual Google searches", "Hiring analysts"],
    "adjacent": ["ChatGPT prompts"],
    "potential": []
}

# Fake pain points
pain_points = {
    "pain_points": ["Research takes 10+ hours/week", "Existing tools too expensive"],
    "problems": ["CB Insights costs $40K+/year"],
    "market_gaps": ["No affordable tool for pre-seed founders"]
}

result = generate_validation_tasks(
    assumptions=assumptions,
    startup_idea="market research agent for founders",
    competitors=competitors,
    pain_points=pain_points,
)

print("=" * 60)
print("VALIDATION TASKS:")
print("=" * 60)
import json
print(json.dumps(result, indent=2))

# Validate
print("\nVALIDATION:")
tasks = result.get("tasks", [])
summary = result.get("summary", {})

checks = [
    ("Has tasks list", len(tasks) > 0),
    ("Each task has assumption", all("assumption" in t for t in tasks)),
    ("Each task has task description", all("task" in t for t in tasks)),
    ("Each task has success_criteria", all("success_criteria" in t for t in tasks)),
    ("Each task has failure_criteria", all("failure_criteria" in t for t in tasks)),
    ("Each task has method", all("method" in t for t in tasks)),
    ("Valid methods", all(t.get("method") in ["customer_interview", "landing_page_test", "competitor_analysis", "survey", "prototype_test", "secondary_research"] for t in tasks)),
    ("Each task has priority", all("priority" in t for t in tasks)),
    ("Valid priorities", all(t.get("priority") in ["high", "medium", "low"] for t in tasks)),
    ("Each task has time_estimate", all("time_estimate" in t for t in tasks)),
    ("Has summary", "total_tasks" in summary),
    ("Has recommended_first_task", "recommended_first_task" in summary),
]

for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")

print(f"\n📋 Total tasks: {summary.get('total_tasks')}")
print(f"🔴 High priority: {summary.get('high_priority_count')}")
print(f"🟡 Medium priority: {summary.get('medium_priority_count')}")
print(f"🟢 Low priority: {summary.get('low_priority_count')}")
print(f"⏱️ Estimated time: {summary.get('estimated_total_time')}")
print(f"🎯 First task: {summary.get('recommended_first_task')}")
