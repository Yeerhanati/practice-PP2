import psycopg2
from psycopg2 import OperationalError
from config import *

def get_db_connection():
    """Establish and return a connection to PostgreSQL"""
    connection = None
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
    except OperationalError as e:
        print(f"Connection failed: {e}")
    return connection

def create_phonebook_table(connection):
    """Create phonebook table if it does not exist"""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        phone_number VARCHAR(50) UNIQUE NOT NULL
    );
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    print("Table 'phonebook' is ready")