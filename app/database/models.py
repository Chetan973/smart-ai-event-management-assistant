"""
Database Models

Contains all database tables.
"""

from datetime import datetime
from sqlalchemy.sql import func

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


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

    def __repr__(self) -> str:
        return (
            f"<Customer("
            f"id={self.customer_id}, "
            f"name='{self.full_name}'"
            f")>"
        )