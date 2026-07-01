"""
Update State Node

Updates the EventState with the user's latest answer.
"""

from app.graph.state import EventState


def update_state_node(state: EventState) -> EventState:

    current = state.get("current_field")

    answer = state.get("user_input", "").strip()

    if current:

        state[current] = answer

        missing = state.get("missing_fields", [])

        if current in missing:
            missing.remove(current)

        state["missing_fields"] = missing

    return state