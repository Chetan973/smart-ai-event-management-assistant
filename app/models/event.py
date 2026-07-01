"""
Event Details Model

Structured response returned by Gemini.
"""

from pydantic import BaseModel, Field


class EventDetails(BaseModel):

    # -----------------------------------------
    # Intent
    # -----------------------------------------

    intent: str = ""

    # -----------------------------------------
    # Event Information
    # -----------------------------------------

    event_name: str = ""
    event_type: str = ""
    event_date: str = ""
    start_time: str = ""
    end_time: str = ""
    guest_count: int = 0

    # -----------------------------------------
    # Venue
    # -----------------------------------------

    venue: str = ""
    venue_address: str = ""
    city: str = ""

    # -----------------------------------------
    # Event Preferences
    # -----------------------------------------

    food_preference: str = ""
    decoration_theme: str = ""
    estimated_budget: float = 0.0

    # -----------------------------------------
    # Customer Information
    # -----------------------------------------

    customer_name: str = ""
    customer_email: str = ""
    customer_phone: str = ""

    # -----------------------------------------
    # Missing Fields
    # -----------------------------------------

    missing_fields: list[str] = Field(
        default_factory=list
    )