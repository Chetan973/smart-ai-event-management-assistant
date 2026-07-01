"""
PostgreSQL Checkpointer
"""

from langgraph.checkpoint.postgres import PostgresSaver

from app.config.settings import DATABASE_URL


checkpointer = PostgresSaver.from_conn_string(
    DATABASE_URL
)