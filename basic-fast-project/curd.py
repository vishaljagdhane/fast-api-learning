from fastapi import FastAPI,APIRouter
from psycopg import Cursor
from sqlalchemy import column, desc
from curdModels import UserCreate,UserRecord,UpdateUserRecord
from databaseconnection import connect_database

curdObject = APIRouter()

@curdObject.get("/get-all-data",tags=["curd"])
def getAllData():
    return{"message":"This is get all data"}

@curdObject.post("/check-database-connection",tags=["curd"])
def checkDatabaseConnection():
    conn = connect_database()
    if conn:
        conn.close()
        return{"message":"Database is connected"}
    else:
        return{"message":"Failed to connect to database"}
@curdObject.post("/Insert-database-Value",tags=["curd"])   
def create_user(user: UserCreate):
    # frist call to database connecton function then use insert Logic to insert data in database
    conn = connect_database()
    if conn:
        # Insert user data into the database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO create_user (name, email) VALUES (%s, %s)", (user.name, user.email))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "User created successfully"}
    else:
        return {"message": "Failed to create user"}
    
@curdObject.post("/fetch-user-data",tags=["curd"])
def fetch_user_data():
    conn = connect_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM create_user")
        user = cursor.fetchall()
        cursor.close()
        # datadic = user.model_dump()
        columns = [desc[0] for desc in cursor.description]

        datadic = [
            dict(zip(columns, row))
            for row in user
        ]
        print("check data dic",datadic)
        conn.close()
        # return {"users": datadic}
        
@curdObject.post("/Add-user-record",tags=["curd"])
def add_user_record(user_record:UserRecord):
    conn = connect_database()
    if conn:
        cursor =conn.cursor() # database is connected stored in value are cursor 
        cursor.execute("INSERT INTO UserRecord(fname,lname,email,mobile,password) Values(%s,%s,%s,%s,%s)",(user_record.fname,user_record.lname,user_record.email,user_record.mobile,user_record.password))
        cursor.close()
        conn.commit()
        conn.close()
    return{"message":"User record added successfully"}

@curdObject.get("/fetch-user-record",tags=["curd"])
def fetch_user_record():
    conn = connect_database()
    if conn:
        Cursor = conn.cursor()
        Cursor.execute("SELECT * FROM userRecord")
        data = Cursor.fetchall()
        columns =[desc[0] for desc in Cursor.description]
        Cursor.close()
        conn.close()
        datadic = [
            dict(zip(columns,row))
            for row in data
        ]
        return {"users": datadic}
    
    
@curdObject.get("/fetch-user-record-by-id/{user_id}",tags=["curd"])
def fetch_user_record_by_id(user_id:int):
    # connect to the database
    conn = connect_database()
    # check if the connection is successful
    if conn:
        cursor = conn.cursor()
        # execute the SQL query to fetch the user record by ID
        cursor.execute("SELECT * FROM userRecord WHERE user_id =%s",(user_id,))
        fetched = cursor.fetchone()
        # get the column name from the cursor description 
        columns =[desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()
        # convert the fetched data to a dictionary
        datadic = dict(zip(columns,fetched))
        return {"user": datadic}


@curdObject.put("/update-user-record/{user_id}",tags=["curd"])
def update_user_record(user_id:int,update_user:UpdateUserRecord):
    connectDatabase = connect_database()
    if connectDatabase:
      try:
          cursor = connectDatabase.cursor()
          cursor.execute("UPDATE userRecord SET fname=%s,lname=%s,email=%s,mobile=%s,password=%s WHERE user_id=%s",(update_user.fname,update_user.lname,update_user.email,update_user.mobile,update_user.password,user_id))
          connectDatabase.commit()
          cursor.close()
          connectDatabase.close()
          return {"message":"User record updated successfully"}
      except Exception as e:
          return {"message":"Failed to update user record","error":str(e)}  
      
@curdObject.delete("/delete-user-record/{user_id}",tags=["curd"])
def delete_user_record(user_id:int):
    connectDatabase = connect_database()
    if connectDatabase:
        try:
            cursor = connectDatabase.cursor()
            cursor.execute("DELETE FROM userRecord WHERE user_id=%s",(user_id,))
            connectDatabase.commit()
            cursor.close()
            connectDatabase.close()
            return {"message":"User record deleted successfully"}
        except Exception as e:
            return {"message":"Failed to delete user record","error":str(e)}     
      