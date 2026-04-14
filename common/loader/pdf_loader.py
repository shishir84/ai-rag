from pypdf import PdfReader

def load_pdf(path):
    reader = PdfReader(path)
    return [page.extract_text() for page in reader.pages]