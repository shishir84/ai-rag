from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

loader = PyPDFLoader("data/AWS Certified AI Practitioner Slides v1.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="./chroma_db",
    collection_name="wiki"
)

print("Wiki indexed with LangChain")