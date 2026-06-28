"""
Database Connection

Creates:

1. Engine
2. Session
3. Database initialization
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import DATABASE_URL

from app.database.base import Base


# ---------------------------------------------------
# Create Database Engine
# ---------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    echo=True
)

# ---------------------------------------------------
# Session Factory
# ---------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def create_database() -> None:
    """
    Creates every table defined
    in models.py
    """

    Base.metadata.create_all(bind=engine)