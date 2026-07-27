import streamlit as st
def file_uploader():
    uploaded_files=st.file_uploader("Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True)
    return uploaded_files
