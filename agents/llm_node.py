from openai import OpenAI

from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_CHAT_DEPLOYMENT,
)

client = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=AZURE_OPENAI_ENDPOINT,
)


def llm_node(state):
    """
    Final LLM Node

    Uses either:
    - RAG Context
    - Tool Result

    Generates final answer.
    """

    question = state["question"]

    context = state.get("context", "")

    tool_result = state.get("tool_result", "")

    prompt = f"""
You are an Enterprise AI Assistant.

Answer ONLY using the provided information.

Question:
{question}

Knowledge Context:
{context}

Tool Result:
{tool_result}

If neither context nor tool result contains the answer,
reply:

"I couldn't find the requested information."
"""

    print("\n[LLM NODE]")

    response = client.chat.completions.create(
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    answer = response.choices[0].message.content

    state["answer"] = answer

    print("\n===== LLM NODE ANSWER =====\n")
    print(state["answer"])

    return state


# if __name__ == "__main__":

#     state = {
#         "question": "How many annual leaves are allowed?",
#         "context": "Employees receive 24 paid annual leave days every calendar year."
#     }

#     result = llm_node(state)
