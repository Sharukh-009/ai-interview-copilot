import json
from pathlib import Path

from langchain_core.documents import Document


def load_questions() -> list[Document]:

    data_path = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "questions.json"
    )

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    for item in data:

        document = Document(
            page_content=item["question"],
            metadata={
                "topic": item["topic"],
                "difficulty": item["difficulty"],
                "type": item["type"]
            }
        )

        documents.append(document)

    return documents