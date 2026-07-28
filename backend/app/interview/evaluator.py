from app.services.llm import llm
from app.schemas.evaluation import AnswerEvaluation


def evaluate_answer(
    question: str,
    answer: str
):

    prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate based on:

1. Technical correctness
2. Understanding
3. Completeness
4. Clarity

Give a score from 0 to 10.

Provide:
- score
- feedback
- strengths
- weaknesses
"""

    structured_llm = llm.with_structured_output(
        AnswerEvaluation
    )

    evaluation = structured_llm.invoke(prompt)

    return evaluation.model_dump()