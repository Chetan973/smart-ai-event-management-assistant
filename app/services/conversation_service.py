"""
Conversation Service
"""

from typing import Optional

from app.database.models import Conversation
from app.repository.conversation_repository import ConversationRepository


class ConversationService:

    def __init__(
        self,
        repository: ConversationRepository
    ):
        self.repository = repository

    def save_conversation(
        self,
        conversation: Conversation
    ) -> Conversation:

        return self.repository.create(conversation)

    def get_conversation(
        self,
        conversation_id: int
    ) -> Optional[Conversation]:

        return self.repository.get_by_id(conversation_id)

    def get_all_conversations(
        self
    ) -> list[Conversation]:

        return self.repository.get_all()

    def delete_conversation(
        self,
        conversation_id: int
    ) -> bool:

        return self.repository.delete(conversation_id)