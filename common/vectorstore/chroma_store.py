import chromadb

client = chromadb.Client()

def get_collection(name: str):
    return client.get_or_create_collection(name=name)


def add_documents(collection_name, texts):
    collection = get_collection(collection_name)

    for i, text in enumerate(texts):
        collection.add(
            documents=[text],
            ids=[f"{collection_name}_{i}"]
        )


def search(collection_name, query, n=3):
    collection = get_collection(collection_name)

    results = collection.query(
        query_texts=[query],
        n_results=n
    )

    return results['documents'][0]