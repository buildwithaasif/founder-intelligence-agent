from datetime import datetime
from pathlib import Path


def save_report(
    startup_idea,
    competitors,
    pain_points,
    founder_fit,
    opportunity_score,
):
    Path("reports").mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"reports/{timestamp}.md"

    report = f"""
# Startup Analysis

## Idea
{startup_idea}

---

## Competitors

{competitors}

---

## Pain Analysis

{pain_points}

---

## Founder Fit

{founder_fit}

---

## Opportunity Score

{opportunity_score}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    return filename
