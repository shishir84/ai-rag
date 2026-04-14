from common.loader.pdf_loader import load_pdf_chunks
from common.vectorstore.chroma_store import add_documents

chunks = load_pdf_chunks("data/AWS Certified AI Practitioner Slides v1.pdf")

add_documents("company", chunks)

print("Company data indexed with chunking")