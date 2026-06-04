import ollama
from config import MODEL_NAME

def extract_pain_points(search_results: list) -> str:
    context = ""

    for result in search_results:
        context += f"""
Title: {result['title']}
URL: {result['url']}
Snippet: {result['body']}
"""

    prompt = f"""
Analyze ONLY the provided search results.

Rules:
1. Use only information present in the search results.
2. Do not use your own knowledge.
3. Do not make assumptions.
4. If evidence is insufficient, say "Insufficient evidence".

Identify:

1. Customer pain points
2. Problems with existing solutions
3. Market gaps

For every point, include the source title that supports it.

Format:

PAIN POINT:
- description
- source title

PROBLEM:
- description
- source title

MARKET GAP:
- description
- source title

Search Results:

{context}
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

    return [
    line.strip()
    for line in response["message"]["content"].split("\n")
    if line.strip()
]
