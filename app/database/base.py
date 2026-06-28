"""
Base Class

Every SQLAlchemy model in this project
inherits from this Base class.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database models.

    SQLAlchemy uses this class to keep track
    of every table defined in the application.
    """

    pass