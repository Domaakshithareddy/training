import requests
 
 
BASE_URL = "http://127.0.0.1:8000/api/v1"
 
 
def test_get_all_employees():
 
    response = requests.get(
        f"{BASE_URL}/employees"
    )
 
    assert response.status_code == 200
 
    data = response.json()
 
    assert data["success"] is True
    assert data["message"] == "Employees retrieved successfully."
    assert isinstance(data["data"], list)
 
 
def test_get_employee_by_id():
 
    response = requests.get(
        f"{BASE_URL}/employees/1"
    )
 
    assert response.status_code == 200
 
    data = response.json()
 
    assert data["success"] is True
    assert data["message"] == "Employee retrieved successfully."
 
    employee = data["data"]
 
    assert employee["id"] == 1
    assert "employee_name" in employee
    assert "department" in employee
    assert "salary" in employee
 
 
def test_create_employee():
 
    payload = {
        "employee_name": "Test Employee",
        "department": "IT",
        "salary": 60000
    }
 
    response = requests.post(
        f"{BASE_URL}/employees",
        json=payload
    )
 
    assert response.status_code == 201
 
    data = response.json()
 
    assert data["success"] is True
    assert data["message"] == "Employee created successfully."
 
    employee = data["data"]
 
    assert "id" in employee
    assert employee["employee_name"] == "Test Employee"
    assert employee["department"] == "IT"
    assert float(employee["salary"]) == 60000
 
 
def test_update_employee():
 
    create_payload = {
        "employee_name": "Update Test",
        "department": "IT",
        "salary": 50000
    }
 
    create_response = requests.post(
        f"{BASE_URL}/employees",
        json=create_payload
    )
 
    assert create_response.status_code == 201
 
    employee_id = create_response.json()["data"]["id"]
 
    update_payload = {
        "employee_name": "Updated Employee",
        "department": "HR",
        "salary": 65000
    }
 
    response = requests.put(
        f"{BASE_URL}/employees/{employee_id}",
        json=update_payload
    )
 
    assert response.status_code == 200
 
    data = response.json()
 
    assert data["success"] is True
    assert data["message"] == "Employee updated successfully."
 
    employee = data["data"]
 
    assert employee["id"] == employee_id
    assert employee["employee_name"] == "Updated Employee"
    assert employee["department"] == "HR"
    assert float(employee["salary"]) == 65000
 
 
def test_patch_employee():
 
    create_payload = {
        "employee_name": "Patch Test",
        "department": "IT",
        "salary": 55000
    }
 
    create_response = requests.post(
        f"{BASE_URL}/employees",
        json=create_payload
    )
 
    assert create_response.status_code == 201
 
    employee_id = create_response.json()["data"]["id"]
 
    patch_payload = {
        "department": "Finance"
    }
 
    response = requests.patch(
        f"{BASE_URL}/employees/{employee_id}",
        json=patch_payload
    )
 
    assert response.status_code == 200
 
    data = response.json()
 
    assert data["success"] is True
    assert data["message"] == "Employee updated successfully."
 
    employee = data["data"]
 
    assert employee["id"] == employee_id
    assert employee["employee_name"] == "Patch Test"
    assert employee["department"] == "Finance"
    assert float(employee["salary"]) == 55000
 
 
def test_delete_employee():
 
    create_payload = {
        "employee_name": "Delete Test",
        "department": "IT",
        "salary": 45000
    }
 
    create_response = requests.post(
        f"{BASE_URL}/employees",
        json=create_payload
    )
 
    assert create_response.status_code == 201
 
    employee_id = create_response.json()["data"]["id"]
 
    response = requests.delete(
        f"{BASE_URL}/employees/{employee_id}"
    )
 
    assert response.status_code == 200
 
    data = response.json()
 
    assert data["success"] is True
    assert data["message"] == "Employee deleted successfully."
 
    employee = data["data"]
 
    assert employee["id"] == employee_id
    assert employee["employee_name"] == "Delete Test"
    assert employee["department"] == "IT"
    assert float(employee["salary"]) == 45000