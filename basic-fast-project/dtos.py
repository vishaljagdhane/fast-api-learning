from datetime import date

from pydantic import BaseModel

class productOTS(BaseModel):
    product_id:int
    product_name:str
    product_price:float
    product_make_date:date

class studentMarkCalculate(BaseModel):
    student_name:str
    stduent_address:str
    student_gender:str
    marathi:float
    hindi:float
    english:float
    math1:float
    math2:float
    geoghrapy:float
    science:float
    
    