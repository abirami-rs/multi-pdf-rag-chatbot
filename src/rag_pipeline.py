import os
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from vector_store import vector_store
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)


#load_dotenv(Path(__file__).parent.parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

llm = genai.GenerativeModel("gemini-2.5-flash")
#print(api_key)          

query,retrieved_text=vector_store()
prompt =f""" Use the following context to answer 

context={retrieved_text}

question={query}

Answer:
"""
response=llm.generate_content(prompt)
print(response.text)
