import streamlit as st
#from src.pdf_reader import extract
#from src.embeddings import get_embeddings
from src.vector_store import vector_store
from src.rag_pipeline import rag_pipeline
st.set_page_config(page_title="Multi-PDF Chat", layout="wide")
st.title("Multi-PDF Chat Assistant")


def file_uploader():
    uploaded_files=st.file_uploader("Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True)
    return uploaded_files
files=file_uploader()
if "messages" not in st.session_state:
    st.session_state.messages=[]
if files:
    st.write("UPLOADED FILES")
    for file in files:
        st.write(file.name)
    file_names = [file.name for file in files]
    if "file_names" not in st.session_state or st.session_state.file_names != file_names:
        st.session_state.file_names = file_names
        if "index" in st.session_state:
            del st.session_state["index"]

    if "index" not in st.session_state:
        chunks,index=vector_store(files)
        st.session_state.index=index
        st.session_state.chunks=chunks
    else:
        chunks=st.session_state.chunks
        index=st.session_state.index
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query=st.chat_input("ASK A QUESTION")
    if query:
        st.session_state.messages.append({"role":"user","content":query})
        answer=rag_pipeline(
            chunks,index,query
        )
        st.session_state.messages.append({"role":"assistant","content":answer})
      
        st.rerun()
