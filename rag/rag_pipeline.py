from openai import OpenAI

from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_CHAT_DEPLOYMENT
)

from rag.retriever import retrieve_documents
from rag.prompt_builder import build_prompt


client = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=AZURE_OPENAI_ENDPOINT
)


def ask_rag(question: str):

    print("\nRetrieving relevant documents...\n")

    documents = retrieve_documents(question)

    print(f"Retrieved {len(documents)} documents\n")

    prompt = build_prompt(question, documents)

    response = client.chat.completions.create(
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": "You are an Enterprise AI Assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    while True:

        question = input("\nAsk Question : ")

        if question.lower() == "exit":
            break

        answer = ask_rag(question)

        print("\nAnswer\n")
        print(answer)