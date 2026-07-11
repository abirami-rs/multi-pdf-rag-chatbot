# 📄 PDF RAG Chatbot using Gemini and FAISS

A Retrieval-Augmented Generation (RAG) based Question Answering system built using Python. This project extracts text from a PDF document, generates semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant information for a user query, and uses Google's Gemini model to generate accurate answers.

---

## 🚀 Features

- Extract text from PDF documents
- Split text into meaningful chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in a FAISS vector database
- Retrieve relevant chunks based on user questions
- Generate answers using Google Gemini
- Simple command-line interface for asking questions

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF
- Python Dotenv

---

## 📂 Project Structure

```
multi-pdf-rag-chatbot/
│── app.py
│── requirements.txt
│── README.md
│── .env.example
│── .gitignore
│
└── src/
    ├── pdf_reader.py
    ├── chunking.py
    ├── embeddings.py
    ├── vector_store.py
    └── rag_pipeline.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abirami-rs/multi-pdf-rag-chatbot.git
```

### 2. Navigate to the project folder

```bash
cd multi-pdf-rag-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=your_api_key_here
```

### 7. Run the project

```bash
python src/rag_pipeline.py
```

---

## 💡 How It Works

1. Read the PDF document.
2. Extract text from the PDF.
3. Split the text into chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in a FAISS vector database.
6. Retrieve the most relevant chunks for a user query.
7. Generate the final answer using Google Gemini.

---

## 📸 Sample Output

```
Ask a question:
When is the internship completion date?

Retrieved Chunks:
Completion Date: 16 Jul 2026

Answer:
The internship completion date is 16 July 2026.
```

---

## 🔮 Future Enhancements

- Support multiple PDF documents
- Streamlit web interface
- PDF upload through the UI
- Chat history
- Conversation memory
- Support for additional document formats (DOCX, TXT)

---

## 👩‍💻 Author

**Abirami R.S**

B.Tech – Artificial Intelligence and Data Science

---

## ⭐ Acknowledgements

This project uses:

- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF
- Hugging Face Transformers


