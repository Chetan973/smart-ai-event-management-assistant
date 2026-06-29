"""
Booking Model

Represents an event booking created by a customer.
"""

from __future__ import annotations

from datetime import date, time, datetime, timezone
from decimal import Decimal

from sqlalchemy import (
    String,
    Date,
    Time,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base
from app.database.models.customer import Customer


class Booking(Base):
    """
    Booking information.

    One customer can have multiple bookings.
    """

    __tablename__ = "bookings"

    # ----------------------------------------
    # Primary Key
    # ----------------------------------------

    booking_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    # ----------------------------------------
    # Foreign Key
    # ----------------------------------------

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id"),
        nullable=False,
    )

    # ----------------------------------------
    # Event Information
    # ----------------------------------------

    event_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    event_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    event_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    start_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    end_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    # ----------------------------------------
    # Guest Information
    # ----------------------------------------

    guest_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    # ----------------------------------------
    # Venue
    # ----------------------------------------

    venue_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    venue_address: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # ----------------------------------------
    # Event Preferences
    # ----------------------------------------

    food_preference: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    decoration_theme: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # ----------------------------------------
    # Budget
    # ----------------------------------------

    estimated_budget: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    # ----------------------------------------
    # Booking Status
    # ----------------------------------------

    booking_status: Mapped[str] = mapped_column(
        String(30),
        default="PENDING",
        nullable=False,
    )

    # ----------------------------------------
    # Additional Notes
    # ----------------------------------------

    special_requirements: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ----------------------------------------
    # Audit Columns
    # ----------------------------------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # ----------------------------------------
    # Relationship
    # ----------------------------------------

    customer: Mapped["Customer"] = relationship(
        "Customer",
        back_populates="bookings",
    )

    # ----------------------------------------
    # String Representation
    # ----------------------------------------

    def __repr__(self):

        return (
            f"<Booking("
            f"id={self.booking_id}, "
            f"event='{self.event_name}', "
            f"customer={self.customer_id})>"
        )