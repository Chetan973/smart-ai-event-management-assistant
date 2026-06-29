"""
Email Log Model

Stores every email sent by the system.
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    String,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from sqlalchemy.sql import func

from app.database.base import Base


class EmailLog(Base):

    __tablename__ = "email_logs"

    email_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    booking_id: Mapped[int] = mapped_column(
        ForeignKey("bookings.booking_id"),
        nullable=False,
    )

    recipient_email: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    subject: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    email_status: Mapped[str] = mapped_column(
        String(30),
        default="SENT",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    booking = relationship(
        "Booking"
    )

    def __repr__(self):

        return (
            f"<EmailLog(id={self.email_id})>"
        )