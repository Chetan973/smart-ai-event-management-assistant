"""
Conversation Router

Decides whether to continue collecting data
or move to approval.
"""

from app.graph.state import EventState


def conversation_router(state: EventState) -> str:

    if state.get("next_step") == "APPROVAL":
        return "approval"

    return "end"