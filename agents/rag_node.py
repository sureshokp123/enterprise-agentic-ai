from rag.retriever import retrieve_documents


def rag_node(state):
    """
    LangGraph RAG Node

    Input:
        state["question"]

    Output:
        state["context"]
    """

    question = state["question"]

    print("\n[RAG NODE]")
    print(f"Question : {question}")

    documents = retrieve_documents(question)

    context = "\n\n".join(
        [doc["content"] for doc in documents]
    )

    state["context"] = context

    return state

if __name__ == "__main__":

    state = {
        "question": "How many annual leaves are allowed?"
    }

    result = rag_node(state)

    print("\nRetrieved Context:\n")
    print(result["context"])