from ninja import NinjaAPI, Schema
from datetime import date
from api.models import *
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class EmployeeIn(Schema): 
    first_name: str
    last_name: str
    department_id:int = None
    birthdate: date = None

class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id:int = None
    birthdate: date = None

@api.post("/employees")
def create_emplayee(requests, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}

@api.get("/emplayees/{employee_id}", response=EmployeeOut)
def get_employee(requests, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee
