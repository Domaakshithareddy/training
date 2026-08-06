from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, status

class EmployeeNotFoundException(Exception):

    def __init__(self, message: str = "Employee not found"):
        self.message = message

class EmployeeAlreadyExistsException(Exception):

    def __init__(self, message: str = "Employee already exists"):
        self.message = message

def employee_not_found_exception_handler(
    request: Request,
    exception: EmployeeNotFoundException
):

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "success": False,
            "message": exception.message,
            "data": None
        }
    )

def employee_already_exists_exception_handler(
    request: Request,
    exception: EmployeeAlreadyExistsException
):

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "success": False,
            "message": exception.message,
            "data": None
        }
    )

def generic_exception_handler(
    request: Request,
    exception: Exception
):

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "message": "Internal Server Error",
            "data": None
        }
    )

def register_exception_handlers(app: FastAPI):

    app.add_exception_handler(
        EmployeeNotFoundException,
        employee_not_found_exception_handler
    )

    app.add_exception_handler(
        EmployeeAlreadyExistsException,
        employee_already_exists_exception_handler
    )

    app.add_exception_handler(
        Exception,
        generic_exception_handler
    )