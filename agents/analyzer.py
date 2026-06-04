import ollama
from config import MODEL_NAME


def extract_competitors(search_results: list) -> str:
    context = ""

    for result in search_results:
        context += f"""
Title: {result['title']}
URL: {result['url']}
Snippet: {result['body']}
"""

    prompt = f"""
You are a startup research analyst.

Below are search results.

Your task:

1. Identify actual competitor companies.
2. Remove duplicates.
3. Ignore advertisements.
4. Ignore blog posts.
5. Return ONLY company names.

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

    return response["message"]["content"]
