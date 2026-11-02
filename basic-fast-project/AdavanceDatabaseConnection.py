import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def Advance_create_connection():
    try:
        connection = psycopg2.connect(
            host =os.getenv("DB_HOST"),
            port =os.getenv("DB_PORT"),
            database =os.getenv("DB_NAME"),
            user =os.getenv("DB_USER"),
            password =os.getenv("DB_PASSWORD")
        )
        
        if connection:
            print("Database connection established successfully.")
            return connection
        else:
            print("Failed to establish database connection.")
            return None
    except Exception as e:
        print("Error occurred while connecting to the database:", e)
        return None