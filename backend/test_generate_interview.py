from app.resume.extractor import extract_text
from app.resume.parser import ResumeParser
from app.rag.candidate_retriever import retrieve_candidate_questions
from app.interview.service import generate_questions


# 1. Extract resume text
print("Extracting resume...")

text = extract_text("resume.pdf")

print("Resume extracted")


# 2. Parse resume using LLM
print("Parsing resume...")

parser = ResumeParser()

profile = parser.parse(text)

print("Resume parsed")


# 3. Retrieve relevant questions
print("Retrieving relevant questions...")

retrieved_questions = retrieve_candidate_questions(
    profile,
    k=5
)

print("Questions retrieved")


# 4. Generate personalized interview questions
print("Generating interview questions...")

questions = generate_questions(
    profile,
    retrieved_questions
)


# 5. Print result
print("\n==============================")
print("GENERATED INTERVIEW QUESTIONS")
print("==============================\n")

print(questions)