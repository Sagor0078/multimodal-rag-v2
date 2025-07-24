# Multilingual RAG System (English & Bengali)

A simple **Multilingual Retrieval-Augmented Generation (RAG)** system that supports English and Bengali queries using documents like *HSC26 Bangla 1st Paper*.

Built with:
- **FastAPI** (backend API)
- **Google Gemini (gemini-2.5-flash)** (generative model)
- **FAISS** (vector similarity search)
- **Bengali Sentence Transformers(intfloat/multilingual-e5-large)** (for embedding)
- **LangChain** (prompt orchestration)
- **Redis** (Context Learning : Recent inputs in the chat sequence)

---

## Features

- **Multilingual Query Support** (English + বাংলা)
- RAG pipeline using **Gemini Pro** for grounded answers
- Chunked document ingestion & vector storage with **FAISS**
- REST API for question-answering
- Evaluation utilities (optional: groundedness, relevance)
- Sliding window chunking for better context retention
- Short-term memory context to improve chat coherence

---

## 📁 Project Structure

```bash
├── app
│   ├── api/                  # FastAPI routes
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/                 # Config & memory (LangChain)
│   │   ├── config.py         # API keys, model configs
│   │   ├── memory.py         # Memory setup
│   │   └── __init__.py
│   ├── rag/                  # Core RAG logic
│   │   ├── chunker.py        # PDF/text chunking (sliding window)
│   │   ├── embedding.py      # Embedding setup (Bengali support)
│   │   ├── evaluator.py      # Optional: Evaluation metrics
│   │   ├── generator.py      # Gemini-based answer generation
│   │   ├── prompts.py        # Prompt templates
│   │   ├── retriver.py       # Combines retrieval & generation
│   │   └── __init__.py
│   ├── retriver/             # FAISS-based vector store
│   │   ├── vector_store.py   # Build / Load / Search
│   │   └── __init__.py
│   ├── utils/                # Data preprocessing
│   │   ├── extractor.py      # Extract text from PDF
│   │   └── __init__.py
│   └── run_preprocess.py     # Chunk + Embed + Index PDF
├── chunks.pkl                # Pickled text chunks
├── data/
│   └── HSC26-Bangla1st-Paper.pdf # Sample document
├── faiss_index.idx           # Saved FAISS index
├── main.py                   # FastAPI app entry point
├── pyproject.toml            # Python project metadata
├── uv.lock                   # `uv` dependency lock file
└── README.md                 # You’re here!
```
---

## uv installation guideline


- clone the repo 
```
git clone https://github.com/Sagor0078/multimodal-rag-v2.git
cd multimodal-rag-v2
```
- [uv docs](https://docs.astral.sh/uv)
- Preprocess the PDF (chunks + FAISS index)
```bash
env PYTHONPATH=. uv run python3 app/run_preprocess.py
```
- Run the API Server
```bash
uv run uvicorn main:app --reload
```
---