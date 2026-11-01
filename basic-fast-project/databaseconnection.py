import psycopg2 

# conn =psycopg2.connect(
#     host="localhost",
#     port=5432,
#     database="learning_database",
#     user ="postgres",
#     password="121"
# )


# if conn :
#     print("database is connected sucssfully!")
    
# else:
#     print("database is not conneted ")
    

# conn.close()

def connect_database():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port = 5432,
            user ="postgres",
            password ="121",
            database = "learning_database"
        )
        if conn :
            print("Database is sucssfully connectd")
            return conn
        else:
            print("Database is not connectd")
    except Exception as e :
        print("Database is not connectd show Exception Error ",e)
        return None
