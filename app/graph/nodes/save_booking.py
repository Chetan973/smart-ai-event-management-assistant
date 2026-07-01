"""
Save Booking Node

Creates Customer and Booking in PostgreSQL.
"""

from datetime import datetime
from decimal import Decimal

from app.graph import state
from app.graph.state import EventState

from app.database.connection import SessionLocal

from app.database.models import Booking

from app.repository.customer_repository import CustomerRepository
from app.repository.booking_repository import BookingRepository

from app.services.customer_service import CustomerService
from app.services.booking_service import BookingService


def save_booking_node(
    state: EventState
) -> EventState:

    db = SessionLocal()

    try:

        # ------------------------------------------
        # Initialize Repositories
        # ------------------------------------------

        customer_repository = CustomerRepository(db)
        booking_repository = BookingRepository(db)

        # ------------------------------------------
        # Initialize Services
        # ------------------------------------------

        customer_service = CustomerService(
            customer_repository
        )
        booking_service = BookingService(
            booking_repository
        )

        # ------------------------------------------
        # Create / Fetch Customer
        # ------------------------------------------

        customer = customer_service.register_customer(

            full_name=state["customer_name"],
            email=state["customer_email"],
            phone_number=state["customer_phone"]

        )

        state["customer_id"] = customer.customer_id

        # ------------------------------------------
        # Convert Date
        # ------------------------------------------

        from datetime import datetime

        event_date = datetime.strptime(
            f'{state["event_date"]} {datetime.now().year}',
            "%d %B %Y"
        ).date()    

        # ------------------------------------------
        # Convert Times
        # ------------------------------------------

        start_time = datetime.strptime(
            state["start_time"],
            "%I:%M %p"
        ).time()

        end_time = datetime.strptime(
            state["end_time"],
            "%I:%M %p"
        ).time()

        # ------------------------------------------
        # Create Booking Object
        # ------------------------------------------

        booking = Booking(

            customer_id=customer.customer_id,
            event_name=state["event_name"],
            event_type=state["event_type"],
            event_date=event_date,
            start_time=start_time,
            end_time=end_time,
            guest_count=state["guest_count"],
            venue_name=state["venue"],
            venue_address=state["venue_address"],
            food_preference=state["food_preference"],
            decoration_theme=state["decoration_theme"],
            estimated_budget=Decimal(
                str(state["estimated_budget"])
            ),
            booking_status="CONFIRMED",
            special_requirements=""
        )

        # ------------------------------------------
        # Save Booking
        # ------------------------------------------

        booking = booking_service.create_booking(
            booking
        )
        state["booking_id"] = booking.booking_id

        # ------------------------------------------
        # Next Node
        # ------------------------------------------

        state["next_step"] = "PAYMENT"
        state["final_response"] = f"""
✅ Booking Confirmed Successfully!

Booking ID : {booking.booking_id}

Customer ID : {customer.customer_id}

Proceeding to payment...
"""

        return state
    finally:
        db.close()