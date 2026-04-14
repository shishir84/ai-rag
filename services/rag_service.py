from common.vectorstore.chroma_store import vector_search
from common.llm.ollama_client import generate


def hybrid_rag_query(collection_name, query):
    # Vector search
    vector_docs = vector_search(collection_name, query, n=3)

    # Combine context
    context = "\n".join(vector_docs)

    prompt = f"""
    Use ONLY the context below to answer.

    Context:
    {context}

    Question:
    {query}
    """

    return generate(prompt)