from rag.loader import load_documents
from rag.chunker import create_chunks
from rag.embedder import generate_embedding

from database.database import SessionLocal
from database.models import DocumentChunk


def index_documents():

    print("\nLoading documents...")

    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    print("\nCreating chunks...")

    chunks = create_chunks(documents)

    print(f"Created {len(chunks)} chunks")

    db = SessionLocal()

    try:

        db.query(DocumentChunk).delete()
        db.commit()

        total = len(chunks)

        for index, chunk in enumerate(chunks, start=1):

            print(f"Embedding {index}/{total}")

            embedding = generate_embedding(
                chunk["content"]
            )

            row = DocumentChunk(

                filename=chunk["filename"],

                category=chunk["category"],

                chunk_id=chunk["chunk_id"],

                content=chunk["content"],

                embedding=embedding
            )

            db.add(row)

            if index % 20 == 0:
                db.commit()

        db.commit()

        print("\nIndexing completed successfully.")

    finally:

        db.close()


if __name__ == "__main__":

    index_documents()