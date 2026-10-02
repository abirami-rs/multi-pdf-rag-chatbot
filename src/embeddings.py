from sentence_transformers import SentenceTransformer
from src.pdf_reader import extract
from src.chunking  import chunking
def get_embeddings(file):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunks = chunking(extract(file), 1000, 200)
    embeddings = model.encode(chunks)
    print("Total Chunks:", len(chunks))
    print("Embedding Shape:", embeddings.shape)
    return chunks, embeddings