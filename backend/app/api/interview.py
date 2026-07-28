from fastapi import APIRouter, HTTPException

from app.schemas.resume import CandidateProfile
from app.schemas.question import AnswerRequest

from app.interview.graph import build_interview_graph

from app.interview.session import (
    create_session,
    get_session,
    get_current_question,
    submit_answer,
    get_interview_result
)

from app.interview.evaluator import evaluate_answer


router = APIRouter()


@router.post("/start")
def start_interview(profile: CandidateProfile):

    print("Starting interview...")

    graph = build_interview_graph()

    initial_state = {
        "profile": profile,
        "retrieved_questions": [],
        "generated_questions": [],
        "current_question": "",
        "candidate_answer": "",
        "evaluation": "",
        "score": 0.0,
        "question_number": 0,
        "interview_complete": False
    }

    # Run LangGraph
    result = graph.invoke(initial_state)

    questions = result["generated_questions"]

    # Create session
    session_id = create_session(
        profile,
        questions
    )

    print("CREATED SESSION ID:", session_id)

    first_question = get_current_question(
        session_id
    )

    return {
        "session_id": session_id,
        "question_number": 1,
        "question": first_question
    }


@router.get("/{session_id}/question")
def get_question(session_id: str):

    print("REQUESTED SESSION ID:", session_id)

    session = get_session(session_id)

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Interview session not found"
        )

    question = get_current_question(
        session_id
    )

    if question is None:
        return {
            "interview_complete": True
        }

    return {
        "interview_complete": False,
        "question_number": session["current_question"] + 1,
        "question": question
    }


@router.post("/{session_id}/answer")
def answer_question(
    session_id: str,
    request: AnswerRequest
):

    session = get_session(session_id)

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Interview session not found"
        )

    # Get the question stored in the backend session
    current_question = get_current_question(
        session_id
    )

    if current_question is None:
        raise HTTPException(
            status_code=400,
            detail="Interview is already completed"
        )

    # Evaluate using backend-controlled question
    evaluation = evaluate_answer(
        question=current_question,
        answer=request.answer
    )

    # Save answer and evaluation
    updated_session = submit_answer(
        session_id=session_id,
        question=current_question,
        answer=request.answer,
        evaluation=evaluation
    )

    # Get next question
    next_question = get_current_question(
        session_id
    )

    # Interview completed
    if next_question is None:

        result = get_interview_result(
            session_id
        )

        return {
            "evaluation": evaluation,
            "interview_complete": True,
            "message": "Interview completed",
            "result": result
        }

    # Interview continues
    return {
        "evaluation": evaluation,
        "interview_complete": False,
        "question_number": (
            updated_session["current_question"] + 1
        ),
        "next_question": next_question
    }


@router.get("/{session_id}/result")
def interview_result(session_id: str):

    session = get_session(session_id)

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Interview session not found"
        )

    result = get_interview_result(session_id)

    return result