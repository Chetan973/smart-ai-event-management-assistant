from app.graph.state import EventState


def approval_router(state: EventState):

    if state.get("approval_status") == "APPROVED":
        return "save_booking"

    if state.get("approval_status") == "REJECTED":
        return "end"

    return "end"