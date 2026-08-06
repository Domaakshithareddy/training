from repository import EmployeeRepository
from schemas import EmployeeCreate, EmployeeUpdate, EmployeePatch
from exceptions import EmployeeNotFoundException

class EmployeeService:

    @staticmethod
    def get_all_employees():
        return EmployeeRepository.get_all_employees()

    @staticmethod
    def get_employee_by_id(employee_id: int):

        employee = EmployeeRepository.get_employee_by_id(employee_id)

        if employee is None:
            raise EmployeeNotFoundException()

        return employee

    @staticmethod
    def create_employee(employee: EmployeeCreate):

        return EmployeeRepository.create_employee(employee)

    @staticmethod
    def update_employee(employee_id: int, employee: EmployeeUpdate):

        existing_employee = EmployeeRepository.get_employee_by_id(employee_id)

        if existing_employee is None:
            raise EmployeeNotFoundException()

        return EmployeeRepository.update_employee(employee_id, employee)

    @staticmethod
    def patch_employee(employee_id: int, employee: EmployeePatch):

        existing_employee = EmployeeRepository.get_employee_by_id(employee_id)

        if existing_employee is None:
            raise EmployeeNotFoundException()

        return EmployeeRepository.patch_employee(employee_id, employee)

    @staticmethod
    def delete_employee(employee_id: int):

        existing_employee = EmployeeRepository.get_employee_by_id(employee_id)

        if existing_employee is None:
            raise EmployeeNotFoundException()

        return EmployeeRepository.delete_employee(employee_id)