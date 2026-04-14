from common.loader.pdf_loader import load_pdf_chunks
from common.vectorstore.chroma_store import add_documents

docs = load_pdf_chunks("data/AWS Certified AI Practitioner Slides v1.pdf")

add_documents("multipdf", docs)

print("Multi-PDF data indexed")