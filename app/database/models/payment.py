"""
Payment Model

Stores payment information for every booking.
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    String,
    DateTime,
    Numeric,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from sqlalchemy.sql import func

from app.database.base import Base


class Payment(Base):
    """
    Payment details.
    """

    __tablename__ = "payments"

    # ----------------------------------------
    # Primary Key
    # ----------------------------------------

    payment_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    # ----------------------------------------
    # Booking
    # ----------------------------------------

    booking_id: Mapped[int] = mapped_column(
        ForeignKey("bookings.booking_id"),
        nullable=False
    )

    # ----------------------------------------
    # Razorpay
    # ----------------------------------------

    razorpay_order_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    razorpay_payment_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    # ----------------------------------------
    # Amount
    # ----------------------------------------

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR"
    )

    payment_method: Mapped[str] = mapped_column(
        String(30),
        default="RAZORPAY"
    )

    payment_status: Mapped[str] = mapped_column(
        String(30),
        default="PENDING"
    )

    # ----------------------------------------
    # Audit
    # ----------------------------------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # ----------------------------------------
    # Relationship
    # ----------------------------------------

    booking = relationship(
        "Booking",
        back_populates="payments"
    )

    # ----------------------------------------

    def __repr__(self):

        return (
            f"<Payment("
            f"id={self.payment_id}, "
            f"status='{self.payment_status}')>"
        )