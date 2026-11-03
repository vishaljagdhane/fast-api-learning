from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
    
    
class UserRecord(BaseModel):
    fname:str
    lname:str
    email:str
    mobile:str
    password:str

class UpdateUserRecord(BaseModel):
    fname:str
    lname:str
    email:str
    mobile:str
    password:str