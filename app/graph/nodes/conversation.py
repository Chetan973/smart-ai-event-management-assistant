"""
Conversation Node

Collects one missing field at a time.
"""

from datetime import datetime
import re

from app.graph.state import EventState


FIELD_LABELS = {

    # -----------------------------------------
    # Event Information
    # -----------------------------------------

    "event_name": "Event Name",

    "event_date": "Event Date",

    "start_time": "Start Time (Example: 10:00 AM)",

    "end_time": "End Time (Example: 04:00 PM)",

    "event_type": "Event Type",

    # -----------------------------------------
    # Venue
    # -----------------------------------------

    "venue": "Venue",

    "venue_address": "Venue Address",

    "city": "City",

    # -----------------------------------------
    # Event Preferences
    # -----------------------------------------

    "food_preference": "Food Preference",

    "decoration_theme": "Decoration Theme",

    "estimated_budget": "Estimated Budget",

    # -----------------------------------------
    # Customer
    # -----------------------------------------

    "customer_name": "Customer Name",

    "customer_email": "Email Address",

    "customer_phone": "Contact Number",
}


def conversation_node(state: EventState) -> EventState:

    # --------------------------------------------------
    # Do not collect fields while waiting for approval
    # --------------------------------------------------

    if state.get("next_step") == "WAIT_CONFIRMATION":
        return state

    # --------------------------------------------------
    # Save previous answer
    # --------------------------------------------------

    current_field = state.get("current_field")

    user_input = state.get("user_input", "").strip()

    if current_field and user_input:

        # -----------------------------
        # Budget
        # -----------------------------

        if current_field == "estimated_budget":

            try:
                state[current_field] = float(user_input)

            except ValueError:

                state["final_response"] = (
                    "Please enter a valid budget amount."
                )

                return state

        # -----------------------------
        # Guest Count
        # -----------------------------

        elif current_field == "guest_count":

            try:
                state[current_field] = int(user_input)

            except ValueError:

                state["final_response"] = (
                    "Please enter a valid guest count."
                )

                return state

        # -----------------------------
        # Start / End Time
        # -----------------------------

        elif current_field in ("start_time", "end_time"):

            try:

                datetime.strptime(
                    user_input,
                    "%I:%M %p"
                )

                state[current_field] = user_input

            except ValueError:

                state["final_response"] = (
                    f"Invalid time.\n\nPlease enter like 10:00 AM."
                )

                return state

        # -----------------------------
        # Email
        # -----------------------------

        elif current_field == "customer_email":

            pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

            if not re.match(pattern, user_input):

                state["final_response"] = (
                    "Please enter a valid email address."
                )

                return state

            state[current_field] = user_input

        # -----------------------------
        # Phone
        # -----------------------------

        elif current_field == "customer_phone":

            if (
                not user_input.isdigit()
                or len(user_input) != 10
            ):

                state["final_response"] = (
                    "Please enter a valid 10-digit mobile number."
                )

                return state

            state[current_field] = user_input

        # -----------------------------
        # Everything else
        # -----------------------------

        else:

            state[current_field] = user_input

        # -----------------------------
        # Remove collected field
        # -----------------------------

        missing = state.get("missing_fields", [])

        if current_field in missing:
            missing.remove(current_field)

        state["missing_fields"] = missing

    # --------------------------------------------------
    # Check remaining fields
    # --------------------------------------------------

    missing = state.get("missing_fields", [])

    if not missing:

        state["current_field"] = ""

        state["next_step"] = "APPROVAL"

        return state

    # --------------------------------------------------
    # Ask next question
    # --------------------------------------------------

    current_field = missing[0]

    state["current_field"] = current_field

    state["next_step"] = "COLLECT"

    label = FIELD_LABELS.get(
        current_field,
        current_field.replace("_", " ").title()
    )

    state["final_response"] = (
        f"Please provide your {label}."
    )

    return state