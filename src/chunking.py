from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunking(text,chunk_size,overlap_size):
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=overlap_size
)
    chunks = splitter.split_text(text)
    print("Chunks:", len(chunks))
    return chunks
#chunking(extract(file_uploader(), 1000, 200))
