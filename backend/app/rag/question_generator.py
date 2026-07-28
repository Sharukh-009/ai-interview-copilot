from app.services.llm import llm
from app.schemas.resume import CandidateProfile


def generate_questions(
    profile: CandidateProfile,
    retrieved_questions: list
):

    context = "\n".join(
        f"- {doc.page_content}"
        for doc in retrieved_questions
    )

    prompt = f"""
You are an expert technical interviewer.

Your job is to create personalized interview questions
for a candidate based on their resume.

Candidate Profile:
{profile}

Relevant questions retrieved from the interview question database:
{context}

Instructions:

1. Generate exactly 5 personalized technical interview questions.
2. Questions must be based on the candidate's actual skills,
   projects, and experience.
3. Use the retrieved questions as guidance.
4. Do not simply copy the retrieved questions.
5. Ask questions that test understanding rather than memorization.
6. Include questions about the candidate's projects when possible.
7. Do not invent technologies that are not present in the candidate profile.
8. Return exactly one question per line.
9. Do not number the questions.
10. Do not add any introduction or explanation.
"""

    response = llm.invoke(prompt)

    content = response.content

    # Handle Gemini structured content blocks
    if isinstance(content, list):

        text = "\n".join(
            block["text"]
            for block in content
            if block.get("type") == "text"
        )

    else:
        text = content

    # Split the single text response into individual questions
    questions = [
        question.strip()
        for question in text.split("\n")
        if question.strip()
    ]

    return questions