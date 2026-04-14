from common.llm.ollama_client import generate

def expand_query(query):
    prompt = f"""
    Generate 3 variations of this query:

    {query}

    Return as list.
    """

    response = generate(prompt)

    return [q.strip("- ") for q in response.split("\n") if q.strip()]