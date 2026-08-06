from fastapi import APIRouter, status

from schemas import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeePatch,
    ApiResponse
)

from service import EmployeeService

router = APIRouter()

@router.get(
    "/employees",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def get_all_employees():

    employees = EmployeeService.get_all_employees()

    return {
        "success": True,
        "message": "Employees retrieved successfully.",
        "data": employees
    }

@router.get(
    "/employees/{employee_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def get_employee(employee_id: int):

    employee = EmployeeService.get_employee_by_id(employee_id)

    return {
        "success": True,
        "message": "Employee retrieved successfully.",
        "data": employee
    }

@router.post(
    "/employees",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(employee: EmployeeCreate):

    created_employee = EmployeeService.create_employee(employee)

    return {
        "success": True,
        "message": "Employee created successfully.",
        "data": created_employee
    }

@router.put(
    "/employees/{employee_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate
):

    updated_employee = EmployeeService.update_employee(
        employee_id,
        employee
    )

    return {
        "success": True,
        "message": "Employee updated successfully.",
        "data": updated_employee
    }

@router.patch(
    "/employees/{employee_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def patch_employee(
    employee_id: int,
    employee: EmployeePatch
):
    updated_employee = EmployeeService.patch_employee(
        employee_id,
        employee
    )

    return {
        "success": True,
        "message": "Employee updated successfully.",
        "data": updated_employee
    }

@router.delete(
    "/employees/{employee_id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK
)
def delete_employee(employee_id: int):

    deleted_employee = EmployeeService.delete_employee(employee_id)

    return {
        "success": True,
        "message": "Employee deleted successfully.",
        "data": deleted_employee
    }