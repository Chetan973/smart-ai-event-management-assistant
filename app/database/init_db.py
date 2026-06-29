"""
Initialize Database.

Creates all database tables.
"""

from app.database.connection import create_database

# Import models so SQLAlchemy knows about them
  # noqa: F401
from app.database.models import Customer


def initialize_database():
    create_database()
    print("Database initialized successfully.")


if __name__ == "__main__":
    create_database()
    print("Database initialized successfully.")