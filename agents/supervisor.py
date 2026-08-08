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


def supervisor(state):

    question = state["question"]

    prompt = f"""
You are an Enterprise AI Router.

Your job is to decide which workflow should handle the user's request.

Available routes:

1. RAG
2. TOOL
3. APPROVAL

Rules:

Return APPROVAL if the user wants to:

- delete employee
- remove employee
- update employee
- modify employee
- update salary
- change salary
- execute shell command
- run terminal command
- delete file
- remove file
- delete record
- update database
- modify database

Return TOOL if the user wants to:

- show employee details
- get employee by id
- list employees
- employee lookup
- calculate
- add numbers
- multiply numbers
- read file

Return RAG if the user asks about:

- leave policy
- attendance policy
- HR policy
- IT policy
- company documentation
- company rules
- handbook
- benefits
- documentation
- knowledge base

Return ONLY ONE WORD.

Valid outputs are:

RAG

TOOL

APPROVAL

Question:
{question}
"""

    response = client.chat.completions.create(
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    decision = response.choices[0].message.content.strip().upper()

    # Safety check
    if decision not in ["RAG", "TOOL", "APPROVAL"]:
        decision = "RAG"

    print(f"\n[SUPERVISOR] -> {decision}")

    state["route"] = decision

    return state


if __name__ == "__main__":

    state = {
        "question": "Delete employee 105"
    }

    result = supervisor(state)

    print("\nState:\n")
    print(result)