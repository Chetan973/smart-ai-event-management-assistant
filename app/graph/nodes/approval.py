"""
Approval Node

Human-in-the-Loop confirmation.
"""

from app.graph.state import EventState


def approval_node(state: EventState) -> EventState:
    """
    Displays booking summary and waits for
    human confirmation (YES / NO).
    """

    # -------------------------------------------------
    # Already waiting for confirmation?
    # -------------------------------------------------

    if state.get("next_step") == "WAIT_CONFIRMATION":

        answer = state.get("user_input", "").strip().upper()

        # ---------------------------------------------
        # User Approved
        # ---------------------------------------------

        if answer == "YES":

            state["approval_status"] = "APPROVED"

            state["next_step"] = "SAVE_BOOKING"

            state["final_response"] = (
                "Booking confirmed.\n\n"
                "Saving your booking..."
            )

            return state

        # ---------------------------------------------
        # User Rejected
        # ---------------------------------------------

        if answer == "NO":

            state["approval_status"] = "REJECTED"

            state["next_step"] = "CANCELLED"

            state["final_response"] = (
                "Booking cancelled."
            )

            return state

        # ---------------------------------------------
        # Invalid Input
        # ---------------------------------------------

        state["final_response"] = (
            "Please reply only with YES or NO."
        )

        return state

    # -------------------------------------------------
    # First visit to Approval Node
    # -------------------------------------------------

    state["next_step"] = "WAIT_CONFIRMATION"

    state["approval_status"] = "PENDING"

    state["final_response"] = f"""
========================================

        BOOKING SUMMARY

========================================

Customer Name      : {state.get("customer_name", "")}

Email              : {state.get("customer_email", "")}

Phone              : {state.get("customer_phone", "")}

----------------------------------------

Event Name         : {state.get("event_name", "")}

Event Type         : {state.get("event_type", "")}

Event Date         : {state.get("event_date", "")}

Start Time         : {state.get("start_time", "")}

End Time           : {state.get("end_time", "")}

Guest Count        : {state.get("guest_count", "")}

Venue              : {state.get("venue", "")}

Venue Address      : {state.get("venue_address", "")}

City               : {state.get("city", "")}

Food Preference    : {state.get("food_preference", "")}

Decoration Theme   : {state.get("decoration_theme", "")}

Estimated Budget   : ₹ {state.get("estimated_budget", "")}

========================================

Reply

YES -> Confirm Booking

NO -> Cancel Booking

========================================
"""

    return state