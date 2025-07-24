# app/retriever/vector_store.py

import os
import faiss
import pickle
from typing import List
from langchain_core.documents import Document

from app.rag.embedding import embed_chunks

VECTOR_DIR = "vector_store"
INDEX_PATH = os.path.join(VECTOR_DIR, "faiss_index.bin")
DOCS_PATH = os.path.join(VECTOR_DIR, "docs.pkl")


def build_vector_store(chunks: List[Document]):
    texts = [doc.page_content for doc in chunks]
    embeddings = embed_chunks(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    os.makedirs(VECTOR_DIR, exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    with open(DOCS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    return index


def load_vector_store():
    if not os.path.exists(INDEX_PATH) or not os.path.exists(DOCS_PATH):
        raise FileNotFoundError("Vector store files not found. Please run build_vector_store first.")

    index = faiss.read_index(INDEX_PATH)

    with open(DOCS_PATH, "rb") as f:
        docs = pickle.load(f)

    return index, docs


def search(query: str, top_k: int = 5):
    index, docs = load_vector_store()
    query_embedding = embed_chunks([query])
    distances, indices = index.search(query_embedding, top_k)
    return [docs[i] for i in indices[0]]
