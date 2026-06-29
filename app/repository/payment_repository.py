"""
Payment Repository
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Payment


class PaymentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        payment: Payment
    ) -> Payment:

        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)

        return payment

    def get_by_id(
        self,
        payment_id: int
    ) -> Optional[Payment]:

        return (
            self.db.query(Payment)
            .filter(
                Payment.payment_id == payment_id
            )
            .first()
        )

    def get_all(self) -> list[Payment]:

        return (
            self.db.query(Payment)
            .all()
        )

    def update(
        self,
        payment: Payment
    ) -> Payment:

        self.db.commit()
        self.db.refresh(payment)

        return payment

    def delete(
        self,
        payment_id: int
    ) -> bool:

        payment = self.get_by_id(payment_id)

        if payment is None:
            return False

        self.db.delete(payment)
        self.db.commit()

        return True