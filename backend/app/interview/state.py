from typing import TypedDict

from app.schemas.resume import CandidateProfile


class InterviewState(TypedDict, total=False):

    profile: CandidateProfile

    retrieved_questions: list

    generated_questions: list[str]

    current_question: str

    candidate_answer: str

    evaluation: str

    score: float

    question_number: int

    interview_complete: bool