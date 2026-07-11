from sentence_transformers import SentenceTransformer
from pdf_reader import extract
from chunking  import chunking
def get_embeddings():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunks = chunking(extract(r"c:\Users\User\Downloads\Thiranex_OfferLetter_Abirami_RS_THX-JUN1726-792.pdf"), 1000, 200)
    embeddings = model.encode(chunks)
    print("Total Chunks:", len(chunks))
    print("Embedding Shape:", embeddings.shape)
    return chunks, embeddings