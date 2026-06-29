"""
Booking Node
"""

from app.graph.state import EventState


FIELD_LABELS = {
    "customer_name": "Customer Name",
    "customer_email": "Email Address",
    "customer_phone": "Contact Number",
    "food_preference": "Food Preference",
    "event_date": "Event Date",
    "venue": "Venue",
}


def booking_node(
    state: EventState
) -> EventState:

    missing_fields = state.get("missing_fields", [])

    if not missing_fields:

        state["booking_response"] = (
            "All booking details have been collected."
        )

        state["final_response"] = state["booking_response"]

        return state

    message = "Great! I already have the following details:\n\n"

    message += f"• Event Type : {state.get('event_type', '')}\n"
    message += f"• Guests : {state.get('guest_count', '')}\n"
    message += f"• Venue : {state.get('venue', '')}\n"
    message += f"• Event Date : {state.get('event_date', '')}\n\n"

    message += "Please provide the remaining details:\n\n"

    for field in missing_fields:

        label = FIELD_LABELS.get(field, field)

        message += f"• {label}\n"

    state["booking_response"] = message

    state["final_response"] = message

    return state