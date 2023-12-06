from ninja import NinjaAPI, Schema
from datetime import date
from api.models import *

api = NinjaAPI()

class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id:int = None
    birthdate: date = None

@api.post("/employees")
def create_emplayee(requests, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}
