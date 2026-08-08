from pathlib import Path


def load_documents():

    base_path = Path("knowledge_base")

    if not base_path.exists():
        raise FileNotFoundError(
            f"Knowledge base folder '{base_path}' not found."
        )

    documents = []

    for file in sorted(base_path.rglob("*.md")):

        with open(file, "r", encoding="utf-8") as f:

            documents.append(
                {
                    "filename": file.name,
                    "category": file.parent.name,
                    "content": f.read()
                }
            )

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print(f"\nLoaded {len(docs)} documents\n")

    for doc in docs:

        print(
            f"{doc['category']} -> {doc['filename']}"
        )