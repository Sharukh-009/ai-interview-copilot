from uuid import uuid4


interview_sessions = {}


def create_session(profile, questions):

    session_id = str(uuid4())

    interview_sessions[session_id] = {
        "profile": profile,
        "questions": questions,
        "current_question": 0,
        "answers": []
    }

    return session_id


def get_session(session_id):

    return interview_sessions.get(session_id)


def get_current_question(session_id):

    session = get_session(session_id)

    if not session:
        return None

    current_index = session["current_question"]

    questions = session["questions"]

    if current_index >= len(questions):
        return None

    return questions[current_index]


def submit_answer(
    session_id,
    question,
    answer,
    evaluation
):

    session = get_session(session_id)

    if not session:
        return None

    session["answers"].append({
        "question": question,
        "answer": answer,
        "evaluation": evaluation
    })

    session["current_question"] += 1

    return session


def get_interview_result(session_id):

    session = interview_sessions.get(session_id)

    if not session:
        return None

    total_score = 0

    evaluations = []

    for item in session["answers"]:

        evaluation = item["evaluation"]

        evaluations.append({
            "question": item["question"],
            "answer": item["answer"],
            "evaluation": evaluation
        })

        # If your evaluator returns a score
        if isinstance(evaluation, dict):
            total_score += evaluation.get("score", 0)

    number_of_answers = len(session["answers"])

    average_score = (
        total_score / number_of_answers
        if number_of_answers > 0
        else 0
    )

    return {
        "total_questions": len(session["questions"]),
        "answered_questions": number_of_answers,
        "average_score": average_score,
        "evaluations": evaluations
    }