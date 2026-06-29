"""
Payment Service
"""

from typing import Optional

from app.database.models import Payment
from app.repository.payment_repository import PaymentRepository


class PaymentService:

    def __init__(
        self,
        repository: PaymentRepository
    ):
        self.repository = repository

    def create_payment(
        self,
        payment: Payment
    ) -> Payment:

        return self.repository.create(payment)

    def get_payment(
        self,
        payment_id: int
    ) -> Optional[Payment]:

        return self.repository.get_by_id(payment_id)

    def get_all_payments(
        self
    ) -> list[Payment]:

        return self.repository.get_all()

    def update_payment(
        self,
        payment: Payment
    ) -> Payment:

        return self.repository.update(payment)

    def delete_payment(
        self,
        payment_id: int
    ) -> bool:

        return self.repository.delete(payment_id)