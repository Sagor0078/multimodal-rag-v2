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

## Project Structure

├── app
│   ├── api/ # FastAPI routes
│   │   ├── init.py
│   │   └── routes.py
│   ├── core/ # Configuration and chat memory
│   │   ├── config.py # API keys, model settings
│   │   ├── memory.py # Memory integration (LangChain)
│   │   └── init.py
│   ├── rag/ # Core RAG pipeline
│   │   ├── chunker.py # Text chunking with sliding window
│   │   ├── embedding.py # Bengali embedding model setup
│   │   ├── evaluator.py # Optional: RAG evaluation metrics
│   │   ├── generator.py # Gemini answer generation logic
│   │   ├── prompts.py # Custom prompts for Gemini
│   │   ├── retriver.py # Combines retriever + generator
│   │   └── init.py
│   ├── retriver/ # Vector store logic (FAISS)
│   │   ├── vector_store.py # FAISS index build/load/search
│   │   └── init.py
│   ├── utils/ # Text & PDF extraction
│   │   ├── extractor.py # PDF -> text conversion
│   │   └── init.py
│   └── run_preprocess.py # One-time chunking + indexing script
├── chunks.pkl # Saved document chunks (pickle)
├── data/
│   └── HSC26-Bangla1st-Paper.pdf # Example source document
├── faiss_index.idx # FAISS index binary
├── main.py # App entrypoint (FastAPI)
├── pyproject.toml # Python package & dependency management
├── uv.lock # uv dependency lock file
└── README.md # This file

---

## uv installation guideline

- [docs](https://docs.astral.sh/uv
- Preprocess the PDF (chunks + FAISS index)
```bash
env PYTHONPATH=. uv run python3 app/run_preprocess.py
```
- Run the API Server
```bash
uv run uvicorn main:app --reload
```
---