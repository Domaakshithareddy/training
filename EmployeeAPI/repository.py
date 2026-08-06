from schemas import EmployeeCreate, EmployeeUpdate, EmployeePatch
from database import get_connection

class EmployeeRepository:

    @staticmethod
    def get_all_employees():

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                id,
                employee_name,
                department,
                salary
            FROM employees
        """

        cursor.execute(query)

        employees = cursor.fetchall()

        cursor.close()
        connection.close()

        return employees

    @staticmethod
    def get_employee_by_id(employee_id: int):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query="""
            SELECT
                id,
                employee_name,
                department,
                salary
            FROM employees
            WHERE id=%s
        """

        cursor.execute(query,(employee_id,))

        employee = cursor.fetchone()

        cursor.close()
        connection.close()

        return employee


    @staticmethod
    def create_employee(employee: EmployeeCreate):

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query="""
            INSERT INTO employees(employee_name,department,salary)
            VALUES(%s,%s,%s)
        """

        cursor.execute(query,(employee.employee_name,employee.department,employee.salary))
        connection.commit()

        employee_id = cursor.lastrowid

        cursor.execute("""
            SELECT
                id,
                employee_name,
                department,
                salary
            FROM employees
            WHERE id=%s
        """,(employee_id,),
        )
        
        created_employee = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return created_employee


    @staticmethod
    def update_employee(employee_id: int, employee):


        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        
        query="""
            UPDATE employees
            SET employee_name = %s,
                department = %s,
                salary = %s
            WHERE id = %s
        """
        
        cursor.execute(query,(employee.employee_name,employee.department,employee.salary,employee_id))
        connection.commit()
        
        if cursor.rowcount==0:
                cursor.close()
                connection.close()
                return None
        
        cursor.execute("""
             SELECT
                id,
                employee_name,
                department,
                salary
            FROM employees
            WHERE id=%s
        """,(employee_id,),
        )
                
        updated_employee = cursor.fetchone()
                
        cursor.close()
        connection.close()
                
        return updated_employee
    
    @staticmethod
    def patch_employee(employee_id: int, employee):


        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
             SELECT
                id,
                employee_name,
                department,
                salary
            FROM employees
            WHERE id=%s
        """,(employee_id,),
        )

        existing_employee=cursor.fetchone()

        if not existing_employee:
                cursor.close()
                connection.close()
                return None

        employee_name = employee.employee_name if employee.employee_name is not None else existing_employee["employee_name"]
        department = employee.department if employee.department is not None else existing_employee["department"]
        salary = employee.salary if employee.salary is not None else existing_employee["salary"]

        query="""
            UPDATE employees
            SET employee_name = %s,
                department = %s,
                salary = %s
            WHERE id = %s
        """
        
        cursor.execute(query,(employee_name,department,salary,employee_id))
        connection.commit()
        
        cursor.execute("""
             SELECT
                id,
                employee_name,
                department,
                salary
            FROM employees
            WHERE id=%s
        """,(employee_id,),
        )
                
        patched_employee = cursor.fetchone()
                
        cursor.close()
        connection.close()
                
        return patched_employee

    @staticmethod
    def delete_employee(employee_id: int):


        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT
                id,
                employee_name,
                department,
                salary
            FROM employees
            WHERE id = %s
            """,
            (employee_id,),
        )

        employee = cursor.fetchone()

        if not employee:
            cursor.close()
            connection.close()
            return None

        cursor.execute(
            "DELETE FROM employees WHERE id = %s",
            (employee_id,),
        )

        connection.commit()

        cursor.close()
        connection.close()

        return employee