from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_reader import extract
def chunking(text,chunk_size,overlap_size):
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=overlap_size
)
    chunks = splitter.split_text(text)
    print("Chunks:", len(chunks))
    return chunks
chunking(extract(r"c:\Users\User\Downloads\Thiranex_OfferLetter_Abirami_RS_THX-JUN1726-792.pdf"), 1000, 200)
