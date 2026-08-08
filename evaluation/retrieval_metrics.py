def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def is_relevant(document, ground_truth: str) -> bool:
    """
    Simple baseline relevance check.

    A retrieved document is considered relevant when
    the ground-truth answer is contained in the document.
    """

    content = normalize(document["content"])
    truth = normalize(ground_truth)

    return truth in content


def hit_at_k(documents, ground_truth: str, k: int = 5) -> int:

    top_documents = documents[:k]

    for document in top_documents:

        if is_relevant(document, ground_truth):
            return 1

    return 0


def precision_at_k(documents, ground_truth: str, k: int = 5) -> float:

    top_documents = documents[:k]

    if not top_documents:
        return 0.0

    relevant_count = sum(
        1
        for document in top_documents
        if is_relevant(document, ground_truth)
    )

    return relevant_count / len(top_documents)


def reciprocal_rank(documents, ground_truth: str) -> float:

    for index, document in enumerate(documents, start=1):

        if is_relevant(document, ground_truth):
            return 1 / index

    return 0.0