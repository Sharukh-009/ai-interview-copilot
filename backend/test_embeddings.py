from app.rag.embeddings import get_embeddings


embeddings = get_embeddings()

text = "Explain Python decorators"

vector = embeddings.embed_query(text)

print("Vector type:", type(vector))
print("Vector length:", len(vector))
print("First 10 values:", vector[:10])