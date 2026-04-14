from os import name

import chromadb
from common.embeddings.embedder import get_embeddings

#client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")

def get_collection(name):
    return client.get_or_create_collection(name=name)
    
def add_documents(collection_name, chunks):
    collection = get_collection(collection_name)

    texts = [c["text"] for c in chunks]
    embeddings = get_embeddings(texts)

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk["text"]],
            embeddings=[embeddings[i]],
            metadatas=[{"page": chunk["page"]}],
            ids=[f"{collection_name}_{i}"]
        )


def vector_search(collection_name, query, n=3):
    collection = get_collection(collection_name)

    results = collection.query(
        query_texts=[query],
        n_results=n
    )

    return results["documents"][0]