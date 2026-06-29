"""
Email Service
"""

from typing import Optional

from app.database.models import EmailLog
from app.repository.email_log_repository import EmailLogRepository


class EmailService:

    def __init__(
        self,
        repository: EmailLogRepository
    ):
        self.repository = repository

    def save_email_log(
        self,
        email: EmailLog
    ) -> EmailLog:

        return self.repository.create(email)

    def get_email(
        self,
        email_id: int
    ) -> Optional[EmailLog]:

        return self.repository.get_by_id(email_id)

    def get_all_emails(
        self
    ) -> list[EmailLog]:

        return self.repository.get_all()