from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)


def extract_text(pdf_path):

    print("Opening PDF:", pdf_path)

    reader = PdfReader(pdf_path)

    print("PDF opened successfully")

    text = ""

    for i, page in enumerate(reader.pages):

        print(f"Reading page {i + 1}")

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    print("Text extraction completed")
    print("Total characters:", len(text))

    return text


def split_text(text):

    print("Splitting text into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    print("Total chunks:", len(chunks))

    return chunks


def create_embeddings(chunks):

    print("Creating embeddings...")

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    print("Embeddings created successfully")

    return embeddings