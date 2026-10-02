from pypdf import PdfReader
def extract(uploaded_file):
    reader= PdfReader(uploaded_file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
        print(text)
    return text 
