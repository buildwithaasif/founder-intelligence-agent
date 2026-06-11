from agents.final_report import generate_final_report

# Updated fake data with yc_advice
recommendation = {
    "red_flags": [
        "Uber for X marketplace model",
        "Market graveyard (Wag bankruptcy, Rover dominance)",
        "Commodity competition on price",
    ],
    "red_flag_analysis": "This market is a known graveyard due to liquidity constraints.",
    "decision": "PIVOT",
    "best_startup_angle": "B2B SaaS for independent dog walkers",
    "why_this_wins": ["Avoids marketplace liquidity trap", "Leverages technical skills"],
    "first_mvp": "Simple scheduling app with route optimization",
    "ideal_customers": ["Independent dog walkers"],
    "pricing_strategy": "$29-$79/mo subscription",
    "biggest_risk": "Walkers may resist migrating workflows",
    "next_30_days": ["Interview 20+ dog walkers", "Build clickable prototype", "Secure 3 pilot customers"],
    "yc_advice": [
        "Your competitor count isn't the problem — it's proof this market has money in it.",
        "You're a technical founder building a sales-heavy business. Find a co-founder who sells.",
        "Do things that don't scale: manually onboard 10 walkers yourself first.",
        "Talk to users before writing another line of code.",
        "The fact that Wag failed is actually good news — they educated the market for you.",
        "Launch something embarrassingly simple this week. Ship speed matters more than features."
    ],
}

opportunity_score = {"overall_score": 55, "verdict": "MAYBE"}

customer_discovery_data = {
    "icp": "Independent dog walkers with 10-30 walks/week",
    "biggest_pain": "Scheduling chaos and no-shows",
}

founder_fit = {"summary": "Strong tech fit, lacks pet industry experience"}

interview_questions = """
## Customer Interview Questions
1. How do you currently manage your walking schedule?
2. What's the biggest pain point in your daily workflow?
"""

print("Testing final_report.py with YC Advice...\n")
print("=" * 50)

report = generate_final_report(
    recommendation=recommendation,
    opportunity_score=opportunity_score,
    customer_discovery_data=customer_discovery_data,
    founder_fit=founder_fit,
    interview_questions=interview_questions,
)

print(report)

# Validations
print("\nVALIDATION:")
checks = [
    ("RED FLAG SCAN section", "RED FLAG SCAN" in report),
    ("Red flag icons", "🚩" in report),
    ("WHAT YC WOULD TELL YOU section", "WHAT YC WOULD TELL YOU" in report),
    ("YC advice icons", "💬" in report),
    ("YC advice content displayed", "Talk to users" in report),
    ("YC advice content displayed", "Do things that don't scale" in report),
    ("No 'No specific advice' message", "No specific advice generated" not in report),
]

for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")