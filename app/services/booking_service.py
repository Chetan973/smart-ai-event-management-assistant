"""
Booking Service

Contains business logic for bookings.
"""

from typing import Optional

from app.database.models import Booking
from app.repository.booking_repository import BookingRepository


class BookingService:
    """
    Service layer for Booking operations.
    """

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    # ---------------------------------------------------------
    # Create Booking
    # ---------------------------------------------------------

    def create_booking(
        self,
        booking: Booking
    ) -> Booking:
        booking.booking_status = "PENDING"

        return self.repository.create(booking)

    # ---------------------------------------------------------
    # Get Booking
    # ---------------------------------------------------------

    def get_booking(
        self,
        booking_id: int
    ) -> Optional[Booking]:

        return self.repository.get_by_id(booking_id)

    # ---------------------------------------------------------
    # Get All Bookings
    # ---------------------------------------------------------

    def get_all_bookings(
        self
    ) -> list[Booking]:

        return self.repository.get_all()

    # ---------------------------------------------------------
    # Get Customer Bookings
    # ---------------------------------------------------------

    def get_customer_bookings(
        self,
        customer_id: int
    ) -> list[Booking]:

        return self.repository.get_by_customer(customer_id)

    # ---------------------------------------------------------
    # Update Booking
    # ---------------------------------------------------------

    def update_booking(
        self,
        booking: Booking
    ) -> Booking:

        return self.repository.update(booking)

    # ---------------------------------------------------------
    # Delete Booking
    # ---------------------------------------------------------

    def delete_booking(
        self,
        booking_id: int
    ) -> bool:

        return self.repository.delete(booking_id)