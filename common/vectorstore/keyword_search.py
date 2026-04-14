from collections import Counter

def simple_bm25_score(doc, query):
    doc_words = doc.lower().split()
    query_words = query.lower().split()

    score = 0
    doc_freq = Counter(doc_words)

    for word in query_words:
        score += doc_freq[word]

    return score


def keyword_search(docs, query, top_k=3):
    scored = [(doc, simple_bm25_score(doc, query)) for doc in docs]
    scored.sort(key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in scored[:top_k]]