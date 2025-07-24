from sentence_transformers import SentenceTransformer

EMBED_MODEL = SentenceTransformer("intfloat/multilingual-e5-large")

def embed_chunks(chunks):
    return EMBED_MODEL.encode(chunks, convert_to_tensor=True)