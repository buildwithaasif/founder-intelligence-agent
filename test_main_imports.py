import sys
sys.path.insert(0, '.')

print("Testing main.py imports and adapter pattern...\n")

# Test 1: All imports work
print("=" * 50)
print("TEST 1: Import checks")
print("=" * 50)

try:
    from agents.analyzer import extract_competitors, get_competitors_flat
    print("✅ analyzer imports OK")
except Exception as e:
    print(f"❌ analyzer import failed: {e}")

try:
    from agents.pain_analyzer import extract_pain_points
    print("✅ pain_analyzer import OK")
except Exception as e:
    print(f"❌ pain_analyzer import failed: {e}")

try:
    from agents.founder_fit import analyze_founder_fit
    print("✅ founder_fit import OK")
except Exception as e:
    print(f"❌ founder_fit import failed: {e}")

try:
    from agents.opportunity_score import calculate_opportunity_score
    print("✅ opportunity_score import OK")
except Exception as e:
    print(f"❌ opportunity_score import failed: {e}")

try:
    from agents.startup_recommendation import recommend_startup
    print("✅ startup_recommendation import OK")
except Exception as e:
    print(f"❌ startup_recommendation import failed: {e}")

try:
    from agents.customer_discovery import customer_discovery
    print("✅ customer_discovery import OK")
except Exception as e:
    print(f"❌ customer_discovery import failed: {e}")

try:
    from agents.customer_interview_questions import generate_interview_questions
    print("✅ interview_questions import OK")
except Exception as e:
    print(f"❌ interview_questions import failed: {e}")

try:
    from agents.final_report import generate_final_report
    print("✅ final_report import OK")
except Exception as e:
    print(f"❌ final_report import failed: {e}")

try:
    from tools.competitors import find_competitors
    print("✅ find_competitors import OK")
except Exception as e:
    print(f"❌ find_competitors import failed: {e}")

try:
    from tools.report_writer import save_report
    print("✅ save_report import OK")
except Exception as e:
    print(f"❌ save_report import failed: {e}")

# Test 2: Adapter pattern
print("\n" + "=" * 50)
print("TEST 2: Adapter pattern (dict → flat list)")
print("=" * 50)

fake_competitors = {
    "direct": ["Rover", "Wag!"],
    "indirect": ["Excel spreadsheets"],
    "adjacent": [],
    "potential": []
}

flat = get_competitors_flat(fake_competitors)
print(f"Dict: {fake_competitors}")
print(f"Flat: {flat}")
print(f"Count: {len(flat)}")

assert len(flat) == 3, f"Expected 3, got {len(flat)}"
assert "Rover" in flat
assert "Excel spreadsheets" in flat
print("✅ Adapter works correctly")

# Test 3: save_report can handle dict competitors
print("\n" + "=" * 50)
print("TEST 3: save_report with dict competitors")
print("=" * 50)

import json
try:
    result = save_report(
        startup_idea="test idea",
        competitors=fake_competitors,
        pain_points={"pain_points": ["test"], "problems": [], "market_gaps": []},
        founder_fit={"summary": "test"},
        opportunity_score={"overall_score": 75}
    )
    print(f"✅ save_report worked: {result}")
except Exception as e:
    print(f"❌ save_report failed: {e}")

print("\n" + "=" * 50)
print("ALL TESTS COMPLETE")
print("=" * 50)
