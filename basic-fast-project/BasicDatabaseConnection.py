import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database ="learning_database",
            user="postgres",
            password="121"
            
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
    