import json

from openai import OpenAI

from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_EVALUATION_DEPLOYMENT,
)


client = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=AZURE_OPENAI_ENDPOINT,
)


def evaluate_context(
    question: str,
    context: str,
    ground_truth: str,
):
    prompt = f"""
You are evaluating the retrieval quality of a RAG system.

Question:
{question}

Ground-truth answer:
{ground_truth}

Retrieved context:
{context}

Evaluate ONLY the retrieved context.

Return JSON with exactly these fields:

{{
    "context_relevance": 0.0,
    "context_precision": 0.0,
    "context_recall": 0.0,
    "reason": ""
}}

Scoring:

context_relevance:
How relevant is the retrieved context to the question?
0.0 = completely irrelevant
0.5 = partially relevant
1.0 = highly relevant

context_precision:
How much of the retrieved context is useful/relevant?
0.0 = mostly irrelevant
0.5 = mixed relevant and irrelevant information
1.0 = almost all retrieved context is relevant

context_recall:
Does the retrieved context contain the information required
to produce the ground-truth answer?
0.0 = required information is missing
0.5 = some required information is present
1.0 = required information is completely present

Return ONLY valid JSON.
"""

    response = client.chat.completions.create(
        model=AZURE_OPENAI_EVALUATION_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": "You are a strict RAG evaluation judge."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:

        print("\nInvalid evaluator response:")
        print(content)

        return {
            "context_relevance": 0.0,
            "context_precision": 0.0,
            "context_recall": 0.0,
            "reason": "Invalid evaluator response"
        }