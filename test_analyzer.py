import sys
sys.path.insert(0, '.')

from agents.analyzer import extract_competitors, get_competitors_flat

# Fake search results
fake_results = [
    {
        "title": "Rover - Dog Walking & Pet Sitting",
        "url": "https://rover.com",
        "body": "Rover connects dog owners with trusted pet sitters and dog walkers."
    },
    {
        "title": "Wag! - Dog Walkers & Sitters",
        "url": "https://wagwalking.com",
        "body": "Wag! offers on-demand dog walking, sitting, and boarding services."
    },
    {
        "title": "Best Dog Walking Apps 2026",
        "url": "https://example-blog.com",
        "body": "We compare Rover, Wag, and Barkly Pets."
    },
    {
        "title": "How to start a dog walking business",
        "url": "https://example-guide.com",
        "body": "Many dog walkers use Excel spreadsheets to manage schedules."
    },
]

print("Testing analyzer.py...\n")

result = extract_competitors(fake_results)

# Test 1: Categorized output
print("=" * 50)
print("CATEGORIZED:")
print("=" * 50)
import json
print(json.dumps(result, indent=2))

# Test 2: Flat output
flat = get_competitors_flat(result)
print("\n" + "=" * 50)
print("FLATTENED:")
print("=" * 50)
print(flat)

# Test 3: Count
print("\n" + "=" * 50)
print("VALIDATION:")
print("=" * 50)
print(f"Total competitors: {len(flat)}")
print(f"Direct: {len(result['direct'])}")
print(f"Indirect: {len(result['indirect'])}")
print(f"Adjacent: {len(result['adjacent'])}")
print(f"Potential: {len(result['potential'])}")

# Quick checks
assert isinstance(result, dict), "Should return dict"
assert isinstance(flat, list), "Flat should be list"
assert "Rover" in flat, "Rover should be in flat list"
assert "Wag!" in flat, "Wag! should be in flat list"
print("\n✅ All assertions passed")
