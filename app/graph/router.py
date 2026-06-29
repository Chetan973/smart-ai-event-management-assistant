"""
Router

Decides which node to execute next.
"""

from app.graph.state import EventState


def router(state: EventState) -> str:
    """
    Route based on detected intent.
    """

    intent = state.get("intent", "GENERAL")

    if intent == "BOOK_EVENT":
        return "booking"

    elif intent == "FAQ":
        return "faq"

    elif intent == "PAYMENT":
        return "payment"

    return "planner"