import faiss
import numpy as np
import os
import pickle
from typing import List


class Retriever:
    def __init__(self, index_path: str = "faiss_index.idx", store_path: str = "chunks.pkl"):
        self.index_path = index_path
        self.store_path = store_path
        self.index = None
        self.chunks: List[str] = []

    def build(self, embeddings: np.ndarray, chunks: List[str]) -> None:
        """
        Build and save the FAISS index and corresponding chunks.
        """
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.chunks = chunks

        # Create directories if needed
        index_dir = os.path.dirname(self.index_path)
        store_dir = os.path.dirname(self.store_path)

        if index_dir:
            os.makedirs(index_dir, exist_ok=True)
        if store_dir:
            os.makedirs(store_dir, exist_ok=True)

        faiss.write_index(self.index, self.index_path)

        with open(self.store_path, "wb") as f:
            pickle.dump(self.chunks, f)

    def load(self) -> None:
        """
        Load FAISS index and stored chunks from disk.
        """
        if not os.path.exists(self.index_path) or not os.path.exists(self.store_path):
            raise FileNotFoundError("FAISS index or chunk store not found. Run preprocessing first.")

        self.index = faiss.read_index(self.index_path)
        with open(self.store_path, "rb") as f:
            self.chunks = pickle.load(f)

    def query(self, embedding: np.ndarray, k: int = 3) -> List[str]:
        """
        Query the FAISS index to retrieve top-k relevant chunks for the given embedding.
        """
        if self.index is None or not self.chunks:
            raise RuntimeError("Retriever not loaded. Call `load()` first.")

        if embedding.ndim == 1:
            embedding = embedding[np.newaxis, :]  # Reshape (dim,) -> (1, dim)

        D, I = self.index.search(embedding, k)
        return [self.chunks[i] for i in I[0] if i < len(self.chunks)]
