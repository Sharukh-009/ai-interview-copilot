from app.resume.extractor import extract_text
from app.resume.parser import ResumeParser
from app.rag.candidate_retriever import retrieve_candidate_questions


# 1. Extract resume text
text = extract_text("resume.pdf")


# 2. Parse resume into CandidateProfile
parser = ResumeParser()
profile = parser.parse(text)


# 3. Retrieve questions based on candidate profile
questions = retrieve_candidate_questions(profile, k=5)


# 4. Print results
print("\nCandidate Profile:")
print(profile)

print("\nRelevant Interview Questions:")

for i, doc in enumerate(questions, start=1):

    print(f"\n{i}. {doc.page_content}")

    print("Metadata:", doc.metadata)