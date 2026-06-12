import sys
sys.path.insert(0, '.')

from agents.assumptions import extract_assumptions

print("Testing assumptions.py...\n")

result = extract_assumptions(
    startup_idea="market research agent for founders",
    founder_profile="MERN Stack Developer, OSCP Certified, learning AI"
)

print("=" * 50)
print("EXTRACTED ASSUMPTIONS:")
print("=" * 50)

import json
print(json.dumps(result, indent=2))

# Validate
assumptions = result.get("assumptions", [])
print("\nVALIDATION:")

checks = [
    ("Has 5-7 assumptions", 5 <= len(assumptions) <= 7),
    ("Each has 'assumption' field", all("assumption" in a for a in assumptions)),
    ("Each has 'category' field", all("category" in a for a in assumptions)),
    ("Each has 'confidence' field", all("confidence" in a for a in assumptions)),
    ("Valid categories", all(a["category"] in ["problem", "solution", "market", "customer", "competition", "founder"] for a in assumptions)),
    ("Valid confidence levels", all(a["confidence"] in ["high", "medium", "low"] for a in assumptions)),
    ("Assumptions are statements", all(not a["assumption"].endswith("?") for a in assumptions)),
]

for name, passed in checks:
    print(f"{'✅' if passed else '❌'} {name}")

print(f"\nTotal assumptions extracted: {len(assumptions)}")
print("Categories covered:", set(a["category"] for a in assumptions))
