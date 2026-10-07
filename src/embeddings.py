from sentence_transformers import SentenceTransformer
from src.pdf_reader import extract
from src.chunking  import chunking
model = SentenceTransformer("all-MiniLM-L6-v2")
def get_file_embeddings(file):
    
    chunks = chunking(extract(file), 1000, 200)
    embeddings = model.encode(chunks)
    print("Total Chunks:", len(chunks))
    print("Embedding Shape:", embeddings.shape)
    return chunks, embeddings
def get_query_embeddings(query):
    query_embedding=model.encode([query])
    return query_embedding