from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name: str = 'default'
    age: Optional[int] = None
    email: EmailStr
    # contrained
    cgpa: float =Field(gt=0,lt=10)

stu_dict={'name':'areeb','age':'24','email':'asdasd@x.com','cgpa':5.0}
# stu_dict={'name':24} # throws error

student=Student(**stu_dict)

# Without dictionary unpacking
# student = Student(
#     name=stu_dict["name"],
#     age=stu_dict["age"], 
#     grade=stu_dict["grade"]
# )

# # With dictionary unpacking (cleaner!)
# student = Student(**stu_dict)


print(student)
print(student.model_dump_json())