"""
Customer Repository

Responsible for all database operations
related to Customer.
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Customer

class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        customer: Customer
    ) -> Customer:

        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)

        return customer

    def get_by_email(
        self,
        email: str
    ) -> Optional[Customer]:

        return (
            self.db.query(Customer)
            .filter(Customer.email == email)
            .first()
        )

    def get_by_phone(
        self,
        phone: str
    ) -> Optional[Customer]:

        return (
            self.db.query(Customer)
            .filter(Customer.phone_number == phone)
            .first()
        )

    def get_by_id(
        self,
        customer_id: int
    ) -> Optional[Customer]:

        return (
            self.db.query(Customer)
            .filter(Customer.customer_id == customer_id)
            .first()
        )

    def get_all(self):

        return (
            self.db.query(Customer)
            .all()
        )