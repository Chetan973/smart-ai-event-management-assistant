"""
Payment Node
"""

from app.graph.state import EventState


def payment_node(
    state: EventState
) -> EventState:

    state["final_response"] = (
        """
Payment will be processed using Razorpay Test Mode.
"""
    )

    return state