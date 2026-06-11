import ollama
import json
from config import MODEL_NAME


def generate_interview_questions(
    startup_idea: str,
    customer_discovery_data: dict,
) -> str:
    cd_text = json.dumps(customer_discovery_data, indent=2)

    prompt = f"""
You are an elite startup advisor trained in Y Combinator's customer discovery methodology.

Startup Idea:
{startup_idea}

Customer Discovery Data:
{cd_text}

---

YC'S CORE PRINCIPLE:
"Interview at least 10-20 potential customers before building anything.
Focus on understanding the PROBLEM, not pitching your SOLUTION.
Ask about current behavior, not hypothetical future behavior.
The goal is to validate whether this problem is URGENT enough that people will PAY."

---

Generate a complete customer interview script with these sections:

SECTION 1: PROBLEM DISCOVERY (10 questions)
Goal: Understand if the problem is real, how they currently solve it, and how painful it is.
- Start broad, then narrow down
- Ask for specific stories and examples, not opinions
- Never mention your solution
- Example: "Tell me about the last time you [experienced this problem]. Walk me through what happened."

SECTION 2: WILLINGNESS TO PAY (5 questions)
Goal: Find out if they've paid for solutions before and if they'd pay for yours.
- Ask what they currently pay for (even imperfect solutions)
- Ask about budgets, not hypothetical willingness
- "How much does this problem cost you today?"
- "What have you tried before? What did you pay?"

SECTION 3: PROBLEM VALIDATION (5 questions)
Goal: Confirm this is a MUST-SOLVE, not a NICE-TO-HAVE.
- How urgent is this problem? (today vs someday)
- What happens if they don't solve it?
- Who else in their team/company cares about this?
- Have they tried to solve it before? What happened?

SECTION 4: YC-STYLE TIPS FOR THE INTERVIEWER
Include 5 practical tips for conducting these interviews:
- How to avoid leading questions
- How to know when you're getting honest answers vs polite ones
- What "signals of urgency" to listen for
- When to abandon an interview (the person isn't your customer)
- How to end the interview and ask for referrals

---

Return in clean markdown format with clear headings.
Use numbered questions. Make every question open-ended (not yes/no).
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]