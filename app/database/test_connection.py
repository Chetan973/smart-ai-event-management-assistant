from sqlalchemy import text

from app.database.connection import engine


def test_database_connection():
    """
    Tests PostgreSQL connection.
    """

    try:

        with engine.connect() as connection:

            version = connection.execute(
                text("SELECT version();")
            )

            print("\n")
            print("Connected Successfully")
            print(version.scalar())

    except Exception as error:

        print(error)


if __name__ == "__main__":
    test_database_connection()