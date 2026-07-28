from app.interview.graph import build_interview_graph


interview_graph = build_interview_graph()


def generate_interview(profile):

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

    result = interview_graph.invoke(
        initial_state
    )

    return result