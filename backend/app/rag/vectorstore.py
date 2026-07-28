from langchain_community.vectorstores import FAISS

from app.rag.embeddings import get_embeddings
from app.rag.loader import load_questions


def create_vectorstore():

    documents = load_questions()

    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    return vectorstore