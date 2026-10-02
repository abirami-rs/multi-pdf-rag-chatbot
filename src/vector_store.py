import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from src.embeddings import get_embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def vector_store(file):
    chunks, embeddings = get_embeddings(file)
    embeddings = np.array(embeddings).astype("float32")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print("Vector Store Created Successfully!")
    print("Total Chunks:", len(chunks))
    print("Total Vectors Stored:", index.ntotal)
    return chunks,index
    #query = input("\nAsk a question: ")
def search_word(chunks,index,query):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

# Search Top 3 similar chunks
    distances, indices = index.search(query_embedding, k=5)

    print("\nRetrieved Chunks:\n")
    
    retrieved_text=""
    for i in indices[0]:
        retrieved_text += chunks[i] + "\n\n"
    return retrieved_text
        
