import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from src.embeddings import get_file_embeddings
from src.embeddings import get_query_embeddings

def vector_store(files):
    all_chunks=[]
    all_embeddings=[]  
    for file in files:
        chunks, embeddings = get_file_embeddings(file)
        if chunks and len(embeddings)>0:
            all_chunks.extend(chunks)
            all_embeddings.extend(embeddings)
    if not all_embeddings:
        print("No embeddings extracted from the files.")
        return [], None
    embeddings = np.array(all_embeddings).astype("float32")
    if embeddings.ndim == 1:
        embeddings = np.expand_dims(embeddings, axis=0)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print("Vector Store Created Successfully!")
    print("Total Chunks:", len(all_chunks))
    print("Total Vectors Stored:", index.ntotal)
    return all_chunks,index
    #query = input("\nAsk a question: ")
def search_word(chunks,index,query):
    query_embedding = get_query_embeddings(query)
    query_embedding = np.array(query_embedding).astype("float32")
    if query_embedding.ndim == 1:
        query_embedding = np.expand_dims(query_embedding, axis=0)

# Search Top 5 similar chunks
    distances, indices = index.search(query_embedding, k=5)

    print("\nRetrieved Chunks:\n")
    
    retrieved_text=""
    for i in indices[0]:
        if 0 <= i < len(chunks):
            retrieved_text += chunks[i] + "\n\n"
    return retrieved_text
        
