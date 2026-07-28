from app.rag.retriever import get_retriever


retriever = get_retriever()

results = retriever.invoke(
    "Ask me questions about Python and object oriented programming"
)

for doc in results:
    print("QUESTION:", doc.page_content)
    print("METADATA:", doc.metadata)
    print("-" * 50)