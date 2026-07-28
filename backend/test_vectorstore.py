from app.rag.vectorstore import create_vectorstore


vectorstore = create_vectorstore()

query = "Ask me a question about Python decorators"

results = vectorstore.similarity_search(
    query,
    k=3
)

print("\nRelevant Questions:\n")

for result in results:

    print("Question:", result.page_content)
    print("Metadata:", result.metadata)
    print("-" * 50)