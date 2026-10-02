import streamlit as st
#from src.pdf_reader import extract
#from src.embeddings import get_embeddings
from src.vector_store import vector_store
from src.rag_pipeline import rag_pipeline
def file_uploader():
    uploaded_files=st.file_uploader("Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True)
    return uploaded_files
files=file_uploader()
if files:
    st.write("UPLOADED FILES")
    for file in files:
        st.write(file.name)
    if "index" not in st.session_state:
        chunks,index=vector_store(files[0])
        st.session_state.index=index
        st.session_state.chunks=chunks
    else:
        chunks=st.session_state.chunks
        index=st.session_state.index
    query=st.text_input("ASK A QUESTION")
    if query:
        answer=rag_pipeline(
            chunks,index,query
        )
        st.write(answer)
