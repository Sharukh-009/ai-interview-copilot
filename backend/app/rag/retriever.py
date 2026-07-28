from app.rag.vectorstore import create_vectorstore


def get_retriever():
    vectorstore = create_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever