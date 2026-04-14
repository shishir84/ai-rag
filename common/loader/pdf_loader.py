from pypdf import PdfReader
from common.loader.text_chunker import chunk_text

def load_pdf_chunks(path):
    reader = PdfReader(path)

    all_chunks = []

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            chunks = chunk_text(text)
            for chunk in chunks:
                all_chunks.append({
                    "text": chunk,
                    "page": page_num
                })

    return all_chunks