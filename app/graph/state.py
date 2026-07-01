"""
Graph State

Shared state across all LangGraph nodes.
"""

from typing import TypedDict
from typing import Any


class EventState(TypedDict, total=False):

    # -------------------------------------
    # User Input
    # -------------------------------------

    user_input: str

    # -------------------------------------
    # AI Planner
    # -------------------------------------

    intent: str
    planner_response: dict[str, Any]

    # -------------------------------------
    # Customer Details
    # -------------------------------------

    customer_name: str
    customer_email: str
    customer_phone: str
    customer_id: int

    # -------------------------------------
    # Event Details
    # -------------------------------------

    event_name: str
    event_type: str
    event_date: str
    start_time: str
    end_time: str
    guest_count: int
    venue: str
    venue_address: str
    city: str
    food_preference: str
    decoration_theme: str
    estimated_budget: float

    # -------------------------------------
    # Booking
    # -------------------------------------

    booking_id: int
    approval_status: str

    # -------------------------------------
    # Conversation
    # -------------------------------------

    missing_fields: list[str]
    current_field: str
    next_step: str

    # -------------------------------------
    # Agent Responses
    # -------------------------------------

    booking_response: str
    payment_response: str
    email_response: str
    final_response: str