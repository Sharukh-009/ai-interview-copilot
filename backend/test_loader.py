from app.rag.loader import load_questions

questions = load_questions()

print(f"Loaded {len(questions)} questions\n")

for q in questions:
    print(q)