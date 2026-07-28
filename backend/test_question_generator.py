from app.resume.extractor import extract_text
from app.resume.parser import ResumeParser

from app.rag.candidate_retriever import (
    retrieve_candidate_questions
)

from app.rag.question_generator import (
    generate_questions
)


# -------------------------
# Step 1: Extract resume
# -------------------------

print("Extracting resume...")

text = extract_text("resume.pdf")


# -------------------------
# Step 2: Parse resume
# -------------------------

print("Parsing resume...")

parser = ResumeParser()

profile = parser.parse(text)


# -------------------------
# Step 3: Retrieve questions
# -------------------------

print("Retrieving relevant questions...")

retrieved_questions = retrieve_candidate_questions(
    profile,
    k=5
)


# -------------------------
# Step 4: Generate questions
# -------------------------

print("Generating personalized questions...")

questions = generate_questions(
    profile,
    retrieved_questions
)


# -------------------------
# Step 5: Print result
# -------------------------

print("\n================================")
print("PERSONALIZED INTERVIEW QUESTIONS")
print("================================\n")

print(questions)