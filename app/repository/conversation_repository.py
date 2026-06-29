"""
Conversation Repository
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Conversation


class ConversationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        conversation: Conversation
    ) -> Conversation:

        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)

        return conversation

    def get_by_id(
        self,
        conversation_id: int
    ) -> Optional[Conversation]:

        return (
            self.db.query(Conversation)
            .filter(
                Conversation.conversation_id == conversation_id
            )
            .first()
        )

    def get_all(self) -> list[Conversation]:

        return (
            self.db.query(Conversation)
            .all()
        )

    def delete(
        self,
        conversation_id: int
    ) -> bool:

        conversation = self.get_by_id(conversation_id)

        if conversation is None:
            return False

        self.db.delete(conversation)
        self.db.commit()

        return True