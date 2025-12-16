from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.models import Employee
from app.schemas import ApiResponse, EmployeeCreate, EmployeeRead
from app.core.orm_protection import protect_queryset
from app.core.pagination import paginate_offset,PaginatedResponse

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("/", response_model=ApiResponse[EmployeeRead])
async def create_employee(payload: EmployeeCreate):
    emp = await Employee.create(**payload.model_dump())
    emp = (
        await Employee
        .get(id=emp.id)
        .select_related("user")
    )
    return ApiResponse(
        success=True,
        message="Employee created successfully",
        data=EmployeeRead.model_validate(emp),
    )

@router.get("/", response_model=PaginatedResponse[EmployeeRead])
async def list_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
):
    queryset = protect_queryset(
        Employee.all(),
        select=["user"],  # 🔥 REQUIRED
    )

    employees, meta = await paginate_offset(
        queryset,
        skip=skip,
        limit=limit,
    )

    return PaginatedResponse(
        message="Employees fetched successfully",
        data=[EmployeeRead.model_validate(e) for e in employees],
        meta=meta,
    )

@router.get("/{emp_id}", response_model=ApiResponse[EmployeeRead])
async def get_employee(emp_id: int):
    emp = (
        await Employee
        .get(id=emp_id)
        .select_related("user")
    )
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return ApiResponse(
        success=True,
        message="Employee retrieved successfully",
        data=EmployeeRead.model_validate(emp),
    )

@router.patch("/{emp_id}", response_model=ApiResponse[EmployeeRead])
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
    return ApiResponse(
        success=True,
        message="Employee updated successfully",
        data=EmployeeRead.model_validate(emp),
    )

@router.delete("/{emp_id}", response_model=ApiResponse[dict])
async def delete_employee(emp_id: int):
    emp = await Employee.get_or_none(id=emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    deleted = await Employee.filter(id=emp_id).delete()
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return ApiResponse(
        success=True,
        message="Employee deleted successfully",
        data={"deleted": True},
    )
