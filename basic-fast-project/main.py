from fastapi import FastAPI
from mockdata import product
from httpmethod import httpmethodRouter
from selfLogic import logical


app = FastAPI()  # this create an instance of the FastAPI class 
app.include_router(httpmethodRouter)
app.include_router(logical)

@app.get("/Home")
def Home():
    return {"message":"fastyapi is working"}


# How to run this main.py 
# activate virtual environment
# uvicorn main:app --reload

# pass path parameters
# http://127.0.0.1:8000/Home?name=John&age=20
# http://127.0.0.1:8000/Home?name=John&age=20&city=New%20York

@app.get("/pathParameters/{user_id}")
def pathParameters(user_id:int):
    return{
        "userParameter":user_id,
        "message":"This is path parameters"
    }

# pass loat off path parameters

@app.get("/pathParameters/{user_id}/{fname} {lname}{email} {age} {mobile}")
def multiplePathParameters(user_id:int,fname:str,lname:str,email:str,age:str,mobile:str):
    return{
        "userParameter":user_id,
        "fname":fname,
        "lname":lname,
        "email":email,
        "age":age,
        "mobile":mobile,
        "message":"This is multiple path parameters"
    }
    
    
# this simple return your mock data 
@app.get("/simple-return-mockdata")
def getHoleData():
    return{"This is mock data":product}

# we can fetch speifc data 

# @app.get("/fetch-spesfic-data/{userId}")
@app.post("/fetch-user-ID/{userId}")
def fetchUserRecord(userId:int):
    # print("We can need logic when user is search UserId show data ")
    # all data product we can find user id  find loop throw 
    userRecord = None
    for findUserId in product:
        if findUserId.get("id") == userId:
            userRecord = findUserId
            return{
                "userRecord":userRecord
            }
    
   
