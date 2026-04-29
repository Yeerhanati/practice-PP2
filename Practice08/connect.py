import psycopg2
from psycopg2 import OperationalError
from config import *

def get_connection():
    """Create and return a PostgreSQL connection"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except OperationalError:
        print("Failed to connect to the database!")
        return None

def create_contacts_table():
    """Create the contacts table (RUN FIRST)"""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        # Table creation script
        create_table_query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL UNIQUE,
            phone VARCHAR(20) NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'contacts' created successfully (or already exists)")
        
        cursor.close()
        conn.close()