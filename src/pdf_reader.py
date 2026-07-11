from pypdf import PdfReader

def extract(pdf_path):
    reader= PdfReader(pdf_path)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
        print(text)
    return text 