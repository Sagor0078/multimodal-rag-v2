from sentence_transformers import SentenceTransformer
import pinecone
from langchain.vectorstores import Pinecone
from config import PINECONE_API_KEY, PINECONE_ENV, INDEX_NAME

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
if INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(INDEX_NAME, dimension=model.get_sentence_embedding_dimension(), metric="cosine")
vectordb = None

def get_vectorstore():
    global vectordb
    if vectordb is None:
        vectordb = Pinecone(pinecone.Index(INDEX_NAME), model.encode, "text")
    return vectordb
