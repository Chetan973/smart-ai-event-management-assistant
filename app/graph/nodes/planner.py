"""
Planner Node

Uses Gemini only for the FIRST user request.
"""

from app.graph.state import EventState
from app.prompts.planner_prompt import PLANNER_PROMPT
from app.services.gemini_service import GeminiService
from app.models.event import EventDetails

gemini = GeminiService()


def planner_node(state: EventState) -> EventState:

    # -------------------------------------------------
    # Skip Gemini while collecting details
    # or waiting for approval. Skip planner once conversation has started
    # -------------------------------------------------

    if state.get("next_step") == "SAVE_BOOKING":
        return state

    prompt = f"""
{PLANNER_PROMPT}

User:

{state["user_input"]}
"""
    # -------------------------------------------------
    # Gemini Extraction
    # -------------------------------------------------

    result = gemini.generate_json(prompt)
    event = EventDetails(**result)

    # -------------------------------------------------
    # Update Graph State
    # -------------------------------------------------

    state["intent"] = event.intent

    # -----------------------------------------
    # Event Information
    # -----------------------------------------

    state["event_name"] = event.event_name
    state["event_type"] = event.event_type
    state["event_date"] = event.event_date
    state["start_time"] = event.start_time
    state["end_time"] = event.end_time
    state["guest_count"] = event.guest_count

    # -----------------------------------------
    # Venue
    # -----------------------------------------

    state["venue"] = event.venue
    state["venue_address"] = event.venue_address
    state["city"] = event.city

    # -----------------------------------------
    # Event Preferences
    # -----------------------------------------

    state["food_preference"] = event.food_preference
    state["decoration_theme"] = event.decoration_theme
    state["estimated_budget"] = event.estimated_budget

    # -----------------------------------------
    # Customer
    # -----------------------------------------

    state["customer_name"] = event.customer_name
    state["customer_email"] = event.customer_email
    state["customer_phone"] = event.customer_phone

    # -----------------------------------------
    # Missing Fields
    # -----------------------------------------

    state["missing_fields"] = event.missing_fields

    # -----------------------------------------
    # Planner Response
    # -----------------------------------------
    state["planner_response"] = event.model_dump()
    return state