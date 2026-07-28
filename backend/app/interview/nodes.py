from app.interview.state import InterviewState
from app.interview.evaluator import evaluate_answer

from app.rag.candidate_retriever import (
    retrieve_candidate_questions
)

from app.rag.question_generator import (
    generate_questions
)


def retrieve_questions_node(state: InterviewState):

    print("Retrieving candidate-specific questions...")

    profile = state["profile"]

    questions = retrieve_candidate_questions(
        profile,
        k=5
    )

    return {
        "retrieved_questions": questions
    }


def generate_questions_node(state: InterviewState):

    print("Generating personalized interview questions...")

    profile = state["profile"]

    retrieved_questions = state["retrieved_questions"]

    generated_questions = generate_questions(
        profile,
        retrieved_questions
    )

    print("TYPE:", type(generated_questions))
    print("VALUE:", generated_questions)

    return {
        "generated_questions": generated_questions
    }


def evaluate_answer_node(state: InterviewState):

    print("Evaluating candidate answer...")

    question = state["current_question"]
    answer = state["candidate_answer"]

    evaluation = evaluate_answer(
        question,
        answer
    )

    return {
        "evaluation": evaluation
    }