from openai import OpenAI

from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION
)

client = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=AZURE_OPENAI_ENDPOINT,
)
# client = AzureOpenAI(
#     api_key=AZURE_OPENAI_API_KEY,
#     api_version=AZURE_OPENAI_API_VERSION,
#     azure_endpoint=AZURE_OPENAI_ENDPOINT,
# )

# EMBEDDING_MODEL = "text-embedding-3-small"


def generate_embedding(text: str):

    response = client.embeddings.create(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=text
    )

    return response.data[0].embedding

if __name__ == "__main__":

    text = "Employees must apply leave through the HR portal."

    # print("Endpoint:", AZURE_OPENAI_ENDPOINT)
    # print("Embedding Deployment:", repr(AZURE_OPENAI_EMBEDDING_DEPLOYMENT))
    # print("API Version:", AZURE_OPENAI_API_VERSION)

    embedding = generate_embedding(text)

    print(f"\nEmbedding Length : {len(embedding)}")

    print("\nFirst 10 values:\n")

    print(embedding[:10])