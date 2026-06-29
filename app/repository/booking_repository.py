"""
Booking Repository

Responsible only for database operations related to bookings.
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Booking


class BookingRepository:
    """
    Repository for Booking table.
    """

    def __init__(self, db: Session):
        self.db = db

    # ---------------------------------------------------------
    # Create Booking
    # ---------------------------------------------------------

    def create(
        self,
        booking: Booking
    ) -> Booking:
        """
        Saves a booking into database.
        """

        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)

        return booking

    # ---------------------------------------------------------
    # Get Booking by ID
    # ---------------------------------------------------------

    def get_by_id(
        self,
        booking_id: int
    ) -> Optional[Booking]:
        """
        Returns booking using booking id.
        """

        return (
            self.db.query(Booking)
            .filter(
                Booking.booking_id == booking_id
            )
            .first()
        )

    # ---------------------------------------------------------
    # Get All Bookings
    # ---------------------------------------------------------

    def get_all(self) -> list[Booking]:
        """
        Returns every booking.
        """

        return (
            self.db.query(Booking)
            .order_by(
                Booking.booking_id.desc()
            )
            .all()
        )

    # ---------------------------------------------------------
    # Get Customer Bookings
    # ---------------------------------------------------------

    def get_by_customer(
        self,
        customer_id: int
    ) -> list[Booking]:
        """
        Returns all bookings of one customer.
        """

        return (
            self.db.query(Booking)
            .filter(
                Booking.customer_id == customer_id
            )
            .order_by(
                Booking.event_date
            )
            .all()
        )

    # ---------------------------------------------------------
    # Update Booking
    # ---------------------------------------------------------

    def update(
        self,
        booking: Booking
    ) -> Booking:
        """
        Updates booking.
        """

        self.db.commit()
        self.db.refresh(booking)

        return booking

    # ---------------------------------------------------------
    # Update Booking Status
    # ---------------------------------------------------------

    # def update_status(
    #     self,
    #     booking_id: int,
    #     status: str
    # ) -> Optional[Booking]:
    #     """
    #     Updates booking status.
    #     """

    #     booking = self.get_by_id(
    #         booking_id
    #     )

    #     if booking is None:
    #         return None

    #     booking.booking_status = status

    #     self.db.commit()

    #     self.db.refresh(booking)

    #     return booking

    # ---------------------------------------------------------
    # Delete Booking
    # ---------------------------------------------------------

    def delete(
        self,
        booking_id: int
    ) -> bool:
        """
        Deletes booking.
        """

        booking = self.get_by_id(
            booking_id
        )

        if booking is None:
            return False

        self.db.delete(booking)

        self.db.commit()

        return True