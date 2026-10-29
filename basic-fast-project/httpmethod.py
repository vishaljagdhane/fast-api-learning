from ctypes import pointer

from fastapi import APIRouter
from mockdata import product

httpmethodRouter = APIRouter()

@httpmethodRouter.get("/TestAPIRouterisWorking")
def TestApiRouter():
    return{"message":"checking API Router is working "}


# we can use HTTP get method and use dummy data 
# we can get simple all data 

@httpmethodRouter.get("/get-all-data")
def fetchAllProductData():
    return{"fetchAllData":product} 

# get method with path Parameter we can pass id and fetching that Id related data 

@httpmethodRouter.get("/fetch-Id-reladted-data/{user_id}")
def fetchIdwiseData(user_id:int):
    fetchId = None
    for finddata in product:
        if finddata.get("id") == user_id:
            fetchId = finddata
        else:
            fetchId ="No data found"
        
        return{"userRecord":fetchId}
        
        
        
   
