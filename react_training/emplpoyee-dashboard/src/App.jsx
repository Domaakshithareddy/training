import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [employees, setEmployees] = useState([]);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [department, setDepartment] = useState("");

  // GET - Read Employees

  function getEmployees() {
    axios
      .get("https://jsonplaceholder.typicode.com/users")
      .then((response) => {
        setEmployees(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  useEffect(() => {
    getEmployees();
  }, []);

  // POST - Add Employee

  function addEmployee() {
    const employee = {
      name: name,
      email: email,
      department: department,
    };

    axios
      .post("https://jsonplaceholder.typicode.com/users", employee)
      .then((response) => {
        alert("Employee Added Successfully");

        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  // PUT - Update Employee

  function updateEmployee() {
    const employee = {
      name: name,
      email: email,
      department: department,
    };

    axios
      .put("https://jsonplaceholder.typicode.com/users/1", employee)
      .then((response) => {
        alert("Employee Updated Successfully");

        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  // DELETE - Delete Employee

  function deleteEmployee() {
    axios
      .delete("https://jsonplaceholder.typicode.com/users/1")
      .then((response) => {
        alert("Employee Deleted Successfully");

        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Employee CRUD Application</h1>
      <hr />
      <label>Name</label>
      <br />
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <br />
      <br />
      <label>Email</label>
      <br />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <br />
      <br />
      <label>Department</label>
      <br />
      <input
        type="text"
        value={department}
        onChange={(e) => setDepartment(e.target.value)}
      />
      <br />
      <br />
      <button onClick={addEmployee}>Add Employee</button>
      &nbsp;
      <button onClick={updateEmployee}>Update Employee</button>
      &nbsp;
      <button onClick={deleteEmployee}>Delete Employee</button>
      <hr />
      <h2>Employee List</h2>
      {employees.map((employee) => (
        <div
          key={employee.id}
          style={{
            border: "1px solid gray",
            padding: "10px",
            marginBottom: "10px",
          }}
        >
          <h3>{employee.name}</h3>

          <p>Email : {employee.email}</p>

          <p>Company : {employee.company?.name}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
