import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )

        print("Database connection successful.")
        return connection

    except psycopg2.Error as error:
        print(f"Database connection failed: {error}")
        return None


if __name__ == "__main__":
    connection = get_connection()

    if connection:
        connection.close()
        print("Database connection closed.")