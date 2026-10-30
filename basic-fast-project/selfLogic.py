from fastapi import APIRouter
from dtos import studentMarkCalculate

logical = APIRouter()

@logical.get("Test-Logical-apiworking",tags=["Logical"])
def LogicalHome():
    
    return{"Message":"Logical_API is working"} 

# calculate student mark and data 
@logical.post("/calculate-mark",tags=["Logical"])
def student_mark(mark:studentMarkCalculate):
    totalStudentmark = mark.marathi + mark.hindi + mark.english + mark.math1 + mark.math2 + mark.science + mark.geoghrapy
    print("Total Mark is ",totalStudentmark,mark.student_name,mark.stduent_address,mark.student_gender)
    calculate_percentage = totalStudentmark / 700 * 100
    
    
    
    return{"StudentNameis  ":mark.student_name,
           "StudentGenderis":mark.student_gender,
           "StudentAddressIs ":mark.stduent_address,
           "StudentPercentage":calculate_percentage
           }
