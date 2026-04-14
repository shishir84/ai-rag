from common.loader.pdf_loader import load_pdf
from common.vectorstore.chroma_store import add_documents

docs = load_pdf("data/AWS Certified AI Practitioner Slides v1.pdf")

add_documents("resume", docs)

print("Resume data indexed")