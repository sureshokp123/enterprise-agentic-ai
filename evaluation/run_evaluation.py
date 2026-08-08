from evaluation.dataset import EVALUATION_DATASET

from rag.retriever import retrieve_documents

from evaluation.retrieval_metrics import (
    hit_at_k,
    precision_at_k,
    reciprocal_rank
)

from evaluation.context_metrics import evaluate_context

def run_retrieval_evaluation():

    print("\n")
    print("=" * 80)
    print("RAG RETRIEVAL EVALUATION")
    print("=" * 80)

    total_hit = 0
    total_precision = 0
    total_mrr = 0

    total_questions = len(EVALUATION_DATASET)

    for item in EVALUATION_DATASET:

        question = item["question"]

        ground_truth = item["ground_truth"]

        print("\n")
        print("-" * 80)
        print(f"Question : {question}")

        documents = retrieve_documents(
            question,
            retrieval_k=10,
            final_k=5
        )

        hit = hit_at_k(
            documents,
            ground_truth,
            k=5
        )

        precision = precision_at_k(
            documents,
            ground_truth,
            k=5
        )

        rr = reciprocal_rank(
            documents,
            ground_truth
        )

        total_hit += hit
        total_precision += precision
        total_mrr += rr

        print(f"Hit@5        : {hit}")
        print(f"Precision@5  : {precision:.2f}")
        print(f"MRR          : {rr:.2f}")

        print("\nTop retrieved documents:")

        for rank, document in enumerate(
            documents,
            start=1
        ):

            print(
                f"{rank}. "
                f"{document['filename']} "
                f"(chunk={document['chunk_id']}) "
                f"rerank={document['rerank_score']:.4f}"
            )

    print("\n")
    print("=" * 80)
    print("FINAL RETRIEVAL METRICS")
    print("=" * 80)

    hit_score = total_hit / total_questions
    precision_score = total_precision / total_questions
    mrr_score = total_mrr / total_questions

    print(f"\nHit@5       : {hit_score:.2%}")
    print(f"Precision@5 : {precision_score:.2%}")
    print(f"MRR         : {mrr_score:.2%}")

    print("\nEvaluation completed.")


if __name__ == "__main__":

    run_retrieval_evaluation()