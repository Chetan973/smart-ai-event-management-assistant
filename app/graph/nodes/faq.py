"""
FAQ Node
"""

from app.graph.state import EventState


def faq_node(
    state: EventState
) -> EventState:

    state["final_response"] = (
        """
We organize

• Weddings

• Birthdays

• Corporate Events

• Baby Showers

• Engagements

Food packages start from ₹500 per guest.
"""
    )

    return state