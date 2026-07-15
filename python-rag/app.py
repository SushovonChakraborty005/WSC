from flask import Flask, request, jsonify
from flask_cors import CORS

print("App Started")

import os

from query import get_context
from groq_client import (
    generate_rag_answer,
    generate_general_answer
)
from embed import (
    extract_text,
    split_text,
    create_embeddings
)
from vector_store import save_index

app = Flask(__name__)

# Enable CORS
CORS(app)


@app.before_request
def before():
    print("Request received:", request.method, request.path)


@app.route("/")
def home():
    return "Server is running"


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================
# Upload PDF
# ==========================
@app.route("/upload", methods=["POST"])
def upload_pdf():

    print("1. Upload API called")

    if "file" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    file = request.files["file"]

    print("2. File received")

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(file_path)

    print("3. File saved")

    text = extract_text(file_path)

    print("4. Text extracted")

    chunks = split_text(text)

    print("5. Chunks created")

    embeddings = create_embeddings(chunks)

    print("6. Embeddings created")

    save_index(
        embeddings,
        chunks
    )

    print("7. FAISS Index Updated")

    return jsonify({
        "message": "PDF processed successfully",
        "chunks": len(chunks)
    })


# ==========================
# Ask Question
# ==========================
@app.route("/ask", methods=["POST"])
def ask():

    print("\n==============================")
    print("Ask API Called")
    print("==============================")

    data = request.get_json()

    question = data.get("question")

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    print("Question:", question)

    # -------------------------
    # Search PDF
    # -------------------------
    context, score = get_context(question)

    print("\nBest Similarity Score:", score)

    THRESHOLD = 1.2

    # -------------------------
    # Answer From PDF
    # -------------------------
    if score <= THRESHOLD:

        print("Using Uploaded PDF")

        answer = generate_rag_answer(
            context,
            question
        )

        source = context

    # -------------------------
    # Answer From AI
    # -------------------------
    else:

        print("Using General AI")

        answer = generate_general_answer(
            question
        )

        source = "General AI Knowledge"

    print("\nAnswer:")
    print(answer)

    return jsonify({
        "question": question,
        "answer": answer,
        "source": source,
        "score": score
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )