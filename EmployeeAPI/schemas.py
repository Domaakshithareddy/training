from typing import Optional, Any

from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    employee_name: str = Field(..., min_length=2, max_length=100)
    department: str = Field(..., min_length=2, max_length=50)
    salary: float = Field(..., gt=0)

class EmployeeUpdate(BaseModel):
    employee_name: str = Field(..., min_length=2, max_length=100)
    department: str = Field(..., min_length=2, max_length=50)
    salary: float = Field(..., gt=0)

class EmployeePatch(BaseModel):
    employee_name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    department: Optional[str] = Field(default=None, min_length=2, max_length=50)
    salary: Optional[float] = Field(default=None, gt=0)

class EmployeeResponse(BaseModel):
    id: int
    employee_name: str
    department: str
    salary: float

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None