import ollama
from config import MODEL_NAME

def generate_interview_questions(
    startup_idea: str,
    customer_discovery: str,
):
    prompt = f"""
You are an expert startup advisor.

Startup Idea:
{startup_idea}

Customer Discovery:
{customer_discovery}

Generate:

1. 10 customer interview questions
2. 5 willingness-to-pay questions
3. 5 problem validation questions

Return in markdown format.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
