from app.resume.extractor import extract_text
from app.resume.parser import ResumeParser

from app.interview.graph import build_interview_graph


# -------------------------
# 1. Extract resume
# -------------------------

print("Extracting resume...")

text = extract_text("resume.pdf")


# -------------------------
# 2. Parse resume
# -------------------------

print("Parsing resume...")

parser = ResumeParser()

profile = parser.parse(text)


# -------------------------
# 3. Build graph
# -------------------------

print("Building interview graph...")

graph = build_interview_graph()


# -------------------------
# 4. Initial state
# -------------------------

initial_state = {
    "profile": profile,
    "retrieved_questions": [],
    "generated_questions": "",
    "current_question": "",
    "candidate_answer": "",
    "evaluation": "",
    "score": 0.0,
    "question_number": 0,
    "interview_complete": False
}


# -------------------------
# 5. Run graph
# -------------------------

print("Running interview graph...")

result = graph.invoke(initial_state)


# -------------------------
# 6. Print result
# -------------------------

print("\n==============================")
print("GENERATED QUESTIONS")
print("==============================\n")

print(result["generated_questions"])