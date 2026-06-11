import sys
sys.path.insert(0, '.')

from agents.opportunity_score import calculate_opportunity_score

print("Testing opportunity_score.py...\n")

# Test 1: With categorized dict (new format)
print("=" * 50)
print("TEST 1: Categorized dict input")
print("=" * 50)

competitors_dict = {
    "direct": ["Rover", "Wag!"],
    "indirect": ["Excel spreadsheets"],
    "adjacent": [],
    "potential": []
}

result = calculate_opportunity_score(
    startup_idea="dog walking app",
    competitors=competitors_dict,
    pain_points={"pain_points": ["expensive", "unreliable"], "problems": [], "market_gaps": []},
    founder_profile="MERN Stack Developer",
)

import json
print(json.dumps(result, indent=2))

# Validate
assert "overall_score" in result
assert "verdict" in result
assert "competition_score" in result
print(f"\n✅ Test 1 passed — verdict: {result['verdict']}")

# Test 2: With flat list (old format - backward compatibility)
print("\n" + "=" * 50)
print("TEST 2: Flat list input (backward compatibility)")
print("=" * 50)

competitors_list = ["Rover", "Wag!", "Barkly"]

result2 = calculate_opportunity_score(
    startup_idea="dog walking app",
    competitors=competitors_list,
    pain_points={"pain_points": ["expensive"], "problems": [], "market_gaps": []},
    founder_profile="MERN Stack Developer",
)

print(f"Verdict: {result2['verdict']}, Score: {result2['overall_score']}")
print("✅ Test 2 passed — backward compatibility works")

# Test 3: Scoring logic
print("\n" + "=" * 50)
print("TEST 3: Scoring logic check")
print("=" * 50)

# Many direct competitors = lower score
many_competitors = {"direct": ["A","B","C","D","E","F","G"], "indirect": [], "adjacent": [], "potential": []}
result_many = calculate_opportunity_score("idea", many_competitors, {"pain_points": ["one"], "problems": [], "market_gaps": []}, "founder")

# Few competitors = higher score  
few_competitors = {"direct": ["A"], "indirect": [], "adjacent": [], "potential": []}
result_few = calculate_opportunity_score("idea", few_competitors, {"pain_points": ["one"], "problems": [], "market_gaps": []}, "founder")

print(f"Many competitors (7): competition_score = {result_many['competition_score']}")
print(f"Few competitors (1): competition_score = {result_few['competition_score']}")
assert result_few["competition_score"] > result_many["competition_score"], "Fewer competitors should give higher score"
print("✅ Scoring logic correct — fewer competitors = higher score")

print("\n" + "=" * 50)
print("ALL TESTS PASSED")
print("=" * 50)
