import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    # Simple chunking
    chunk_size = 1000
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]