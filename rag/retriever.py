from sqlalchemy import text

from database.database import SessionLocal

from rag.embedder import generate_embedding
from rag.reranker import rerank_documents


def retrieve_documents(
    query: str,
    retrieval_k: int = 10,
    final_k: int = 5
):

    query_embedding = generate_embedding(query)

    db = SessionLocal()

    try:

        sql = text("""
            SELECT
                filename,
                category,
                chunk_id,
                content,
                embedding <=> CAST(:embedding AS vector) AS distance
            FROM document_chunks
            ORDER BY embedding <=> CAST(:embedding AS vector)
            LIMIT :top_k
        """)

        result = db.execute(
            sql,
            {
                "embedding": str(query_embedding),
                "top_k": retrieval_k
            }
        )

        documents = []

        for row in result:

            documents.append(
                {
                    "filename": row.filename,
                    "category": row.category,
                    "chunk_id": row.chunk_id,
                    "content": row.content,
                    "distance": float(row.distance)
                }
            )

    finally:

        db.close()

    print(
        f"\nVector Search Retrieved: {len(documents)} documents"
    )

    # -----------------------------------
    # RERANK
    # -----------------------------------

    reranked_documents = rerank_documents(
        query=query,
        documents=documents,
        top_k=final_k
    )

    print(
        f"After Reranking: {len(reranked_documents)} documents"
    )

    # -----------------------------------
    # Debug ranking
    # -----------------------------------

    for index, document in enumerate(
        reranked_documents,
        start=1
    ):

        print(
            f"\nRank {index}"
        )

        print(
            f"File       : {document['filename']}"
        )

        print(
            f"Chunk      : {document['chunk_id']}"
        )

        print(
            f"Vector     : {document['distance']:.4f}"
        )

        print(
            f"Rerank     : {document['rerank_score']:.4f}"
        )

        print(
            f"Content    : {document['content'][:200]}"
        )

    return reranked_documents


if __name__ == "__main__":

    docs = retrieve_documents(
        "How many annual leaves are allowed?"
    )

    print("\n\n===== FINAL RERANKED DOCUMENTS =====")

    for doc in docs:

        print("=" * 80)

        print(doc["filename"])

        print(
            "Vector distance:",
            doc["distance"]
        )

        print(
            "Rerank score:",
            doc["rerank_score"]
        )

        print()

        print(
            doc["content"][:250]
        )