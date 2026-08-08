from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(

    chunk_size=800,

    chunk_overlap=150,

    separators=["\n\n", "\n", ".", " ", ""]
)


def create_chunks(documents):

    chunks = []

    for doc in documents:

        splits = splitter.split_text(doc["content"])

        for i, chunk in enumerate(splits):

            chunks.append(
                {
                    "filename": doc["filename"],
                    "category": doc["category"],
                    "chunk_id": i,
                    "content": chunk,
                    "chunk_length": len(chunk)
                }
            )

    return chunks