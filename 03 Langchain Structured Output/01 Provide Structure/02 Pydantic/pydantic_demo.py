from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str
    # default value
    age: int = 18
    # optional
    course: Optional[str] = None
    email: EmailStr
    cgpa: float = Field(gt=0, ls=10, default=5, description="A decimal value, representing the cgpa of the student")

new_student = {"name": "Amit Mondal","age":"21","email":"amit123@gmail.com"}
# pydantic helps in automatic type conversion => type coercion

student = Student(**new_student)

# print(student)

# we can convert it to many forms => dict,json
student_dict = dict(student)
# print(student_dict)
student_json = student.model_dump_json()
print(student_json)