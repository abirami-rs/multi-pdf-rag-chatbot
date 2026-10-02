import os
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from src.vector_store import vector_store
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / ".env"
from src.vector_store import search_word
load_dotenv(env_path) 
#load_dotenv(Path(__file__).parent.parent / ".env")
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

llm = genai.GenerativeModel("gemini-2.5-flash")
#print(api_key)          
def rag_pipeline(chunks,index,query):
    retrieved_text = search_word(chunks,index,query)
    prompt =f""" Use the following context to answer 
    context={retrieved_text}
    question={query}
    Answer:"""
    response=llm.generate_content(prompt)
    return response.text
