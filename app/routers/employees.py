from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeRead

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("/", response_model=EmployeeRead)
async def create_employee(payload: EmployeeCreate):
    emp = await Employee.create(**payload.model_dump())

    emp = (
        await Employee
        .get(id=emp.id)
        .select_related("user")
    )

    return EmployeeRead.model_validate(emp)

@router.get("/", response_model=List[EmployeeRead])
async def list_employees(skip: int = 0, limit: int = 100):
    employees = (
        await Employee
        .all()
        .offset(skip)
        .limit(limit)
        .select_related("user")
    )

    return [EmployeeRead.model_validate(e) for e in employees]

@router.get("/{emp_id}", response_model=EmployeeRead)
async def get_employee(emp_id: int):
    emp = (
        await Employee
        .get(id=emp_id)
        .select_related("user")
    )
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    return EmployeeRead.model_validate(emp)

@router.patch("/{emp_id}", response_model=EmployeeRead)
async def update_employee(emp_id: int, payload: EmployeeCreate):
    emp = await Employee.get_or_none(id=emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(emp, key, value)
    await emp.save()
    emp = (
        await Employee
        .get(id=emp.id)
        .select_related("user")
    )
    return EmployeeRead.model_validate(emp)


@router.delete("/{emp_id}")
async def delete_employee(emp_id: int):
    deleted = await Employee.filter(id=emp_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"deleted": True}
