import sys
sys.path.insert(0, '.')

from agents.customer_interview_questions import generate_interview_questions

print("Testing customer_interview_questions.py with YC methodology...\n")

customer_data = {
    "icp": "Independent dog walkers with 10-30 walks/week",
    "buyer_persona": "30-year-old gig worker managing their own small business",
    "biggest_pain": "Scheduling chaos and client no-shows costing them money",
    "trigger_event": "Double-booked a client and lost $200 in one day",
    "where_they_hang_out": ["Facebook dog walker groups", "Nextdoor", "Rover forums"],
    "first_100_customers": ["Post in dog walker Facebook groups", "Offer free trial to first 20"],
    "pricing_expectation": "low",
    "competitive_advantage": "Route optimization + automated client updates"
}

result = generate_interview_questions(
    startup_idea="B2B SaaS scheduling tool for independent dog walkers",
    customer_discovery_data=customer_data,
)

print("=" * 60)
print("GENERATED INTERVIEW QUESTIONS:")
print("=" * 60)
print(result)

# Quick validations
print("\n" + "=" * 60)
print("VALIDATION:")
print("=" * 60)

checks = [
    ("Problem Discovery section", "PROBLEM DISCOVERY" in result.upper() or "Problem Discovery" in result),
    ("Willingness to Pay section", "WILLINGNESS TO PAY" in result.upper() or "Willingness to Pay" in result),
    ("Problem Validation section", "PROBLEM VALIDATION" in result.upper() or "Problem Validation" in result),
    ("Has numbered questions", any(f"{i}." in result for i in range(1, 6))),
    ("Mentions YC or Y Combinator", "YC" in result or "Y Combinator" in result),
    ("Contains tips for interviewer", "tip" in result.lower() or "TIP" in result),
    ("Not empty", len(result) > 200),
]

for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")

print("\n✅ Test complete")
