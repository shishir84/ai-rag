from common.vectorstore.chroma_store import vector_search
from common.vectorstore.keyword_search import keyword_search
from common.llm.ollama_client import generate
from services.query_expansion import expand_query


def hybrid_rag_query(collection, query):
    vector_docs = vector_search(collection, query, n=5)
    keyword_docs = keyword_search(vector_docs, query, top_k=3)

    context = "\n".join(keyword_docs)

    prompt = f"""
    Answer using ONLY the context below.

    Context:
    {context}

    Question:
    {query}
    """

    return generate(prompt)


def advanced_rag_query(collection, query):
    queries = expand_query(query)

    all_docs = []

    for q in queries:
        docs = vector_search(collection, q, n=2)
        all_docs.extend(docs)

    unique_docs = list(set(all_docs))
    context = "\n".join(unique_docs)

    prompt = f"""
    Answer using ONLY this context:

    {context}

    Question:
    {query}
    """

    answer = generate(prompt)

    return answer, context   