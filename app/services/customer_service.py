"""
Customer Service
Contains business logic.
"""
from app.database.models import Customer

from app.repository.customer_repository import CustomerRepository


class CustomerService:
    def __init__(
        self,
        repository: CustomerRepository
    ):
        self.repository = repository

    def register_customer(
        self,
        full_name: str,
        email: str,
        phone_number: str
    ) -> Customer:
        existing_customer = (
            self.repository.get_by_email(email)
        )
        if existing_customer:
            return existing_customer
        customer = Customer(
            full_name=full_name,
            email=email,
            phone_number=phone_number
        )
        return self.repository.create(customer)