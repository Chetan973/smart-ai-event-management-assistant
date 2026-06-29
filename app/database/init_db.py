"""
Initialize Database.

Creates all database tables.
"""

from app.database.connection import create_database
import app.database.models


def initialize_database() -> None:
    create_database()
    print("Database initialized successfully.")


if __name__ == "__main__":
    initialize_database()