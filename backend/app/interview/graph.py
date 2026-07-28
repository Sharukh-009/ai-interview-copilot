from langgraph.graph import StateGraph, START, END

from app.interview.state import InterviewState

from app.interview.nodes import (
    retrieve_questions_node,
    generate_questions_node
)


def build_interview_graph():

    graph = StateGraph(InterviewState)

    graph.add_node(
        "retrieve_questions",
        retrieve_questions_node
    )

    graph.add_node(
        "generate_questions",
        generate_questions_node
    )

    graph.add_edge(
        START,
        "retrieve_questions"
    )

    graph.add_edge(
        "retrieve_questions",
        "generate_questions"
    )

    graph.add_edge(
        "generate_questions",
        END
    )

    return graph.compile()