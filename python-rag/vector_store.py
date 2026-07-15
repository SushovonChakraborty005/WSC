import faiss
import pickle
import numpy as np
import os

from config import FAISS_INDEX_PATH, CHUNKS_PATH
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL


model = SentenceTransformer(EMBEDDING_MODEL)


# ===========================
# Save FAISS Index
# ===========================
def save_index(embeddings, chunks):

    os.makedirs("faiss_index", exist_ok=True)

    embeddings = np.array(embeddings).astype("float32")


    # Existing index থাকলে নতুন PDF add করবে
    if os.path.exists(FAISS_INDEX_PATH) and os.path.exists(CHUNKS_PATH):

        print("Existing FAISS index found. Adding new PDF...")


        index = faiss.read_index(
            FAISS_INDEX_PATH
        )


        with open(CHUNKS_PATH, "rb") as f:
            old_chunks = pickle.load(f)


        index.add(embeddings)


        old_chunks.extend(chunks)


        faiss.write_index(
            index,
            FAISS_INDEX_PATH
        )


        with open(CHUNKS_PATH, "wb") as f:
            pickle.dump(
                old_chunks,
                f
            )


    else:

        print("Creating new FAISS index...")


        dimension = embeddings.shape[1]


        index = faiss.IndexFlatL2(
            dimension
        )


        index.add(embeddings)


        faiss.write_index(
            index,
            FAISS_INDEX_PATH
        )


        with open(CHUNKS_PATH, "wb") as f:
            pickle.dump(
                chunks,
                f
            )


    return True



# ===========================
# Load FAISS Index
# ===========================
def load_index():

    index = faiss.read_index(
        FAISS_INDEX_PATH
    )


    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)


    return index, chunks



# ===========================
# Search PDF Context
# ===========================
def search(query, top_k=3):

    index, chunks = load_index()


    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")


    distances, indices = index.search(
        query_embedding,
        top_k
    )


    results = []
    scores = []


    for idx, distance in zip(
        indices[0],
        distances[0]
    ):

        if idx != -1:

            results.append(
                chunks[idx]
            )

            scores.append(
                float(distance)
            )


    return results, scores