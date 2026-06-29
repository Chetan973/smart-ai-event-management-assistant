"""
Conversation Model

Stores chat history between customer and AI assistant.
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    DateTime,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from sqlalchemy.sql import func

from app.database.base import Base


class Conversation(Base):

    __tablename__ = "conversations"

    conversation_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id"),
        nullable=False,
    )

    user_message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    assistant_response: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    customer = relationship(
        "Customer"
    )

    def __repr__(self):

        return (
            f"<Conversation(id={self.conversation_id})>"
        )