import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Retrieval config
CHUNK_SIZE = 700
CHUNK_OVERLAP = 100
TOP_K = 5

# Vector DB
VECTOR_DB_DIR = "vectorstore"