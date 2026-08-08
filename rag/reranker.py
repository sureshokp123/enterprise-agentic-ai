from sentence_transformers import CrossEncoder


# Load once when the application starts
reranker_model = CrossEncoder(
    "BAAI/bge-reranker-base"
)


def rerank_documents(
    query: str,
    documents: list,
    top_k: int = 5
):
    """
    Rerank retrieved documents using a cross-encoder.

    query:
        User question

    documents:
        Documents returned by pgvector

    top_k:
        Number of final documents to return
    """

    if not documents:
        return []

    pairs = [
        [query, document["content"]]
        for document in documents
    ]

    scores = reranker_model.predict(pairs)

    reranked_documents = []

    for document, score in zip(documents, scores):

        reranked_document = document.copy()

        reranked_document["rerank_score"] = float(score)

        reranked_documents.append(
            reranked_document
        )

    # Highest reranker score = most relevant
    reranked_documents.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked_documents[:top_k]