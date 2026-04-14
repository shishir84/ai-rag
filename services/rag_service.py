from common.vectorstore.chroma_store import search
from common.llm.ollama_client import generate

def rag_query(collection_name, query):
    docs = search(collection_name, query)

    context = "\n".join(docs)

    prompt = f"""
    Answer ONLY using this context:

    {context}

    Question:
    {query}
    """

    return generate(prompt)