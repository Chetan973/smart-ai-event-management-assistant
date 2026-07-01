"""
Temporary Session Manager

Later this will be replaced by
LangGraph PostgreSQL Checkpointer.
"""

from app.graph.state import EventState


_sessions: dict[str, EventState] = {}


def get_state(session_id: str) -> EventState:

    """
    Returns existing conversation state.
    """
    return _sessions.get(session_id, {})


def save_state(
    session_id: str,
    state: EventState,
):

    """
    Saves updated conversation state.
    """
    _sessions[session_id] = state