def build_prompt(question: str, documents):

    context = "\n\n".join(
        [
            f"[Document {i+1}]\n{doc['content']}"
            for i, doc in enumerate(documents)
        ]
    )

    prompt = f"""
You are an Enterprise AI Assistant.

Answer ONLY using the provided context.

If the answer is not available in the context, reply exactly:

"I couldn't find this information in the company knowledge base."

=========================
Context
=========================

{context}

=========================
Question
=========================

{question}

=========================
Answer
=========================
"""

    return prompt