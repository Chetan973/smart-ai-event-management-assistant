"""
Initialize Database.

Creates all database tables.
"""

from app.database.connection import create_database

# Import models so SQLAlchemy knows about them
from app.database import models  # noqa: F401


def initialize_database():
    create_database()
    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()