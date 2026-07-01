"""
Entry Router

Determines where the graph should begin.
"""

from app.graph.state import EventState


def entry_router(
    state: EventState,
) -> str:

    next_step = state.get("next_step")

    if next_step == "COLLECT":
        return "conversation"

    if next_step == "WAIT_CONFIRMATION":
        return "approval"

    if next_step == "SAVE_BOOKING":
        return "save_booking"

    return "planner"