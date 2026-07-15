import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

UPLOAD_FOLDER = "uploads"

FAISS_INDEX_PATH = "faiss_index/index.faiss"

CHUNKS_PATH = "faiss_index/chunks.pkl"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_MODEL = "llama-3.3-70b-versatile"