"""
Database Models

Contains all database tables.
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base

if TYPE_CHECKING:
    from app.database.models.booking import Booking

class Customer(Base):
    """
    Customer information.

    One customer can create multiple bookings.
    """

    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    phone_number: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
    onupdate=func.now()
    )

    bookings: Mapped[list["Booking"]] = relationship(
        "Booking",
        back_populates="customer",
        cascade="all, delete-orphan",
   )

    def __repr__(self) -> str:
        return (
            f"<Customer("
            f"id={self.customer_id}, "
            f"name='{self.full_name}'"
            f")>"
        )