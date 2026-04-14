from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma(
    persist_directory="./chroma_db",
    collection_name="wiki",
    embedding_function=embedding
)

retriever = vectorstore.as_retriever()

llm = Ollama(model="llama3")

prompt = PromptTemplate.from_template("""
Answer using ONLY this context:

{context}

Question: {question}
""")


def format_docs(docs):
    return "\n".join([doc.page_content for doc in docs])


chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)


def wiki_query(query):
    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt_input = {
        "context": context,
        "question": query
    }

    answer = (prompt | llm | StrOutputParser()).invoke(prompt_input)

    return answer, docs