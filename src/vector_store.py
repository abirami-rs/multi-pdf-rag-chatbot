import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from embeddings import get_embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def vector_store():
    chunks, embeddings = get_embeddings()
    embeddings = np.array(embeddings).astype("float32")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print("Vector Store Created Successfully!")
    print("Total Chunks:", len(chunks))
    print("Total Vectors Stored:", index.ntotal)

    query = input("\nAsk a question: ")

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

# Search Top 3 similar chunks
    distances, indices = index.search(query_embedding, k=1)

    print("\nRetrieved Chunks:\n")
    
    retrieved_text=""
    for i in indices[0]:
        retrieved_text += chunks[i] + "\n\n"
    return query,retrieved_text
        
