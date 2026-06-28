"""
Test Customer Registration
"""

from app.database.connection import SessionLocal
from app.repository.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService


def test_customer():

    db = SessionLocal()

    try:

        repository = CustomerRepository(db)

        service = CustomerService(repository)

        customer = service.register_customer(

            full_name="Chetan P",

            email="chetan@example.com",

            phone_number="9876543210"

        )

        print("\nCustomer Created Successfully\n")

        print(customer)

    except Exception as error:

        print(error)

    finally:

        db.close()


if __name__ == "__main__":

    test_customer()