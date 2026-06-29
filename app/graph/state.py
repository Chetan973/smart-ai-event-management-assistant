"""
Graph State

Shared state across all LangGraph nodes.
"""

from typing import TypedDict
from typing import Any


class EventState(TypedDict, total=False):

    user_input: str

    intent: str

    customer_name: str

    customer_email: str

    customer_phone: str

    event_name: str

    event_type: str

    event_date: str

    guest_count: int

    venue: str

    food_preference: str

    decoration_theme: str

    budget: float

    planner_response: dict[str, Any]

    booking_response: str

    payment_response: str

    email_response: str

    final_response: str
    
    city: str

    missing_fields: list[str]