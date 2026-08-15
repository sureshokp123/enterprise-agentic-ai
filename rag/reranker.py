from sentence_transformers import CrossEncoder

reranker_model = None


def get_reranker_model():
    global reranker_model

    if reranker_model is None:
        reranker_model = CrossEncoder(
            "BAAI/bge-reranker-base"
        )

    return reranker_model


def rerank_documents(
    query: str,
    documents: list,
    top_k: int = 5
):
    """
    Rerank retrieved documents using a cross-encoder.
    """

    if not documents:
        return []

    pairs = [
        [query, document["content"]]
        for document in documents
    ]

    model = get_reranker_model()

    scores = model.predict(pairs)

    reranked_documents = []

    for document, score in zip(documents, scores):

        reranked_document = document.copy()

        reranked_document["rerank_score"] = float(score)

        reranked_documents.append(
            reranked_document
        )

    reranked_documents.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked_documents[:top_k]