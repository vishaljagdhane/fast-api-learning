from ctypes import pointer

from fastapi import APIRouter
from mockdata import product
from dtos import productOTS

httpmethodRouter = APIRouter()

@httpmethodRouter.get("/TestAPIRouterisWorking",tags=["HTTPMETHOD"])
def TestApiRouter():
    return{"message":"checking API Router is working "}


# we can use HTTP get method and use dummy data 
# we can get simple all data 

@httpmethodRouter.get("/get-all-data",tags=["HTTPMETHOD"])
def fetchAllProductData():
    return{"fetchAllData":product} 

# get method with path Parameter we can pass id and fetching that Id related data  we are used int with id we can find 

@httpmethodRouter.get("/fetch-Id-reladted-data/{user_id}",tags=["HTTPMETHOD"])
def fetchIdwiseData(user_id:int):
    fetchId = None
    for finddata in product:
        if finddata.get("id") == user_id:
            fetchId = finddata
        else:
            fetchId ="No data found"
        
        return{"userRecord":fetchId}
    
    
# we can use string with get method and path parameter and HTTPP get method 

@httpmethodRouter.get("/search-data-by-name/{first_name}",tags=["HTTPMETHOD"])
def fetchDataByName(first_name:str):
    searchName = None
    for nameSearch in product:
        if nameSearch.get("fname") == first_name:
            searchName = nameSearch
            return {"Name_Is":searchName}
        

productdata =[]
# we need to use post api We will add the routes we create Models 
@httpmethodRouter.post("/post-api-use-request-body",tags=["HTTPMETHOD"])
def postEndpointUsingRequestBoday(productsDetails:productOTS):
    # print("check post data ",productsDetails)
    # conver this data to model dump ()
    datadisc = productsDetails.model_dump()
    print(datadisc)
    # we can store this data in json file 
    productdata.append(datadisc)
    return{"postedData":datadisc,"returnAppendData":productdata}
        
        
        
        
        
        
        
        
        
   
