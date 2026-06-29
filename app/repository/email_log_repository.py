"""
Email Log Repository
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import EmailLog


class EmailLogRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        email: EmailLog
    ) -> EmailLog:

        self.db.add(email)
        self.db.commit()
        self.db.refresh(email)

        return email

    def get_by_id(
        self,
        email_id: int
    ) -> Optional[EmailLog]:

        return (
            self.db.query(EmailLog)
            .filter(
                EmailLog.email_id == email_id
            )
            .first()
        )

    def get_all(self) -> list[EmailLog]:

        return (
            self.db.query(EmailLog)
            .all()
        )